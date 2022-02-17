"""
Interact with the Bundle module of the app. Previously `collection`.
"""

from typing import List
from thirdweb_web3 import Web3
from ..abi.erc20 import ERC20
from ..abi.nft import SignatureMint721 as NFT
from ..abi.nft_collection import NFTCollection as NFTBundle
from ..types.bundle import BundleMetadata, CreateBundleArg, MintBundleArg
from ..types.metadata import Metadata
from ..types.nft import NftMetadata
from .base import BaseModule


class BundleModule(BaseModule):
    """
    Interact with the Bundle module of the app. Previously `collection`.
    """
    address: str
    """
    Address of the module
    """
    __abi_module: NFTBundle

    def __init__(self, address: str, client: Web3):
        """
        :param address: The address of the module
        :param client: Web3 client

        Initializes the module
        """
        super().__init__()
        self.address = address
        self.__abi_module = NFTBundle(client, address)

    def get(self, token_id: int) -> BundleMetadata:
        """
        :param token_id: The token id to get
        :return: Metadata of the bundle

        Get the metadata for a given token id
        """
        uri = self.__abi_module.uri.call(token_id)
        meta_str = self.get_storage().get(uri)
        meta: NftMetadata = NftMetadata.from_json(meta_str)
        meta.id = token_id
        return BundleMetadata(
            metadata=meta,
            supply=self.__abi_module.total_supply.call(token_id),
            creator=self.__abi_module.creator.call(token_id),
            id=token_id
        )

    def get_all(self) -> List[BundleMetadata]:
        '''
        :return: A list of metadata

        Returns all the bundles in the contract

        '''
        return [self.get(i) for i in range(self.__abi_module.next_token_id.call())]

    def balance_of(self, address: str, token_id: int) -> int:
        '''
        :param address: The address to check
        :param token_id: The token id to check
        :return: The balance

        Returns the balance for a given token at owned by a specific address

        '''
        return self.__abi_module.balance_of.call(address, token_id)

    def balance(self, token_id: int) -> int:
        '''
        :param token_id: The token id to check
        :return: The balance

        Returns the balance for a given token id for the current signers address

        '''
        return self.__abi_module.balance_of.call(
            self.get_signer_address(),
            token_id
        )

    def is_approved(self, address: str, operator: str) -> bool:
        """
        :param address: The address to check
        :param operator: The operator to check
        :return: True if approved, False otherwise

        """
        return self.__abi_module.is_approved_for_all.call(address, operator)

    def set_approval(self, operator: str, approved: bool = True):
        """
        :param operator: The operator to set approval for
        :param approved: True if you want to approve, False otherwise
        """
        self.execute_tx(self.__abi_module.set_approval_for_all.build_transaction(
            operator, approved, self.get_transact_opts()
        ))

    def transfer(self, to_address: str, token_id: int, amount: int):
        """
        :param to_address: The address to transfer to
        :param token_id: The token id to transfer
        :param amount: The amount to transfer

        Transfers a token to a new owner

        """
        self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            self.get_signer_address(), to_address, token_id, amount, "", self.get_transact_opts()
        ))

    def create(self, metadata: Metadata) -> BundleMetadata:
        """
        :param metadata: The metadata to be stored
        :return: Metadata of the bundle

        Creates a bundle.

        """
        return self.create_batch([metadata])[0]

    def create_batch(self, metas: List[Metadata]) -> List[BundleMetadata]:
        """
        :param metas: The metadata to be stored
        :return: List of metadatas of the bundles

        Creates a bundle of NFTs

        """
        meta_with_supply = [CreateBundleArg(
            metadata=m, supply=0) for m in metas]
        return self.create_and_mint_batch(meta_with_supply)

    def create_and_mint(self, meta_with_supply: CreateBundleArg) -> BundleMetadata:
        """
        :param meta_with_supply: Metadata with supply
        :return: A metadata with supply

        Create a bundle and mint it to the current signer address

        """
        return self.create_and_mint_batch([meta_with_supply])[0]

    def create_and_mint_batch(self, meta_with_supply: List[CreateBundleArg]) -> List[BundleMetadata]:
        """
        :param meta_with_supply: A list of metadata with supply
        :return: A list of metadata with supply

        Creates bundles and mints them to the current signer address

        """
        if len(meta_with_supply) == 0:
            raise Exception("No metadata supplied")
        uris = [self.upload_metadata(meta.metadata)
                for meta in meta_with_supply]
        supplies = [a.supply for a in meta_with_supply]
        receipt = self.execute_tx(self.__abi_module.create_native_tokens.build_transaction(
            self.get_signer_address(), uris, supplies, "", self.get_transact_opts()
        ))
        result = self.__abi_module.get_native_tokens_event(
            tx_hash=receipt.transactionHash.hex())
        token_ids = result[0]['args']['tokenIds']
        return [self.get(i) for i in token_ids]

    def create_with_token(self, token_contract: str, token_amount: int, metadata: dict = None):
        """
        :param token_contract: The address of the token contract
        :param token_amount: The amount of tokens to mint
        :param metadata: The metadata to be stored

        WIP: This method is not yet complete. 

        """
        if token_contract == "" or token_contract is None or not self.get_client().isAddress(token_contract):
            raise Exception("token_contract not a valid address")
        if token_amount <= 0:
            raise Exception("token_amount must be greater than 0")

        uri = self.upload_metadata(metadata)
        erc20 = ERC20(self.get_client(), token_contract)
        allowance = erc20.allowance.call(
            self.get_signer_address(), self.address)
        if allowance < token_amount:
            tx = erc20.increase_allowance.build_transaction(self.address,
                                                            token_amount,
                                                            self.get_transact_opts())
            self.execute_tx(tx)

        self.execute_tx(self.__abi_module.wrap_erc20.build_transaction(
            token_contract, token_amount, token_amount, uri, self.get_transact_opts()
        ))

    def create_with_nft(self, token_contract: str, token_id: int, metadata):
        """
        :param token_contract: The address of the token contract
        :param token_id: The id of the token
        :param metadata: The metadata to be stored

        WIP: This method is not yet complete.

        """
        asset = NFT(self.get_client(), token_contract)
        approved = asset.is_approved_for_all.call(
            self.get_signer_address(), self.address)

        if not approved:
            is_token_approved = asset.get_approved.call(
                token_id).lower() == self.address.lower()
            if not is_token_approved:
                self.execute_tx(asset.set_approval_for_all.build_transaction(
                    self.address, True, self.get_transact_opts()))

        uri = self.upload_metadata(metadata)
        self.execute_tx(self.__abi_module.wrap_erc721.build_transaction(
            token_contract, token_id, uri, self.get_transact_opts()
        ))

    def create_with_erc721(self, token_contract: str, token_id: int, metadata):
        """
        :param token_contract: The address of the token contract
        :param token_id: The id of the token
        :param metadata: The metadata to be stored

        WIP: This method is not yet complete. Same as create_with_nft()

        """
        return self.create_with_nft(token_contract, token_id, metadata)

    def create_with_erc20(self, token_contract: str, token_amount: int, metadata):
        """
        :param token_contract: The address of the token contract
        :param token_amount: The amount of tokens to mint
        :param metadata: The metadata to be stored

        WIP: This method is not yet complete. Same as create_with_token()

        """
        return self.create_with_token(token_contract, token_amount, metadata)

    def mint(self, args: MintBundleArg):
        """
        :param args: The arguments for the mint

        Mints a bundle to the current signer address

        """
        self.mint_to(self.get_signer_address(), args)

    def mint_to(self, to_address: str, arg: MintBundleArg):
        """
        :param to_address: The address to mint to
        :param arg: The arguments for the mint

        Mints a bundle to the given address

        """
        self.execute_tx(self.__abi_module.mint.build_transaction(
            to_address, arg.token_id, arg.amount, "", self.get_transact_opts()
        ))

    def mint_batch(self, args: List[MintBundleArg]):
        """
        :param args: The arguments for the mint

        Mints a list of bundles to the current signer address

        """
        self.mint_batch_to(self.get_signer_address(), args)

    def mint_batch_to(self, to_address, args: List[MintBundleArg]):
        """
        :param to_address: The address to mint to
        :param args: The arguments for the mint
        :return: A list of minted bundles

        Mints a list of bundles to the given address

        """

        ids = [a.token_id for a in args]
        amounts = [a.amount for a in args]
        tx = self.__abi_module.mint_batch.build_transaction(
            to_address, ids, amounts, self.get_transact_opts())
        self.execute_tx(tx)

    def burn(self, args: MintBundleArg):
        """
        :param args: The arguments for the burn

        Burns a bundle from the current signer address

        """

        self.burn_from(self.get_signer_address(), args)

    def burn_batch(self, args: List[MintBundleArg]):
        """
        :param args: List of the arguments to burn

        Burns a list of bundles from the current signer address

        """
        self.burn_batch_from(self.get_signer_address(), args)

    def burn_from(self, account: str, args: MintBundleArg):
        """
        :param account: The account to burn from
        :param args: The arguments for the burn

        Burns a bundle from the given account

        """

        self.execute_tx(self.__abi_module.burn.build_transaction(
            account, args.token_id, args.amount, self.get_transact_opts()
        ))

    def burn_batch_from(self, account: str, args: List[MintBundleArg]):
        """
        :param account: The account to burn from
        :param args: The arguments for the burn

        Burns a list of bundles from the given account

        """

        self.execute_tx(self.__abi_module.burn_batch.build_transaction(
            account, [i.id for i in args], [
                i.amount for i in args], self.get_transact_opts()
        ))

    def transfer_from(self, from_address: str, to_address: str, args: MintBundleArg):
        """
        :param from_address: The account to transfer from
        :param to_address: The address to transfer to
        :param args: The arguments for the transfer

        Transfers a bundle from the given account to the given address

        """
        self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            from_address, to_address, args.token_id, args.amount, "", self.get_transact_opts()
        ))

    def transfer_batch_from(self, from_address: str, to_address: str, args):
        """
        :param from_address: The account to transfer from
        :param to_address: The address to transfer to
        :param args: The arguments for the transfer

        Transfers a list of bundles from the given account to the given address

        """
        self.execute_tx(self.__abi_module.safe_batch_transfer_from.build_transaction(
            from_address, to_address, args.token_id, args.amount, "", self.get_transact_opts()
        ))

    def set_royalty_bps(self, amount: int):
        """
        :param amount: The amount of BPS to set

        Sets the royalty BPS

        """

        self.execute_tx(self.__abi_module.set_royalty_bps.build_transaction(
            amount, self.get_transact_opts()
        ))

    def get_abi_module(self) -> NFTBundle:
        """
        :return: The ABI module

        Returns the ABI module
        """
        return self.__abi_module
