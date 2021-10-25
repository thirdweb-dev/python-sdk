"""Types for the Currency Module."""

import dataclasses


@dataclasses.dataclass
class Currency:
    """Currency class."""
    name: str
    symbol: str
    decimals: int


@dataclasses.dataclass
class CurrencyValue(Currency):
    """ 
    Type for currency values.
    """
    value: str
    display_value: str
