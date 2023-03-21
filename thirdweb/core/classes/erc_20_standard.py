from typing import Generic
from thirdweb.abi.token_erc20 import TokenERC20
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_20 import ERC20
from thirdweb.core.classes.ipfs_storage import IpfsStorage

class ERC20Standard(BaseContract[TokenERC20]):
    _storage: IpfsStorage
    _erc20: ERC20

    def __init__(self, contract_wrapper: ContractWrapper, storage: IpfsStorage):
        super().__init__(contract_wrapper)
        self._storage = storage

        self._erc20 = ERC20(contract_wrapper, storage)
        self.get = self._erc20.get
        self.balance = self._erc20.balance
        self.balance_of = self._erc20.balance_of
        self.total_supply = self._erc20.total_supply
        self.allowance = self._erc20.allowance
        self.allowance_of = self._erc20.allowance_of
        self.is_transfer_restricted = self._erc20.is_transfer_restricted
        self.transfer = self._erc20.transfer
        self.transfer_from = self._erc20.transfer_from
        self.set_allowance = self._erc20.set_allowance
        self.transfer_batch = self._erc20.transfer_batch
        self.burn = self._erc20.burn
        self.burn_from = self._erc20.burn_from
