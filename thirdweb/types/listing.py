"""
Type for a listing.
"""

import datetime
from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from .currency import CurrencyValue
from .nft import NftMetadata


@dataclass_json
@dataclass
class Listing:
    """A listing of an some asset (e.g. a NFT, Bundle, Pack, etc.)

    Attributes:
        id        (str): The id of the listing
        seller    (str): The wallet address of the seller
        token_contract (str): The address of the token contract
        token_id  (str): The id of the token (e.g. id of NFT, Pack, or Bundle)
        quantity  (int): The quantity of token being listed (a single listing could sell >= 1 token)
        currency_contract (str): The address of the currency contract. This property is set to 0x0 if the listing is free.
        price_per_token (int): The price per token. E.g. if the currency_contract is pointing to a contract with token symbol $DAI, then this listing costs (price_per_token * $DAI).
        sale_start (datetime.datetime): The date and time when the sale starts
        sale_end (datetime.datetime): The date and time when the sale ends
        token_metadata (Metadata): The metadata of the token being listed
        tokens_per_buyer (int): The number of tokens that a buyer is allowed to purchase from a listing
        currency_metadata (CurencyValue): Contains the display value and converted price of the listing based on the currency contract
    """
    id: str
    seller: str
    token_contract: str
    token_id: str
    quantity: int
    currency_contract: str
    price_per_token: int
    sale_start: datetime.datetime
    sale_end: datetime.datetime
    tokens_per_buyer: int
    token_metadata: Optional[NftMetadata] = None
    currency_metadata: Optional[CurrencyValue] = None
