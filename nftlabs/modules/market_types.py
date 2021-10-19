from dataclasses import dataclass


@dataclass.dataclass
class ListArg:
    asset_contract: str
    token_id: int
    currency: str
    price_per_token: int
    quantity: int
    tokens_per_buyer: int
    seconds_until_start: int
    seconds_until_end: int


@dataclass.dataclass
class ListUpdate:
    listing_id : int
    price_per_token: int
    currency: int
    tokens_per_buyer: int
    seconds_until_start: int
    seconds_until_end: int