"""
Interact with the Pack module of the app.
"""
from datetime import datetime
from typing import Dict, List
from json import dumps

from thirdweb_web3 import Web3
from eth_abi import encode_abi


from ..abi.erc1155 import ERC1155
from ..abi.pack import Pack
from ..errors import AssetNotFoundException, UnsupportedAssetException
from ..types.currency import CurrencyValue
from ..types.nft import NftMetadata
from ..types.pack import (AssetAmountPair, CreatePackArg, PackMetadata,
                          PackNftMetadata)
from .base import BaseModule


class PackModule(BaseModule):
    """
    Interact with the Pack module of the app.
    """
    address: str
    """
    Address of the module
    """
    __abi_module: Pack

    def __init__(self, address: str, client: Web3):
        """
        :param address: The address of the module
        :param client: Web3 client

        Initializes the module
        """
        super().__init__()
        self.address = address
        self.__abi_module = Pack(client, address)

    def get(self, pack_id: int) -> PackMetadata:
        """
        :param pack_id: The id of the pack to get.
        :return: The metadata for the pack.

        Gets the metadata for a pack.
        """
        uri = self.__abi_module.uri.call(pack_id)
        if uri == "":
            raise AssetNotFoundException(pack_id)
        metadata = self.get_storage().get(uri)
        state = self.__abi_module.get_pack.call(pack_id)
        total_supply = self.__abi_module.total_supply.call(pack_id)
        return PackMetadata(
            id=pack_id,
            creator_address=state['creator'],
            current_supply=total_supply,
            metadata=metadata,
            open_start=None if state['openStart'] <= 0 else datetime.fromtimestamp(
                state['openStart']),
        )

    def open(self, pack_id: int) -> List[NftMetadata]:
        """
        :param pack_id: The id of the pack to open.
        :return: The NFTs in the pack.

        Opens a pack and returns the NFTs in the pack.
        """
        uri = self.__abi_module.uri.call(pack_id)
        if uri == "":
            raise AssetNotFoundException(pack_id)
        self.__abi_module.open.send(pack_id)
        return self.get_storage().get(uri)
        pass

    def get_all(self) -> List[PackMetadata]:
        """
        :return: List of metadata for all the packs.

        Gets all the packs.
        """
        max_id = self.__abi_module.next_token_id.call()
        return [self.get(i) for i in range(max_id)]

    def get_nfts(self, pack_id: int) -> List[PackNftMetadata]:
        """
        :param pack_id: The id of the pack to get the nfts for.
        :return: The nfts for the pack.

        WIP: This method is not ready to be called.
        """
        pass

    def balance_of(self, address: str, token_id: int) -> int:
        """
        :param address: The address to get the balance for.
        :param token_id: The token id to get the balance for.
        :return: The balance of the token for the given address.

        Gets the balance of a token for a given address.
        """
        return self.__abi_module.balance_of.call(address, token_id)

    def balance(self, token_id: int) -> int:
        """
        :param token_id: The token id to get the balance for.
        :return: The balance of the token for the pack.

        Gets the balance of a token for the current address.

        """
        return self.__abi_module.balance_of.call(self.get_signer_address(), token_id)

    def is_approved(self, address: str, operator: str) -> bool:
        """
        :param address: The address to check.
        :param operator: The operator to check.
        :return: True if the address is approved by the operator.

        Checks if a given address is approved by a given operator.

        """
        return self.__abi_module.is_approved_for_all.call(address, operator)

    def set_approval(self, operator: str, approved: bool):
        """
        :param operator: The operator to set the approval for.
        :param approved: True if the operator should be approved, false otherwise.
        :return: The transaction receipt.

        Approves a given operator to perform an action on the pack.
        """
        return self.execute_tx(self.__abi_module.set_approval_for_all.build_transaction(
            operator, approved, self.get_transact_opts()
        ))

    def transfer(self, to_address: str, token_id: int, amount: int):
        """
        :param to_address: The address to transfer the token to.
        :param token_id: The token id to transfer.
        :param amount: The amount to transfer.
        :return: The transaction receipt.

        Transfers a token to a given address.
        """
        return self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            self.get_signer_address(), to_address, token_id, amount, "", self.get_transact_opts(),
        ))

    def create(self, arg: CreatePackArg) -> PackMetadata:
        """

        :param arg: The arguments to create the pack with.
        :return: The metadata for the newly created pack.

        WIP: This method is not ready to be called.

        Suffers from same issue as MarketModule.list
        """

        if not self.is_erc1155(arg.asset_contract_address):
            raise UnsupportedAssetException(arg.asset_contract_address)

        asset_contract = ERC1155(
            self.get_client(), arg.asset_contract_address)
        from_address = self.get_signer_address()
        ids = [a.token_id for a in arg.assets]
        amounts = [a.amount for a in arg.assets]
        uri = self.upload_metadata(arg.metadata)

        params = encode_abi(
            ['string', 'uint256', 'uint256'],
            [uri, arg.seconds_until_open_start, arg.rewards_per_open]
        )

        receipt = self.execute_tx(asset_contract.safe_batch_transfer_from.build_transaction(
            from_address, self.address, ids, amounts, params, self.get_transact_opts(),
        ))
        result = self.__abi_module.get_pack_created_event(
            receipt.transactionHash)
        new_pack_id = result[0]['args']['packId']
        return self.get(new_pack_id)

    def transfer_from(self, from_address: str, to_address: str, args: AssetAmountPair):
        """
        :param from_address: The address to transfer the token from.
        :param to_address: The address to transfer the token to.
        :param args: The token id and amount to transfer.
        :return: The transaction receipt.

        Transfers a token from a given address to a given address.

        """
        return self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            from_address, to_address, args.token_id, args.amount, "", self.get_transact_opts(),
        ))

    def transfer_batch_from(self, from_address: str, to_address: str, args: List[AssetAmountPair]):
        """
        :param from_address: The address to transfer the token from.
        :param to_address: The address to transfer the token to.
        :param args: The token ids and amounts to transfer.
        :return: The transaction receipt.

        Transfers a batch of tokens from a given address to a given address.

        """
        ids, amounts = [i.token_id for i in args], [i.amount for i in args]
        return self.execute_tx(self.__abi_module.safe_batch_transfer_from.build_transaction(
            from_address, to_address, ids, amounts, "", self.get_transact_opts(),
        ))

    def get_link_balance(self) -> CurrencyValue:
        """
        :return: The balance of the pack.

        WIP: This method is not ready to be called.

        """
        pass

    def deposit_link(self, amount: int):
        """
        :param amount: The amount to deposit.

        WIP: This method is not ready to be called.
        """
        pass

    def withdraw_link(self, to_address: str, amount: int):
        """
        :param to_address: The address to transfer the token to.
        :param amount: The amount to transfer.

        WIP: This method is not ready to be called.
        """
        pass

    def set_royalty_bps(self, amount: int):
        """
        :param amount: The amount to set the royalty BPS to.
        :return: The transaction receipt.

        Sets the royalty BPS for the pack.

        """
        return self.execute_tx(self.__abi_module.set_royalty_bps.build_transaction(
            amount, self.get_transact_opts()
        ))

    def set_restricted_transfer(self, restricted: bool = True):
        """
        :param restricted: Whether to grant restricted transfer or revoke it

        Sets restricted transfer for the NFT, defaults to restricted.

        """
        return self.execute_tx(self.__abi_module.set_restricted_transfer.build_transaction(
            restricted, self.get_transact_opts()
        ))

    def get_abi_module(self) -> Pack:
        """
        :return: The ABI module for the pack.

        Gets the ABI module for the pack.
        """
        return self.__abi_module
