import dataclasses
from dataclasses import dataclass
from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Union
from thirdweb.constants.currency import ZERO_ADDRESS
from dacite import from_dict


@dataclass
class ContractMetadataSchema:
    name: str = ""
    description: Optional[str] = None
    image: Optional[Union[str, TextIO, BinaryIO]] = None
    external_link: Optional[str] = None

    @staticmethod
    def from_json(json: Dict[str, Any]) -> "ContractMetadataSchema":
        return from_dict(ContractMetadataSchema, json)

    def to_json(self) -> Dict[str, Any]:
        json = {}
        for key, value in self.__dict__.items():
            if (value is not None and value != "") or key == "name":
                json[key] = value
        return json


@dataclass
class ContractRoyaltySchema:
    seller_fee_basis_points: int = 0
    fee_recipient: str = ZERO_ADDRESS


@dataclass
class ContractPrimarySaleSchema:
    primary_sale_recipient: str = ZERO_ADDRESS


@dataclass
class ContractPlatformFeeSchema:
    platform_fee_basis_points: int = 0
    platform_fee_recipient: str = ZERO_ADDRESS


@dataclass
class ContractSymbolSchema:
    symbol: str = ""


@dataclass
class ContractTrustedForwarderSchema:
    trusted_forwarders: List[str] = dataclasses.field(default_factory=list)


@dataclass
class MerkleSchema:
    merkle: Dict[str, str] = dataclasses.field(default_factory=lambda: {})


@dataclass
class NFTCollectionContractMetadata(
    ContractMetadataSchema,
    ContractRoyaltySchema,
    ContractSymbolSchema,
    ContractPlatformFeeSchema,
    ContractPrimarySaleSchema,
    ContractTrustedForwarderSchema,
):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "NFTCollectionContractMetadata":
        return from_dict(NFTCollectionContractMetadata, json)


@dataclass
class EditionContractMetadata(
    ContractMetadataSchema,
    ContractSymbolSchema,
    ContractRoyaltySchema,
    ContractPlatformFeeSchema,
    ContractPrimarySaleSchema,
    ContractTrustedForwarderSchema,
):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "EditionContractMetadata":
        return from_dict(EditionContractMetadata, json)


@dataclass
class TokenContractMetadata(
    ContractMetadataSchema,
    ContractSymbolSchema,
    ContractPrimarySaleSchema,
    ContractTrustedForwarderSchema,
    ContractPlatformFeeSchema,
):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "TokenContractMetadata":
        return from_dict(TokenContractMetadata, json)


@dataclass
class MarketplaceContractMetadata(
    ContractMetadataSchema, ContractPlatformFeeSchema, ContractTrustedForwarderSchema
):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "MarketplaceContractMetadata":
        return from_dict(MarketplaceContractMetadata, json)


@dataclass
class NFTDropContractMetadata(
    ContractMetadataSchema,
    ContractRoyaltySchema,
    ContractSymbolSchema,
    ContractPrimarySaleSchema,
    ContractPlatformFeeSchema,
    ContractTrustedForwarderSchema,
    MerkleSchema,
):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "NFTDropContractMetadata":
        return from_dict(NFTDropContractMetadata, json)


@dataclass
class EditionDropContractMetadata(
    ContractMetadataSchema,
    ContractRoyaltySchema,
    ContractSymbolSchema,
    ContractPrimarySaleSchema,
    ContractPlatformFeeSchema,
    ContractTrustedForwarderSchema,
    MerkleSchema,
):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "EditionDropContractMetadata":
        return from_dict(EditionDropContractMetadata, json)


@dataclass
class CustomContractMetadata(ContractMetadataSchema):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "CustomContractMetadata":
        return from_dict(CustomContractMetadata, json)
