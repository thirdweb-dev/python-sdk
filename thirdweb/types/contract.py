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
    DropERC721,
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
        DropERC721,
    ],
)

TERC721 = TypeVar("TERC721", bound=Union[TokenERC721, DropERC721])

TPrimarySaleABI = TypeVar(
    "TPrimarySaleABI",
    bound=Union[TokenERC721, TokenERC1155, TokenERC20, DropERC721],
)

TPlatformFeeABI = TypeVar(
    "TPlatformFeeABI",
    bound=Union[TokenERC721, TokenERC1155, TokenERC20, Marketplace, DropERC721],
)

TRoyaltyABI = TypeVar(
    "TRoyaltyABI",
    bound=Union[TokenERC721, TokenERC1155, DropERC721],
)

TMetadataABI = TypeVar(
    "TMetadataABI",
    bound=Union[TokenERC721, TokenERC1155, TokenERC20, Marketplace, DropERC721],
)

TContractSchema = TypeVar("TContractSchema", bound=ContractMetadataSchema)


class ContractType(Enum):
    NFT_COLLECTION = "nft-collection"
    EDITION = "edition"
    TOKEN = "token"
    MARKETPLACE = "marketplace"
    NFT_DROP = "nft-drop"
