from dataclasses import dataclass
from typing import NewType

Price = float
PriceWei = int
Amount = Price


@dataclass
class Currency:
    name: str
    symbol: str
    decimals: int


@dataclass
class CurrencyValue(Currency):
    value: PriceWei
    display_value: Price


@dataclass
class TokenAmount:
    to_address: str
    amount: Price


@dataclass
class WrappedToken:
    address: str
    name: str
    symbol: str


@dataclass
class NativeToken:
    name: str
    symbol: str
    decimals: int
    wrapped: WrappedToken
