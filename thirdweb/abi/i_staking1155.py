"""Generated wrapper for IStaking1155 Solidity contract."""

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
# constructor for IStaking1155 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IStaking1155Validator,
    )
except ImportError:

    class IStaking1155Validator(Validator):  # type: ignore
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
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the claimRewards method."""
        self.validator.assert_valid(
            method_name="claimRewards",
            parameter_name="tokenId",
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
            parameter_name="staker",
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
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="getStakeInfoForToken",
            parameter_name="staker",
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
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="stake",
            parameter_name="amount",
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
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="withdraw",
            parameter_name="amount",
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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IStaking1155:
    """Wrapper class for IStaking1155 Solidity contract."""

    claim_rewards: ClaimRewardsMethod
    """Constructor-initialized instance of
    :class:`ClaimRewardsMethod`.
    """

    get_stake_info: GetStakeInfoMethod
    """Constructor-initialized instance of
    :class:`GetStakeInfoMethod`.
    """

    get_stake_info_for_token: GetStakeInfoForTokenMethod
    """Constructor-initialized instance of
    :class:`GetStakeInfoForTokenMethod`.
    """

    stake: StakeMethod
    """Constructor-initialized instance of
    :class:`StakeMethod`.
    """

    withdraw: WithdrawMethod
    """Constructor-initialized instance of
    :class:`WithdrawMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IStaking1155Validator = None,
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
            validator = IStaking1155Validator(
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
            abi=IStaking1155.abi(),
        ).functions

        self.claim_rewards = ClaimRewardsMethod(
            web3_or_provider,
            contract_address,
            functions.claimRewards,
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

        self.stake = StakeMethod(
            web3_or_provider, contract_address, functions.stake, validator
        )

        self.withdraw = WithdrawMethod(
            web3_or_provider, contract_address, functions.withdraw, validator
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
                abi=IStaking1155.abi(),
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
                abi=IStaking1155.abi(),
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
                abi=IStaking1155.abi(),
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
                abi=IStaking1155.abi(),
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
                abi=IStaking1155.abi(),
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
                abi=IStaking1155.abi(),
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
                abi=IStaking1155.abi(),
            )
            .events.UpdatedTimeUnit()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":false,"internalType":"uint256","name":"rewardAmount","type":"uint256"}],"name":"RewardsClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokensStaked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"staker","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokensWithdrawn","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldRewardsPerUnitTime","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newRewardsPerUnitTime","type":"uint256"}],"name":"UpdatedDefaultRewardsPerUnitTime","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldTimeUnit","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newTimeUnit","type":"uint256"}],"name":"UpdatedDefaultTimeUnit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"_tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"oldRewardsPerUnitTime","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newRewardsPerUnitTime","type":"uint256"}],"name":"UpdatedRewardsPerUnitTime","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"_tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"oldTimeUnit","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newTimeUnit","type":"uint256"}],"name":"UpdatedTimeUnit","type":"event"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"claimRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"staker","type":"address"}],"name":"getStakeInfo","outputs":[{"internalType":"uint256[]","name":"_tokensStaked","type":"uint256[]"},{"internalType":"uint256[]","name":"_tokenAmounts","type":"uint256[]"},{"internalType":"uint256","name":"_totalRewards","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"staker","type":"address"}],"name":"getStakeInfoForToken","outputs":[{"internalType":"uint256","name":"_tokensStaked","type":"uint256"},{"internalType":"uint256","name":"_rewards","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"stake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
