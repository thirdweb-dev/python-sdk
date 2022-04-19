from typing import Generic
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.types.contract import TContractABI


class ContractEvents(Generic[TContractABI]):
    _contract_wrapper: ContractWrapper[TContractABI]

    def __init__(self, contract_wrapper: ContractWrapper[TContractABI]):
        self._contract_wrapper = contract_wrapper

    def add_transaction_listener(self, listener):
        pass

    def remove_transaction_listener(self, listener):
        pass

    def add_event_listener(self, event_name, listener):
        pass

    def remove_event_listener(self, event_name, listner):
        pass
