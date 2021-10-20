from dataclasses import dataclass
from typing import Optional


@dataclass.dataclass
class ListArg:
    asset_contract: str
    token_id: int
    currency_contract: str
    price_per_token: int
    quantity: int
    tokens_per_buyer: int
    seconds_until_start: int
    seconds_until_end: int


@dataclass.dataclass
class Filter:
    seller: Optional[str] = None
    tokenContract: Optional[str] = None
    tokenId: Optional[int] = None