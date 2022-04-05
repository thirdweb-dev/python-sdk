from enum import Enum
from typing import TypeVar, Union
from thirdweb.abi import (
    TWRegistry,
    TWFactory,
    TokenERC20,
    TokenERC721,
    TokenERC1155,
    Marketplace,
    IERC20,
    IERC721,
    IERC1155,
)
from thirdweb.types.settings.metadata import ContractMetadataSchema


TContractABI = TypeVar(
    "TContractABI",
    bound=Union[
        TokenERC721,
        TokenERC1155,
        TokenERC20,
        Marketplace,
        IERC20,
        IERC721,
        IERC1155,
        TWRegistry,
        TWFactory,
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
