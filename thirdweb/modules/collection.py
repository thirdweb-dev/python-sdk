from typing import List
import warnings

from thirdweb_web3 import Web3

from ..abi.nft_collection import NFTCollection
from ..types.collection import (CollectionMetadata, CreateCollectionArg,
                                MintCollectionArg)
from ..types.metadata import Metadata
from ..types.nft import NftMetadata
from .base import BaseModule


class CollectionModule(BaseModule):
    """
    COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. .Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
    """
    address: str
    __abi_module: NFTCollection

    def __init__(self, address: str, client: Web3):
        super().__init__()
        self.address = address
        self.__abi_module = NFTCollection(client, address)

    def get(self, token_id: int) -> CollectionMetadata:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        uri = self.__abi_module.uri.call(token_id)
        meta_str = self.get_storage().get(uri)
        meta: NftMetadata = NftMetadata.from_json(meta_str)
        meta.id = token_id
        return CollectionMetadata(
            metadata=meta,
            supply=self.__abi_module.total_supply.call(token_id),
            creator=self.__abi_module.creator.call(token_id),
            id=token_id
        )

    def get_all(self) -> List[CollectionMetadata]:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        return [self.get(i) for i in range(self.__abi_module.next_token_id.call())]

    '''
    Returns the balance for a given token at owned by a specific address
    '''

    def balance_of(self, address: str, token_id: int) -> int:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        return self.__abi_module.balance_of.call(address, token_id)

    '''
    Returns the balance for a given token id for the current signers address
    '''

    def balance(self, token_id: int) -> int:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        return self.__abi_module.balance_of.call(
            self.get_signer_address(),
            token_id
        )

    def is_approved(self, address: str, operator: str) -> bool:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        return self.__abi_module.is_approved_for_all.call(
            address,
            operator
        )

    def set_approval(self, operator: str, approved: bool = True):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.execute_tx(self.__abi_module.set_approval_for_all.build_transaction(
            operator, approved, self.get_transact_opts()
        ))

    def transfer(self, to_address: str, token_id: int, amount: int):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            self.get_signer_address(), to_address, token_id, amount, "", self.get_transact_opts()
        ))

    def create(self, metadata: Metadata) -> CollectionMetadata:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        return self.create_batch([metadata])[0]

    def create_batch(self, metas: List[Metadata]) -> List[CollectionMetadata]:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        meta_with_supply = [CreateCollectionArg(
            metadata=m, supply=0) for m in metas]
        return self.create_and_mint_batch(meta_with_supply)

    def create_and_mint(self, meta_with_supply: CreateCollectionArg) -> CollectionMetadata:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        return self.create_and_mint_batch([meta_with_supply])[0]

    def create_and_mint_batch(self, meta_with_supply: List[CreateCollectionArg]) -> List[CollectionMetadata]:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        uris = [self.get_storage().upload(meta.to_json(), self.address,
                                          self.get_signer_address()) for meta in meta_with_supply]
        supplies = [a.supply for a in meta_with_supply]
        receipt = self.execute_tx(self.__abi_module.create_native_tokens.build_transaction(
            self.get_signer_address(), uris, supplies, "", self.get_transact_opts()
        ))
        result = self.__abi_module.get_native_tokens_event(
            tx_hash=receipt.transactionHash.hex())
        token_ids = result[0]['args']['tokenIds']
        return [self.get(i) for i in token_ids]

    def create_with_erc20(self, token_contract: str, token_amount: int, arg: CreateCollectionArg):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        uri = self.get_storage().upload(
            arg.metadata, self.address, self.get_signer_address())
        self.execute_tx(self.__abi_module.wrap_erc20.build_transaction(
            token_contract, token_amount, arg.supply, uri, self.get_transact_opts()
        ))

    def create_with_erc721(self, token_contract: str, token_id: int, metadata):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        uri = self.get_storage().upload(
            metadata.metadata, self.address, self.get_signer_address())
        self.execute_tx(self.__abi_module.wrap_erc721.build_transaction(
            token_contract, token_id, uri, self.get_transact_opts()
        ))

    def mint(self, args: MintCollectionArg):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.mint_to(self.get_signer_address(), args)

    def mint_to(self, to_address: str, arg: MintCollectionArg):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.execute_tx(self.__abi_module.mint.build_transaction(
            to_address, arg.token_id, arg.amount, "", self.get_transact_opts()
        ))

    def mint_batch(self, args: List[MintCollectionArg]):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.mint_batch_to(self.get_signer_address(), args)

    def mint_batch_to(self, to_address, args: List[MintCollectionArg]):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        ids = [a.token_id for a in args]
        amounts = [a.amount for a in args]
        tx = self.__abi_module.mint_batch.build_transaction(
            to_address, ids, amounts, self.get_transact_opts())
        self.execute_tx(tx)

    def burn(self, args: MintCollectionArg):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.burn_from(self.get_signer_address(), args)

    def burn_batch(self, args: List[MintCollectionArg]):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.burn_batch_from(self.get_signer_address(), args)

    def burn_from(self, account: str, args: MintCollectionArg):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.execute_tx(self.__abi_module.burn.build_transaction(
            account, args.token_id, args.amount, self.get_transact_opts()
        ))

    def burn_batch_from(self, account: str, args: List[MintCollectionArg]):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.execute_tx(self.__abi_module.burn_batch.build_transaction(
            account, [i.id for i in args], [
                i.amount for i in args], self.get_transact_opts()
        ))

    def transfer_from(self, from_address: str, to_address: str, args: MintCollectionArg):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            from_address, to_address, args.token_id, args.amount, "", self.get_transact_opts()
        ))

    def transfer_batch_from(self, from_address: str, to_address: str, args):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.execute_tx(self.__abi_module.safe_batch_transfer_from.build_transaction(
            from_address, to_address, args.token_id, args.amount, "", self.get_transact_opts()
        ))

    def set_royalty_bps(self, amount: int):
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        self.execute_tx(self.__abi_module.set_royalty_bps.build_transaction(
            amount, self.get_transact_opts()
        ))

    def get_abi_module(self) -> NFTCollection:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html
        """
        warnings.warn("COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD. Detailed documentation is available at https://python-docs.nftlabs.co/modules.bundle.html")
        return self.__abi_module
