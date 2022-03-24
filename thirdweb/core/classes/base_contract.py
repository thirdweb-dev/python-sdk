from typing import Optional
from web3 import Web3
from eth_account.account import LocalAccount

from thirdweb.core.classes.contract_wrapper import ContractWrapper


class BaseContract:
    __contract_wrapper: ContractWrapper

    def __init__(self, contract_wrapper: ContractWrapper):
        self.__contract_wrapper = contract_wrapper

    def on_provider_updated(self, provider: Web3):
        self.__contract_wrapper.update_provider(provider)

    def on_signer_updated(self, signer: Optional[LocalAccount]):
        self.__contract_wrapper.update_signer(signer)

    def get_address(self):
        self.__contract_wrapper.__contract_abi.address
