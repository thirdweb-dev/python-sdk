from dataclasses import dataclass
from typing import Any, Dict, Optional, Union


@dataclass
class NFTMetadataInput:
    """
    The metadata of an NFT to mint

    You can use the NFTMetadataInput.from_json(json) method to create
    an instance of this class from a dictionary.

    :param name: The name of the NFT
    :param description: The optional description of the NFT
    :param image: The optional image of the NFT
    :param external_url: The optional external URL of the NFT
    :param animation_url: The optional animation URL of the NFT
    :param background_color: The optional background color of the NFT
    :param properties: The optional properties of the NFT
    """

    name: str
    description: Optional[str] = None
    image: Optional[str] = None
    external_url: Optional[str] = None
    animation_url: Optional[str] = None
    background_color: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_json(json: Dict[str, Any]) -> "NFTMetadataInput":
        return NFTMetadataInput(
            json["name"],
            json.get("description"),
            json.get("image"),
            json.get("external_url"),
            json.get("animation_url"),
            json.get("background_color"),
            json.get("properties"),
        )

    def to_json(self) -> Dict[str, Any]:
        json: Dict[str, Any] = {}
        json["name"] = self.name
        if self.description is not None:
            json["description"] = self.description
        if self.image is not None:
            json["image"] = self.image
        if self.external_url is not None:
            json["external_url"] = self.external_url
        if self.animation_url is not None:
            json["animation_url"] = self.animation_url
        if self.background_color is not None:
            json["background_color"] = self.background_color
        if self.properties is not None:
            json["properties"] = self.properties

        return json


@dataclass
class NFTMetadata:
    id: int
    uri: str
    name: str
    description: Optional[str] = None
    image: Optional[str] = None
    external_url: Optional[str] = None
    animation_url: Optional[str] = None
    background_color: Optional[str] = None
    properties: Optional[Dict[Any, Any]] = None

    @staticmethod
    def from_json(json: Dict[str, Any]) -> "NFTMetadata":
        return NFTMetadata(
            json["id"],
            json["uri"],
            json["name"],
            json.get("description"),
            json.get("image"),
            json.get("external_url"),
            json.get("animation_url"),
            json.get("background_color"),
            json.get("properties"),
        )


@dataclass
class NFTMetadataOwner:
    metadata: NFTMetadata
    owner: str


@dataclass
class EditionMetadata:
    metadata: NFTMetadata
    supply: int


@dataclass
class EditionMetadataInput:
    """
    The metadata of an edition NFT to mint

    :param metadata: The metadata of the edition NFT
    :param supply: The supply of the edition NFT
    """

    metadata: Union[NFTMetadataInput, str]
    supply: int


@dataclass
class EditionMetadataOwner(EditionMetadata):
    owner: str
    quantity_owned: int


@dataclass
class QueryAllParams:
    start: int = 0
    count: int = 100
