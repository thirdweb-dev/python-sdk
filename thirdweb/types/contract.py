from enum import Enum
from typing import TypeVar, Union
from thirdweb.abi import (
    TokenERC20,
    TokenERC721,
    TokenERC1155,
    Marketplace,
    TWRegistry,
    TWFactory,
)
from thirdweb.types.settings.metadata import ContractMetadataSchema


TContractABI = TypeVar(
    "TContractABI",
    bound=Union[
        TokenERC721, TokenERC1155, TokenERC20, Marketplace, TWRegistry, TWFactory
    ],
)

TPrimarySaleABI = TypeVar(
    "TPrimarySaleABI",
    bound=Union[
        TokenERC721,
        TokenERC1155,
        TokenERC20,
    ],
)

TPlatformFeeABI = TypeVar(
    "TPlatformFeeABI",
    bound=Union[TokenERC721, TokenERC1155, TokenERC20, Marketplace],
)

TRoyaltyABI = TypeVar(
    "TRoyaltyABI",
    bound=Union[
        TokenERC721,
        TokenERC1155,
    ],
)

TMetadataABI = TypeVar(
    "TMetadataABI",
    bound=Union[
        TokenERC721,
        TokenERC1155,
        TokenERC20,
        Marketplace,
    ],
)

TContractSchema = TypeVar("TContractSchema", bound=ContractMetadataSchema)


class ContractType(Enum):
    NFT_COLLECTION = "nft-collection"
    EDITION = "edition"
    TOKEN = "token"
    MARKETPLACE = "marketplace"
