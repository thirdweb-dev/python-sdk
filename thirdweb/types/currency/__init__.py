"""Types for the Currency Module."""

import dataclasses
from dataclasses_json import dataclass_json


@dataclasses.dataclass
class Currency:
    """Currency class."""
    name: str
    symbol: str
    decimals: int


@dataclass_json
@dataclasses.dataclass
class TokenBatchMintArgs:
    address: str
    amount: int


@dataclasses.dataclass
class CurrencyValue(Currency):
    """ 
    Type for currency values.
    """
    value: str
    display_value: str
