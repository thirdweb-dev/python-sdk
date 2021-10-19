from dataclasses import dataclass
from typing import Optional, Union

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Listing:
    name: str
    description: str
    image: str
    properties: Optional[Union[str, dict]] = None
    token_id: int
    uri: str