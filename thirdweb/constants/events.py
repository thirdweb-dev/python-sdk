from enum import Enum


class EventType(Enum):
    TRANSACTION = "transaction"
    SIGNATURE = "signature"


class EventStatus(Enum):
    SUBMITTED = "submitted"
    COMPLETED = "completed"
