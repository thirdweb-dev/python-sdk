from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from ..nft import NftMetadata


@dataclass_json
@dataclass
class CollectionMetadata:
    id: Optional[int] = None
    creator: Optional[str] = None
    supply: Optional[int] = None
    metadata: Optional[NftMetadata] = None
