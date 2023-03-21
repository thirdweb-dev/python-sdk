"""Generated wrapper for IBurnableERC20 Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for IBurnableERC20 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IBurnableERC20Validator,
    )
except ImportError:

    class IBurnableERC20Validator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class BurnMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the burn method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, amount: int):
        """Validate the inputs to the burn method."""
        self.validator.assert_valid(
            method_name="burn",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return amount

    def call(self, amount: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(amount).call(tx_params.as_dict())

    def send_transaction(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).transact(tx_params.as_dict())

    def build_transaction(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).estimateGas(tx_params.as_dict())


class BurnFromMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the burnFrom method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, amount: int):
        """Validate the inputs to the burnFrom method."""
        self.validator.assert_valid(
            method_name="burnFrom",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="burnFrom",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (account, amount)

    def call(
        self, account: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, amount).call(tx_params.as_dict())

    def send_transaction(
        self, account: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, account: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, amount).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IBurnableERC20:
    """Wrapper class for IBurnableERC20 Solidity contract."""

    burn: BurnMethod
    """Constructor-initialized instance of
    :class:`BurnMethod`.
    """

    burn_from: BurnFromMethod
    """Constructor-initialized instance of
    :class:`BurnFromMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IBurnableERC20Validator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param web3_or_provider: Either an instance of `web3.Web3`:code: or
            `web3.providers.base.BaseProvider`:code:
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        # pylint: disable=too-many-statements

        self.contract_address = contract_address

        if not validator:
            validator = IBurnableERC20Validator(
                web3_or_provider, contract_address
            )

        web3 = None
        if isinstance(web3_or_provider, BaseProvider):
            web3 = Web3(web3_or_provider)
        elif isinstance(web3_or_provider, Web3):
            web3 = web3_or_provider
        else:
            raise TypeError(
                "Expected parameter 'web3_or_provider' to be an instance of either"
                + " Web3 or BaseProvider"
            )

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                        middleware["function"],
                        layer=middleware["layer"],
                    )
            except ValueError as value_error:
                if value_error.args == (
                    "You can't add the same un-named instance twice",
                ):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(
            address=to_checksum_address(contract_address),
            abi=IBurnableERC20.abi(),
        ).functions

        self.burn = BurnMethod(
            web3_or_provider, contract_address, functions.burn, validator
        )

        self.burn_from = BurnFromMethod(
            web3_or_provider, contract_address, functions.burnFrom, validator
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
