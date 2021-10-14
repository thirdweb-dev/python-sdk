import dataclasses


@dataclasses.dataclass
class NFT:
    id: int
    name: str
    description: str
    image_uri: str
    properties: dict
