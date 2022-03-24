from typing import Final, List, Optional, Union
from thirdweb.abi import TokenERC20
from web3 import Web3
from web3.eth import TxReceipt
from eth_account.account import LocalAccount
from thirdweb.common.currency import parse_units
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
        return self.get_vote_balance_of(self._contract_wrapper.get_signer_address())

    def get_vote_balance_of(self, account: str) -> CurrencyValue:
        return self._get_value(self._get_abi().get_votes.call(account))

    def get_delegation(self) -> str:
        return self.get_delegation_of(self._contract_wrapper.get_signer_address())

    def get_delegation_of(self, account: str) -> str:
        return self._get_abi().delegates.call(account)

    """
    WRITE FUNCTIONS
    """

    def mint(self, amount: int) -> TxReceipt:
        return self.mint_to(self._contract_wrapper.get_signer_address(), amount)

    def mint_to(self, to: str, amount: int) -> TxReceipt:
        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "mintTo", [to, amount_with_decimals]
        )

    def mint_batch_to(self, args: List[TokenAmount]) -> TxReceipt:
        # TODO: Implement - Relies on MULTICALL
        pass

    def delegate_to(self, delegatee_address: str) -> TxReceipt:
        return self._contract_wrapper.send_transaction("delegate", [delegatee_address])
