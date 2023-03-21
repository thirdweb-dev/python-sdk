"""Generated wrapper for DefaultOperatorFiltererUpgradeable Solidity contract."""

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
# constructor for DefaultOperatorFiltererUpgradeable below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        DefaultOperatorFiltererUpgradeableValidator,
    )
except ImportError:

    class DefaultOperatorFiltererUpgradeableValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class OperatorRestrictionMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the operatorRestriction method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class SetOperatorRestrictionMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setOperatorRestriction method."""

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

    def validate_and_normalize_inputs(self, restriction: bool):
        """Validate the inputs to the setOperatorRestriction method."""
        self.validator.assert_valid(
            method_name="setOperatorRestriction",
            parameter_name="_restriction",
            argument_value=restriction,
        )
        return restriction

    def call(
        self, restriction: bool, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (restriction) = self.validate_and_normalize_inputs(restriction)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(restriction).call(tx_params.as_dict())

    def send_transaction(
        self, restriction: bool, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (restriction) = self.validate_and_normalize_inputs(restriction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(restriction).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, restriction: bool, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (restriction) = self.validate_and_normalize_inputs(restriction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(restriction).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, restriction: bool, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (restriction) = self.validate_and_normalize_inputs(restriction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(restriction).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class DefaultOperatorFiltererUpgradeable:
    """Wrapper class for DefaultOperatorFiltererUpgradeable Solidity contract."""

    operator_restriction: OperatorRestrictionMethod
    """Constructor-initialized instance of
    :class:`OperatorRestrictionMethod`.
    """

    set_operator_restriction: SetOperatorRestrictionMethod
    """Constructor-initialized instance of
    :class:`SetOperatorRestrictionMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: DefaultOperatorFiltererUpgradeableValidator = None,
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
            validator = DefaultOperatorFiltererUpgradeableValidator(
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
            abi=DefaultOperatorFiltererUpgradeable.abi(),
        ).functions

        self.operator_restriction = OperatorRestrictionMethod(
            web3_or_provider, contract_address, functions.operatorRestriction
        )

        self.set_operator_restriction = SetOperatorRestrictionMethod(
            web3_or_provider,
            contract_address,
            functions.setOperatorRestriction,
            validator,
        )

    def get_operator_restriction_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OperatorRestriction event.

        :param tx_hash: hash of transaction emitting OperatorRestriction event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DefaultOperatorFiltererUpgradeable.abi(),
            )
            .events.OperatorRestriction()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"operator","type":"address"}],"name":"OperatorNotAllowed","type":"error"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"restriction","type":"bool"}],"name":"OperatorRestriction","type":"event"},{"inputs":[],"name":"operatorRestriction","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_restriction","type":"bool"}],"name":"setOperatorRestriction","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
