from dataclasses import dataclass
from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Union
from thirdweb.constants.currency import ZERO_ADDRESS
from dacite import from_dict


@dataclass
class ContractMetadata:
    name: str = ""
    description: Optional[str] = None
    image: Optional[Union[str, TextIO, BinaryIO]] = None
    external_link: Optional[str] = None

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
    trusted_forwardesr: List[str] = []


@dataclass
class NFTCollectionContractMetadata(
    ContractMetadata,
    ContractRoyalty,
    ContractSymbol,
    ContractPlatformFee,
    ContractPrimarySale,
    ContractTrustedForwarder,
):
    def from_json(self, json: Dict[str, Any]) -> "NFTCollectionContractMetadata":
        return from_dict(data_class=NFTCollectionContractMetadata, data=json)


@dataclass
class EditionContractMetadata(
    ContractMetadata,
    ContractRoyalty,
    ContractPlatformFee,
    ContractPrimarySale,
    ContractTrustedForwarder,
):
    def from_json(self, json: Dict[str, Any]) -> "EditionContractMetadata":
        return from_dict(data_class=EditionContractMetadata, data=json)


@dataclass
class TokenContractMetadata(
    ContractMetadata, ContractSymbol, ContractPrimarySale, ContractTrustedForwarder
):
    def from_json(self, json: Dict[str, Any]) -> "TokenContractMetadata":
        return from_dict(data_class=TokenContractMetadata, data=json)
