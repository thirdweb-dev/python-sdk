"""Generated wrapper for Multiwrap Solidity contract."""

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
# constructor for Multiwrap below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        MultiwrapValidator,
    )
except ImportError:

    class MultiwrapValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class ITokenBundleToken(TypedDict):
    """Python representation of a tuple or struct.

    Solidity compiler output does not include the names of structs that appear
    in method definitions.  A tuple found in an ABI may have been written in
    Solidity as a literal, anonymous tuple, or it may have been written as a
    named `struct`:code:, but there is no way to tell from the compiler
    output.  This class represents a tuple that appeared in a method
    definition.  Its name is derived from a hash of that tuple's field names,
    and every method whose ABI refers to a tuple with that same list of field
    names will have a generated wrapper method that refers to this class.

    Any members of type `bytes`:code: should be encoded as UTF-8, which can be
    accomplished via `str.encode("utf_8")`:code:
    """

    assetContract: str

    tokenType: int

    tokenId: int

    totalAmount: int


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

class ApproveMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the approve method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, to: str, token_id: int):
        """Validate the inputs to the approve method."""
        self.validator.assert_valid(
            method_name='approve',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='approve',
            parameter_name='tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (to, token_id)

    def call(self, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (to, token_id) = self.validate_and_normalize_inputs(to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(to, token_id).call(tx_params.as_dict())

    def send_transaction(self, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, token_id) = self.validate_and_normalize_inputs(to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, token_id).transact(tx_params.as_dict())

    def build_transaction(self, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, token_id) = self.validate_and_normalize_inputs(to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, token_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (to, token_id) = self.validate_and_normalize_inputs(to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, token_id).estimateGas(tx_params.as_dict())

class BalanceOfMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the balanceOf method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, owner: str):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name='balanceOf',
            parameter_name='owner',
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        return (owner)

    def call(self, owner: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, owner: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).transact(tx_params.as_dict())

    def build_transaction(self, owner: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, owner: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (owner) = self.validate_and_normalize_inputs(owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner).estimateGas(tx_params.as_dict())

class ContractTypeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the contractType method."""

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

class ContractUriMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the contractURI method."""

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

class ContractVersionMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the contractVersion method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

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

class GetApprovedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getApproved method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the getApproved method."""
        self.validator.assert_valid(
            method_name='getApproved',
            parameter_name='tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (token_id)

    def call(self, token_id: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, token_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).estimateGas(tx_params.as_dict())

class GetDefaultRoyaltyInfoMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getDefaultRoyaltyInfo method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return (returned[0],returned[1],)

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

class GetRoyaltyInfoForTokenMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRoyaltyInfoForToken method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the getRoyaltyInfoForToken method."""
        self.validator.assert_valid(
            method_name='getRoyaltyInfoForToken',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (token_id)

    def call(self, token_id: int, tx_params: Optional[TxParams] = None) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id).call(tx_params.as_dict())
        return (returned[0],returned[1],)

    def send_transaction(self, token_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).estimateGas(tx_params.as_dict())

class GetTokenCountOfBundleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getTokenCountOfBundle method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, bundle_id: int):
        """Validate the inputs to the getTokenCountOfBundle method."""
        self.validator.assert_valid(
            method_name='getTokenCountOfBundle',
            parameter_name='_bundleId',
            argument_value=bundle_id,
        )
        # safeguard against fractional inputs
        bundle_id = int(bundle_id)
        return (bundle_id)

    def call(self, bundle_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(bundle_id).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, bundle_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).transact(tx_params.as_dict())

    def build_transaction(self, bundle_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, bundle_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).estimateGas(tx_params.as_dict())

class GetTokenOfBundleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getTokenOfBundle method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, bundle_id: int, index: int):
        """Validate the inputs to the getTokenOfBundle method."""
        self.validator.assert_valid(
            method_name='getTokenOfBundle',
            parameter_name='_bundleId',
            argument_value=bundle_id,
        )
        # safeguard against fractional inputs
        bundle_id = int(bundle_id)
        self.validator.assert_valid(
            method_name='getTokenOfBundle',
            parameter_name='index',
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (bundle_id, index)

    def call(self, bundle_id: int, index: int, tx_params: Optional[TxParams] = None) -> ITokenBundleToken:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (bundle_id, index) = self.validate_and_normalize_inputs(bundle_id, index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(bundle_id, index).call(tx_params.as_dict())
        return ITokenBundleToken(assetContract=returned[0],tokenType=returned[1],tokenId=returned[2],totalAmount=returned[3],)

    def send_transaction(self, bundle_id: int, index: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (bundle_id, index) = self.validate_and_normalize_inputs(bundle_id, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id, index).transact(tx_params.as_dict())

    def build_transaction(self, bundle_id: int, index: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (bundle_id, index) = self.validate_and_normalize_inputs(bundle_id, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id, index).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, bundle_id: int, index: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (bundle_id, index) = self.validate_and_normalize_inputs(bundle_id, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id, index).estimateGas(tx_params.as_dict())

class GetUriOfBundleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getUriOfBundle method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, bundle_id: int):
        """Validate the inputs to the getUriOfBundle method."""
        self.validator.assert_valid(
            method_name='getUriOfBundle',
            parameter_name='_bundleId',
            argument_value=bundle_id,
        )
        # safeguard against fractional inputs
        bundle_id = int(bundle_id)
        return (bundle_id)

    def call(self, bundle_id: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(bundle_id).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, bundle_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).transact(tx_params.as_dict())

    def build_transaction(self, bundle_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, bundle_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).estimateGas(tx_params.as_dict())

class GetWrappedContentsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getWrappedContents method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the getWrappedContents method."""
        self.validator.assert_valid(
            method_name='getWrappedContents',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (token_id)

    def call(self, token_id: int, tx_params: Optional[TxParams] = None) -> List[ITokenBundleToken]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id).call(tx_params.as_dict())
        return [ITokenBundleToken(assetContract=element[0],tokenType=element[1],tokenId=element[2],totalAmount=element[3],) for element in returned]

    def send_transaction(self, token_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).estimateGas(tx_params.as_dict())

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

class HasRoleWithSwitchMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the hasRoleWithSwitch method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the hasRoleWithSwitch method."""
        self.validator.assert_valid(
            method_name='hasRoleWithSwitch',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='hasRoleWithSwitch',
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

class InitializeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the initialize method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, default_admin: str, name: str, symbol: str, contract_uri: str, trusted_forwarders: List[str], royalty_recipient: str, royalty_bps: int):
        """Validate the inputs to the initialize method."""
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_defaultAdmin',
            argument_value=default_admin,
        )
        default_admin = self.validate_and_checksum_address(default_admin)
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_name',
            argument_value=name,
        )
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_symbol',
            argument_value=symbol,
        )
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_contractURI',
            argument_value=contract_uri,
        )
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_trustedForwarders',
            argument_value=trusted_forwarders,
        )
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_royaltyRecipient',
            argument_value=royalty_recipient,
        )
        royalty_recipient = self.validate_and_checksum_address(royalty_recipient)
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_royaltyBps',
            argument_value=royalty_bps,
        )
        # safeguard against fractional inputs
        royalty_bps = int(royalty_bps)
        return (default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps)

    def call(self, default_admin: str, name: str, symbol: str, contract_uri: str, trusted_forwarders: List[str], royalty_recipient: str, royalty_bps: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps).call(tx_params.as_dict())

    def send_transaction(self, default_admin: str, name: str, symbol: str, contract_uri: str, trusted_forwarders: List[str], royalty_recipient: str, royalty_bps: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps).transact(tx_params.as_dict())

    def build_transaction(self, default_admin: str, name: str, symbol: str, contract_uri: str, trusted_forwarders: List[str], royalty_recipient: str, royalty_bps: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, default_admin: str, name: str, symbol: str, contract_uri: str, trusted_forwarders: List[str], royalty_recipient: str, royalty_bps: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin, name, symbol, contract_uri, trusted_forwarders, royalty_recipient, royalty_bps).estimateGas(tx_params.as_dict())

class IsApprovedForAllMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isApprovedForAll method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, owner: str, operator: str):
        """Validate the inputs to the isApprovedForAll method."""
        self.validator.assert_valid(
            method_name='isApprovedForAll',
            parameter_name='owner',
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name='isApprovedForAll',
            parameter_name='operator',
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return (owner, operator)

    def call(self, owner: str, operator: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner, operator) = self.validate_and_normalize_inputs(owner, operator)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner, operator).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, owner: str, operator: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner, operator) = self.validate_and_normalize_inputs(owner, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, operator).transact(tx_params.as_dict())

    def build_transaction(self, owner: str, operator: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner, operator) = self.validate_and_normalize_inputs(owner, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, operator).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, owner: str, operator: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (owner, operator) = self.validate_and_normalize_inputs(owner, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, operator).estimateGas(tx_params.as_dict())

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

class NameMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the name method."""

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

class NextTokenIdToMintMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the nextTokenIdToMint method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

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

class OnErc1155BatchReceivedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the onERC1155BatchReceived method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str, index_1: str, index_2: List[int], index_3: List[int], index_4: Union[bytes, str]):
        """Validate the inputs to the onERC1155BatchReceived method."""
        self.validator.assert_valid(
            method_name='onERC1155BatchReceived',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name='onERC1155BatchReceived',
            parameter_name='index_1',
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name='onERC1155BatchReceived',
            parameter_name='index_2',
            argument_value=index_2,
        )
        self.validator.assert_valid(
            method_name='onERC1155BatchReceived',
            parameter_name='index_3',
            argument_value=index_3,
        )
        self.validator.assert_valid(
            method_name='onERC1155BatchReceived',
            parameter_name='index_4',
            argument_value=index_4,
        )
        return (index_0, index_1, index_2, index_3, index_4)

    def call(self, index_0: str, index_1: str, index_2: List[int], index_3: List[int], index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1, index_2, index_3, index_4).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, index_0: str, index_1: str, index_2: List[int], index_3: List[int], index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, index_1: str, index_2: List[int], index_3: List[int], index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, index_1: str, index_2: List[int], index_3: List[int], index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).estimateGas(tx_params.as_dict())

class OnErc1155ReceivedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the onERC1155Received method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str, index_1: str, index_2: int, index_3: int, index_4: Union[bytes, str]):
        """Validate the inputs to the onERC1155Received method."""
        self.validator.assert_valid(
            method_name='onERC1155Received',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name='onERC1155Received',
            parameter_name='index_1',
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name='onERC1155Received',
            parameter_name='index_2',
            argument_value=index_2,
        )
        # safeguard against fractional inputs
        index_2 = int(index_2)
        self.validator.assert_valid(
            method_name='onERC1155Received',
            parameter_name='index_3',
            argument_value=index_3,
        )
        # safeguard against fractional inputs
        index_3 = int(index_3)
        self.validator.assert_valid(
            method_name='onERC1155Received',
            parameter_name='index_4',
            argument_value=index_4,
        )
        return (index_0, index_1, index_2, index_3, index_4)

    def call(self, index_0: str, index_1: str, index_2: int, index_3: int, index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1, index_2, index_3, index_4).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, index_0: str, index_1: str, index_2: int, index_3: int, index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, index_1: str, index_2: int, index_3: int, index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, index_1: str, index_2: int, index_3: int, index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).estimateGas(tx_params.as_dict())

class OnErc721ReceivedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the onERC721Received method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str, index_1: str, index_2: int, index_3: Union[bytes, str]):
        """Validate the inputs to the onERC721Received method."""
        self.validator.assert_valid(
            method_name='onERC721Received',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name='onERC721Received',
            parameter_name='index_1',
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name='onERC721Received',
            parameter_name='index_2',
            argument_value=index_2,
        )
        # safeguard against fractional inputs
        index_2 = int(index_2)
        self.validator.assert_valid(
            method_name='onERC721Received',
            parameter_name='index_3',
            argument_value=index_3,
        )
        return (index_0, index_1, index_2, index_3)

    def call(self, index_0: str, index_1: str, index_2: int, index_3: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1, index_2, index_3) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1, index_2, index_3).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, index_0: str, index_1: str, index_2: int, index_3: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1, index_2, index_3) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, index_1: str, index_2: int, index_3: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1, index_2, index_3) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, index_1: str, index_2: int, index_3: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1, index_2, index_3) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3).estimateGas(tx_params.as_dict())

class OwnerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the owner method."""

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

class OwnerOfMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the ownerOf method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the ownerOf method."""
        self.validator.assert_valid(
            method_name='ownerOf',
            parameter_name='tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (token_id)

    def call(self, token_id: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, token_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).estimateGas(tx_params.as_dict())

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

class RoyaltyInfoMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the royaltyInfo method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int, sale_price: int):
        """Validate the inputs to the royaltyInfo method."""
        self.validator.assert_valid(
            method_name='royaltyInfo',
            parameter_name='tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='royaltyInfo',
            parameter_name='salePrice',
            argument_value=sale_price,
        )
        # safeguard against fractional inputs
        sale_price = int(sale_price)
        return (token_id, sale_price)

    def call(self, token_id: int, sale_price: int, tx_params: Optional[TxParams] = None) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, sale_price) = self.validate_and_normalize_inputs(token_id, sale_price)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id, sale_price).call(tx_params.as_dict())
        return (returned[0],returned[1],)

    def send_transaction(self, token_id: int, sale_price: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, sale_price) = self.validate_and_normalize_inputs(token_id, sale_price)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, sale_price).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, sale_price: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, sale_price) = self.validate_and_normalize_inputs(token_id, sale_price)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, sale_price).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, sale_price: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id, sale_price) = self.validate_and_normalize_inputs(token_id, sale_price)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, sale_price).estimateGas(tx_params.as_dict())

class SafeTransferFrom1Method(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the safeTransferFrom method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _from: str, to: str, token_id: int):
        """Validate the inputs to the safeTransferFrom method."""
        self.validator.assert_valid(
            method_name='safeTransferFrom',
            parameter_name='from',
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name='safeTransferFrom',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='safeTransferFrom',
            parameter_name='tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (_from, to, token_id)

    def call(self, _from: str, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, token_id) = self.validate_and_normalize_inputs(_from, to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, token_id).call(tx_params.as_dict())

    def send_transaction(self, _from: str, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, token_id) = self.validate_and_normalize_inputs(_from, to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, token_id).transact(tx_params.as_dict())

    def build_transaction(self, _from: str, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, token_id) = self.validate_and_normalize_inputs(_from, to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, token_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _from: str, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, token_id) = self.validate_and_normalize_inputs(_from, to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, token_id).estimateGas(tx_params.as_dict())

class SafeTransferFrom2Method(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the safeTransferFrom method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _from: str, to: str, token_id: int, data: Union[bytes, str]):
        """Validate the inputs to the safeTransferFrom method."""
        self.validator.assert_valid(
            method_name='safeTransferFrom',
            parameter_name='from',
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name='safeTransferFrom',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='safeTransferFrom',
            parameter_name='tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='safeTransferFrom',
            parameter_name='data',
            argument_value=data,
        )
        return (_from, to, token_id, data)

    def call(self, _from: str, to: str, token_id: int, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, token_id, data) = self.validate_and_normalize_inputs(_from, to, token_id, data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, token_id, data).call(tx_params.as_dict())

    def send_transaction(self, _from: str, to: str, token_id: int, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, token_id, data) = self.validate_and_normalize_inputs(_from, to, token_id, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, token_id, data).transact(tx_params.as_dict())

    def build_transaction(self, _from: str, to: str, token_id: int, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, token_id, data) = self.validate_and_normalize_inputs(_from, to, token_id, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, token_id, data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _from: str, to: str, token_id: int, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, token_id, data) = self.validate_and_normalize_inputs(_from, to, token_id, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, token_id, data).estimateGas(tx_params.as_dict())

class SetApprovalForAllMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setApprovalForAll method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, operator: str, approved: bool):
        """Validate the inputs to the setApprovalForAll method."""
        self.validator.assert_valid(
            method_name='setApprovalForAll',
            parameter_name='operator',
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name='setApprovalForAll',
            parameter_name='approved',
            argument_value=approved,
        )
        return (operator, approved)

    def call(self, operator: str, approved: bool, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator, approved) = self.validate_and_normalize_inputs(operator, approved)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(operator, approved).call(tx_params.as_dict())

    def send_transaction(self, operator: str, approved: bool, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator, approved) = self.validate_and_normalize_inputs(operator, approved)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, approved).transact(tx_params.as_dict())

    def build_transaction(self, operator: str, approved: bool, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator, approved) = self.validate_and_normalize_inputs(operator, approved)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, approved).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, operator: str, approved: bool, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (operator, approved) = self.validate_and_normalize_inputs(operator, approved)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, approved).estimateGas(tx_params.as_dict())

class SetContractUriMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setContractURI method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, uri: str):
        """Validate the inputs to the setContractURI method."""
        self.validator.assert_valid(
            method_name='setContractURI',
            parameter_name='_uri',
            argument_value=uri,
        )
        return (uri)

    def call(self, uri: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(uri).call(tx_params.as_dict())

    def send_transaction(self, uri: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).transact(tx_params.as_dict())

    def build_transaction(self, uri: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, uri: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).estimateGas(tx_params.as_dict())

class SetDefaultRoyaltyInfoMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setDefaultRoyaltyInfo method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, royalty_recipient: str, royalty_bps: int):
        """Validate the inputs to the setDefaultRoyaltyInfo method."""
        self.validator.assert_valid(
            method_name='setDefaultRoyaltyInfo',
            parameter_name='_royaltyRecipient',
            argument_value=royalty_recipient,
        )
        royalty_recipient = self.validate_and_checksum_address(royalty_recipient)
        self.validator.assert_valid(
            method_name='setDefaultRoyaltyInfo',
            parameter_name='_royaltyBps',
            argument_value=royalty_bps,
        )
        # safeguard against fractional inputs
        royalty_bps = int(royalty_bps)
        return (royalty_recipient, royalty_bps)

    def call(self, royalty_recipient: str, royalty_bps: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(royalty_recipient, royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(royalty_recipient, royalty_bps).call(tx_params.as_dict())

    def send_transaction(self, royalty_recipient: str, royalty_bps: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(royalty_recipient, royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(royalty_recipient, royalty_bps).transact(tx_params.as_dict())

    def build_transaction(self, royalty_recipient: str, royalty_bps: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(royalty_recipient, royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(royalty_recipient, royalty_bps).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, royalty_recipient: str, royalty_bps: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(royalty_recipient, royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(royalty_recipient, royalty_bps).estimateGas(tx_params.as_dict())

class SetOwnerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setOwner method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, new_owner: str):
        """Validate the inputs to the setOwner method."""
        self.validator.assert_valid(
            method_name='setOwner',
            parameter_name='_newOwner',
            argument_value=new_owner,
        )
        new_owner = self.validate_and_checksum_address(new_owner)
        return (new_owner)

    def call(self, new_owner: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_owner).call(tx_params.as_dict())

    def send_transaction(self, new_owner: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).transact(tx_params.as_dict())

    def build_transaction(self, new_owner: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, new_owner: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).estimateGas(tx_params.as_dict())

class SetRoyaltyInfoForTokenMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setRoyaltyInfoForToken method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int, recipient: str, bps: int):
        """Validate the inputs to the setRoyaltyInfoForToken method."""
        self.validator.assert_valid(
            method_name='setRoyaltyInfoForToken',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='setRoyaltyInfoForToken',
            parameter_name='_recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        self.validator.assert_valid(
            method_name='setRoyaltyInfoForToken',
            parameter_name='_bps',
            argument_value=bps,
        )
        # safeguard against fractional inputs
        bps = int(bps)
        return (token_id, recipient, bps)

    def call(self, token_id: int, recipient: str, bps: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, recipient, bps) = self.validate_and_normalize_inputs(token_id, recipient, bps)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, recipient, bps).call(tx_params.as_dict())

    def send_transaction(self, token_id: int, recipient: str, bps: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, recipient, bps) = self.validate_and_normalize_inputs(token_id, recipient, bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient, bps).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, recipient: str, bps: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, recipient, bps) = self.validate_and_normalize_inputs(token_id, recipient, bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient, bps).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, recipient: str, bps: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id, recipient, bps) = self.validate_and_normalize_inputs(token_id, recipient, bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient, bps).estimateGas(tx_params.as_dict())

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

class SymbolMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the symbol method."""

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

class TokenByIndexMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the tokenByIndex method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index: int):
        """Validate the inputs to the tokenByIndex method."""
        self.validator.assert_valid(
            method_name='tokenByIndex',
            parameter_name='index',
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (index)

    def call(self, index: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, index: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index).transact(tx_params.as_dict())

    def build_transaction(self, index: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index).estimateGas(tx_params.as_dict())

class TokenOfOwnerByIndexMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the tokenOfOwnerByIndex method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, owner: str, index: int):
        """Validate the inputs to the tokenOfOwnerByIndex method."""
        self.validator.assert_valid(
            method_name='tokenOfOwnerByIndex',
            parameter_name='owner',
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name='tokenOfOwnerByIndex',
            parameter_name='index',
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (owner, index)

    def call(self, owner: str, index: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner, index) = self.validate_and_normalize_inputs(owner, index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner, index).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, owner: str, index: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner, index) = self.validate_and_normalize_inputs(owner, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, index).transact(tx_params.as_dict())

    def build_transaction(self, owner: str, index: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner, index) = self.validate_and_normalize_inputs(owner, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, index).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, owner: str, index: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (owner, index) = self.validate_and_normalize_inputs(owner, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, index).estimateGas(tx_params.as_dict())

class TokenUriMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the tokenURI method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the tokenURI method."""
        self.validator.assert_valid(
            method_name='tokenURI',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (token_id)

    def call(self, token_id: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, token_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).estimateGas(tx_params.as_dict())

class TotalSupplyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the totalSupply method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

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

class TransferFromMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the transferFrom method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _from: str, to: str, token_id: int):
        """Validate the inputs to the transferFrom method."""
        self.validator.assert_valid(
            method_name='transferFrom',
            parameter_name='from',
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name='transferFrom',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='transferFrom',
            parameter_name='tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (_from, to, token_id)

    def call(self, _from: str, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, token_id) = self.validate_and_normalize_inputs(_from, to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, token_id).call(tx_params.as_dict())

    def send_transaction(self, _from: str, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, token_id) = self.validate_and_normalize_inputs(_from, to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, token_id).transact(tx_params.as_dict())

    def build_transaction(self, _from: str, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, token_id) = self.validate_and_normalize_inputs(_from, to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, token_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _from: str, to: str, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, token_id) = self.validate_and_normalize_inputs(_from, to, token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, token_id).estimateGas(tx_params.as_dict())

class UnwrapMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the unwrap method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int, recipient: str):
        """Validate the inputs to the unwrap method."""
        self.validator.assert_valid(
            method_name='unwrap',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='unwrap',
            parameter_name='_recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        return (token_id, recipient)

    def call(self, token_id: int, recipient: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, recipient) = self.validate_and_normalize_inputs(token_id, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, recipient).call(tx_params.as_dict())

    def send_transaction(self, token_id: int, recipient: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, recipient) = self.validate_and_normalize_inputs(token_id, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, recipient: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, recipient) = self.validate_and_normalize_inputs(token_id, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, recipient: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id, recipient) = self.validate_and_normalize_inputs(token_id, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient).estimateGas(tx_params.as_dict())

class WrapMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the wrap method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, tokens_to_wrap: List[ITokenBundleToken], uri_for_wrapped_token: str, recipient: str):
        """Validate the inputs to the wrap method."""
        self.validator.assert_valid(
            method_name='wrap',
            parameter_name='_tokensToWrap',
            argument_value=tokens_to_wrap,
        )
        self.validator.assert_valid(
            method_name='wrap',
            parameter_name='_uriForWrappedToken',
            argument_value=uri_for_wrapped_token,
        )
        self.validator.assert_valid(
            method_name='wrap',
            parameter_name='_recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        return (tokens_to_wrap, uri_for_wrapped_token, recipient)

    def call(self, tokens_to_wrap: List[ITokenBundleToken], uri_for_wrapped_token: str, recipient: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (tokens_to_wrap, uri_for_wrapped_token, recipient) = self.validate_and_normalize_inputs(tokens_to_wrap, uri_for_wrapped_token, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(tokens_to_wrap, uri_for_wrapped_token, recipient).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, tokens_to_wrap: List[ITokenBundleToken], uri_for_wrapped_token: str, recipient: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (tokens_to_wrap, uri_for_wrapped_token, recipient) = self.validate_and_normalize_inputs(tokens_to_wrap, uri_for_wrapped_token, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(tokens_to_wrap, uri_for_wrapped_token, recipient).transact(tx_params.as_dict())

    def build_transaction(self, tokens_to_wrap: List[ITokenBundleToken], uri_for_wrapped_token: str, recipient: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (tokens_to_wrap, uri_for_wrapped_token, recipient) = self.validate_and_normalize_inputs(tokens_to_wrap, uri_for_wrapped_token, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(tokens_to_wrap, uri_for_wrapped_token, recipient).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tokens_to_wrap: List[ITokenBundleToken], uri_for_wrapped_token: str, recipient: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (tokens_to_wrap, uri_for_wrapped_token, recipient) = self.validate_and_normalize_inputs(tokens_to_wrap, uri_for_wrapped_token, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(tokens_to_wrap, uri_for_wrapped_token, recipient).estimateGas(tx_params.as_dict())

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Multiwrap:
    """Wrapper class for Multiwrap Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """
    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

    approve: ApproveMethod
    """Constructor-initialized instance of
    :class:`ApproveMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    contract_type: ContractTypeMethod
    """Constructor-initialized instance of
    :class:`ContractTypeMethod`.
    """

    contract_uri: ContractUriMethod
    """Constructor-initialized instance of
    :class:`ContractUriMethod`.
    """

    contract_version: ContractVersionMethod
    """Constructor-initialized instance of
    :class:`ContractVersionMethod`.
    """

    get_approved: GetApprovedMethod
    """Constructor-initialized instance of
    :class:`GetApprovedMethod`.
    """

    get_default_royalty_info: GetDefaultRoyaltyInfoMethod
    """Constructor-initialized instance of
    :class:`GetDefaultRoyaltyInfoMethod`.
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

    get_royalty_info_for_token: GetRoyaltyInfoForTokenMethod
    """Constructor-initialized instance of
    :class:`GetRoyaltyInfoForTokenMethod`.
    """

    get_token_count_of_bundle: GetTokenCountOfBundleMethod
    """Constructor-initialized instance of
    :class:`GetTokenCountOfBundleMethod`.
    """

    get_token_of_bundle: GetTokenOfBundleMethod
    """Constructor-initialized instance of
    :class:`GetTokenOfBundleMethod`.
    """

    get_uri_of_bundle: GetUriOfBundleMethod
    """Constructor-initialized instance of
    :class:`GetUriOfBundleMethod`.
    """

    get_wrapped_contents: GetWrappedContentsMethod
    """Constructor-initialized instance of
    :class:`GetWrappedContentsMethod`.
    """

    grant_role: GrantRoleMethod
    """Constructor-initialized instance of
    :class:`GrantRoleMethod`.
    """

    has_role: HasRoleMethod
    """Constructor-initialized instance of
    :class:`HasRoleMethod`.
    """

    has_role_with_switch: HasRoleWithSwitchMethod
    """Constructor-initialized instance of
    :class:`HasRoleWithSwitchMethod`.
    """

    initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
    """

    is_approved_for_all: IsApprovedForAllMethod
    """Constructor-initialized instance of
    :class:`IsApprovedForAllMethod`.
    """

    is_trusted_forwarder: IsTrustedForwarderMethod
    """Constructor-initialized instance of
    :class:`IsTrustedForwarderMethod`.
    """

    multicall: MulticallMethod
    """Constructor-initialized instance of
    :class:`MulticallMethod`.
    """

    name: NameMethod
    """Constructor-initialized instance of
    :class:`NameMethod`.
    """

    next_token_id_to_mint: NextTokenIdToMintMethod
    """Constructor-initialized instance of
    :class:`NextTokenIdToMintMethod`.
    """

    on_erc1155_batch_received: OnErc1155BatchReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc1155BatchReceivedMethod`.
    """

    on_erc1155_received: OnErc1155ReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc1155ReceivedMethod`.
    """

    on_erc721_received: OnErc721ReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc721ReceivedMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    owner_of: OwnerOfMethod
    """Constructor-initialized instance of
    :class:`OwnerOfMethod`.
    """

    renounce_role: RenounceRoleMethod
    """Constructor-initialized instance of
    :class:`RenounceRoleMethod`.
    """

    revoke_role: RevokeRoleMethod
    """Constructor-initialized instance of
    :class:`RevokeRoleMethod`.
    """

    royalty_info: RoyaltyInfoMethod
    """Constructor-initialized instance of
    :class:`RoyaltyInfoMethod`.
    """

    safe_transfer_from1: SafeTransferFrom1Method
    """Constructor-initialized instance of
    :class:`SafeTransferFrom1Method`.
    """

    safe_transfer_from2: SafeTransferFrom2Method
    """Constructor-initialized instance of
    :class:`SafeTransferFrom2Method`.
    """

    set_approval_for_all: SetApprovalForAllMethod
    """Constructor-initialized instance of
    :class:`SetApprovalForAllMethod`.
    """

    set_contract_uri: SetContractUriMethod
    """Constructor-initialized instance of
    :class:`SetContractUriMethod`.
    """

    set_default_royalty_info: SetDefaultRoyaltyInfoMethod
    """Constructor-initialized instance of
    :class:`SetDefaultRoyaltyInfoMethod`.
    """

    set_owner: SetOwnerMethod
    """Constructor-initialized instance of
    :class:`SetOwnerMethod`.
    """

    set_royalty_info_for_token: SetRoyaltyInfoForTokenMethod
    """Constructor-initialized instance of
    :class:`SetRoyaltyInfoForTokenMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    symbol: SymbolMethod
    """Constructor-initialized instance of
    :class:`SymbolMethod`.
    """

    token_by_index: TokenByIndexMethod
    """Constructor-initialized instance of
    :class:`TokenByIndexMethod`.
    """

    token_of_owner_by_index: TokenOfOwnerByIndexMethod
    """Constructor-initialized instance of
    :class:`TokenOfOwnerByIndexMethod`.
    """

    token_uri: TokenUriMethod
    """Constructor-initialized instance of
    :class:`TokenUriMethod`.
    """

    total_supply: TotalSupplyMethod
    """Constructor-initialized instance of
    :class:`TotalSupplyMethod`.
    """

    transfer_from: TransferFromMethod
    """Constructor-initialized instance of
    :class:`TransferFromMethod`.
    """

    unwrap: UnwrapMethod
    """Constructor-initialized instance of
    :class:`UnwrapMethod`.
    """

    wrap: WrapMethod
    """Constructor-initialized instance of
    :class:`WrapMethod`.
    """


    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: MultiwrapValidator = None,
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
            validator = MultiwrapValidator(web3_or_provider, contract_address)

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

        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=Multiwrap.abi()).functions

        self.default_admin_role = DefaultAdminRoleMethod(web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE)

        self.approve = ApproveMethod(web3_or_provider, contract_address, functions.approve, validator)

        self.balance_of = BalanceOfMethod(web3_or_provider, contract_address, functions.balanceOf, validator)

        self.contract_type = ContractTypeMethod(web3_or_provider, contract_address, functions.contractType)

        self.contract_uri = ContractUriMethod(web3_or_provider, contract_address, functions.contractURI)

        self.contract_version = ContractVersionMethod(web3_or_provider, contract_address, functions.contractVersion)

        self.get_approved = GetApprovedMethod(web3_or_provider, contract_address, functions.getApproved, validator)

        self.get_default_royalty_info = GetDefaultRoyaltyInfoMethod(web3_or_provider, contract_address, functions.getDefaultRoyaltyInfo)

        self.get_role_admin = GetRoleAdminMethod(web3_or_provider, contract_address, functions.getRoleAdmin, validator)

        self.get_role_member = GetRoleMemberMethod(web3_or_provider, contract_address, functions.getRoleMember, validator)

        self.get_role_member_count = GetRoleMemberCountMethod(web3_or_provider, contract_address, functions.getRoleMemberCount, validator)

        self.get_royalty_info_for_token = GetRoyaltyInfoForTokenMethod(web3_or_provider, contract_address, functions.getRoyaltyInfoForToken, validator)

        self.get_token_count_of_bundle = GetTokenCountOfBundleMethod(web3_or_provider, contract_address, functions.getTokenCountOfBundle, validator)

        self.get_token_of_bundle = GetTokenOfBundleMethod(web3_or_provider, contract_address, functions.getTokenOfBundle, validator)

        self.get_uri_of_bundle = GetUriOfBundleMethod(web3_or_provider, contract_address, functions.getUriOfBundle, validator)

        self.get_wrapped_contents = GetWrappedContentsMethod(web3_or_provider, contract_address, functions.getWrappedContents, validator)

        self.grant_role = GrantRoleMethod(web3_or_provider, contract_address, functions.grantRole, validator)

        self.has_role = HasRoleMethod(web3_or_provider, contract_address, functions.hasRole, validator)

        self.has_role_with_switch = HasRoleWithSwitchMethod(web3_or_provider, contract_address, functions.hasRoleWithSwitch, validator)

        self.initialize = InitializeMethod(web3_or_provider, contract_address, functions.initialize, validator)

        self.is_approved_for_all = IsApprovedForAllMethod(web3_or_provider, contract_address, functions.isApprovedForAll, validator)

        self.is_trusted_forwarder = IsTrustedForwarderMethod(web3_or_provider, contract_address, functions.isTrustedForwarder, validator)

        self.multicall = MulticallMethod(web3_or_provider, contract_address, functions.multicall, validator)

        self.name = NameMethod(web3_or_provider, contract_address, functions.name)

        self.next_token_id_to_mint = NextTokenIdToMintMethod(web3_or_provider, contract_address, functions.nextTokenIdToMint)

        self.on_erc1155_batch_received = OnErc1155BatchReceivedMethod(web3_or_provider, contract_address, functions.onERC1155BatchReceived, validator)

        self.on_erc1155_received = OnErc1155ReceivedMethod(web3_or_provider, contract_address, functions.onERC1155Received, validator)

        self.on_erc721_received = OnErc721ReceivedMethod(web3_or_provider, contract_address, functions.onERC721Received, validator)

        self.owner = OwnerMethod(web3_or_provider, contract_address, functions.owner)

        self.owner_of = OwnerOfMethod(web3_or_provider, contract_address, functions.ownerOf, validator)

        self.renounce_role = RenounceRoleMethod(web3_or_provider, contract_address, functions.renounceRole, validator)

        self.revoke_role = RevokeRoleMethod(web3_or_provider, contract_address, functions.revokeRole, validator)

        self.royalty_info = RoyaltyInfoMethod(web3_or_provider, contract_address, functions.royaltyInfo, validator)

        self.safe_transfer_from1 = SafeTransferFrom1Method(web3_or_provider, contract_address, functions.safeTransferFrom, validator)

        self.safe_transfer_from2 = SafeTransferFrom2Method(web3_or_provider, contract_address, functions.safeTransferFrom, validator)

        self.set_approval_for_all = SetApprovalForAllMethod(web3_or_provider, contract_address, functions.setApprovalForAll, validator)

        self.set_contract_uri = SetContractUriMethod(web3_or_provider, contract_address, functions.setContractURI, validator)

        self.set_default_royalty_info = SetDefaultRoyaltyInfoMethod(web3_or_provider, contract_address, functions.setDefaultRoyaltyInfo, validator)

        self.set_owner = SetOwnerMethod(web3_or_provider, contract_address, functions.setOwner, validator)

        self.set_royalty_info_for_token = SetRoyaltyInfoForTokenMethod(web3_or_provider, contract_address, functions.setRoyaltyInfoForToken, validator)

        self.supports_interface = SupportsInterfaceMethod(web3_or_provider, contract_address, functions.supportsInterface, validator)

        self.symbol = SymbolMethod(web3_or_provider, contract_address, functions.symbol)

        self.token_by_index = TokenByIndexMethod(web3_or_provider, contract_address, functions.tokenByIndex, validator)

        self.token_of_owner_by_index = TokenOfOwnerByIndexMethod(web3_or_provider, contract_address, functions.tokenOfOwnerByIndex, validator)

        self.token_uri = TokenUriMethod(web3_or_provider, contract_address, functions.tokenURI, validator)

        self.total_supply = TotalSupplyMethod(web3_or_provider, contract_address, functions.totalSupply)

        self.transfer_from = TransferFromMethod(web3_or_provider, contract_address, functions.transferFrom, validator)

        self.unwrap = UnwrapMethod(web3_or_provider, contract_address, functions.unwrap, validator)

        self.wrap = WrapMethod(web3_or_provider, contract_address, functions.wrap, validator)

    def get_approval_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Approval event.

        :param tx_hash: hash of transaction emitting Approval event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.Approval().processReceipt(tx_receipt)
    def get_approval_for_all_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ApprovalForAll event.

        :param tx_hash: hash of transaction emitting ApprovalForAll event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.ApprovalForAll().processReceipt(tx_receipt)
    def get_contract_uri_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ContractURIUpdated event.

        :param tx_hash: hash of transaction emitting ContractURIUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.ContractURIUpdated().processReceipt(tx_receipt)
    def get_default_royalty_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for DefaultRoyalty event.

        :param tx_hash: hash of transaction emitting DefaultRoyalty event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.DefaultRoyalty().processReceipt(tx_receipt)
    def get_initialized_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Initialized event.

        :param tx_hash: hash of transaction emitting Initialized event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.Initialized().processReceipt(tx_receipt)
    def get_owner_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OwnerUpdated event.

        :param tx_hash: hash of transaction emitting OwnerUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.OwnerUpdated().processReceipt(tx_receipt)
    def get_role_admin_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleAdminChanged event.

        :param tx_hash: hash of transaction emitting RoleAdminChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.RoleAdminChanged().processReceipt(tx_receipt)
    def get_role_granted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleGranted event.

        :param tx_hash: hash of transaction emitting RoleGranted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.RoleGranted().processReceipt(tx_receipt)
    def get_role_revoked_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleRevoked event.

        :param tx_hash: hash of transaction emitting RoleRevoked event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.RoleRevoked().processReceipt(tx_receipt)
    def get_royalty_for_token_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoyaltyForToken event.

        :param tx_hash: hash of transaction emitting RoyaltyForToken event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.RoyaltyForToken().processReceipt(tx_receipt)
    def get_tokens_unwrapped_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensUnwrapped event.

        :param tx_hash: hash of transaction emitting TokensUnwrapped event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.TokensUnwrapped().processReceipt(tx_receipt)
    def get_tokens_wrapped_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensWrapped event.

        :param tx_hash: hash of transaction emitting TokensWrapped event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.TokensWrapped().processReceipt(tx_receipt)
    def get_transfer_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Transfer event.

        :param tx_hash: hash of transaction emitting Transfer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Multiwrap.abi()).events.Transfer().processReceipt(tx_receipt)

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_nativeTokenWrapper","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"prevURI","type":"string"},{"indexed":false,"internalType":"string","name":"newURI","type":"string"}],"name":"ContractURIUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"newRoyaltyRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"newRoyaltyBps","type":"uint256"}],"name":"DefaultRoyalty","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prevOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"royaltyRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"royaltyBps","type":"uint256"}],"name":"RoyaltyForToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"unwrapper","type":"address"},{"indexed":true,"internalType":"address","name":"recipientOfWrappedContents","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenIdOfWrappedToken","type":"uint256"}],"name":"TokensUnwrapped","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"wrapper","type":"address"},{"indexed":true,"internalType":"address","name":"recipientOfWrappedToken","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenIdOfWrappedToken","type":"uint256"},{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"enum ITokenBundle.TokenType","name":"tokenType","type":"uint8"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"totalAmount","type":"uint256"}],"indexed":false,"internalType":"struct ITokenBundle.Token[]","name":"wrappedContents","type":"tuple[]"}],"name":"TokensWrapped","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractType","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractVersion","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getDefaultRoyaltyInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"member","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"count","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getRoyaltyInfoForToken","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_bundleId","type":"uint256"}],"name":"getTokenCountOfBundle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_bundleId","type":"uint256"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getTokenOfBundle","outputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"enum ITokenBundle.TokenType","name":"tokenType","type":"uint8"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"totalAmount","type":"uint256"}],"internalType":"struct ITokenBundle.Token","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_bundleId","type":"uint256"}],"name":"getUriOfBundle","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getWrappedContents","outputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"enum ITokenBundle.TokenType","name":"tokenType","type":"uint8"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"totalAmount","type":"uint256"}],"internalType":"struct ITokenBundle.Token[]","name":"contents","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRoleWithSwitch","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_defaultAdmin","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"string","name":"_contractURI","type":"string"},{"internalType":"address[]","name":"_trustedForwarders","type":"address[]"},{"internalType":"address","name":"_royaltyRecipient","type":"address"},{"internalType":"uint256","name":"_royaltyBps","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextTokenIdToMint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256[]","name":"index_2","type":"uint256[]"},{"internalType":"uint256[]","name":"index_3","type":"uint256[]"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155BatchReceived","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"uint256","name":"index_3","type":"uint256"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"bytes","name":"index_3","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"salePrice","type":"uint256"}],"name":"royaltyInfo","outputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"royaltyAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_uri","type":"string"}],"name":"setContractURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_royaltyRecipient","type":"address"},{"internalType":"uint256","name":"_royaltyBps","type":"uint256"}],"name":"setDefaultRoyaltyInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newOwner","type":"address"}],"name":"setOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_bps","type":"uint256"}],"name":"setRoyaltyInfoForToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"address","name":"_recipient","type":"address"}],"name":"unwrap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"enum ITokenBundle.TokenType","name":"tokenType","type":"uint8"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"totalAmount","type":"uint256"}],"internalType":"struct ITokenBundle.Token[]","name":"_tokensToWrap","type":"tuple[]"},{"internalType":"string","name":"_uriForWrappedToken","type":"string"},{"internalType":"address","name":"_recipient","type":"address"}],"name":"wrap","outputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
