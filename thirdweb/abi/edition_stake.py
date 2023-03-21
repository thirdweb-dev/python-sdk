"""Generated wrapper for EditionStake Solidity contract."""

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
# constructor for EditionStake below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        EditionStakeValidator,
    )
except ImportError:

    class EditionStakeValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class DefaultAdminRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the DEFAULT_ADMIN_ROLE method."""

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


class ClaimRewardsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the claimRewards method."""

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

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the claimRewards method."""
        self.validator.assert_valid(
            method_name="claimRewards",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return token_id

    def call(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id).call(tx_params.as_dict())

    def send_transaction(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).transact(tx_params.as_dict())

    def build_transaction(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).estimateGas(
            tx_params.as_dict()
        )


class ContractTypeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractType method."""

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


class ContractUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractURI method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
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


class ContractVersionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractVersion method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
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


class DepositRewardTokensMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the depositRewardTokens method."""

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
        """Validate the inputs to the depositRewardTokens method."""
        self.validator.assert_valid(
            method_name="depositRewardTokens",
            parameter_name="_amount",
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


class GetDefaultRewardsPerUnitTimeMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getDefaultRewardsPerUnitTime method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
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


class GetDefaultTimeUnitMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getDefaultTimeUnit method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
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


class GetRewardTokenBalanceMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getRewardTokenBalance method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
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


class GetRewardsPerUnitTimeMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getRewardsPerUnitTime method."""

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

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the getRewardsPerUnitTime method."""
        self.validator.assert_valid(
            method_name="getRewardsPerUnitTime",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return token_id

    def call(self, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).transact(tx_params.as_dict())

    def build_transaction(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).estimateGas(
            tx_params.as_dict()
        )


class GetRoleAdminMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getRoleAdmin method."""

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

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleAdmin method."""
        self.validator.assert_valid(
            method_name="getRoleAdmin",
            parameter_name="role",
            argument_value=role,
        )
        return role

    def call(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())


class GetRoleMemberMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getRoleMember method."""

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
        self, role: Union[bytes, str], index: int
    ):
        """Validate the inputs to the getRoleMember method."""
        self.validator.assert_valid(
            method_name="getRoleMember",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="getRoleMember",
            parameter_name="index",
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (role, index)

    def call(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, index).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).estimateGas(
            tx_params.as_dict()
        )


class GetRoleMemberCountMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getRoleMemberCount method."""

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

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleMemberCount method."""
        self.validator.assert_valid(
            method_name="getRoleMemberCount",
            parameter_name="role",
            argument_value=role,
        )
        return role

    def call(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())


class GetStakeInfoMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getStakeInfo method."""

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

    def validate_and_normalize_inputs(self, staker: str):
        """Validate the inputs to the getStakeInfo method."""
        self.validator.assert_valid(
            method_name="getStakeInfo",
            parameter_name="_staker",
            argument_value=staker,
        )
        staker = self.validate_and_checksum_address(staker)
        return staker

    def call(
        self, staker: str, tx_params: Optional[TxParams] = None
    ) -> Tuple[List[int], List[int], int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (staker) = self.validate_and_normalize_inputs(staker)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(staker).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def send_transaction(
        self, staker: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (staker) = self.validate_and_normalize_inputs(staker)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker).transact(tx_params.as_dict())

    def build_transaction(
        self, staker: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (staker) = self.validate_and_normalize_inputs(staker)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, staker: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (staker) = self.validate_and_normalize_inputs(staker)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(staker).estimateGas(tx_params.as_dict())


class GetStakeInfoForTokenMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getStakeInfoForToken method."""

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

    def validate_and_normalize_inputs(self, token_id: int, staker: str):
        """Validate the inputs to the getStakeInfoForToken method."""
        self.validator.assert_valid(
            method_name="getStakeInfoForToken",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="getStakeInfoForToken",
            parameter_name="_staker",
            argument_value=staker,
        )
        staker = self.validate_and_checksum_address(staker)
        return (token_id, staker)

    def call(
        self, token_id: int, staker: str, tx_params: Optional[TxParams] = None
    ) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, staker) = self.validate_and_normalize_inputs(
            token_id, staker
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id, staker).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self, token_id: int, staker: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, staker) = self.validate_and_normalize_inputs(
            token_id, staker
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, staker).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, token_id: int, staker: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, staker) = self.validate_and_normalize_inputs(
            token_id, staker
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, staker).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token_id: int, staker: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id, staker) = self.validate_and_normalize_inputs(
            token_id, staker
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, staker).estimateGas(
            tx_params.as_dict()
        )


class GetTimeUnitMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getTimeUnit method."""

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

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the getTimeUnit method."""
        self.validator.assert_valid(
            method_name="getTimeUnit",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return token_id

    def call(self, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).transact(tx_params.as_dict())

    def build_transaction(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).estimateGas(
            tx_params.as_dict()
        )


class GrantRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the grantRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the grantRole method."""
        self.validator.assert_valid(
            method_name="grantRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="grantRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class HasRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the hasRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the hasRole method."""
        self.validator.assert_valid(
            method_name="hasRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="hasRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, account).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class HasRoleWithSwitchMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the hasRoleWithSwitch method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the hasRoleWithSwitch method."""
        self.validator.assert_valid(
            method_name="hasRoleWithSwitch",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="hasRoleWithSwitch",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, account).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class IndexedTokensMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the indexedTokens method."""

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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the indexedTokens method."""
        self.validator.assert_valid(
            method_name="indexedTokens",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class InitializeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the initialize method."""

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
        default_admin: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        reward_token: str,
        staking_token: str,
        default_time_unit: int,
        default_rewards_per_unit_time: int,
    ):
        """Validate the inputs to the initialize method."""
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_defaultAdmin",
            argument_value=default_admin,
        )
        default_admin = self.validate_and_checksum_address(default_admin)
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_contractURI",
            argument_value=contract_uri,
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_trustedForwarders",
            argument_value=trusted_forwarders,
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_rewardToken",
            argument_value=reward_token,
        )
        reward_token = self.validate_and_checksum_address(reward_token)
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_stakingToken",
            argument_value=staking_token,
        )
        staking_token = self.validate_and_checksum_address(staking_token)
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_defaultTimeUnit",
            argument_value=default_time_unit,
        )
        # safeguard against fractional inputs
        default_time_unit = int(default_time_unit)
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_defaultRewardsPerUnitTime",
            argument_value=default_rewards_per_unit_time,
        )
        # safeguard against fractional inputs
        default_rewards_per_unit_time = int(default_rewards_per_unit_time)
        return (
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        )

    def call(
        self,
        default_admin: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        reward_token: str,
        staking_token: str,
        default_time_unit: int,
        default_rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        ) = self.validate_and_normalize_inputs(
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        default_admin: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        reward_token: str,
        staking_token: str,
        default_time_unit: int,
        default_rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        ) = self.validate_and_normalize_inputs(
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        default_admin: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        reward_token: str,
        staking_token: str,
        default_time_unit: int,
        default_rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        ) = self.validate_and_normalize_inputs(
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        default_admin: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        reward_token: str,
        staking_token: str,
        default_time_unit: int,
        default_rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        ) = self.validate_and_normalize_inputs(
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            default_admin,
            contract_uri,
            trusted_forwarders,
            reward_token,
            staking_token,
            default_time_unit,
            default_rewards_per_unit_time,
        ).estimateGas(tx_params.as_dict())


class IsIndexedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isIndexed method."""

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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the isIndexed method."""
        self.validator.assert_valid(
            method_name="isIndexed",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class IsTrustedForwarderMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isTrustedForwarder method."""

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

    def validate_and_normalize_inputs(self, forwarder: str):
        """Validate the inputs to the isTrustedForwarder method."""
        self.validator.assert_valid(
            method_name="isTrustedForwarder",
            parameter_name="forwarder",
            argument_value=forwarder,
        )
        forwarder = self.validate_and_checksum_address(forwarder)
        return forwarder

    def call(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(forwarder).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).transact(tx_params.as_dict())

    def build_transaction(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).estimateGas(
            tx_params.as_dict()
        )


class MulticallMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the multicall method."""

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

    def validate_and_normalize_inputs(self, data: List[Union[bytes, str]]):
        """Validate the inputs to the multicall method."""
        self.validator.assert_valid(
            method_name="multicall",
            parameter_name="data",
            argument_value=data,
        )
        return data

    def call(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> List[Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data).call(tx_params.as_dict())
        return [Union[bytes, str](element) for element in returned]

    def send_transaction(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).transact(tx_params.as_dict())

    def build_transaction(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).estimateGas(tx_params.as_dict())


class OnErc1155BatchReceivedMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the onERC1155BatchReceived method."""

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
        operator: str,
        _from: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
    ):
        """Validate the inputs to the onERC1155BatchReceived method."""
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="ids",
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="values",
            argument_value=values,
        )
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="data",
            argument_value=data,
        )
        return (operator, _from, ids, values, data)

    def call(
        self,
        operator: str,
        _from: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            operator,
            _from,
            ids,
            values,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            operator, _from, ids, values, data
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        operator: str,
        _from: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            operator,
            _from,
            ids,
            values,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, ids, values, data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        operator: str,
        _from: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            operator,
            _from,
            ids,
            values,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, ids, values, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        operator: str,
        _from: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            operator,
            _from,
            ids,
            values,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, ids, values, data
        ).estimateGas(tx_params.as_dict())


class OnErc1155ReceivedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the onERC1155Received method."""

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
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
    ):
        """Validate the inputs to the onERC1155Received method."""
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_2",
            argument_value=index_2,
        )
        # safeguard against fractional inputs
        index_2 = int(index_2)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_3",
            argument_value=index_3,
        )
        # safeguard against fractional inputs
        index_3 = int(index_3)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_4",
            argument_value=index_4,
        )
        return (index_0, index_1, index_2, index_3, index_4)

    def call(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).estimateGas(tx_params.as_dict())


class RenounceRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the renounceRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the renounceRole method."""
        self.validator.assert_valid(
            method_name="renounceRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="renounceRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class RevokeRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the revokeRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the revokeRole method."""
        self.validator.assert_valid(
            method_name="revokeRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="revokeRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class RewardTokenMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the rewardToken method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
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


class SetContractUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setContractURI method."""

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

    def validate_and_normalize_inputs(self, uri: str):
        """Validate the inputs to the setContractURI method."""
        self.validator.assert_valid(
            method_name="setContractURI",
            parameter_name="_uri",
            argument_value=uri,
        )
        return uri

    def call(self, uri: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(uri).call(tx_params.as_dict())

    def send_transaction(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).transact(tx_params.as_dict())

    def build_transaction(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).estimateGas(tx_params.as_dict())


class SetDefaultRewardsPerUnitTimeMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setDefaultRewardsPerUnitTime method."""

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
        self, default_rewards_per_unit_time: int
    ):
        """Validate the inputs to the setDefaultRewardsPerUnitTime method."""
        self.validator.assert_valid(
            method_name="setDefaultRewardsPerUnitTime",
            parameter_name="_defaultRewardsPerUnitTime",
            argument_value=default_rewards_per_unit_time,
        )
        # safeguard against fractional inputs
        default_rewards_per_unit_time = int(default_rewards_per_unit_time)
        return default_rewards_per_unit_time

    def call(
        self,
        default_rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (default_rewards_per_unit_time) = self.validate_and_normalize_inputs(
            default_rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(default_rewards_per_unit_time).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        default_rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (default_rewards_per_unit_time) = self.validate_and_normalize_inputs(
            default_rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_rewards_per_unit_time).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        default_rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (default_rewards_per_unit_time) = self.validate_and_normalize_inputs(
            default_rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            default_rewards_per_unit_time
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        default_rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (default_rewards_per_unit_time) = self.validate_and_normalize_inputs(
            default_rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            default_rewards_per_unit_time
        ).estimateGas(tx_params.as_dict())


class SetDefaultTimeUnitMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setDefaultTimeUnit method."""

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

    def validate_and_normalize_inputs(self, default_time_unit: int):
        """Validate the inputs to the setDefaultTimeUnit method."""
        self.validator.assert_valid(
            method_name="setDefaultTimeUnit",
            parameter_name="_defaultTimeUnit",
            argument_value=default_time_unit,
        )
        # safeguard against fractional inputs
        default_time_unit = int(default_time_unit)
        return default_time_unit

    def call(
        self, default_time_unit: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (default_time_unit) = self.validate_and_normalize_inputs(
            default_time_unit
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(default_time_unit).call(tx_params.as_dict())

    def send_transaction(
        self, default_time_unit: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (default_time_unit) = self.validate_and_normalize_inputs(
            default_time_unit
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_time_unit).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, default_time_unit: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (default_time_unit) = self.validate_and_normalize_inputs(
            default_time_unit
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_time_unit).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, default_time_unit: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (default_time_unit) = self.validate_and_normalize_inputs(
            default_time_unit
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_time_unit).estimateGas(
            tx_params.as_dict()
        )


class SetRewardsPerUnitTimeMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setRewardsPerUnitTime method."""

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
        self, token_id: int, rewards_per_unit_time: int
    ):
        """Validate the inputs to the setRewardsPerUnitTime method."""
        self.validator.assert_valid(
            method_name="setRewardsPerUnitTime",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="setRewardsPerUnitTime",
            parameter_name="_rewardsPerUnitTime",
            argument_value=rewards_per_unit_time,
        )
        # safeguard against fractional inputs
        rewards_per_unit_time = int(rewards_per_unit_time)
        return (token_id, rewards_per_unit_time)

    def call(
        self,
        token_id: int,
        rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, rewards_per_unit_time) = self.validate_and_normalize_inputs(
            token_id, rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, rewards_per_unit_time).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        token_id: int,
        rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, rewards_per_unit_time) = self.validate_and_normalize_inputs(
            token_id, rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, rewards_per_unit_time
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        token_id: int,
        rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, rewards_per_unit_time) = self.validate_and_normalize_inputs(
            token_id, rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, rewards_per_unit_time
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        token_id: int,
        rewards_per_unit_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id, rewards_per_unit_time) = self.validate_and_normalize_inputs(
            token_id, rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, rewards_per_unit_time
        ).estimateGas(tx_params.as_dict())


class SetTimeUnitMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setTimeUnit method."""

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

    def validate_and_normalize_inputs(self, token_id: int, time_unit: int):
        """Validate the inputs to the setTimeUnit method."""
        self.validator.assert_valid(
            method_name="setTimeUnit",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="setTimeUnit",
            parameter_name="_timeUnit",
            argument_value=time_unit,
        )
        # safeguard against fractional inputs
        time_unit = int(time_unit)
        return (token_id, time_unit)

    def call(
        self,
        token_id: int,
        time_unit: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, time_unit) = self.validate_and_normalize_inputs(
            token_id, time_unit
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, time_unit).call(tx_params.as_dict())

    def send_transaction(
        self,
        token_id: int,
        time_unit: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, time_unit) = self.validate_and_normalize_inputs(
            token_id, time_unit
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, time_unit).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        token_id: int,
        time_unit: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, time_unit) = self.validate_and_normalize_inputs(
            token_id, time_unit
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, time_unit).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        token_id: int,
        time_unit: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id, time_unit) = self.validate_and_normalize_inputs(
            token_id, time_unit
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, time_unit).estimateGas(
            tx_params.as_dict()
        )


class StakeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the stake method."""

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

    def validate_and_normalize_inputs(self, token_id: int, amount: int):
        """Validate the inputs to the stake method."""
        self.validator.assert_valid(
            method_name="stake",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="stake",
            parameter_name="_amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (token_id, amount)

    def call(
        self, token_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, amount) = self.validate_and_normalize_inputs(
            token_id, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, amount).call(tx_params.as_dict())

    def send_transaction(
        self, token_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, amount) = self.validate_and_normalize_inputs(
            token_id, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, token_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, amount) = self.validate_and_normalize_inputs(
            token_id, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id, amount) = self.validate_and_normalize_inputs(
            token_id, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, amount).estimateGas(
            tx_params.as_dict()
        )


class StakersMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the stakers method."""

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

    def validate_and_normalize_inputs(self, index_0: int, index_1: str):
        """Validate the inputs to the stakers method."""
        self.validator.assert_valid(
            method_name="stakers",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        self.validator.assert_valid(
            method_name="stakers",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        return (index_0, index_1)

    def call(
        self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None
    ) -> Tuple[int, int, int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
        )

    def send_transaction(
        self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


class StakersArrayMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the stakersArray method."""

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

    def validate_and_normalize_inputs(self, index_0: int, index_1: int):
        """Validate the inputs to the stakersArray method."""
        self.validator.assert_valid(
            method_name="stakersArray",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        self.validator.assert_valid(
            method_name="stakersArray",
            parameter_name="index_1",
            argument_value=index_1,
        )
        # safeguard against fractional inputs
        index_1 = int(index_1)
        return (index_0, index_1)

    def call(
        self, index_0: int, index_1: int, tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self, index_0: int, index_1: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, index_0: int, index_1: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, index_1: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


class StakingTokenMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the stakingToken method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
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


class SupportsInterfaceMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the supportsInterface method."""

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

    def validate_and_normalize_inputs(self, interface_id: Union[bytes, str]):
        """Validate the inputs to the supportsInterface method."""
        self.validator.assert_valid(
            method_name="supportsInterface",
            parameter_name="interfaceId",
            argument_value=interface_id,
        )
        return interface_id

    def call(
        self,
        interface_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(interface_id).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        interface_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        interface_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        interface_id: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).estimateGas(
            tx_params.as_dict()
        )


class WithdrawMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the withdraw method."""

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

    def validate_and_normalize_inputs(self, token_id: int, amount: int):
        """Validate the inputs to the withdraw method."""
        self.validator.assert_valid(
            method_name="withdraw",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="withdraw",
            parameter_name="_amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (token_id, amount)

    def call(
        self, token_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, amount) = self.validate_and_normalize_inputs(
            token_id, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, amount).call(tx_params.as_dict())

    def send_transaction(
        self, token_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, amount) = self.validate_and_normalize_inputs(
            token_id, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, token_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, amount) = self.validate_and_normalize_inputs(
            token_id, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id, amount) = self.validate_and_normalize_inputs(
            token_id, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, amount).estimateGas(
            tx_params.as_dict()
        )


class WithdrawRewardTokensMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the withdrawRewardTokens method."""

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
        """Validate the inputs to the withdrawRewardTokens method."""
        self.validator.assert_valid(
            method_name="withdrawRewardTokens",
            parameter_name="_amount",
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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class EditionStake:
    """Wrapper class for EditionStake Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

    claim_rewards: ClaimRewardsMethod
    """Constructor-initialized instance of
    :class:`ClaimRewardsMethod`.
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

    deposit_reward_tokens: DepositRewardTokensMethod
    """Constructor-initialized instance of
    :class:`DepositRewardTokensMethod`.
    """

    get_default_rewards_per_unit_time: GetDefaultRewardsPerUnitTimeMethod
    """Constructor-initialized instance of
    :class:`GetDefaultRewardsPerUnitTimeMethod`.
    """

    get_default_time_unit: GetDefaultTimeUnitMethod
    """Constructor-initialized instance of
    :class:`GetDefaultTimeUnitMethod`.
    """

    get_reward_token_balance: GetRewardTokenBalanceMethod
    """Constructor-initialized instance of
    :class:`GetRewardTokenBalanceMethod`.
    """

    get_rewards_per_unit_time: GetRewardsPerUnitTimeMethod
    """Constructor-initialized instance of
    :class:`GetRewardsPerUnitTimeMethod`.
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

    get_stake_info: GetStakeInfoMethod
    """Constructor-initialized instance of
    :class:`GetStakeInfoMethod`.
    """

    get_stake_info_for_token: GetStakeInfoForTokenMethod
    """Constructor-initialized instance of
    :class:`GetStakeInfoForTokenMethod`.
    """

    get_time_unit: GetTimeUnitMethod
    """Constructor-initialized instance of
    :class:`GetTimeUnitMethod`.
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

    indexed_tokens: IndexedTokensMethod
    """Constructor-initialized instance of
    :class:`IndexedTokensMethod`.
    """

    initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
    """

    is_indexed: IsIndexedMethod
    """Constructor-initialized instance of
    :class:`IsIndexedMethod`.
    """

    is_trusted_forwarder: IsTrustedForwarderMethod
    """Constructor-initialized instance of
    :class:`IsTrustedForwarderMethod`.
    """

    multicall: MulticallMethod
    """Constructor-initialized instance of
    :class:`MulticallMethod`.
    """

    on_erc1155_batch_received: OnErc1155BatchReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc1155BatchReceivedMethod`.
    """

    on_erc1155_received: OnErc1155ReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc1155ReceivedMethod`.
    """

    renounce_role: RenounceRoleMethod
    """Constructor-initialized instance of
    :class:`RenounceRoleMethod`.
    """

    revoke_role: RevokeRoleMethod
    """Constructor-initialized instance of
    :class:`RevokeRoleMethod`.
    """

    reward_token: RewardTokenMethod
    """Constructor-initialized instance of
    :class:`RewardTokenMethod`.
    """

    set_contract_uri: SetContractUriMethod
    """Constructor-initialized instance of
    :class:`SetContractUriMethod`.
    """

    set_default_rewards_per_unit_time: SetDefaultRewardsPerUnitTimeMethod
    """Constructor-initialized instance of
    :class:`SetDefaultRewardsPerUnitTimeMethod`.
    """

    set_default_time_unit: SetDefaultTimeUnitMethod
    """Constructor-initialized instance of
    :class:`SetDefaultTimeUnitMethod`.
    """

    set_rewards_per_unit_time: SetRewardsPerUnitTimeMethod
    """Constructor-initialized instance of
    :class:`SetRewardsPerUnitTimeMethod`.
    """

    set_time_unit: SetTimeUnitMethod
    """Constructor-initialized instance of
    :class:`SetTimeUnitMethod`.
    """

    stake: StakeMethod
    """Constructor-initialized instance of
    :class:`StakeMethod`.
    """

    stakers: StakersMethod
    """Constructor-initialized instance of
    :class:`StakersMethod`.
    """

    stakers_array: StakersArrayMethod
    """Constructor-initialized instance of
    :class:`StakersArrayMethod`.
    """

    staking_token: StakingTokenMethod
    """Constructor-initialized instance of
    :class:`StakingTokenMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    withdraw: WithdrawMethod
    """Constructor-initialized instance of
    :class:`WithdrawMethod`.
    """

    withdraw_reward_tokens: WithdrawRewardTokensMethod
    """Constructor-initialized instance of
    :class:`WithdrawRewardTokensMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: EditionStakeValidator = None,
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
            validator = EditionStakeValidator(
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
            abi=EditionStake.abi(),
        ).functions

        self.default_admin_role = DefaultAdminRoleMethod(
            web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE
        )

        self.claim_rewards = ClaimRewardsMethod(
            web3_or_provider,
            contract_address,
            functions.claimRewards,
            validator,
        )

        self.contract_type = ContractTypeMethod(
            web3_or_provider, contract_address, functions.contractType
        )

        self.contract_uri = ContractUriMethod(
            web3_or_provider, contract_address, functions.contractURI
        )

        self.contract_version = ContractVersionMethod(
            web3_or_provider, contract_address, functions.contractVersion
        )

        self.deposit_reward_tokens = DepositRewardTokensMethod(
            web3_or_provider,
            contract_address,
            functions.depositRewardTokens,
            validator,
        )

        self.get_default_rewards_per_unit_time = (
            GetDefaultRewardsPerUnitTimeMethod(
                web3_or_provider,
                contract_address,
                functions.getDefaultRewardsPerUnitTime,
            )
        )

        self.get_default_time_unit = GetDefaultTimeUnitMethod(
            web3_or_provider, contract_address, functions.getDefaultTimeUnit
        )

        self.get_reward_token_balance = GetRewardTokenBalanceMethod(
            web3_or_provider, contract_address, functions.getRewardTokenBalance
        )

        self.get_rewards_per_unit_time = GetRewardsPerUnitTimeMethod(
            web3_or_provider,
            contract_address,
            functions.getRewardsPerUnitTime,
            validator,
        )

        self.get_role_admin = GetRoleAdminMethod(
            web3_or_provider,
            contract_address,
            functions.getRoleAdmin,
            validator,
        )

        self.get_role_member = GetRoleMemberMethod(
            web3_or_provider,
            contract_address,
            functions.getRoleMember,
            validator,
        )

        self.get_role_member_count = GetRoleMemberCountMethod(
            web3_or_provider,
            contract_address,
            functions.getRoleMemberCount,
            validator,
        )

        self.get_stake_info = GetStakeInfoMethod(
            web3_or_provider,
            contract_address,
            functions.getStakeInfo,
            validator,
        )

        self.get_stake_info_for_token = GetStakeInfoForTokenMethod(
            web3_or_provider,
            contract_address,
            functions.getStakeInfoForToken,
            validator,
        )

        self.get_time_unit = GetTimeUnitMethod(
            web3_or_provider,
            contract_address,
            functions.getTimeUnit,
            validator,
        )

        self.grant_role = GrantRoleMethod(
            web3_or_provider, contract_address, functions.grantRole, validator
        )

        self.has_role = HasRoleMethod(
            web3_or_provider, contract_address, functions.hasRole, validator
        )

        self.has_role_with_switch = HasRoleWithSwitchMethod(
            web3_or_provider,
            contract_address,
            functions.hasRoleWithSwitch,
            validator,
        )

        self.indexed_tokens = IndexedTokensMethod(
            web3_or_provider,
            contract_address,
            functions.indexedTokens,
            validator,
        )

        self.initialize = InitializeMethod(
            web3_or_provider, contract_address, functions.initialize, validator
        )

        self.is_indexed = IsIndexedMethod(
            web3_or_provider, contract_address, functions.isIndexed, validator
        )

        self.is_trusted_forwarder = IsTrustedForwarderMethod(
            web3_or_provider,
            contract_address,
            functions.isTrustedForwarder,
            validator,
        )

        self.multicall = MulticallMethod(
            web3_or_provider, contract_address, functions.multicall, validator
        )

        self.on_erc1155_batch_received = OnErc1155BatchReceivedMethod(
            web3_or_provider,
            contract_address,
            functions.onERC1155BatchReceived,
            validator,
        )

        self.on_erc1155_received = OnErc1155ReceivedMethod(
            web3_or_provider,
            contract_address,
            functions.onERC1155Received,
            validator,
        )

        self.renounce_role = RenounceRoleMethod(
            web3_or_provider,
            contract_address,
            functions.renounceRole,
            validator,
        )

        self.revoke_role = RevokeRoleMethod(
            web3_or_provider, contract_address, functions.revokeRole, validator
        )

        self.reward_token = RewardTokenMethod(
            web3_or_provider, contract_address, functions.rewardToken
        )

        self.set_contract_uri = SetContractUriMethod(
            web3_or_provider,
            contract_address,
            functions.setContractURI,
            validator,
        )

        self.set_default_rewards_per_unit_time = (
            SetDefaultRewardsPerUnitTimeMethod(
                web3_or_provider,
                contract_address,
                functions.setDefaultRewardsPerUnitTime,
                validator,
            )
        )

        self.set_default_time_unit = SetDefaultTimeUnitMethod(
            web3_or_provider,
            contract_address,
            functions.setDefaultTimeUnit,
            validator,
        )

        self.set_rewards_per_unit_time = SetRewardsPerUnitTimeMethod(
            web3_or_provider,
            contract_address,
            functions.setRewardsPerUnitTime,
            validator,
        )

        self.set_time_unit = SetTimeUnitMethod(
            web3_or_provider,
            contract_address,
            functions.setTimeUnit,
            validator,
        )

        self.stake = StakeMethod(
            web3_or_provider, contract_address, functions.stake, validator
        )

        self.stakers = StakersMethod(
            web3_or_provider, contract_address, functions.stakers, validator
        )

        self.stakers_array = StakersArrayMethod(
            web3_or_provider,
            contract_address,
            functions.stakersArray,
            validator,
        )

        self.staking_token = StakingTokenMethod(
            web3_or_provider, contract_address, functions.stakingToken
        )

        self.supports_interface = SupportsInterfaceMethod(
            web3_or_provider,
            contract_address,
            functions.supportsInterface,
            validator,
        )

        self.withdraw = WithdrawMethod(
            web3_or_provider, contract_address, functions.withdraw, validator
        )

        self.withdraw_reward_tokens = WithdrawRewardTokensMethod(
            web3_or_provider,
            contract_address,
            functions.withdrawRewardTokens,
            validator,
        )

    def get_contract_uri_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ContractURIUpdated event.

        :param tx_hash: hash of transaction emitting ContractURIUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.ContractURIUpdated()
            .processReceipt(tx_receipt)
        )

    def get_initialized_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Initialized event.

        :param tx_hash: hash of transaction emitting Initialized event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.Initialized()
            .processReceipt(tx_receipt)
        )

    def get_reward_tokens_deposited_by_admin_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RewardTokensDepositedByAdmin event.

        :param tx_hash: hash of transaction emitting
            RewardTokensDepositedByAdmin event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.RewardTokensDepositedByAdmin()
            .processReceipt(tx_receipt)
        )

    def get_reward_tokens_withdrawn_by_admin_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RewardTokensWithdrawnByAdmin event.

        :param tx_hash: hash of transaction emitting
            RewardTokensWithdrawnByAdmin event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.RewardTokensWithdrawnByAdmin()
            .processReceipt(tx_receipt)
        )

    def get_rewards_claimed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RewardsClaimed event.

        :param tx_hash: hash of transaction emitting RewardsClaimed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.RewardsClaimed()
            .processReceipt(tx_receipt)
        )

    def get_role_admin_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleAdminChanged event.

        :param tx_hash: hash of transaction emitting RoleAdminChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.RoleAdminChanged()
            .processReceipt(tx_receipt)
        )

    def get_role_granted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleGranted event.

        :param tx_hash: hash of transaction emitting RoleGranted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.RoleGranted()
            .processReceipt(tx_receipt)
        )

    def get_role_revoked_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleRevoked event.

        :param tx_hash: hash of transaction emitting RoleRevoked event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.RoleRevoked()
            .processReceipt(tx_receipt)
        )

    def get_tokens_staked_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensStaked event.

        :param tx_hash: hash of transaction emitting TokensStaked event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.TokensStaked()
            .processReceipt(tx_receipt)
        )

    def get_tokens_withdrawn_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensWithdrawn event.

        :param tx_hash: hash of transaction emitting TokensWithdrawn event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.TokensWithdrawn()
            .processReceipt(tx_receipt)
        )

    def get_updated_default_rewards_per_unit_time_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for UpdatedDefaultRewardsPerUnitTime event.

        :param tx_hash: hash of transaction emitting
            UpdatedDefaultRewardsPerUnitTime event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.UpdatedDefaultRewardsPerUnitTime()
            .processReceipt(tx_receipt)
        )

    def get_updated_default_time_unit_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for UpdatedDefaultTimeUnit event.

        :param tx_hash: hash of transaction emitting UpdatedDefaultTimeUnit
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.UpdatedDefaultTimeUnit()
            .processReceipt(tx_receipt)
        )

    def get_updated_rewards_per_unit_time_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for UpdatedRewardsPerUnitTime event.

        :param tx_hash: hash of transaction emitting UpdatedRewardsPerUnitTime
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.UpdatedRewardsPerUnitTime()
            .processReceipt(tx_receipt)
        )

    def get_updated_time_unit_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for UpdatedTimeUnit event.

        :param tx_hash: hash of transaction emitting UpdatedTimeUnit event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EditionStake.abi(),
            )
            .events.UpdatedTimeUnit()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_nativeTokenWrapper","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"prevURI","type":"string"},{"indexed":false,"internalType":"string","name":"newURI","type":"string"}],"name":"ContractURIUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"RewardTokensDepositedByAdmin","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"RewardTokensWithdrawnByAdmin","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":false,"internalType":"uint256","name":"rewardAmount","type":"uint256"}],"name":"RewardsClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokensStaked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokensWithdrawn","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldRewardsPerUnitTime","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newRewardsPerUnitTime","type":"uint256"}],"name":"UpdatedDefaultRewardsPerUnitTime","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldTimeUnit","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newTimeUnit","type":"uint256"}],"name":"UpdatedDefaultTimeUnit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"_tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"oldRewardsPerUnitTime","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newRewardsPerUnitTime","type":"uint256"}],"name":"UpdatedRewardsPerUnitTime","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"_tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"oldTimeUnit","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newTimeUnit","type":"uint256"}],"name":"UpdatedTimeUnit","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"claimRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"contractType","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractVersion","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"depositRewardTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getDefaultRewardsPerUnitTime","outputs":[{"internalType":"uint256","name":"_rewardsPerUnitTime","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getDefaultTimeUnit","outputs":[{"internalType":"uint256","name":"_timeUnit","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getRewardTokenBalance","outputs":[{"internalType":"uint256","name":"_rewardsAvailableInContract","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getRewardsPerUnitTime","outputs":[{"internalType":"uint256","name":"_rewardsPerUnitTime","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"member","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"count","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_staker","type":"address"}],"name":"getStakeInfo","outputs":[{"internalType":"uint256[]","name":"_tokensStaked","type":"uint256[]"},{"internalType":"uint256[]","name":"_tokenAmounts","type":"uint256[]"},{"internalType":"uint256","name":"_totalRewards","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"address","name":"_staker","type":"address"}],"name":"getStakeInfoForToken","outputs":[{"internalType":"uint256","name":"_tokensStaked","type":"uint256"},{"internalType":"uint256","name":"_rewards","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getTimeUnit","outputs":[{"internalType":"uint256","name":"_timeUnit","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRoleWithSwitch","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"indexedTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_defaultAdmin","type":"address"},{"internalType":"string","name":"_contractURI","type":"string"},{"internalType":"address[]","name":"_trustedForwarders","type":"address[]"},{"internalType":"address","name":"_rewardToken","type":"address"},{"internalType":"address","name":"_stakingToken","type":"address"},{"internalType":"uint256","name":"_defaultTimeUnit","type":"uint256"},{"internalType":"uint256","name":"_defaultRewardsPerUnitTime","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"isIndexed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"onERC1155BatchReceived","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"uint256","name":"index_3","type":"uint256"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rewardToken","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_uri","type":"string"}],"name":"setContractURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_defaultRewardsPerUnitTime","type":"uint256"}],"name":"setDefaultRewardsPerUnitTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_defaultTimeUnit","type":"uint256"}],"name":"setDefaultTimeUnit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_rewardsPerUnitTime","type":"uint256"}],"name":"setRewardsPerUnitTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_timeUnit","type":"uint256"}],"name":"setTimeUnit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"stake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"},{"internalType":"address","name":"index_1","type":"address"}],"name":"stakers","outputs":[{"internalType":"uint256","name":"amountStaked","type":"uint256"},{"internalType":"uint256","name":"timeOfLastUpdate","type":"uint256"},{"internalType":"uint256","name":"unclaimedRewards","type":"uint256"},{"internalType":"uint256","name":"conditionIdOflastUpdate","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"},{"internalType":"uint256","name":"index_1","type":"uint256"}],"name":"stakersArray","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stakingToken","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawRewardTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
