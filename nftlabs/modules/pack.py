from typing import Dict, List

from web3 import Web3

from ..abi.pack import Pack
from ..errors import AssetNotFoundException
from ..types.currency import CurrencyValue
from ..types.nft import NftMetadata
from ..types.pack import (AssetAmountPair, CreatePackArg, PackMetadata,
                          PackNftMetadata)
from .base import BaseModule


class PackModule(BaseModule):
    address: str
    __abi_module: Pack

    def __init__(self, address: str, client: Web3):
        super().__init__()
        self.address = address
        self.__abi_module = Pack(client, address)

    def get(self, pack_id: int) -> PackMetadata:
        uri = self.__abi_module.token_uri.call(pack_id)
        if uri == "":
            raise AssetNotFoundException(pack_id)
        metadata = self.get_storage().get(uri)
        return None

    def open(self, pack_id: int) -> List[NftMetadata]:
        pass

    def get_all(self) -> List[PackMetadata]:
        pass

    def get_nfts(self, pack_id: int) -> List[PackNftMetadata]:
        pass

    def balance_of(self, address: str, token_id: int) -> int:
        return self.__abi_module.balance_of.call(address, token_id)

    def balance(self, token_id: int) -> int:
        return self.__abi_module.balance_of.call(self.get_signer_address(), token_id)

    def is_approved(self, address: str, operator: str) -> bool:
        return self.__abi_module.is_approved_for_all.call(address, operator)

    def set_approval(self, operator: str, approved: bool):
        return self.execute_tx(self.__abi_module.set_approval_for_all.build_transaction(
            operator, approved, self.get_transact_opts()
        ))

    def transfer(self, to_address: str, token_id: int, amount: int):
        return self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            self.get_signer_address(), to_address, token_id, amount, "", self.get_transact_opts(),
        ))

    def create(self, arg: CreatePackArg) -> PackMetadata:
        pass

    def transfer_from(self, from_address: str, to_address: str, args: AssetAmountPair):
        return self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            from_address, to_address, args.token_id, args.amount, "", self.get_transact_opts(),
        ))

    def transfer_batch_from(self, from_address: str, to_address: str, args: List[AssetAmountPair]):
        ids, amounts = [i.token_id for i in args], [i.amount for i in args]
        return self.execute_tx(self.__abi_module.safe_batch_transfer_from.build_transaction(
            from_address, to_address, ids, amounts, "", self.get_transact_opts(),
        ))

    def get_link_balance(self) -> CurrencyValue:
        """
        WIP: This method is not ready to be called.
        """
        pass

    def deposit_link(self, amount: int):
        """
        WIP: This method is not ready to be called.
        """
        pass

    def withdraw_link(self, to_address: str, amount: int):
        """
        WIP: This method is not ready to be called.
        """
        pass

    def set_royalty_bps(self, amount: int):
        return self.execute_tx(self.__abi_module.set_royalty_bps.build_transaction(
            amount, self.get_transact_opts()
        ))

    def set_restricted_transfer(self, restricted: bool = True):
        return self.execute_tx(self.__abi_module.set_restricted_transfer.build_transaction(
            restricted, self.get_transact_opts()
        ))

    def get_abi_module(self) -> Pack:
        return self.__abi_module
