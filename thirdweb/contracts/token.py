from typing import Final, List, Optional, Union
from thirdweb.abi import TokenERC20
from web3 import Web3
from web3.eth import TxReceipt
from eth_account.account import LocalAccount
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_20 import ERC20
from thirdweb.types.currency import CurrencyValue, TokenAmount

from thirdweb.types.sdk import SDKOptions


class Token(ERC20):
    contract_type: Final[str] = "token"
    contract_roles: Final[List[str]] = ["admin", "minter", "transfer"]

    def __init__(
        self,
        provider: Web3,
        address: str,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC20(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper)

    """
    READ FUNCTIONS
    """

    def get_vote_balance(self) -> CurrencyValue:
        pass

    def get_vote_balance_of(self, address: str) -> CurrencyValue:
        pass

    def get_delegate(self) -> str:
        pass

    def get_delegate_of(self, address: str) -> str:
        pass

    """
    WRITE FUNCTIONS
    """

    def mint(self, amount: Union[int, str]) -> TxReceipt:
        pass

    def mint_to(self, to: str, amount: Union[int, str]) -> TxReceipt:
        pass

    def mint_batch_to(self, args: List[TokenAmount]) -> TxReceipt:
        pass

    def delegate_to(self, delegate_address: str) -> TxReceipt:
        pass
