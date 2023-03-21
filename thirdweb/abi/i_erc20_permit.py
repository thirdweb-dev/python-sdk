"""Generated wrapper for IERC20Permit Solidity contract."""

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
# constructor for IERC20Permit below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IERC20PermitValidator,
    )
except ImportError:

    class IERC20PermitValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class DomainSeparatorMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the DOMAIN_SEPARATOR method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

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


class NoncesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the nonces method."""

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

    def validate_and_normalize_inputs(self, owner: str):
        """Validate the inputs to the nonces method."""
        self.validator.assert_valid(
            method_name="nonces",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        return owner

    def call(self, owner: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).transact(tx_params.as_dict())

    def build_transaction(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, owner: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).estimateGas(tx_params.as_dict())


class PermitMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the permit method."""

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

    def validate_and_normalize_inputs(
        self,
        owner: str,
        spender: str,
        value: int,
        deadline: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
    ):
        """Validate the inputs to the permit method."""
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="spender",
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="value",
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="deadline",
            argument_value=deadline,
        )
        # safeguard against fractional inputs
        deadline = int(deadline)
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="v",
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="r",
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name="permit",
            parameter_name="s",
            argument_value=s,
        )
        return (owner, spender, value, deadline, v, r, s)

    def call(
        self,
        owner: str,
        spender: str,
        value: int,
        deadline: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            owner,
            spender,
            value,
            deadline,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            owner, spender, value, deadline, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(owner, spender, value, deadline, v, r, s).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        owner: str,
        spender: str,
        value: int,
        deadline: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            owner,
            spender,
            value,
            deadline,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            owner, spender, value, deadline, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            owner, spender, value, deadline, v, r, s
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        owner: str,
        spender: str,
        value: int,
        deadline: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            owner,
            spender,
            value,
            deadline,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            owner, spender, value, deadline, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            owner, spender, value, deadline, v, r, s
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        owner: str,
        spender: str,
        value: int,
        deadline: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            owner,
            spender,
            value,
            deadline,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            owner, spender, value, deadline, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            owner, spender, value, deadline, v, r, s
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IERC20Permit:
    """Wrapper class for IERC20Permit Solidity contract."""

    domain_separator: DomainSeparatorMethod
    """Constructor-initialized instance of
    :class:`DomainSeparatorMethod`.
    """

    nonces: NoncesMethod
    """Constructor-initialized instance of
    :class:`NoncesMethod`.
    """

    permit: PermitMethod
    """Constructor-initialized instance of
    :class:`PermitMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IERC20PermitValidator = None,
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
            validator = IERC20PermitValidator(
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
            abi=IERC20Permit.abi(),
        ).functions

        self.domain_separator = DomainSeparatorMethod(
            web3_or_provider, contract_address, functions.DOMAIN_SEPARATOR
        )

        self.nonces = NoncesMethod(
            web3_or_provider, contract_address, functions.nonces, validator
        )

        self.permit = PermitMethod(
            web3_or_provider, contract_address, functions.permit, validator
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
