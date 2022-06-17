from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class LoginOptions:
    nonce: Optional[str] = None
    expirationTime: Optional[datetime] = None
    chainId: Optional[int] = None


@dataclass
class LoginPayloadData:
    domain: str
    address: str
    nonce: str
    expirationTime: datetime
    chainId: Optional[int] = None


@dataclass
class LoginPayload:
    payload: LoginPayloadData
    signature: str


@dataclass
class VerifyOptions:
    chainId: Optional[int] = None


@dataclass
class AuthenticationOptions:
    invalidBefore: Optional[datetime] = None
    expirationTime: Optional[datetime] = None


@dataclass
class AuthenticationPayloadData:
    iss: str
    sub: str
    aud: str
    exp: int
    nbf: int
    iat: int
    jti: str


@dataclass
class AuthenticationPayload:
    payload: AuthenticationPayloadData
    signature: str
