from dataclasses import dataclass
from typing import Optional
from thirdweb.common.signature_minting import resolve_or_generate_id
from thirdweb.types.currency import Price
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.types.nft import NFTMetadataInput


@dataclass
class BaseSignaturePayloadInput:
    to: str
    price: Price
    currency_address: str
    mint_start_time: int
    mint_end_time: int
    uid: Optional[str]
    primary_sale_recipient: Optional[str]

    def __init__(
        self,
        to: str,
        price: Price,
        currency_address: str,
        mint_start_time: int,
        mint_end_time: int,
        uid: Optional[str] = None,
        primary_sale_recipient: str = ZERO_ADDRESS,
    ):
        self.to = to
        self.price = price
        self.currency_address = currency_address
        self.mint_start_time = mint_start_time
        self.mint_end_time = mint_end_time
        self.uid = resolve_or_generate_id(uid)
        self.primary_sale_recipient = primary_sale_recipient


@dataclass
class Signature20PayloadInput(BaseSignaturePayloadInput):
    quantity: Price


@dataclass
class Signature20PayloadOutput(Signature20PayloadInput):
    pass


@dataclass
class Signature721PayloadInput(BaseSignaturePayloadInput):
    metadata: NFTMetadataInput
    royalty_recipient: str = ZERO_ADDRESS
    royalty_bps: int = 0


@dataclass
class Signature721PayloadOutput(BaseSignaturePayloadInput):
    metadata: NFTMetadataInput
    royalty_recipient: str
    royalty_bps: int
    uri: str


@dataclass
class Signature1155PayloadInput(BaseSignaturePayloadInput):
    metadata: NFTMetadataInput
    token_id: int
    quantity: int
    royalty_recipient: str = ZERO_ADDRESS
    royalty_bps: int = 0


@dataclass
class Signature1155PayloadOutput(BaseSignaturePayloadInput):
    uri: str
    royalty_bps: int
    token_id: int
    quantity: int


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
