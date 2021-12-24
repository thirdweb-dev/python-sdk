"""Deprecated. Use `types.nft` instead."""
import io
from dataclasses import dataclass
from typing import Optional, Union


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
