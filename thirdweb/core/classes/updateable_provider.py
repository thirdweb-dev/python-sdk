from thirdweb.core.classes.contract_wrapper import ContractWrapper
from web3 import Web3

class UpdateableProvider:
    __contract_wrapper: ContractWrapper

    def __init__(self, contract_wrapper: ContractWrapper):
        self.__contract_wrapper = contract_wrapper

    def on_update_provider(self, provider: Web3):
        self.contract_wrapper.update_provider = provider

    def get_address(self) -> str:
        return self.contract_wrapper.read_contract.address