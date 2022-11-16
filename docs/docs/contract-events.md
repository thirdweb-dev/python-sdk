<a id="core.classes.contract_events"></a>

# core.classes.contract\_events

<a id="core.classes.contract_events.ContractEvents"></a>

## ContractEvents Objects

```python
class ContractEvents(Generic[TContractABI])
```

<a id="core.classes.contract_events.ContractEvents.add_transaction_listener"></a>

#### add\_transaction\_listener

```python
def add_transaction_listener(listener: Callable[[TxEvent], Any])
```

Add a listener for transaction events to this contract. This will be called

whenever a transaction event is executed from the SDK interface.

**Arguments**:

- `listener`: The listener function to be called on transaction events.

<a id="core.classes.contract_events.ContractEvents.remove_transaction_listener"></a>

#### remove\_transaction\_listener

```python
def remove_transaction_listener(listener: Callable[[TxEvent], Any])
```

Remove a listener from transaction events.

**Arguments**:

- `listener`: The listener function to be removed.

<a id="core.classes.contract_events.ContractEvents.add_event_listener"></a>

#### add\_event\_listener

```python
def add_event_listener(event_name: str, listener: Callable[[Dict[str, Any]],
                                                           None])
```

Add an event listener to this contract to listen for a specific event type.

**Arguments**:

- `event_name`: The name of the event to listen for.
- `listener`: The listener function to be called on the event.

<a id="core.classes.contract_events.ContractEvents.remove_event_listener"></a>

#### remove\_event\_listener

```python
def remove_event_listener(event_name: str, listener)
```

Remove an event listener listening to a specific event type.

**Arguments**:

- `event_name`: The name of the event to stop listening for.
- `listener`: The listener function to be removed.

<a id="core.classes.contract_events.ContractEvents.remove_all_listeners"></a>

#### remove\_all\_listeners

```python
def remove_all_listeners()
```

Remove all event listeners from this contract.

<a id="core.classes.contract_events.ContractEvents.get_events"></a>

#### get\_events

```python
def get_events(
    event_name: str, options: EventQueryOptions = EventQueryOptions()
) -> Tuple[AttributeDict]
```

Query past events of a specific type on the contract.

**Arguments**:

- `event_name`: The name of the event to query.
- `options`: The options to use when querying for events, including block range specifications and filters

**Returns**:

A list of events.

