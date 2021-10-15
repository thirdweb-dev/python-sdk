import dataclasses


@dataclasses.dataclass
class Currency:
    name: str
    symbol: str
    decimals: int

@dataclasses.dataclass
class CurrencyValue(Currency):
    value: str
    display_value: str

