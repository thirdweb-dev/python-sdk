from dataclasses import dataclass
import dataclasses
from typing import Any, Dict, Optional, Union
from thirdweb.constants.events import EventStatus
from web3.types import BlockIdentifier


@dataclass
class TxEvent:
    status: EventStatus
    tx_hash: str


@dataclass
class SignatureEvent:
    status: EventStatus
    message: str
    signature: Union[str, bytes]

@dataclass
class EventQueryOptions:
    filters: Dict[str, Any] = dataclasses.field(default_factory=dict)
    from_block: Optional[BlockIdentifier] = "earliest"
    to_block: Optional[BlockIdentifier] = "latest"