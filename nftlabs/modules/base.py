from typing import Callable

import web3


class BaseModule:
    get_client: Callable[[], web3.Web3]



    def __init__(self, get_client: Callable[[], web3.Web3]):
        self.get_client = get_client
