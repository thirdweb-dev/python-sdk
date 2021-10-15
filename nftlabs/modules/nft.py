import copy

import json

from web3 import Web3

from . import BaseModule
from typing import Dict, List
from ..abi.nft import NFT

from ..types import NFT as NftType, Role
from .nft_types import MintArg


class NftModule(BaseModule):
    address: str
    __abi_module: NFT

    def __init__(self, address: str, client: Web3):
        super().__init__()
        self.address = address
        self.__abi_module = NFT(client, address)

    def mint(self, arg: MintArg):
        return self.mint_to(self.get_signer_address(), arg)

    def mint_to(
            self,
            to_address: str,
            arg: MintArg,
    ):
        final_properties: Dict
        if arg.properties is None:
            final_properties = {}
        else:
            final_properties = copy.copy(arg.properties)
        storage = self.get_storage()

        meta = {
            'name': arg.name,
            'description': arg.description,
            'image': arg.image_uri,
            'properties': final_properties
        }

        uri = storage.upload(json.dumps(meta), self.address, self.get_signer_address())
        tx = self.__abi_module.mint_nft.build_transaction(to_address, uri, self.get_transact_opts())
        receipt = self.execute_tx(tx)
        result = self.__abi_module.get_minted_event(tx_hash=receipt.transactionHash.hex())
        token_id = result[0]['args']['tokenId']
        return self.get(token_id)

    def total_supply(self) -> int:
        return self.__abi_module.total_supply.call()

    def get(self, nft_id: int) -> NftType:
        return self.__get_metadata(nft_id)

    def __get_metadata(self, nft_id: int) -> NftType:
        uri = self.__get_metadata_uri(nft_id)
        meta = self.get_storage().get(uri)
        meta_obj: NftType = NftType.from_json(meta)
        meta_obj.id = nft_id
        meta_obj.uri = uri
        return meta_obj

    def __get_metadata_uri(self, nft_id: int):
        uri = self.__abi_module.token_uri.call(nft_id)
        if uri == "":
            raise Exception("Could not find NFT metadata, are you sure it exists?")
        return uri

    def mint_batch(self, args: List[MintArg]):
        return self.mint_batch_to(self.get_signer_address(), args)

    def mint_batch_to(self, to_address: str, args: List[MintArg]):
        uris = [self.get_storage().upload(json.dumps({
            'name': arg.name,
            'description': arg.description,
            'image': arg.image_uri,
            'properties': arg.properties if arg.properties is not None else {}
        }), self.address, self.get_signer_address()) for arg in args]

        tx = self.__abi_module.mint_nft_batch.build_transaction(to_address, uris, self.get_transact_opts())

        receipt = self.execute_tx(tx)
        result = self.__abi_module.get_minted_batch_event(tx_hash=receipt.transactionHash.hex())
        token_ids = result[0]['args']['tokenIds']
        return [self.get(i) for i in token_ids]

    def burn(self, token_id: int):
        tx = self.__abi_module.burn.build_transaction(
            token_id,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    def transfer_from(self, from_address: str, to_address: str, token_id: int):
        tx = self.__abi_module.transfer_from.build_transaction(
            from_address,
            to_address,
            token_id,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    """
    Transfers NFT from the current signers wallet to another wallet
    """
    def transfer(self, to_address: str, token_id: int):
        tx = self.__abi_module.safe_transfer_from1.build_transaction(
            self.get_signer_address(),
            to_address,
            token_id,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    def set_royalty_bps(self, amount: int):
        tx = self.__abi_module.set_royalty_bps.build_transaction(amount, self.get_transact_opts())
        self.execute_tx(tx)

    def get_all(self) -> List[NftType]:
        max_id = self.__abi_module.next_token_id.call()
        return [self.get(i) for i in range(max_id)]

    """
    Defaults to fetching the NFTs owned by the current signer (as indicated by the private key)
    if the address parameter is not supplied
    """
    def get_owned(self, address: str = "") -> List[NftType]:
        if address == "":
            address = self.get_signer_address()

        balance = self.__abi_module.balance_of.call(address)
        owned_tokens = [self.__token_of_owner_by_index(address, i) for i in range(balance)]
        return [self.get(i) for i in owned_tokens]

    def __token_of_owner_by_index(self, address: str, token_id: int) -> int:
        return self.__abi_module.token_of_owner_by_index.call(address, token_id)

    """
    Returns balance of the current signers wallet
    """
    def balance(self) -> int:
        return self.__abi_module.balance_of.call(self.get_signer_address())

    def balance_of(self, address: str) -> int:
        return self.__abi_module.balance_of.call(address)

    def is_approved(self, address: str, operator: str) -> bool:
        return self.__abi_module.is_approved_for_all.call(address, operator)

    """
    Sets approval for specified operator, defaults to grant approval
    """
    def set_approval(self, operator: str, approved: bool = True):
        self.execute_tx(self.__abi_module.set_approval_for_all.call(
            operator, approved, self.get_transact_opts()
        ))

    def grant_role(self, role: Role, address: str):
        role_hash = role.get_hash()
        self.execute_tx(self.__abi_module.grant_role.build_transaction(
            role_hash, address, self.get_transact_opts()
        ))

    def revoke_role(self, role, address: str):
        role_hash = role.get_hash()
        self.execute_tx(self.__abi_module.revoke_role.build_transaction(
            role_hash, address, self.get_transact_opts()
        ))
