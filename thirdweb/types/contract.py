from enum import Enum

from thirdweb.abi.token_erc20 import TokenERC20
from thirdweb.abi.token_erc721 import TokenERC721
from thirdweb.abi.token_erc1155 import TokenERC1155


class ContractABI(Enum):
    """
    The ABIs for each contract
    """

    NFT_COLLECTION = TokenERC721
    EDITION = TokenERC1155
    TOKEN = TokenERC20
