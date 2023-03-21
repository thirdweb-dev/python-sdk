"""Generated wrapper for IVotes Solidity contract."""

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
# constructor for IVotes below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IVotesValidator,
    )
except ImportError:

    class IVotesValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class DelegateMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the delegate method."""

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

    def validate_and_normalize_inputs(self, delegatee: str):
        """Validate the inputs to the delegate method."""
        self.validator.assert_valid(
            method_name="delegate",
            parameter_name="delegatee",
            argument_value=delegatee,
        )
        delegatee = self.validate_and_checksum_address(delegatee)
        return delegatee

    def call(
        self, delegatee: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (delegatee) = self.validate_and_normalize_inputs(delegatee)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(delegatee).call(tx_params.as_dict())

    def send_transaction(
        self, delegatee: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (delegatee) = self.validate_and_normalize_inputs(delegatee)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(delegatee).transact(tx_params.as_dict())

    def build_transaction(
        self, delegatee: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (delegatee) = self.validate_and_normalize_inputs(delegatee)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(delegatee).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, delegatee: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (delegatee) = self.validate_and_normalize_inputs(delegatee)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(delegatee).estimateGas(
            tx_params.as_dict()
        )


class DelegateBySigMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the delegateBySig method."""

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
        delegatee: str,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
    ):
        """Validate the inputs to the delegateBySig method."""
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="delegatee",
            argument_value=delegatee,
        )
        delegatee = self.validate_and_checksum_address(delegatee)
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="nonce",
            argument_value=nonce,
        )
        # safeguard against fractional inputs
        nonce = int(nonce)
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="expiry",
            argument_value=expiry,
        )
        # safeguard against fractional inputs
        expiry = int(expiry)
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="v",
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="r",
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name="delegateBySig",
            parameter_name="s",
            argument_value=s,
        )
        return (delegatee, nonce, expiry, v, r, s)

    def call(
        self,
        delegatee: str,
        nonce: int,
        expiry: int,
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
            delegatee,
            nonce,
            expiry,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            delegatee, nonce, expiry, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(delegatee, nonce, expiry, v, r, s).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        delegatee: str,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            delegatee,
            nonce,
            expiry,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            delegatee, nonce, expiry, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            delegatee, nonce, expiry, v, r, s
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        delegatee: str,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            delegatee,
            nonce,
            expiry,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            delegatee, nonce, expiry, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            delegatee, nonce, expiry, v, r, s
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        delegatee: str,
        nonce: int,
        expiry: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            delegatee,
            nonce,
            expiry,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            delegatee, nonce, expiry, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            delegatee, nonce, expiry, v, r, s
        ).estimateGas(tx_params.as_dict())


class DelegatesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the delegates method."""

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

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the delegates method."""
        self.validator.assert_valid(
            method_name="delegates",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return account

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(
            tx_params.as_dict()
        )


class GetPastTotalSupplyMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getPastTotalSupply method."""

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

    def validate_and_normalize_inputs(self, block_number: int):
        """Validate the inputs to the getPastTotalSupply method."""
        self.validator.assert_valid(
            method_name="getPastTotalSupply",
            parameter_name="blockNumber",
            argument_value=block_number,
        )
        # safeguard against fractional inputs
        block_number = int(block_number)
        return block_number

    def call(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(block_number).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).estimateGas(
            tx_params.as_dict()
        )


class GetPastVotesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getPastVotes method."""

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

    def validate_and_normalize_inputs(self, account: str, block_number: int):
        """Validate the inputs to the getPastVotes method."""
        self.validator.assert_valid(
            method_name="getPastVotes",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="getPastVotes",
            parameter_name="blockNumber",
            argument_value=block_number,
        )
        # safeguard against fractional inputs
        block_number = int(block_number)
        return (account, block_number)

    def call(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, block_number).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, block_number).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, block_number).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, block_number).estimateGas(
            tx_params.as_dict()
        )


class GetVotesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getVotes method."""

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

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the getVotes method."""
        self.validator.assert_valid(
            method_name="getVotes",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return account

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IVotes:
    """Wrapper class for IVotes Solidity contract."""

    delegate: DelegateMethod
    """Constructor-initialized instance of
    :class:`DelegateMethod`.
    """

    delegate_by_sig: DelegateBySigMethod
    """Constructor-initialized instance of
    :class:`DelegateBySigMethod`.
    """

    delegates: DelegatesMethod
    """Constructor-initialized instance of
    :class:`DelegatesMethod`.
    """

    get_past_total_supply: GetPastTotalSupplyMethod
    """Constructor-initialized instance of
    :class:`GetPastTotalSupplyMethod`.
    """

    get_past_votes: GetPastVotesMethod
    """Constructor-initialized instance of
    :class:`GetPastVotesMethod`.
    """

    get_votes: GetVotesMethod
    """Constructor-initialized instance of
    :class:`GetVotesMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IVotesValidator = None,
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
            validator = IVotesValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=IVotes.abi()
        ).functions

        self.delegate = DelegateMethod(
            web3_or_provider, contract_address, functions.delegate, validator
        )

        self.delegate_by_sig = DelegateBySigMethod(
            web3_or_provider,
            contract_address,
            functions.delegateBySig,
            validator,
        )

        self.delegates = DelegatesMethod(
            web3_or_provider, contract_address, functions.delegates, validator
        )

        self.get_past_total_supply = GetPastTotalSupplyMethod(
            web3_or_provider,
            contract_address,
            functions.getPastTotalSupply,
            validator,
        )

        self.get_past_votes = GetPastVotesMethod(
            web3_or_provider,
            contract_address,
            functions.getPastVotes,
            validator,
        )

        self.get_votes = GetVotesMethod(
            web3_or_provider, contract_address, functions.getVotes, validator
        )

    def get_delegate_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for DelegateChanged event.

        :param tx_hash: hash of transaction emitting DelegateChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IVotes.abi(),
            )
            .events.DelegateChanged()
            .processReceipt(tx_receipt)
        )

    def get_delegate_votes_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for DelegateVotesChanged event.

        :param tx_hash: hash of transaction emitting DelegateVotesChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IVotes.abi(),
            )
            .events.DelegateVotesChanged()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"delegator","type":"address"},{"indexed":true,"internalType":"address","name":"fromDelegate","type":"address"},{"indexed":true,"internalType":"address","name":"toDelegate","type":"address"}],"name":"DelegateChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"delegate","type":"address"},{"indexed":false,"internalType":"uint256","name":"previousBalance","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newBalance","type":"uint256"}],"name":"DelegateVotesChanged","type":"event"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"}],"name":"delegate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"delegateBySig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"delegates","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPastTotalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPastVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
