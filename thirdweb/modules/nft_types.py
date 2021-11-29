"""Deprecated. Use `types.nft` instead."""
from dataclasses import dataclass
from typing import Optional, Union
import io


@dataclass
class MintArg:
    """
    Arguments for minting new tokens
    """
    name: str
    description: str = ""
    image: Union[str, io.TextIOWrapper] = ""
    properties: Optional[dict] = None
    image_uri: str = ""

