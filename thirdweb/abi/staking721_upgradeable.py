"""Generated wrapper for Staking721Upgradeable Solidity contract."""

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
# constructor for Staking721Upgradeable below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        Staking721UpgradeableValidator,
    )
except ImportError:

    class Staking721UpgradeableValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class ClaimRewardsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the claimRewards method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

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
    ) -> Tuple[List[int], int]:
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


class GetTimeUnitMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getTimeUnit method."""

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

    def validate_and_normalize_inputs(self, rewards_per_unit_time: int):
        """Validate the inputs to the setRewardsPerUnitTime method."""
        self.validator.assert_valid(
            method_name="setRewardsPerUnitTime",
            parameter_name="_rewardsPerUnitTime",
            argument_value=rewards_per_unit_time,
        )
        # safeguard against fractional inputs
        rewards_per_unit_time = int(rewards_per_unit_time)
        return rewards_per_unit_time

    def call(
        self, rewards_per_unit_time: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (rewards_per_unit_time) = self.validate_and_normalize_inputs(
            rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(rewards_per_unit_time).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self, rewards_per_unit_time: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (rewards_per_unit_time) = self.validate_and_normalize_inputs(
            rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(rewards_per_unit_time).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, rewards_per_unit_time: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (rewards_per_unit_time) = self.validate_and_normalize_inputs(
            rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(rewards_per_unit_time).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, rewards_per_unit_time: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (rewards_per_unit_time) = self.validate_and_normalize_inputs(
            rewards_per_unit_time
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(rewards_per_unit_time).estimateGas(
            tx_params.as_dict()
        )


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

    def validate_and_normalize_inputs(self, time_unit: int):
        """Validate the inputs to the setTimeUnit method."""
        self.validator.assert_valid(
            method_name="setTimeUnit",
            parameter_name="_timeUnit",
            argument_value=time_unit,
        )
        # safeguard against fractional inputs
        time_unit = int(time_unit)
        return time_unit

    def call(
        self, time_unit: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (time_unit) = self.validate_and_normalize_inputs(time_unit)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(time_unit).call(tx_params.as_dict())

    def send_transaction(
        self, time_unit: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (time_unit) = self.validate_and_normalize_inputs(time_unit)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time_unit).transact(tx_params.as_dict())

    def build_transaction(
        self, time_unit: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (time_unit) = self.validate_and_normalize_inputs(time_unit)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time_unit).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, time_unit: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (time_unit) = self.validate_and_normalize_inputs(time_unit)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time_unit).estimateGas(
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

    def validate_and_normalize_inputs(self, token_ids: List[int]):
        """Validate the inputs to the stake method."""
        self.validator.assert_valid(
            method_name="stake",
            parameter_name="_tokenIds",
            argument_value=token_ids,
        )
        return token_ids

    def call(
        self, token_ids: List[int], tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_ids) = self.validate_and_normalize_inputs(token_ids)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_ids).call(tx_params.as_dict())

    def send_transaction(
        self, token_ids: List[int], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_ids) = self.validate_and_normalize_inputs(token_ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_ids).transact(tx_params.as_dict())

    def build_transaction(
        self, token_ids: List[int], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_ids) = self.validate_and_normalize_inputs(token_ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_ids).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token_ids: List[int], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_ids) = self.validate_and_normalize_inputs(token_ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_ids).estimateGas(
            tx_params.as_dict()
        )


class StakerAddressMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the stakerAddress method."""

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
        """Validate the inputs to the stakerAddress method."""
        self.validator.assert_valid(
            method_name="stakerAddress",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return str(returned)

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

    def validate_and_normalize_inputs(self, index_0: str):
        """Validate the inputs to the stakers method."""
        self.validator.assert_valid(
            method_name="stakers",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return index_0

    def call(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> Tuple[int, int, int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
        )

    def send_transaction(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the stakersArray method."""
        self.validator.assert_valid(
            method_name="stakersArray",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return str(returned)

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

    def validate_and_normalize_inputs(self, token_ids: List[int]):
        """Validate the inputs to the withdraw method."""
        self.validator.assert_valid(
            method_name="withdraw",
            parameter_name="_tokenIds",
            argument_value=token_ids,
        )
        return token_ids

    def call(
        self, token_ids: List[int], tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_ids) = self.validate_and_normalize_inputs(token_ids)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_ids).call(tx_params.as_dict())

    def send_transaction(
        self, token_ids: List[int], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_ids) = self.validate_and_normalize_inputs(token_ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_ids).transact(tx_params.as_dict())

    def build_transaction(
        self, token_ids: List[int], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_ids) = self.validate_and_normalize_inputs(token_ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_ids).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token_ids: List[int], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_ids) = self.validate_and_normalize_inputs(token_ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_ids).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Staking721Upgradeable:
    """Wrapper class for Staking721Upgradeable Solidity contract."""

    claim_rewards: ClaimRewardsMethod
    """Constructor-initialized instance of
    :class:`ClaimRewardsMethod`.
    """

    get_reward_token_balance: GetRewardTokenBalanceMethod
    """Constructor-initialized instance of
    :class:`GetRewardTokenBalanceMethod`.
    """

    get_rewards_per_unit_time: GetRewardsPerUnitTimeMethod
    """Constructor-initialized instance of
    :class:`GetRewardsPerUnitTimeMethod`.
    """

    get_stake_info: GetStakeInfoMethod
    """Constructor-initialized instance of
    :class:`GetStakeInfoMethod`.
    """

    get_time_unit: GetTimeUnitMethod
    """Constructor-initialized instance of
    :class:`GetTimeUnitMethod`.
    """

    indexed_tokens: IndexedTokensMethod
    """Constructor-initialized instance of
    :class:`IndexedTokensMethod`.
    """

    is_indexed: IsIndexedMethod
    """Constructor-initialized instance of
    :class:`IsIndexedMethod`.
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

    staker_address: StakerAddressMethod
    """Constructor-initialized instance of
    :class:`StakerAddressMethod`.
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

    withdraw: WithdrawMethod
    """Constructor-initialized instance of
    :class:`WithdrawMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: Staking721UpgradeableValidator = None,
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
            validator = Staking721UpgradeableValidator(
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
            abi=Staking721Upgradeable.abi(),
        ).functions

        self.claim_rewards = ClaimRewardsMethod(
            web3_or_provider, contract_address, functions.claimRewards
        )

        self.get_reward_token_balance = GetRewardTokenBalanceMethod(
            web3_or_provider, contract_address, functions.getRewardTokenBalance
        )

        self.get_rewards_per_unit_time = GetRewardsPerUnitTimeMethod(
            web3_or_provider, contract_address, functions.getRewardsPerUnitTime
        )

        self.get_stake_info = GetStakeInfoMethod(
            web3_or_provider,
            contract_address,
            functions.getStakeInfo,
            validator,
        )

        self.get_time_unit = GetTimeUnitMethod(
            web3_or_provider, contract_address, functions.getTimeUnit
        )

        self.indexed_tokens = IndexedTokensMethod(
            web3_or_provider,
            contract_address,
            functions.indexedTokens,
            validator,
        )

        self.is_indexed = IsIndexedMethod(
            web3_or_provider, contract_address, functions.isIndexed, validator
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

        self.staker_address = StakerAddressMethod(
            web3_or_provider,
            contract_address,
            functions.stakerAddress,
            validator,
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

        self.withdraw = WithdrawMethod(
            web3_or_provider, contract_address, functions.withdraw, validator
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
                abi=Staking721Upgradeable.abi(),
            )
            .events.Initialized()
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
                abi=Staking721Upgradeable.abi(),
            )
            .events.RewardsClaimed()
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
                abi=Staking721Upgradeable.abi(),
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
                abi=Staking721Upgradeable.abi(),
            )
            .events.TokensWithdrawn()
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
                abi=Staking721Upgradeable.abi(),
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
                abi=Staking721Upgradeable.abi(),
            )
            .events.UpdatedTimeUnit()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":false,"internalType":"uint256","name":"rewardAmount","type":"uint256"}],"name":"RewardsClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"TokensStaked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"TokensWithdrawn","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldRewardsPerUnitTime","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newRewardsPerUnitTime","type":"uint256"}],"name":"UpdatedRewardsPerUnitTime","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldTimeUnit","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newTimeUnit","type":"uint256"}],"name":"UpdatedTimeUnit","type":"event"},{"inputs":[],"name":"claimRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getRewardTokenBalance","outputs":[{"internalType":"uint256","name":"_rewardsAvailableInContract","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getRewardsPerUnitTime","outputs":[{"internalType":"uint256","name":"_rewardsPerUnitTime","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_staker","type":"address"}],"name":"getStakeInfo","outputs":[{"internalType":"uint256[]","name":"_tokensStaked","type":"uint256[]"},{"internalType":"uint256","name":"_rewards","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTimeUnit","outputs":[{"internalType":"uint256","name":"_timeUnit","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"indexedTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"isIndexed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_rewardsPerUnitTime","type":"uint256"}],"name":"setRewardsPerUnitTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_timeUnit","type":"uint256"}],"name":"setTimeUnit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"stake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"stakerAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"stakers","outputs":[{"internalType":"uint256","name":"amountStaked","type":"uint256"},{"internalType":"uint256","name":"timeOfLastUpdate","type":"uint256"},{"internalType":"uint256","name":"unclaimedRewards","type":"uint256"},{"internalType":"uint256","name":"conditionIdOflastUpdate","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"stakersArray","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stakingToken","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
