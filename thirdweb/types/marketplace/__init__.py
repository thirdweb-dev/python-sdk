"""
Types for the market module.
"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
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
    listing_type: str = "NewDirectListing"


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
    listing_type: str = "NewAuctionListing"


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


@dataclass
@dataclass_json
class DirectListing:
    id: str
    assetContractAddress: str
    tokenId: int
    asset: NftMetadata
    startTimeInSeconds: int
    secondsUntilEnd: int
    quantity: int
    currencyContractAddress: str
    buyoutCurrencyValuePerToken: CurrencyValue
    buyoutPrice: int
    sellerAddress: int
    listing_type: int


@dataclass
@dataclass_json
class AuctionListing:
    id: str
    assetContractAddress: str
    tokenId: int
    asset: NftMetadata
    startTimeInSeconds: int
    secondsUntilEnd: int
    quantity: int
    currencyContractAddress: str
    buyoutCurrencyValuePerToken: CurrencyValue
    reservePriceCurrencyValuePerToken: CurrencyValue
    reservePrice: int
    buyoutPrice: int
    sellerAddress: int
    listing_type: int

@dataclass
@dataclass_json
class Offer:
  listingId: int
  buyerAddress: str
  quantityDesired: int
  pricePerToken: int
  currencyValue: CurrencyValue
  currencyContractAddress: str  