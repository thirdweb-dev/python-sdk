from typing import Any, Callable, Dict, Generic
from thirdweb.constants.events import EventType
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.types.contract import TContractABI


class ContractEvents(Generic[TContractABI]):
    _contract_wrapper: ContractWrapper[TContractABI]

    def __init__(self, contract_wrapper: ContractWrapper[TContractABI]):
        self._contract_wrapper = contract_wrapper

    def add_transaction_listener(self, listener):
        self._contract_wrapper.add_listener(EventType.TRANSACTION, listener)

    def remove_transaction_listener(self, listener):
        self._contract_wrapper.remove_listener(EventType.TRANSACTION, listener)

    def add_event_listener(
        self, event_name: str, listener: Callable[[Dict[str, Any]], None]
    ):
        interface = self._contract_wrapper.get_contract_interface()
        event = interface.events[event_name].abi
        event_names = [i["name"] for i in event["inputs"]]

        def event_listener(*args):
            results: Dict[str, Any] = {}
            for i, arg in enumerate(event_names):
                results[arg] = args[i]
            listener(results)

        self._contract_wrapper.on(event["name"], event_listener)

    def remove_event_listener(self, event_name: str, listener):
        interface = self._contract_wrapper.get_contract_interface()
        event = interface.events[event_name].abi

        self._contract_wrapper.remove_listener(event["name"], listener)

    def remove_all_listeners(self):
        self._contract_wrapper.remove_all_listeners()
