from typing import Callable

import web3

from ..abi.coin import Coin
from .base import BaseModule
from .currency_types import Currency
from ..abi.erc20 import ERC20
from ..storage.ipfs_storage import IpfsStorage

from zero_ex.contract_wrappers import TxParams


class CurrencyModule(BaseModule):
    address: str
    __abi_module: Coin

    def __init__(
            self,
            address: str,
            get_client: Callable[[], web3.Web3],
            get_storage: Callable[[], IpfsStorage],
            get_signer_address: Callable[[], str],
            get_private_key: Callable[[], str],
            get_transact_opts: Callable[[], TxParams]
    ):
        super().__init__(get_client,get_storage, get_signer_address, get_private_key, get_transact_opts)

        self.address = address
        self.__abi_module = Coin(self.get_client(), address)

    def total_supply(self) -> int:
        return self.__abi_module.total_supply.call()

    """
    Gets the currency name, symbol, and decimals
    """
    def get(self) -> Currency:
        return self.__get_currency_metadata()

    def __get_currency_metadata(self):
        erc20_client = ERC20(self.get_client(), self.address)
        name = erc20_client.name.call()
        symbol = erc20_client.symbol.call()
        decimals = erc20_client.decimals.call()

        return Currency(name, symbol, decimals)

    def balance_of(self, address: str) -> int:
        return self.__abi_module.balance_of.call(address)

    # def balance(self):
    #     return self.__abi_module.balance_of.call(self.get_client().)
