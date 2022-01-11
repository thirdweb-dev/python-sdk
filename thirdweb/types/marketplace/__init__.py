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
@dataclass_json
class NewListing:
    """
    Arguments for listing a new item
    """
    assetContractAddress: str
    tokenId: int
    startTimeInSeconds: int
    listingDurationInSeconds: int
    quantity: int
    currencyContractAddress: str
    buyoutPricePerToken: int


@dataclass
@dataclass_json
class NewAuctionListing:
    """
    Arguments for listing a new item
    """
    assetContractAddress: str
    tokenId: int
    startTimeInSeconds: int
    listingDurationInSeconds: int
    quantity: int
    currencyContractAddress: str
    buyoutPricePerToken: int
    reservePricePerToken: int


@dataclass
@dataclass_json
class NewOffer:
    """
    Arguments for creating a new offer
    """
    listing_id: int
    quantity_desired: int
    currency_contract_address: str
    price_per_token: int


@dataclass
@dataclass_json
class NewBid:
    """
    Arguments for creating a new bid
    """
    listing_id: int
    price_per_token: int


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
