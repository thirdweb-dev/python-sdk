from typing import List, Union
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.types.currency import Currency, CurrencyValue, TokenAmount
from web3.eth import TxReceipt


class ERC20(BaseContract):
    def __init__(self, contract_wrapper: ContractWrapper):
        super().__init__(contract_wrapper)

    """
    READ FUNCTIONS
    """

    def get(self) -> Currency:
        pass

    def balance(self) -> CurrencyValue:
        pass

    def balanceOf(self, address: str) -> CurrencyValue:
        pass

    def total_supply(self) -> CurrencyValue:
        pass

    def allowance(self, spender: str) -> CurrencyValue:
        pass

    def allowance_of(self, owner: str, spender: str) -> CurrencyValue:
        pass

    def is_transfer_restricted(self) -> bool:
        pass

    """
    WRITE FUNCTIONS
    """

    def transfer(self, to: str, amount: Union[int, str]) -> TxReceipt:
        pass

    def transfer_from(self, fr: str, to: str, amount: Union[int, str]) -> TxReceipt:
        pass

    def set_allowance(self, spender: str, amount: Union[int, str]) -> TxReceipt:
        pass

    def transfer_batch(self, args: List[TokenAmount]):
        pass

    def burn(self, amount: Union[int, str]) -> TxReceipt:
        pass

    def burn_from(self, amount: Union[int, str]) -> TxReceipt:
        pass
