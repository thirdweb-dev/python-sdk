from dataclasses import dataclass
from enum import Enum
from typing import Optional
from thirdweb.types.currency import CurrencyValue

from thirdweb.types.nft import NFTMetadata


class ListingType(Enum):
    DIRECT = 0
    AUCTION = 1


@dataclass
class MarketplaceFilter:
    start: int = 0
    count: int = 100
    seller: Optional[str] = None
    token_contract: Optional[str] = None
    token_id: Optional[int] = None


@dataclass
class NewDirectListing:
    type = "NewDirectListing"
    asset_contract_address: str
    token_id: int
    start_time_in_seconds: int
    listing_duration_in_seconds: int
    quantity: int
    currency_contract_address: str
    buyout_price_per_token: int


@dataclass
class NewAuctionListing:
    type = "NewAuctionListing"
    asset_contract_address: str
    token_id: int
    start_time_in_seconds: int
    listing_duration_in_seconds: int
    quantity: int
    currency_contract_address: str
    reserve_price_per_token: int
    buyout_price_per_token: int


@dataclass
class ContractListing:
    listing_id: int
    token_owner: str
    asset_contract: str
    token_id: int
    start_time: int
    end_time: int
    quantity: int
    currency: str
    reserve_price_per_token: int
    buyout_price_per_token: int
    token_type: int
    listing_type: int


@dataclass
class DirectListing:
    id: int
    asset_contract_address: str
    token_id: int
    asset: NFTMetadata
    start_time_in_seconds: int
    seconds_until_end: int
    quantity: int
    currency_contract_address: str
    buyout_currency_value_per_token: CurrencyValue
    buyout_price: int
    seller_address: str
    type = ListingType.DIRECT


@dataclass
class AuctionListing:
    id: int
    asset_contract_address: str
    token_id: int
    asset: NFTMetadata
    start_time_in_epoch_seconds: int
    end_time_in_epoch_seconds: int
    quantity: int
    currency_contract_address: str
    reserve_price: int
    buyout_price: int
    buyout_currency_value_per_token: CurrencyValue
    reserve_price_currency_value_per_token: CurrencyValue
    seller_address: str
    type = ListingType.AUCTION


@dataclass
class ContractOffer:
    listing_id: int
    offeror: str
    quantity_wanted: int
    currency: str
    price_per_token: int


@dataclass
class Offer:
    listing_id: int
    buyer_address: str
    quantity_desired: int
    price_per_token: int
    currency_value: CurrencyValue
    currency_contract_address: str
