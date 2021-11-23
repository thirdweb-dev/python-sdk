from dataclasses import dataclass
from typing import Optional, Union
from dataclasses_json import dataclass_json
import io

@dataclass
class MintArg:
    name: str
    description: str = ""
    image: Union[str, io.TextIOWrapper] = ""
    properties: Optional[dict] = None
    image_uri: str = ""


@dataclass_json
@dataclass
class NftMetadata:
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    properties: Optional[Union[str, dict]] = None
    id: Optional[int] = None
    uri: Optional[str] = None
