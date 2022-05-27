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
    DropERC1155,
    ThirdwebContract,
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
        DropERC1155,
        ThirdwebContract,
    ],
)

TERC721 = TypeVar("TERC721", bound=Union[TokenERC721, DropERC721])
TERC1155 = TypeVar("TERC1155", bound=Union[TokenERC1155, DropERC1155])

TPrimarySaleABI = TypeVar(
    "TPrimarySaleABI",
    bound=Union[TokenERC721, TokenERC1155, TokenERC20, DropERC721, DropERC1155],
)

TPlatformFeeABI = TypeVar(
    "TPlatformFeeABI",
    bound=Union[
        TokenERC721, TokenERC1155, TokenERC20, Marketplace, DropERC721, DropERC1155
    ],
)

TRoyaltyABI = TypeVar(
    "TRoyaltyABI",
    bound=Union[TokenERC721, TokenERC1155, DropERC721, DropERC1155],
)

TMetadataABI = TypeVar(
    "TMetadataABI",
    bound=Union[
        TokenERC721,
        TokenERC1155,
        TokenERC20,
        Marketplace,
        DropERC721,
        DropERC1155,
    ],
)

TContractSchema = TypeVar("TContractSchema", bound=ContractMetadataSchema)


class ContractType(Enum):
    NFT_COLLECTION = "nft-collection"
    EDITION = "edition"
    TOKEN = "token"
    MARKETPLACE = "marketplace"
    NFT_DROP = "nft-drop"
    EDITION_DROP = "edition-drop"
    CUSTOM = "custom"
