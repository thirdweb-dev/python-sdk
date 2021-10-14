from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class NFT:
    name: str
    description: str
    image: str
    properties: Optional[str] = None
    id: Optional[int] = None
