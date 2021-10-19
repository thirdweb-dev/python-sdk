from dataclasses import dataclass
from typing import Optional, Union

from dataclasses_json import dataclass_json


@dataclass
class MintArg:
    name: str
    description: str = ""
    image_uri: str = ""
    properties: Optional[dict] = None


@dataclass_json
@dataclass
class NftMetadata:
    name: str
    description: str
    image: str
    properties: Optional[Union[str, dict]] = None
    id: Optional[int] = None
    uri: Optional[str] = None
