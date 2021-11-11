from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from ..nft import NftMetadata
from ..metadata import Metadata


@dataclass_json
@dataclass
class CollectionMetadata:
    """
    COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD.
    """
    id: Optional[int] = None
    creator: Optional[str] = None
    supply: Optional[int] = None
    metadata: Optional[NftMetadata] = None


@dataclass_json
@dataclass
class CreateCollectionArg:
    """
    COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD.
    """
    metadata: Optional[Metadata] = None
    supply: Optional[int] = None


@dataclass_json
@dataclass
class MintCollectionArg:
    """
    COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD.
    """
    token_id: Optional[int] = None
    amount: Optional[int] = None
