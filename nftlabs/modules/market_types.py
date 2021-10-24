"""Types for the Merket Module."""

from dataclasses import dataclass
from typing import Optional


@dataclass.dataclass
class ListArg:
    """
    Arguments for listing a new item
    """
    market_type: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
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
    """ 
    Filter for the list_all method.
    """
    seller: Optional[str] = None
    tokenContract: Optional[str] = None
    tokenId: Optional[int] = None