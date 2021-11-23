from typing import List

from thirdweb_web3 import Web3

from ..abi.erc20 import ERC20
from ..abi.nft import NFT
from ..abi.nft_collection import NFTCollection as NFTBundle
from ..constants import ZeroAddress
from ..types.bundle import BundleMetadata, CreateBundleArg, MintBundleArg
from ..types.metadata import Metadata
from ..types.nft import NftMetadata
from .base import BaseModule


class BundleModule(BaseModule):
    address: str
    __abi_module: NFTBundle

    def __init__(self, address: str, client: Web3):
        super().__init__()
        self.address = address
        self.__abi_module = NFTBundle(client, address)

    def get(self, token_id: int) -> BundleMetadata:
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
        Returns all the bundles in the contract
        '''
        return [self.get(i) for i in range(self.__abi_module.next_token_id.call())]

    def balance_of(self, address: str, token_id: int) -> int:
        '''
        Returns the balance for a given token at owned by a specific address
        '''
        return self.__abi_module.balance_of.call(address, token_id)

    def balance(self, token_id: int) -> int:
        '''
        Returns the balance for a given token id for the current signers address
        '''
        return self.__abi_module.balance_of.call(
            self.get_signer_address(),
            token_id
        )

    def is_approved(self, address: str, operator: str) -> bool:
        return self.__abi_module.is_approved_for_all.call(address, operator)

    def set_approval(self, operator: str, approved: bool = True):
        self.execute_tx(self.__abi_module.set_approval_for_all.build_transaction(
            operator, approved, self.get_transact_opts()
        ))

    def transfer(self, to_address: str, token_id: int, amount: int):
        self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            self.get_signer_address(), to_address, token_id, amount, "", self.get_transact_opts()
        ))

    def create(self, metadata: Metadata) -> BundleMetadata:
        return self.create_batch([metadata])[0]

    def create_batch(self, metas: List[Metadata]) -> List[BundleMetadata]:
        meta_with_supply = [CreateBundleArg(
            metadata=m, supply=0) for m in metas]
        return self.create_and_mint_batch(meta_with_supply)

    def create_and_mint(self, meta_with_supply: CreateBundleArg) -> BundleMetadata:
        return self.create_and_mint_batch([meta_with_supply])[0]

    def create_and_mint_batch(self, meta_with_supply: List[CreateBundleArg]) -> List[BundleMetadata]:
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
        WIP: This method is not yet complete.
        """
        #token_module = sdk.get_nft_module(token_contract)
        nft_module = NFT(self.get_client(), token_contract)

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
        return self.create_with_nft(token_contract, token_id, metadata)

    def create_with_erc20(self, token_contract: str, token_amount: int, metadata):
        return self.create_with_token(token_contract, token_amount, metadata)

    def mint(self, args: MintBundleArg):
        self.mint_to(self.get_signer_address(), args)

    def mint_to(self, to_address: str, arg: MintBundleArg):
        self.execute_tx(self.__abi_module.mint.build_transaction(
            to_address, arg.token_id, arg.amount, "", self.get_transact_opts()
        ))

    def mint_batch(self, args: List[MintBundleArg]):
        self.mint_batch_to(self.get_signer_address(), args)

    def mint_batch_to(self, to_address, args: List[MintBundleArg]):
        ids = [a.token_id for a in args]
        amounts = [a.amount for a in args]
        tx = self.__abi_module.mint_batch.build_transaction(
            to_address, ids, amounts, self.get_transact_opts())
        self.execute_tx(tx)

    def burn(self, args: MintBundleArg):
        self.burn_from(self.get_signer_address(), args)

    def burn_batch(self, args: List[MintBundleArg]):
        self.burn_batch_from(self.get_signer_address(), args)

    def burn_from(self, account: str, args: MintBundleArg):
        self.execute_tx(self.__abi_module.burn.build_transaction(
            account, args.token_id, args.amount, self.get_transact_opts()
        ))

    def burn_batch_from(self, account: str, args: List[MintBundleArg]):
        self.execute_tx(self.__abi_module.burn_batch.build_transaction(
            account, [i.id for i in args], [
                i.amount for i in args], self.get_transact_opts()
        ))

    def transfer_from(self, from_address: str, to_address: str, args: MintBundleArg):
        self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            from_address, to_address, args.token_id, args.amount, "", self.get_transact_opts()
        ))

    def transfer_batch_from(self, from_address: str, to_address: str, args):
        self.execute_tx(self.__abi_module.safe_batch_transfer_from.build_transaction(
            from_address, to_address, args.token_id, args.amount, "", self.get_transact_opts()
        ))

    def set_royalty_bps(self, amount: int):
        self.execute_tx(self.__abi_module.set_royalty_bps.build_transaction(
            amount, self.get_transact_opts()
        ))

    def get_abi_module(self) -> NFTBundle:
        return self.__abi_module
