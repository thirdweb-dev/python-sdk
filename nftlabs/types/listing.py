from dataclasses import dataclass
from typing import Optional, Union
from .nft import NftMetadata
from .currency import CurrencyValue
from dataclasses_json import dataclass_json
import datetime

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
