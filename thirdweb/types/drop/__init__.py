"""
Types for Drop module.
"""

from dataclasses import dataclass
from typing import Optional, Union
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Query:
    start: int = None
    count: int = None


@dataclass_json
@dataclass
class claim:
    startTimestamp: int
    maxMintSupply: int
    currentMintSupply: int
    quantityLimitPerTransaction: int
    waitTimeSecondsLimitPerTransaction: int
    merkleRoot: bytes
    pricePerToken: int
    currency: str  # todo
