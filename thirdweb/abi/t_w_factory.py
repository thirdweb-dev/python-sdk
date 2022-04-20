"""Generated wrapper for TWFactory Solidity contract."""

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
# constructor for TWFactory below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        TWFactoryValidator,
    )
except ImportError:

    class TWFactoryValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass





class DefaultAdminRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the DEFAULT_ADMIN_ROLE method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class FactoryRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the FACTORY_ROLE method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class AddImplementationMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addImplementation method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, implementation: str):
        """Validate the inputs to the addImplementation method."""
        self.validator.assert_valid(
            method_name='addImplementation',
            parameter_name='_implementation',
            argument_value=implementation,
        )
        implementation = self.validate_and_checksum_address(implementation)
        return (implementation)

    def call(self, implementation: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (implementation) = self.validate_and_normalize_inputs(implementation)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(implementation).call(tx_params.as_dict())

    def send_transaction(self, implementation: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (implementation) = self.validate_and_normalize_inputs(implementation)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation).transact(tx_params.as_dict())

    def build_transaction(self, implementation: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (implementation) = self.validate_and_normalize_inputs(implementation)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, implementation: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (implementation) = self.validate_and_normalize_inputs(implementation)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation).estimateGas(tx_params.as_dict())

class ApprovalMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the approval method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str):
        """Validate the inputs to the approval method."""
        self.validator.assert_valid(
            method_name='approval',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)

    def call(self, index_0: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class ApproveImplementationMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the approveImplementation method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, implementation: str, to_approve: bool):
        """Validate the inputs to the approveImplementation method."""
        self.validator.assert_valid(
            method_name='approveImplementation',
            parameter_name='_implementation',
            argument_value=implementation,
        )
        implementation = self.validate_and_checksum_address(implementation)
        self.validator.assert_valid(
            method_name='approveImplementation',
            parameter_name='_toApprove',
            argument_value=to_approve,
        )
        return (implementation, to_approve)

    def call(self, implementation: str, to_approve: bool, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (implementation, to_approve) = self.validate_and_normalize_inputs(implementation, to_approve)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(implementation, to_approve).call(tx_params.as_dict())

    def send_transaction(self, implementation: str, to_approve: bool, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (implementation, to_approve) = self.validate_and_normalize_inputs(implementation, to_approve)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation, to_approve).transact(tx_params.as_dict())

    def build_transaction(self, implementation: str, to_approve: bool, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (implementation, to_approve) = self.validate_and_normalize_inputs(implementation, to_approve)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation, to_approve).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, implementation: str, to_approve: bool, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (implementation, to_approve) = self.validate_and_normalize_inputs(implementation, to_approve)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation, to_approve).estimateGas(tx_params.as_dict())

class CurrentVersionMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the currentVersion method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str]):
        """Validate the inputs to the currentVersion method."""
        self.validator.assert_valid(
            method_name='currentVersion',
            parameter_name='index_0',
            argument_value=index_0,
        )
        return (index_0)

    def call(self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class DeployProxyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the deployProxy method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _type: Union[bytes, str], data: Union[bytes, str]):
        """Validate the inputs to the deployProxy method."""
        self.validator.assert_valid(
            method_name='deployProxy',
            parameter_name='_type',
            argument_value=_type,
        )
        self.validator.assert_valid(
            method_name='deployProxy',
            parameter_name='_data',
            argument_value=data,
        )
        return (_type, data)

    def call(self, _type: Union[bytes, str], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_type, data) = self.validate_and_normalize_inputs(_type, data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_type, data).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, _type: Union[bytes, str], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_type, data) = self.validate_and_normalize_inputs(_type, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, data).transact(tx_params.as_dict())

    def build_transaction(self, _type: Union[bytes, str], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_type, data) = self.validate_and_normalize_inputs(_type, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _type: Union[bytes, str], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_type, data) = self.validate_and_normalize_inputs(_type, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, data).estimateGas(tx_params.as_dict())

class DeployProxyByImplementationMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the deployProxyByImplementation method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, implementation: str, data: Union[bytes, str], salt: Union[bytes, str]):
        """Validate the inputs to the deployProxyByImplementation method."""
        self.validator.assert_valid(
            method_name='deployProxyByImplementation',
            parameter_name='_implementation',
            argument_value=implementation,
        )
        implementation = self.validate_and_checksum_address(implementation)
        self.validator.assert_valid(
            method_name='deployProxyByImplementation',
            parameter_name='_data',
            argument_value=data,
        )
        self.validator.assert_valid(
            method_name='deployProxyByImplementation',
            parameter_name='_salt',
            argument_value=salt,
        )
        return (implementation, data, salt)

    def call(self, implementation: str, data: Union[bytes, str], salt: Union[bytes, str], tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (implementation, data, salt) = self.validate_and_normalize_inputs(implementation, data, salt)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(implementation, data, salt).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, implementation: str, data: Union[bytes, str], salt: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (implementation, data, salt) = self.validate_and_normalize_inputs(implementation, data, salt)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation, data, salt).transact(tx_params.as_dict())

    def build_transaction(self, implementation: str, data: Union[bytes, str], salt: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (implementation, data, salt) = self.validate_and_normalize_inputs(implementation, data, salt)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation, data, salt).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, implementation: str, data: Union[bytes, str], salt: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (implementation, data, salt) = self.validate_and_normalize_inputs(implementation, data, salt)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(implementation, data, salt).estimateGas(tx_params.as_dict())

class DeployProxyDeterministicMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the deployProxyDeterministic method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _type: Union[bytes, str], data: Union[bytes, str], salt: Union[bytes, str]):
        """Validate the inputs to the deployProxyDeterministic method."""
        self.validator.assert_valid(
            method_name='deployProxyDeterministic',
            parameter_name='_type',
            argument_value=_type,
        )
        self.validator.assert_valid(
            method_name='deployProxyDeterministic',
            parameter_name='_data',
            argument_value=data,
        )
        self.validator.assert_valid(
            method_name='deployProxyDeterministic',
            parameter_name='_salt',
            argument_value=salt,
        )
        return (_type, data, salt)

    def call(self, _type: Union[bytes, str], data: Union[bytes, str], salt: Union[bytes, str], tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_type, data, salt) = self.validate_and_normalize_inputs(_type, data, salt)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_type, data, salt).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, _type: Union[bytes, str], data: Union[bytes, str], salt: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_type, data, salt) = self.validate_and_normalize_inputs(_type, data, salt)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, data, salt).transact(tx_params.as_dict())

    def build_transaction(self, _type: Union[bytes, str], data: Union[bytes, str], salt: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_type, data, salt) = self.validate_and_normalize_inputs(_type, data, salt)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, data, salt).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _type: Union[bytes, str], data: Union[bytes, str], salt: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_type, data, salt) = self.validate_and_normalize_inputs(_type, data, salt)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, data, salt).estimateGas(tx_params.as_dict())

class DeployerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the deployer method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str):
        """Validate the inputs to the deployer method."""
        self.validator.assert_valid(
            method_name='deployer',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)

    def call(self, index_0: str, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class GetImplementationMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getImplementation method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _type: Union[bytes, str], version: int):
        """Validate the inputs to the getImplementation method."""
        self.validator.assert_valid(
            method_name='getImplementation',
            parameter_name='_type',
            argument_value=_type,
        )
        self.validator.assert_valid(
            method_name='getImplementation',
            parameter_name='_version',
            argument_value=version,
        )
        # safeguard against fractional inputs
        version = int(version)
        return (_type, version)

    def call(self, _type: Union[bytes, str], version: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_type, version) = self.validate_and_normalize_inputs(_type, version)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_type, version).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, _type: Union[bytes, str], version: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_type, version) = self.validate_and_normalize_inputs(_type, version)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, version).transact(tx_params.as_dict())

    def build_transaction(self, _type: Union[bytes, str], version: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_type, version) = self.validate_and_normalize_inputs(_type, version)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, version).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _type: Union[bytes, str], version: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_type, version) = self.validate_and_normalize_inputs(_type, version)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type, version).estimateGas(tx_params.as_dict())

class GetLatestImplementationMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getLatestImplementation method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _type: Union[bytes, str]):
        """Validate the inputs to the getLatestImplementation method."""
        self.validator.assert_valid(
            method_name='getLatestImplementation',
            parameter_name='_type',
            argument_value=_type,
        )
        return (_type)

    def call(self, _type: Union[bytes, str], tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_type) = self.validate_and_normalize_inputs(_type)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_type).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, _type: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_type) = self.validate_and_normalize_inputs(_type)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type).transact(tx_params.as_dict())

    def build_transaction(self, _type: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_type) = self.validate_and_normalize_inputs(_type)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _type: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_type) = self.validate_and_normalize_inputs(_type)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_type).estimateGas(tx_params.as_dict())

class GetRoleAdminMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRoleAdmin method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleAdmin method."""
        self.validator.assert_valid(
            method_name='getRoleAdmin',
            parameter_name='role',
            argument_value=role,
        )
        return (role)

    def call(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())

class GetRoleMemberMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRoleMember method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], index: int):
        """Validate the inputs to the getRoleMember method."""
        self.validator.assert_valid(
            method_name='getRoleMember',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='getRoleMember',
            parameter_name='index',
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (role, index)

    def call(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, index).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).estimateGas(tx_params.as_dict())

class GetRoleMemberCountMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRoleMemberCount method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleMemberCount method."""
        self.validator.assert_valid(
            method_name='getRoleMemberCount',
            parameter_name='role',
            argument_value=role,
        )
        return (role)

    def call(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())

class GrantRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the grantRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the grantRole method."""
        self.validator.assert_valid(
            method_name='grantRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='grantRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class HasRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the hasRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the hasRole method."""
        self.validator.assert_valid(
            method_name='hasRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='hasRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, account).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class ImplementationMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the implementation method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str], index_1: int):
        """Validate the inputs to the implementation method."""
        self.validator.assert_valid(
            method_name='implementation',
            parameter_name='index_0',
            argument_value=index_0,
        )
        self.validator.assert_valid(
            method_name='implementation',
            parameter_name='index_1',
            argument_value=index_1,
        )
        # safeguard against fractional inputs
        index_1 = int(index_1)
        return (index_0, index_1)

    def call(self, index_0: Union[bytes, str], index_1: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, index_0: Union[bytes, str], index_1: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).transact(tx_params.as_dict())

    def build_transaction(self, index_0: Union[bytes, str], index_1: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: Union[bytes, str], index_1: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(tx_params.as_dict())

class IsTrustedForwarderMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isTrustedForwarder method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, forwarder: str):
        """Validate the inputs to the isTrustedForwarder method."""
        self.validator.assert_valid(
            method_name='isTrustedForwarder',
            parameter_name='forwarder',
            argument_value=forwarder,
        )
        forwarder = self.validate_and_checksum_address(forwarder)
        return (forwarder)

    def call(self, forwarder: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(forwarder).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, forwarder: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).transact(tx_params.as_dict())

    def build_transaction(self, forwarder: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, forwarder: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).estimateGas(tx_params.as_dict())

class MulticallMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the multicall method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, data: List[Union[bytes, str]]):
        """Validate the inputs to the multicall method."""
        self.validator.assert_valid(
            method_name='multicall',
            parameter_name='data',
            argument_value=data,
        )
        return (data)

    def call(self, data: List[Union[bytes, str]], tx_params: Optional[TxParams] = None) -> List[Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data).call(tx_params.as_dict())
        return [Union[bytes, str](element) for element in returned]

    def send_transaction(self, data: List[Union[bytes, str]], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).transact(tx_params.as_dict())

    def build_transaction(self, data: List[Union[bytes, str]], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, data: List[Union[bytes, str]], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).estimateGas(tx_params.as_dict())

class RegistryMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the registry method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class RenounceRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the renounceRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the renounceRole method."""
        self.validator.assert_valid(
            method_name='renounceRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='renounceRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class RevokeRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the revokeRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the revokeRole method."""
        self.validator.assert_valid(
            method_name='revokeRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='revokeRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class SupportsInterfaceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the supportsInterface method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, interface_id: Union[bytes, str]):
        """Validate the inputs to the supportsInterface method."""
        self.validator.assert_valid(
            method_name='supportsInterface',
            parameter_name='interfaceId',
            argument_value=interface_id,
        )
        return (interface_id)

    def call(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(interface_id).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).transact(tx_params.as_dict())

    def build_transaction(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).estimateGas(tx_params.as_dict())

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class TWFactory:
    """Wrapper class for TWFactory Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """
    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

    factory_role: FactoryRoleMethod
    """Constructor-initialized instance of
    :class:`FactoryRoleMethod`.
    """

    add_implementation: AddImplementationMethod
    """Constructor-initialized instance of
    :class:`AddImplementationMethod`.
    """

    approval: ApprovalMethod
    """Constructor-initialized instance of
    :class:`ApprovalMethod`.
    """

    approve_implementation: ApproveImplementationMethod
    """Constructor-initialized instance of
    :class:`ApproveImplementationMethod`.
    """

    current_version: CurrentVersionMethod
    """Constructor-initialized instance of
    :class:`CurrentVersionMethod`.
    """

    deploy_proxy: DeployProxyMethod
    """Constructor-initialized instance of
    :class:`DeployProxyMethod`.
    """

    deploy_proxy_by_implementation: DeployProxyByImplementationMethod
    """Constructor-initialized instance of
    :class:`DeployProxyByImplementationMethod`.
    """

    deploy_proxy_deterministic: DeployProxyDeterministicMethod
    """Constructor-initialized instance of
    :class:`DeployProxyDeterministicMethod`.
    """

    deployer: DeployerMethod
    """Constructor-initialized instance of
    :class:`DeployerMethod`.
    """

    get_implementation: GetImplementationMethod
    """Constructor-initialized instance of
    :class:`GetImplementationMethod`.
    """

    get_latest_implementation: GetLatestImplementationMethod
    """Constructor-initialized instance of
    :class:`GetLatestImplementationMethod`.
    """

    get_role_admin: GetRoleAdminMethod
    """Constructor-initialized instance of
    :class:`GetRoleAdminMethod`.
    """

    get_role_member: GetRoleMemberMethod
    """Constructor-initialized instance of
    :class:`GetRoleMemberMethod`.
    """

    get_role_member_count: GetRoleMemberCountMethod
    """Constructor-initialized instance of
    :class:`GetRoleMemberCountMethod`.
    """

    grant_role: GrantRoleMethod
    """Constructor-initialized instance of
    :class:`GrantRoleMethod`.
    """

    has_role: HasRoleMethod
    """Constructor-initialized instance of
    :class:`HasRoleMethod`.
    """

    implementation: ImplementationMethod
    """Constructor-initialized instance of
    :class:`ImplementationMethod`.
    """

    is_trusted_forwarder: IsTrustedForwarderMethod
    """Constructor-initialized instance of
    :class:`IsTrustedForwarderMethod`.
    """

    multicall: MulticallMethod
    """Constructor-initialized instance of
    :class:`MulticallMethod`.
    """

    registry: RegistryMethod
    """Constructor-initialized instance of
    :class:`RegistryMethod`.
    """

    renounce_role: RenounceRoleMethod
    """Constructor-initialized instance of
    :class:`RenounceRoleMethod`.
    """

    revoke_role: RevokeRoleMethod
    """Constructor-initialized instance of
    :class:`RevokeRoleMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """


    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: TWFactoryValidator = None,
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
            validator = TWFactoryValidator(web3_or_provider, contract_address)

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
                         middleware['function'], layer=middleware['layer'],
                    )
            except ValueError as value_error:
                if value_error.args == ("You can't add the same un-named instance twice",):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=TWFactory.abi()).functions

        self.default_admin_role = DefaultAdminRoleMethod(web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE)

        self.factory_role = FactoryRoleMethod(web3_or_provider, contract_address, functions.FACTORY_ROLE)

        self.add_implementation = AddImplementationMethod(web3_or_provider, contract_address, functions.addImplementation, validator)

        self.approval = ApprovalMethod(web3_or_provider, contract_address, functions.approval, validator)

        self.approve_implementation = ApproveImplementationMethod(web3_or_provider, contract_address, functions.approveImplementation, validator)

        self.current_version = CurrentVersionMethod(web3_or_provider, contract_address, functions.currentVersion, validator)

        self.deploy_proxy = DeployProxyMethod(web3_or_provider, contract_address, functions.deployProxy, validator)

        self.deploy_proxy_by_implementation = DeployProxyByImplementationMethod(web3_or_provider, contract_address, functions.deployProxyByImplementation, validator)

        self.deploy_proxy_deterministic = DeployProxyDeterministicMethod(web3_or_provider, contract_address, functions.deployProxyDeterministic, validator)

        self.deployer = DeployerMethod(web3_or_provider, contract_address, functions.deployer, validator)

        self.get_implementation = GetImplementationMethod(web3_or_provider, contract_address, functions.getImplementation, validator)

        self.get_latest_implementation = GetLatestImplementationMethod(web3_or_provider, contract_address, functions.getLatestImplementation, validator)

        self.get_role_admin = GetRoleAdminMethod(web3_or_provider, contract_address, functions.getRoleAdmin, validator)

        self.get_role_member = GetRoleMemberMethod(web3_or_provider, contract_address, functions.getRoleMember, validator)

        self.get_role_member_count = GetRoleMemberCountMethod(web3_or_provider, contract_address, functions.getRoleMemberCount, validator)

        self.grant_role = GrantRoleMethod(web3_or_provider, contract_address, functions.grantRole, validator)

        self.has_role = HasRoleMethod(web3_or_provider, contract_address, functions.hasRole, validator)

        self.implementation = ImplementationMethod(web3_or_provider, contract_address, functions.implementation, validator)

        self.is_trusted_forwarder = IsTrustedForwarderMethod(web3_or_provider, contract_address, functions.isTrustedForwarder, validator)

        self.multicall = MulticallMethod(web3_or_provider, contract_address, functions.multicall, validator)

        self.registry = RegistryMethod(web3_or_provider, contract_address, functions.registry)

        self.renounce_role = RenounceRoleMethod(web3_or_provider, contract_address, functions.renounceRole, validator)

        self.revoke_role = RevokeRoleMethod(web3_or_provider, contract_address, functions.revokeRole, validator)

        self.supports_interface = SupportsInterfaceMethod(web3_or_provider, contract_address, functions.supportsInterface, validator)

    def get_implementation_added_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ImplementationAdded event.

        :param tx_hash: hash of transaction emitting ImplementationAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TWFactory.abi()).events.ImplementationAdded().processReceipt(tx_receipt)
    def get_implementation_approved_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ImplementationApproved event.

        :param tx_hash: hash of transaction emitting ImplementationApproved
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TWFactory.abi()).events.ImplementationApproved().processReceipt(tx_receipt)
    def get_proxy_deployed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ProxyDeployed event.

        :param tx_hash: hash of transaction emitting ProxyDeployed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TWFactory.abi()).events.ProxyDeployed().processReceipt(tx_receipt)
    def get_role_admin_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleAdminChanged event.

        :param tx_hash: hash of transaction emitting RoleAdminChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TWFactory.abi()).events.RoleAdminChanged().processReceipt(tx_receipt)
    def get_role_granted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleGranted event.

        :param tx_hash: hash of transaction emitting RoleGranted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TWFactory.abi()).events.RoleGranted().processReceipt(tx_receipt)
    def get_role_revoked_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleRevoked event.

        :param tx_hash: hash of transaction emitting RoleRevoked event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TWFactory.abi()).events.RoleRevoked().processReceipt(tx_receipt)

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_trustedForwarder","type":"address"},{"internalType":"address","name":"_registry","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"implementation","type":"address"},{"indexed":true,"internalType":"bytes32","name":"contractType","type":"bytes32"},{"indexed":false,"internalType":"uint256","name":"version","type":"uint256"}],"name":"ImplementationAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"implementation","type":"address"},{"indexed":false,"internalType":"bool","name":"isApproved","type":"bool"}],"name":"ImplementationApproved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"},{"indexed":false,"internalType":"address","name":"proxy","type":"address"},{"indexed":true,"internalType":"address","name":"deployer","type":"address"}],"name":"ProxyDeployed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"FACTORY_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_implementation","type":"address"}],"name":"addImplementation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"approval","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_implementation","type":"address"},{"internalType":"bool","name":"_toApprove","type":"bool"}],"name":"approveImplementation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"currentVersion","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_type","type":"bytes32"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"deployProxy","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_implementation","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes32","name":"_salt","type":"bytes32"}],"name":"deployProxyByImplementation","outputs":[{"internalType":"address","name":"deployedProxy","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_type","type":"bytes32"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"bytes32","name":"_salt","type":"bytes32"}],"name":"deployProxyDeterministic","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"deployer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_type","type":"bytes32"},{"internalType":"uint256","name":"_version","type":"uint256"}],"name":"getImplementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_type","type":"bytes32"}],"name":"getLatestImplementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"},{"internalType":"uint256","name":"index_1","type":"uint256"}],"name":"implementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"registry","outputs":[{"internalType":"contract TWRegistry","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
