from dataclasses import dataclass
from typing import Optional, Union
from ..nft import NftMetadata
from ..currency import CurrenctValue
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Listing:
    id: str
    seller: str
    tokenContract: str
    tokenId: str
    tokenMetadata: NFTMetadata
    quantity: int
    currencyContract: str
    currencyMetadata: CurrencyValue | null
    price: int
    saleStart: str
    saleEnd: str