from typing import List, Union, cast
from thirdweb.abi.token_erc20 import TokenERC20
from thirdweb.common.currency import (
    fetch_currency_metadata,
    fetch_currency_value,
    parse_units,
)
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.currency import Currency, CurrencyValue, TokenAmount
from web3.eth import TxReceipt


class ERC20(BaseContract):
    _storage: IpfsStorage

    def __init__(
        self,
        contract_wrapper: ContractWrapper,
        storage: IpfsStorage,
    ):
        super().__init__(contract_wrapper)
        self._storage = storage

    """
    READ FUNCTIONS
    """

    def get(self) -> Currency:
        return fetch_currency_metadata(
            self._contract_wrapper.get_provider(), self.get_address()
        )

    def balance(self) -> CurrencyValue:
        return self.balance_of(self._contract_wrapper.get_signer_address())

    def balance_of(self, address: str) -> CurrencyValue:
        return self._get_value(self._get_abi().balance_of.call(address))

    def total_supply(self) -> CurrencyValue:
        return self._get_value(self._get_abi().total_supply.call())

    def allowance(self, spender: str) -> CurrencyValue:
        return self.allowance_of(self._contract_wrapper.get_signer_address(), spender)

    def allowance_of(self, owner: str, spender: str) -> CurrencyValue:
        return self._get_value(self._get_abi().allowance.call(owner, spender))

    def is_transfer_restricted(self) -> bool:
        # TODO: Implement - Relies on ROLES
        raise NotImplementedError

    """
    WRITE FUNCTIONS
    """

    def transfer(self, to: str, amount: int) -> TxReceipt:
        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "transfer", [to, amount_with_decimals]
        )

    def transfer_from(self, fr: str, to: str, amount: int) -> TxReceipt:
        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "transfer_from", [fr, to, amount_with_decimals]
        )

    def set_allowance(self, spender: str, amount: int) -> TxReceipt:
        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "approve", [spender, amount_with_decimals]
        )

    def transfer_batch(self, args: List[TokenAmount]):
        # TODO: Implement - relies on MULTICALL
        raise NotImplementedError

    def burn(self, amount: int) -> TxReceipt:
        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction("burn", [amount_with_decimals])

    def burn_from(self, holder: str, amount: int) -> TxReceipt:
        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "burn_from", [holder, amount_with_decimals]
        )

    """
    PROTECTED FUNCTIONS
    """

    def _get_abi(self) -> TokenERC20:
        return cast(TokenERC20, self._contract_wrapper._contract_abi)

    def _get_value(self, value: int) -> CurrencyValue:
        return fetch_currency_value(
            self._contract_wrapper.get_provider(),
            self.get_address(),
            value,
        )
