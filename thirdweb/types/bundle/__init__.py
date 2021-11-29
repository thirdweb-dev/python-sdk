"""Types for the bundle module"""

from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from ..nft import NftMetadata
from ..metadata import Metadata


@dataclass_json
@dataclass
class BundleMetadata:
    """
    Metadata for a bundle
    """
    id: Optional[int] = None
    """
    ID of the bundle
    """
    creator: Optional[str] = None
    """
    Creator of the bundle
    """
    supply: Optional[int] = None
    """
    Supply of the bundle
    """
    metadata: Optional[NftMetadata] = None


@dataclass_json
@dataclass
class CreateBundleArg:
    metadata: Optional[Metadata] = None
    supply: Optional[int] = None


@dataclass_json
@dataclass
class MintBundleArg:
    token_id: Optional[int] = None
    amount: Optional[int] = None

