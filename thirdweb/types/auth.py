from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional


@dataclass
class LoginOptions:
    nonce: Optional[str] = None
    expiration_time: Optional[datetime] = None
    chain_id: Optional[int] = None


@dataclass
class LoginPayloadData:
    domain: str
    address: str
    nonce: str
    expiration_time: datetime
    chain_id: Optional[int] = None

    @staticmethod
    def from_json(json: Dict[str, Any]) -> "LoginPayloadData":
        return LoginPayloadData(
            json["domain"],
            json["address"],
            json["nonce"],
            datetime.strptime(json["expiration_time"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            json.get("chain_id"),
        )


@dataclass
class LoginPayload:
    payload: LoginPayloadData
    signature: str

    @staticmethod
    def from_json(json: Dict[str, Any]) -> "LoginPayload":
        data = LoginPayloadData.from_json(json["payload"])
        return LoginPayload(
            data,
            signature=json["signature"],
        )


@dataclass
class VerifyOptions:
    chain_id: Optional[int] = None


@dataclass
class AuthenticationOptions:
    invalid_before: Optional[datetime] = None
    expiration_time: Optional[datetime] = None


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
