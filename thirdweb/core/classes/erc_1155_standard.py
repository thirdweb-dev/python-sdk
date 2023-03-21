from typing import Generic
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_1155 import ERC1155
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import TERC1155


class ERC1155Standard(Generic[TERC1155], BaseContract[TERC1155]):
    _storage: IpfsStorage
    _erc1155: ERC1155

    def __init__(self, contract_wrapper: ContractWrapper, storage: IpfsStorage):
        super().__init__(contract_wrapper)
        self._storage = storage

        self._erc1155 = ERC1155(contract_wrapper, storage)
        self.get = self._erc1155.get
        self.get_all = self._erc1155.get_all
        self.get_total_count = self._erc1155.get_total_count
        self.get_owned = self._erc1155.get_owned
        self.total_supply = self._erc1155.total_supply
        self.balance = self._erc1155.balance
        self.balance_of = self._erc1155.balance_of
        self.is_transfer_restricted = self._erc1155.is_transfer_restricted
        self.is_approved = self._erc1155.is_approved
        self.transfer = self._erc1155.transfer
        self.burn = self._erc1155.burn
        self.set_approval_for_all = self._erc1155.set_approval_for_all