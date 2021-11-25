"""
Types for the market module.
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from ..nft import NftMetadata
from ..currency import CurrencyValue
import datetime


@dataclass
class ListArg:
    """
    Arguments for listing a new item
    """
    asset_contract: str
    token_id: int
    currency_contract: str
    price_per_token: int
    quantity: int
    tokens_per_buyer: int
    seconds_until_start: int
    seconds_until_end: int


@dataclass
class Filter:
    """ 
    Filter for the list_all method.
    """
    seller: Optional[str] = None
    tokenContract: Optional[str] = None
    tokenId: Optional[int] = None


@dataclass_json
@dataclass
class MarketListing:
    listingId: int
    seller: str
    assetContract: str
    tokenId: int
    quantity: int
    currency: str
    pricePerToken: int
    saleStart: int
    saleEnd: int
    tokensPerBuyer: int
    tokenType: int


@dataclass_json
@dataclass
class Listing:
    id: str
    seller: str
    token_contract: str
    token_id: str
    quantity: int
    currency_contract: str
    price_per_token: int
    sale_start: datetime.datetime
    sale_end: datetime.datetime
    token_metadata: Optional[NftMetadata] = None
    currency_metadata: Optional[CurrencyValue] = None
