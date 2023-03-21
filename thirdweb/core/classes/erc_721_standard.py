from typing import Generic
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_721 import ERC721
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import TERC721


class ERC721Standard(Generic[TERC721], BaseContract[TERC721]):
    _storage: IpfsStorage
    _erc721: ERC721

    def __init__(
        self,
        contract_wrapper: ContractWrapper,
        storage: IpfsStorage,
    ):
        super().__init__(contract_wrapper)
        self._storage = storage

        self._erc721 = ERC721(contract_wrapper, storage)
        self.get = self._erc721.get
        self.get_all = self._erc721.get_all
        self.get_total_count = self._erc721.get_total_count
        self.owner_of = self._erc721.owner_of
        self.total_supply = self._erc721.total_supply
        self.balance = self._erc721.balance
        self.balance_of = self._erc721.balance_of
        self.is_transfer_restricted = self._erc721.is_transfer_restricted
        self.is_approved = self._erc721.is_approved
        self.transfer = self._erc721.transfer
        self.burn = self._erc721.burn
        self.set_approval_for_all = self._erc721.set_approval_for_all
        self.set_approval_for_token = self._erc721.set_approval_for_token
