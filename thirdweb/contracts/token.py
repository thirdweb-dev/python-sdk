from typing import Final, List
from thirdweb.abi.token_erc20 import TokenERC20
from web3 import Web3

class Token(object):
    __abi: Final = TokenERC20

    contract_type: Final[str] = "token"
    contract_roles: Final[List[str]] = ["admin", "minter", "transfer"]

    def __init__(self, provider: Web3, address: str):
        pass