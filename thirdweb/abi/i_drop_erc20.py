"""Generated wrapper for IDropERC20 Solidity contract."""

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
# constructor for IDropERC20 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IDropERC20Validator,
    )
except ImportError:

    class IDropERC20Validator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IDropClaimConditionClaimCondition(TypedDict):
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

    startTimestamp: int

    maxClaimableSupply: int

    supplyClaimed: int

    quantityLimitPerWallet: int

    waitTimeInSecondsBetweenClaims: int

    merkleRoot: Union[bytes, str]

    pricePerToken: int

    currency: str


class IDropERC20AllowlistProof(TypedDict):
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

    proof: List[Union[bytes, str]]

    maxQuantityInAllowlist: int


class AllowanceMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the allowance method."""

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

    def validate_and_normalize_inputs(self, owner: str, spender: str):
        """Validate the inputs to the allowance method."""
        self.validator.assert_valid(
            method_name="allowance",
            parameter_name="owner",
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name="allowance",
            parameter_name="spender",
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        return (owner, spender)

    def call(
        self, owner: str, spender: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner, spender).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, owner: str, spender: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, owner: str, spender: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, owner: str, spender: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).estimateGas(
            tx_params.as_dict()
        )


class ApproveMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the approve method."""

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

    def validate_and_normalize_inputs(self, spender: str, amount: int):
        """Validate the inputs to the approve method."""
        self.validator.assert_valid(
            method_name="approve",
            parameter_name="spender",
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name="approve",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (spender, amount)

    def call(
        self, spender: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(spender, amount).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self, spender: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, spender: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, spender: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).estimateGas(
            tx_params.as_dict()
        )


class BalanceOfMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the balanceOf method."""

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
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name="balanceOf",
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


class ClaimMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the claim method."""

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
        receiver: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDropERC20AllowlistProof,
        data: Union[bytes, str],
    ):
        """Validate the inputs to the claim method."""
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="receiver",
            argument_value=receiver,
        )
        receiver = self.validate_and_checksum_address(receiver)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="pricePerToken",
            argument_value=price_per_token,
        )
        # safeguard against fractional inputs
        price_per_token = int(price_per_token)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="allowlistProof",
            argument_value=allowlist_proof,
        )
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="data",
            argument_value=data,
        )
        return (
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        )

    def call(
        self,
        receiver: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDropERC20AllowlistProof,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ) = self.validate_and_normalize_inputs(
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        receiver: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDropERC20AllowlistProof,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ) = self.validate_and_normalize_inputs(
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        receiver: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDropERC20AllowlistProof,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ) = self.validate_and_normalize_inputs(
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        receiver: str,
        quantity: int,
        currency: str,
        price_per_token: int,
        allowlist_proof: IDropERC20AllowlistProof,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ) = self.validate_and_normalize_inputs(
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            quantity,
            currency,
            price_per_token,
            allowlist_proof,
            data,
        ).estimateGas(tx_params.as_dict())


class SetClaimConditionsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setClaimConditions method."""

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
        phases: List[IDropClaimConditionClaimCondition],
        reset_claim_eligibility: bool,
    ):
        """Validate the inputs to the setClaimConditions method."""
        self.validator.assert_valid(
            method_name="setClaimConditions",
            parameter_name="phases",
            argument_value=phases,
        )
        self.validator.assert_valid(
            method_name="setClaimConditions",
            parameter_name="resetClaimEligibility",
            argument_value=reset_claim_eligibility,
        )
        return (phases, reset_claim_eligibility)

    def call(
        self,
        phases: List[IDropClaimConditionClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(
            phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(phases, reset_claim_eligibility).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        phases: List[IDropClaimConditionClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(
            phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            phases, reset_claim_eligibility
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        phases: List[IDropClaimConditionClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(
            phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            phases, reset_claim_eligibility
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        phases: List[IDropClaimConditionClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(
            phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            phases, reset_claim_eligibility
        ).estimateGas(tx_params.as_dict())


class TotalSupplyMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the totalSupply method."""

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


class TransferMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the transfer method."""

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

    def validate_and_normalize_inputs(self, to: str, amount: int):
        """Validate the inputs to the transfer method."""
        self.validator.assert_valid(
            method_name="transfer",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="transfer",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (to, amount)

    def call(
        self, to: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(to, amount).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self, to: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, to: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, to: str, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).estimateGas(
            tx_params.as_dict()
        )


class TransferFromMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the transferFrom method."""

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

    def validate_and_normalize_inputs(self, _from: str, to: str, amount: int):
        """Validate the inputs to the transferFrom method."""
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="transferFrom",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (_from, to, amount)

    def call(
        self,
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_from, to, amount).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        _from: str,
        to: str,
        amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, amount) = self.validate_and_normalize_inputs(
            _from, to, amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IDropERC20:
    """Wrapper class for IDropERC20 Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    allowance: AllowanceMethod
    """Constructor-initialized instance of
    :class:`AllowanceMethod`.
    """

    approve: ApproveMethod
    """Constructor-initialized instance of
    :class:`ApproveMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    claim: ClaimMethod
    """Constructor-initialized instance of
    :class:`ClaimMethod`.
    """

    set_claim_conditions: SetClaimConditionsMethod
    """Constructor-initialized instance of
    :class:`SetClaimConditionsMethod`.
    """

    total_supply: TotalSupplyMethod
    """Constructor-initialized instance of
    :class:`TotalSupplyMethod`.
    """

    transfer: TransferMethod
    """Constructor-initialized instance of
    :class:`TransferMethod`.
    """

    transfer_from: TransferFromMethod
    """Constructor-initialized instance of
    :class:`TransferFromMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IDropERC20Validator = None,
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
            validator = IDropERC20Validator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=IDropERC20.abi()
        ).functions

        self.allowance = AllowanceMethod(
            web3_or_provider, contract_address, functions.allowance, validator
        )

        self.approve = ApproveMethod(
            web3_or_provider, contract_address, functions.approve, validator
        )

        self.balance_of = BalanceOfMethod(
            web3_or_provider, contract_address, functions.balanceOf, validator
        )

        self.claim = ClaimMethod(
            web3_or_provider, contract_address, functions.claim, validator
        )

        self.set_claim_conditions = SetClaimConditionsMethod(
            web3_or_provider,
            contract_address,
            functions.setClaimConditions,
            validator,
        )

        self.total_supply = TotalSupplyMethod(
            web3_or_provider, contract_address, functions.totalSupply
        )

        self.transfer = TransferMethod(
            web3_or_provider, contract_address, functions.transfer, validator
        )

        self.transfer_from = TransferFromMethod(
            web3_or_provider,
            contract_address,
            functions.transferFrom,
            validator,
        )

    def get_approval_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Approval event.

        :param tx_hash: hash of transaction emitting Approval event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC20.abi(),
            )
            .events.Approval()
            .processReceipt(tx_receipt)
        )

    def get_claim_conditions_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ClaimConditionsUpdated event.

        :param tx_hash: hash of transaction emitting ClaimConditionsUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC20.abi(),
            )
            .events.ClaimConditionsUpdated()
            .processReceipt(tx_receipt)
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
                abi=IDropERC20.abi(),
            )
            .events.ContractURIUpdated()
            .processReceipt(tx_receipt)
        )

    def get_max_total_supply_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for MaxTotalSupplyUpdated event.

        :param tx_hash: hash of transaction emitting MaxTotalSupplyUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC20.abi(),
            )
            .events.MaxTotalSupplyUpdated()
            .processReceipt(tx_receipt)
        )

    def get_tokens_claimed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensClaimed event.

        :param tx_hash: hash of transaction emitting TokensClaimed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC20.abi(),
            )
            .events.TokensClaimed()
            .processReceipt(tx_receipt)
        )

    def get_transfer_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Transfer event.

        :param tx_hash: hash of transaction emitting Transfer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC20.abi(),
            )
            .events.Transfer()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerWallet","type":"uint256"},{"internalType":"uint256","name":"waitTimeInSecondsBetweenClaims","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"indexed":false,"internalType":"struct IDropClaimCondition.ClaimCondition[]","name":"claimConditions","type":"tuple[]"}],"name":"ClaimConditionsUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"prevURI","type":"string"},{"indexed":false,"internalType":"string","name":"newURI","type":"string"}],"name":"ContractURIUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"maxTotalSupply","type":"uint256"}],"name":"MaxTotalSupplyUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"claimConditionIndex","type":"uint256"},{"indexed":true,"internalType":"address","name":"claimer","type":"address"},{"indexed":true,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantityClaimed","type":"uint256"}],"name":"TokensClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"components":[{"internalType":"bytes32[]","name":"proof","type":"bytes32[]"},{"internalType":"uint256","name":"maxQuantityInAllowlist","type":"uint256"}],"internalType":"struct IDropERC20.AllowlistProof","name":"allowlistProof","type":"tuple"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"claim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerWallet","type":"uint256"},{"internalType":"uint256","name":"waitTimeInSecondsBetweenClaims","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"internalType":"struct IDropClaimCondition.ClaimCondition[]","name":"phases","type":"tuple[]"},{"internalType":"bool","name":"resetClaimEligibility","type":"bool"}],"name":"setClaimConditions","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
