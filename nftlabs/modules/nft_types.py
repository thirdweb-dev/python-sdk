from dataclasses import dataclass
from typing import Optional


@dataclass
class MintArg:
    name: str
    description: str = ""
    image_uri: str = ""
    properties: Optional[dict] = None

