from dataclasses import dataclass
import dataclasses
from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Union
from thirdweb.constants.currency import ZERO_ADDRESS
from dacite import from_dict


@dataclass
class ContractMetadata:
    name: str = ""
    description: Optional[str] = None
    image: Optional[Union[str, TextIO, BinaryIO]] = None
    external_link: Optional[str] = None

    @staticmethod
    def from_json(json: Dict[str, Any]) -> "ContractMetadata":
        return from_dict(ContractMetadata, json)

    def to_json(self) -> Dict[str, Any]:
        return self.__dict__


@dataclass
class ContractRoyalty:
    seller_fee_basis_points: int = 0
    fee_recipient: str = ZERO_ADDRESS


@dataclass
class ContractPrimarySale:
    primary_sale_recipient: str = ZERO_ADDRESS


@dataclass
class ContractPlatformFee:
    platform_fee_basis_points: int = 0
    platform_fee_recipient: str = ZERO_ADDRESS


@dataclass
class ContractSymbol:
    symbol: str = ""


@dataclass
class ContractTrustedForwarder:
    trusted_forwarders: List[str] = dataclasses.field(default_factory=list)


@dataclass
class NFTCollectionContractMetadata(
    ContractMetadata,
    ContractRoyalty,
    ContractSymbol,
    ContractPlatformFee,
    ContractPrimarySale,
    ContractTrustedForwarder,
):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "NFTCollectionContractMetadata":
        return from_dict(NFTCollectionContractMetadata, json)


@dataclass
class EditionContractMetadata(
    ContractMetadata,
    ContractRoyalty,
    ContractPlatformFee,
    ContractPrimarySale,
    ContractTrustedForwarder,
):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "EditionContractMetadata":
        return from_dict(EditionContractMetadata, json)


@dataclass
class TokenContractMetadata(
    ContractMetadata, ContractSymbol, ContractPrimarySale, ContractTrustedForwarder
):
    @staticmethod
    def from_json(json: Dict[str, Any]) -> "TokenContractMetadata":
        return from_dict(TokenContractMetadata, json)
