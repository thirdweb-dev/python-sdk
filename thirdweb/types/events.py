from dataclasses import dataclass
from typing import Union

from thirdweb.constants.events import EventStatus


@dataclass
class TxEvent:
    status: EventStatus
    tx_hash: str


@dataclass
class SignatureEvent:
    status: EventStatus
    message: str
    signature: Union[str, bytes]
