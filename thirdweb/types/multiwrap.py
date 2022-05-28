from dataclasses import dataclass
import dataclasses
from typing import List

from thirdweb.types.currency import Price


@dataclass
class ERC20Wrappable:
    contract_address: str
    quantity: Price


@dataclass
class ERC721Wrappable:
    contract_address: str
    token_id: int


@dataclass
class ERC1155Wrappable:
    contract_address: str
    token_id: int
    quantity: int


@dataclass
class TokensToWrap:
    erc20_tokens: List[ERC20Wrappable] = dataclasses.field(default_factory=list)
    erc721_tokens: List[ERC721Wrappable] = dataclasses.field(default_factory=list)
    erc1155_tokens: List[ERC1155Wrappable] = dataclasses.field(default_factory=list)


@dataclass
class WrappedTokens:
    erc20_tokens: List[ERC20Wrappable] = dataclasses.field(default_factory=list)
    erc721_tokens: List[ERC721Wrappable] = dataclasses.field(default_factory=list)
    erc1155_tokens: List[ERC1155Wrappable] = dataclasses.field(default_factory=list)
