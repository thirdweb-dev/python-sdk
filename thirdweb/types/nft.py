from dataclasses import dataclass
from typing import Any, Dict, NewType, Optional, Union


@dataclass
class NFTMetadata:
    id: int
    uri: str
    name: str
    description: Optional[str]
    image: Optional[str]
    external_url: Optional[str]
    animation_url: Optional[str]
    background_color: Optional[str]
    properties: Optional[Dict[Any, Any]]


@dataclass
class NFTMetadataOwner:
    metadata: NFTMetadata
    owner: str


@dataclass
class EditionMetadata:
    metadata: NFTMetadata
    supply: int


@dataclass
class QueryAllParams:
    start: int = 0
    count: int = 100
