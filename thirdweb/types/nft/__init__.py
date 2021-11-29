"""
Types for NFT module.
"""

from dataclasses import dataclass
from typing import Optional, Union
from dataclasses_json import dataclass_json
import io

@dataclass
class MintArg:
    """The name of the NFT being minted"""
    name: str
    """Short description of the NFT (optional)"""
    description: str = ""
    """
    Either an image URI *or* a `bytes`/`bytesarray` object.

    If the property is a `bytes`/`bytesarray` object, it'll be uploaded
    to the default storage provider and the uri will replace this properties
    value.
    """
    image: Union[str, bytes, bytearray] = ""
    properties: Optional[dict] = None
    """
    .. deprecated:: 0.4.0
        This property is deprecated. Use the `image` property instead
    """
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
