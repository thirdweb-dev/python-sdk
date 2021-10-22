from dataclasses import dataclass

from ..nft import NftMetadata


@dataclass
class CollectionMetadata:
    creator: str
    supply: int
    metadata: NftMetadata
