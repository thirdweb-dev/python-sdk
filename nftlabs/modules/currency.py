from typing import Callable

import web3

from nftlabs.abi.coin import Coin
from nftlabs.modules.base import BaseModule


class CurrencyModule(BaseModule):
    address: str
    __abi_module: Coin

    def __init__(self, get_client: Callable[[], web3.Web3], address: str):
        super().__init__(get_client)

        self.__abi_module = Coin(self.get_client(), address)

    def total_supply(self) -> int:
        return self.__abi_module.total_supply.call()
