from typing import Optional
from thirdweb.types.sdk import SDKOptions
from web3 import Web3, HttpProvider

class AccountHandler(object):
    __provider: Web3
    __options: SDKOptions

    def __init__(self, provider: Web3, options: SDKOptions):
        self.__provider = provider
        self.__options = options

    def update_provider(self, provider: Web3):
        self.__provider = provider

    def get_provider(self) -> Web3:
        return self.__provider
    
    def __get_read_only_provider__(self) -> Optional[Web3]:
        if (self.__options.read_only_rpc_url != ""):
            return Web3(HttpProvider(self.__options.read_only_rpc_url))
        return None