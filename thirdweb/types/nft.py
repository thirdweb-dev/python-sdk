from dataclasses import dataclass
from typing import Any, Dict, NewType, Optional, Union


@dataclass
class NFTMetadataInput:
    name: str
    description: Optional[str]
    image: Optional[str]
    external_url: Optional[str]
    animation_url: Optional[str]
    background_color: Optional[str]
    properties: Optional[Dict[str, Any]]

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
    description: Optional[str]
    image: Optional[str]
    external_url: Optional[str]
    animation_url: Optional[str]
    background_color: Optional[str]
    properties: Optional[Dict[Any, Any]]

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
