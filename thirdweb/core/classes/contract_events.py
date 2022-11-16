from typing import Any, Callable, Dict, Generic, Tuple
from thirdweb.constants.events import EventType
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.types.contract import TContractABI
from thirdweb.types.events import EventQueryOptions, TxEvent
from web3.datastructures import AttributeDict
class ContractEvents(Generic[TContractABI]):
    _contract_wrapper: ContractWrapper[TContractABI]

    def __init__(self, contract_wrapper: ContractWrapper[TContractABI]):
        self._contract_wrapper = contract_wrapper

    def add_transaction_listener(self, listener: Callable[[TxEvent], Any]):
        """
        Add a listener for transaction events to this contract. This will be called
        whenever a transaction event is executed from the SDK interface.

        :param listener: The listener function to be called on transaction events.
        """

        self._contract_wrapper.add_listener(EventType.TRANSACTION, listener)  # type: ignore

    def remove_transaction_listener(self, listener: Callable[[TxEvent], Any]):
        """
        Remove a listener from transaction events.

        :param listener: The listener function to be removed.
        """

        self._contract_wrapper.remove_listener(EventType.TRANSACTION, listener)  # type: ignore

    def add_event_listener(
        self, event_name: str, listener: Callable[[Dict[str, Any]], None]
    ):
        """
        Add an event listener to this contract to listen for a specific event type.

        :param event_name: The name of the event to listen for.
        :param listener: The listener function to be called on the event.
        """

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
        """
        Remove an event listener listening to a specific event type.

        :param event_name: The name of the event to stop listening for.
        :param listener: The listener function to be removed.
        """

        interface = self._contract_wrapper.get_contract_interface()
        event = interface.events[event_name].abi

        self._contract_wrapper.remove_listener(event["name"], listener)

    def remove_all_listeners(self):
        """
        Remove all event listeners from this contract.
        """

        self._contract_wrapper.remove_all_listeners()

    def get_events(self, event_name: str, options: EventQueryOptions = EventQueryOptions()) -> Tuple[AttributeDict]:
        """
        Query past events of a specific type on the contract.

        :param event_name: The name of the event to query.
        :param options: The options to use when querying for events, including block range specifications and filters
        :return: A list of events.
        """

        events_interface = self._contract_wrapper.get_contract_interface().events[event_name]
        return events_interface.getLogs(options.filters, options.from_block, options.to_block)

