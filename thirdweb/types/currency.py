from dataclasses import dataclass


@dataclass
class Currency:
    name: str
    symbol: str
    decimals: int


@dataclass
class CurrencyValue(Currency):
    value: int
    display_value: int


@dataclass
class TokenAmount:
    to_address: str
    amount: int


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
