from dataclasses import dataclass
from time import time
from typing import Optional
from thirdweb.common.signature_minting import resolve_or_generate_id
from thirdweb.types.currency import Price
from thirdweb.constants.currency import NATIVE_TOKEN_ADDRESS, ZERO_ADDRESS
from thirdweb.types.nft import NFTMetadataInput


@dataclass
class BaseSignaturePayloadInput:
    to: str
    price: Price = 0
    currency_address: str = NATIVE_TOKEN_ADDRESS
    mint_start_time: int = int(time())
    mint_end_time: int = int(time()) + 60 * 60 * 24 * 1000 * 1000
    uid: Optional[bytes] = None
    primary_sale_recipient: Optional[str] = ZERO_ADDRESS

    def set_uid(self, uid: str) -> "BaseSignaturePayloadInput":
        self.uid = resolve_or_generate_id(uid)
        return self


@dataclass
class Signature20PayloadInput(BaseSignaturePayloadInput):
    quantity: Price = 0


@dataclass
class Signature20PayloadOutput(Signature20PayloadInput):
    pass


@dataclass
class Signature721PayloadInput:
    to: str
    metadata: NFTMetadataInput
    royalty_recipient: str = ZERO_ADDRESS
    royalty_bps: int = 0
    price: Price = 0
    currency_address: str = NATIVE_TOKEN_ADDRESS
    mint_start_time: int = int(time())
    mint_end_time: int = int(time()) + 60 * 60 * 24 * 1000 * 1000
    uid: Optional[bytes] = None
    primary_sale_recipient: Optional[str] = ZERO_ADDRESS

    def set_uid(self, uid: str) -> "Signature721PayloadInput":
        self.uid = resolve_or_generate_id(uid)
        return self


@dataclass
class Signature721PayloadOutput:
    to: str
    metadata: NFTMetadataInput
    royalty_recipient: str = ZERO_ADDRESS
    royalty_bps: int = 0
    uri: str = ""
    price: Price = 0
    currency_address: str = NATIVE_TOKEN_ADDRESS
    mint_start_time: int = int(time())
    mint_end_time: int = int(time()) + 60 * 60 * 24 * 1000 * 1000
    uid: Optional[bytes] = None
    primary_sale_recipient: Optional[str] = ZERO_ADDRESS

    def set_uid(self, uid: str) -> "Signature721PayloadOutput":
        self.uid = resolve_or_generate_id(uid)
        return self


@dataclass
class Signature1155PayloadInput:
    to: str
    metadata: NFTMetadataInput
    token_id: int
    quantity: int
    royalty_recipient: str = ZERO_ADDRESS
    royalty_bps: int = 0
    price: Price = 0
    currency_address: str = NATIVE_TOKEN_ADDRESS
    mint_start_time: int = int(time())
    mint_end_time: int = int(time()) + 60 * 60 * 24 * 1000 * 1000
    uid: Optional[bytes] = None
    primary_sale_recipient: Optional[str] = ZERO_ADDRESS

    def set_uid(self, uid: str) -> "Signature1155PayloadInput":
        self.uid = resolve_or_generate_id(uid)
        return self


@dataclass
class Signature1155PayloadOutput:
    to: str
    metadata: NFTMetadataInput
    royalty_bps: int
    royalty_recipient: str
    uri: str
    token_id: int
    quantity: int
    price: Price = 0
    currency_address: str = NATIVE_TOKEN_ADDRESS
    mint_start_time: int = int(time())
    mint_end_time: int = int(time()) + 60 * 60 * 24 * 1000 * 1000
    uid: Optional[bytes] = None
    primary_sale_recipient: Optional[str] = ZERO_ADDRESS

    def set_uid(self, uid: str) -> "Signature1155PayloadOutput":
        self.uid = resolve_or_generate_id(uid)
        return self


FilledSignaturePayload20 = Signature20PayloadInput
PayloadWithUri20 = Signature20PayloadOutput
PayloadToSign20 = Signature20PayloadInput


@dataclass
class SignedPayload20:
    payload: Signature20PayloadInput
    signature: str


FilledSignaturePayload721 = Signature721PayloadInput
PayloadWithUri721 = Signature721PayloadOutput
PayloadToSign721 = Signature721PayloadInput


@dataclass
class SignedPayload721:
    payload: Signature721PayloadInput
    signature: str


FilledSignaturePayload1155 = Signature1155PayloadInput
PayloadWithUri1155 = Signature1155PayloadOutput
PayloadToSign1155 = Signature1155PayloadInput


@dataclass
class SignedPayload1155:
    payload: Signature1155PayloadInput
    signature: str


MintRequest20 = [
    {"name": "to", "type": "address"},
    {"name": "primarySaleRecipient", "type": "address"},
    {"name": "quantity", "type": "uint256"},
    {"name": "price", "type": "uint256"},
    {"name": "currency", "type": "address"},
    {"name": "validityStartTimestamp", "type": "uint128"},
    {"name": "validityEndTimestamp", "type": "uint128"},
    {"name": "uid", "type": "bytes32"},
]

MintRequest721 = [
    {"name": "to", "type": "address"},
    {"name": "royaltyRecipient", "type": "address"},
    {"name": "royaltyBps", "type": "uint256"},
    {"name": "primarySaleRecipient", "type": "address"},
    {"name": "uri", "type": "string"},
    {"name": "price", "type": "uint256"},
    {"name": "currency", "type": "address"},
    {"name": "validityStartTimestamp", "type": "uint128"},
    {"name": "validityEndTimestamp", "type": "uint128"},
    {"name": "uid", "type": "bytes32"},
]

MintRequest1155 = [
    {"name": "to", "type": "address"},
    {"name": "royaltyRecipient", "type": "address"},
    {"name": "royaltyBps", "type": "uint256"},
    {"name": "primarySaleRecipient", "type": "address"},
    {"name": "tokenId", "type": "uint256"},
    {"name": "uri", "type": "string"},
    {"name": "quantity", "type": "uint256"},
    {"name": "pricePerToken", "type": "uint256"},
    {"name": "currency", "type": "address"},
    {"name": "validityStartTimestamp", "type": "uint128"},
    {"name": "validityEndTimestamp", "type": "uint128"},
    {"name": "uid", "type": "bytes32"},
]

EIP712DomainType = [
    {"name": "name", "type": "string"},
    {"name": "version", "type": "string"},
    {"name": "chainId", "type": "uint256"},
    {"name": "verifyingContract", "type": "address"},
]
