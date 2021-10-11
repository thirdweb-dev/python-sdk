import dataclasses


@dataclasses.dataclass
class Currency:
    name: str
    symbol: str
    decimals: int
