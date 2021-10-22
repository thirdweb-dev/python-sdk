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
    token_contract: str
    token_id: str
    token_metadata: Optional[NFTMetadata] = None
    quantity: int
    currency_contract: str
    currency_metadata: CurrencyValue | null
    price: int
    sale_start: str
    sale_end: str