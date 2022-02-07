"""
Types for NFT module.
"""

from dataclasses import dataclass
from typing import Any, Optional, Union
from dataclasses_json import dataclass_json


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


@dataclass_json
@dataclass
class BatchGeneratedSignature:
    payload: Any
    signature: str

@dataclass_json
@dataclass
class MintRequestStructOutput:
    to: str
    price: int
    currency: str
    validity_start_timestamp: int
    validity_end_timestamp: int
    uid: str

@dataclass_json
@dataclass
class SignaturePayload:
    metadata: dict
    to: str
    price: int
    currency_address: str
    mint_start_time_epoch_seconds: int
    mint_end_time_epoch_seconds: int
    id: Optional[str] = None


@dataclass_json
@dataclass
class NewSignaturePayload:
    metadata: dict
    mint_start_time_epoch_seconds: int
    mint_end_time_epoch_seconds: int
    uri: Optional[str] = None
    price: int = 0
    currency_address: str = "0x0000000000000000000000000000000000000000"
    to: str = "0x0000000000000000000000000000000000000000"
    id: Optional[str] = None
