"""Generated wrapper for IDropERC1155_V2 Solidity contract."""

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
# constructor for IDropERC1155_V2 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IDropERC1155_V2Validator,
    )
except ImportError:

    class IDropERC1155_V2Validator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IDropClaimCondition_V2ClaimCondition(TypedDict):
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

    quantityLimitPerTransaction: int

    waitTimeInSecondsBetweenClaims: int

    merkleRoot: Union[bytes, str]

    pricePerToken: int

    currency: str


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

    def validate_and_normalize_inputs(self, account: str, _id: int):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name="balanceOf",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="balanceOf",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (account, _id)

    def call(
        self, account: str, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, _id) = self.validate_and_normalize_inputs(account, _id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, _id).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, account: str, _id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, _id) = self.validate_and_normalize_inputs(account, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, account: str, _id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, _id) = self.validate_and_normalize_inputs(account, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, _id) = self.validate_and_normalize_inputs(account, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id).estimateGas(
            tx_params.as_dict()
        )


class BalanceOfBatchMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the balanceOfBatch method."""

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
        self, accounts: List[str], ids: List[int]
    ):
        """Validate the inputs to the balanceOfBatch method."""
        self.validator.assert_valid(
            method_name="balanceOfBatch",
            parameter_name="accounts",
            argument_value=accounts,
        )
        self.validator.assert_valid(
            method_name="balanceOfBatch",
            parameter_name="ids",
            argument_value=ids,
        )
        return (accounts, ids)

    def call(
        self,
        accounts: List[str],
        ids: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> List[int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (accounts, ids) = self.validate_and_normalize_inputs(accounts, ids)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(accounts, ids).call(
            tx_params.as_dict()
        )
        return [int(element) for element in returned]

    def send_transaction(
        self,
        accounts: List[str],
        ids: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (accounts, ids) = self.validate_and_normalize_inputs(accounts, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(accounts, ids).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        accounts: List[str],
        ids: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (accounts, ids) = self.validate_and_normalize_inputs(accounts, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(accounts, ids).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        accounts: List[str],
        ids: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (accounts, ids) = self.validate_and_normalize_inputs(accounts, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(accounts, ids).estimateGas(
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
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
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
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
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
            parameter_name="proofs",
            argument_value=proofs,
        )
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="proofMaxQuantityPerTransaction",
            argument_value=proof_max_quantity_per_transaction,
        )
        # safeguard against fractional inputs
        proof_max_quantity_per_transaction = int(
            proof_max_quantity_per_transaction
        )
        return (
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        )

    def call(
        self,
        receiver: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        receiver: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        receiver: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        receiver: str,
        token_id: int,
        quantity: int,
        currency: str,
        price_per_token: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_per_transaction: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ) = self.validate_and_normalize_inputs(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver,
            token_id,
            quantity,
            currency,
            price_per_token,
            proofs,
            proof_max_quantity_per_transaction,
        ).estimateGas(tx_params.as_dict())


class IsApprovedForAllMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isApprovedForAll method."""

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

    def validate_and_normalize_inputs(self, account: str, operator: str):
        """Validate the inputs to the isApprovedForAll method."""
        self.validator.assert_valid(
            method_name="isApprovedForAll",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="isApprovedForAll",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return (account, operator)

    def call(
        self, account: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, operator) = self.validate_and_normalize_inputs(
            account, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, operator).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self, account: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, operator) = self.validate_and_normalize_inputs(
            account, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, operator).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, account: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, operator) = self.validate_and_normalize_inputs(
            account, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, operator).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, operator: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, operator) = self.validate_and_normalize_inputs(
            account, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, operator).estimateGas(
            tx_params.as_dict()
        )


class LazyMintMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the lazyMint method."""

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
        self, amount: int, base_uri_for_tokens: str
    ):
        """Validate the inputs to the lazyMint method."""
        self.validator.assert_valid(
            method_name="lazyMint",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name="lazyMint",
            parameter_name="baseURIForTokens",
            argument_value=base_uri_for_tokens,
        )
        return (amount, base_uri_for_tokens)

    def call(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (amount, base_uri_for_tokens) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(amount, base_uri_for_tokens).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount, base_uri_for_tokens) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, base_uri_for_tokens).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount, base_uri_for_tokens) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            amount, base_uri_for_tokens
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (amount, base_uri_for_tokens) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            amount, base_uri_for_tokens
        ).estimateGas(tx_params.as_dict())


class SafeBatchTransferFromMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the safeBatchTransferFrom method."""

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
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
    ):
        """Validate the inputs to the safeBatchTransferFrom method."""
        self.validator.assert_valid(
            method_name="safeBatchTransferFrom",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="safeBatchTransferFrom",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="safeBatchTransferFrom",
            parameter_name="ids",
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="safeBatchTransferFrom",
            parameter_name="amounts",
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name="safeBatchTransferFrom",
            parameter_name="data",
            argument_value=data,
        )
        return (_from, to, ids, amounts, data)

    def call(
        self,
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, ids, amounts, data) = self.validate_and_normalize_inputs(
            _from, to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, ids, amounts, data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, ids, amounts, data) = self.validate_and_normalize_inputs(
            _from, to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, ids, amounts, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, ids, amounts, data) = self.validate_and_normalize_inputs(
            _from, to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, ids, amounts, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        _from: str,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, ids, amounts, data) = self.validate_and_normalize_inputs(
            _from, to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, ids, amounts, data
        ).estimateGas(tx_params.as_dict())


class SafeTransferFromMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the safeTransferFrom method."""

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
        _from: str,
        to: str,
        _id: int,
        amount: int,
        data: Union[bytes, str],
    ):
        """Validate the inputs to the safeTransferFrom method."""
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name="safeTransferFrom",
            parameter_name="data",
            argument_value=data,
        )
        return (_from, to, _id, amount, data)

    def call(
        self,
        _from: str,
        to: str,
        _id: int,
        amount: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, _id, amount, data) = self.validate_and_normalize_inputs(
            _from, to, _id, amount, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, _id, amount, data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        _from: str,
        to: str,
        _id: int,
        amount: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, _id, amount, data) = self.validate_and_normalize_inputs(
            _from, to, _id, amount, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, _id, amount, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        _from: str,
        to: str,
        _id: int,
        amount: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, _id, amount, data) = self.validate_and_normalize_inputs(
            _from, to, _id, amount, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, _id, amount, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        _from: str,
        to: str,
        _id: int,
        amount: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, _id, amount, data) = self.validate_and_normalize_inputs(
            _from, to, _id, amount, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            _from, to, _id, amount, data
        ).estimateGas(tx_params.as_dict())


class SetApprovalForAllMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setApprovalForAll method."""

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

    def validate_and_normalize_inputs(self, operator: str, approved: bool):
        """Validate the inputs to the setApprovalForAll method."""
        self.validator.assert_valid(
            method_name="setApprovalForAll",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="setApprovalForAll",
            parameter_name="approved",
            argument_value=approved,
        )
        return (operator, approved)

    def call(
        self,
        operator: str,
        approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator, approved) = self.validate_and_normalize_inputs(
            operator, approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(operator, approved).call(tx_params.as_dict())

    def send_transaction(
        self,
        operator: str,
        approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator, approved) = self.validate_and_normalize_inputs(
            operator, approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, approved).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        operator: str,
        approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator, approved) = self.validate_and_normalize_inputs(
            operator, approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, approved).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        operator: str,
        approved: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (operator, approved) = self.validate_and_normalize_inputs(
            operator, approved
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(operator, approved).estimateGas(
            tx_params.as_dict()
        )


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
        token_id: int,
        phases: List[IDropClaimCondition_V2ClaimCondition],
        reset_claim_eligibility: bool,
    ):
        """Validate the inputs to the setClaimConditions method."""
        self.validator.assert_valid(
            method_name="setClaimConditions",
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
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
        return (token_id, phases, reset_claim_eligibility)

    def call(
        self,
        token_id: int,
        phases: List[IDropClaimCondition_V2ClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            token_id,
            phases,
            reset_claim_eligibility,
        ) = self.validate_and_normalize_inputs(
            token_id, phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            token_id, phases, reset_claim_eligibility
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        token_id: int,
        phases: List[IDropClaimCondition_V2ClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            token_id,
            phases,
            reset_claim_eligibility,
        ) = self.validate_and_normalize_inputs(
            token_id, phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, phases, reset_claim_eligibility
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        token_id: int,
        phases: List[IDropClaimCondition_V2ClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            token_id,
            phases,
            reset_claim_eligibility,
        ) = self.validate_and_normalize_inputs(
            token_id, phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, phases, reset_claim_eligibility
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        token_id: int,
        phases: List[IDropClaimCondition_V2ClaimCondition],
        reset_claim_eligibility: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            token_id,
            phases,
            reset_claim_eligibility,
        ) = self.validate_and_normalize_inputs(
            token_id, phases, reset_claim_eligibility
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, phases, reset_claim_eligibility
        ).estimateGas(tx_params.as_dict())


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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IDropERC1155_V2:
    """Wrapper class for IDropERC1155_V2 Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    balance_of_batch: BalanceOfBatchMethod
    """Constructor-initialized instance of
    :class:`BalanceOfBatchMethod`.
    """

    claim: ClaimMethod
    """Constructor-initialized instance of
    :class:`ClaimMethod`.
    """

    is_approved_for_all: IsApprovedForAllMethod
    """Constructor-initialized instance of
    :class:`IsApprovedForAllMethod`.
    """

    lazy_mint: LazyMintMethod
    """Constructor-initialized instance of
    :class:`LazyMintMethod`.
    """

    safe_batch_transfer_from: SafeBatchTransferFromMethod
    """Constructor-initialized instance of
    :class:`SafeBatchTransferFromMethod`.
    """

    safe_transfer_from: SafeTransferFromMethod
    """Constructor-initialized instance of
    :class:`SafeTransferFromMethod`.
    """

    set_approval_for_all: SetApprovalForAllMethod
    """Constructor-initialized instance of
    :class:`SetApprovalForAllMethod`.
    """

    set_claim_conditions: SetClaimConditionsMethod
    """Constructor-initialized instance of
    :class:`SetClaimConditionsMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IDropERC1155_V2Validator = None,
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
            validator = IDropERC1155_V2Validator(
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
            abi=IDropERC1155_V2.abi(),
        ).functions

        self.balance_of = BalanceOfMethod(
            web3_or_provider, contract_address, functions.balanceOf, validator
        )

        self.balance_of_batch = BalanceOfBatchMethod(
            web3_or_provider,
            contract_address,
            functions.balanceOfBatch,
            validator,
        )

        self.claim = ClaimMethod(
            web3_or_provider, contract_address, functions.claim, validator
        )

        self.is_approved_for_all = IsApprovedForAllMethod(
            web3_or_provider,
            contract_address,
            functions.isApprovedForAll,
            validator,
        )

        self.lazy_mint = LazyMintMethod(
            web3_or_provider, contract_address, functions.lazyMint, validator
        )

        self.safe_batch_transfer_from = SafeBatchTransferFromMethod(
            web3_or_provider,
            contract_address,
            functions.safeBatchTransferFrom,
            validator,
        )

        self.safe_transfer_from = SafeTransferFromMethod(
            web3_or_provider,
            contract_address,
            functions.safeTransferFrom,
            validator,
        )

        self.set_approval_for_all = SetApprovalForAllMethod(
            web3_or_provider,
            contract_address,
            functions.setApprovalForAll,
            validator,
        )

        self.set_claim_conditions = SetClaimConditionsMethod(
            web3_or_provider,
            contract_address,
            functions.setClaimConditions,
            validator,
        )

        self.supports_interface = SupportsInterfaceMethod(
            web3_or_provider,
            contract_address,
            functions.supportsInterface,
            validator,
        )

    def get_approval_for_all_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ApprovalForAll event.

        :param tx_hash: hash of transaction emitting ApprovalForAll event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC1155_V2.abi(),
            )
            .events.ApprovalForAll()
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
                abi=IDropERC1155_V2.abi(),
            )
            .events.ClaimConditionsUpdated()
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
                abi=IDropERC1155_V2.abi(),
            )
            .events.MaxTotalSupplyUpdated()
            .processReceipt(tx_receipt)
        )

    def get_max_wallet_claim_count_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for MaxWalletClaimCountUpdated event.

        :param tx_hash: hash of transaction emitting MaxWalletClaimCountUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC1155_V2.abi(),
            )
            .events.MaxWalletClaimCountUpdated()
            .processReceipt(tx_receipt)
        )

    def get_sale_recipient_for_token_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for SaleRecipientForTokenUpdated event.

        :param tx_hash: hash of transaction emitting
            SaleRecipientForTokenUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC1155_V2.abi(),
            )
            .events.SaleRecipientForTokenUpdated()
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
                abi=IDropERC1155_V2.abi(),
            )
            .events.TokensClaimed()
            .processReceipt(tx_receipt)
        )

    def get_tokens_lazy_minted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensLazyMinted event.

        :param tx_hash: hash of transaction emitting TokensLazyMinted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC1155_V2.abi(),
            )
            .events.TokensLazyMinted()
            .processReceipt(tx_receipt)
        )

    def get_transfer_batch_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TransferBatch event.

        :param tx_hash: hash of transaction emitting TransferBatch event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC1155_V2.abi(),
            )
            .events.TransferBatch()
            .processReceipt(tx_receipt)
        )

    def get_transfer_single_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TransferSingle event.

        :param tx_hash: hash of transaction emitting TransferSingle event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC1155_V2.abi(),
            )
            .events.TransferSingle()
            .processReceipt(tx_receipt)
        )

    def get_uri_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for URI event.

        :param tx_hash: hash of transaction emitting URI event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC1155_V2.abi(),
            )
            .events.URI()
            .processReceipt(tx_receipt)
        )

    def get_wallet_claim_count_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for WalletClaimCountUpdated event.

        :param tx_hash: hash of transaction emitting WalletClaimCountUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IDropERC1155_V2.abi(),
            )
            .events.WalletClaimCountUpdated()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerTransaction","type":"uint256"},{"internalType":"uint256","name":"waitTimeInSecondsBetweenClaims","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"indexed":false,"internalType":"struct IDropClaimCondition_V2.ClaimCondition[]","name":"claimConditions","type":"tuple[]"}],"name":"ClaimConditionsUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"maxTotalSupply","type":"uint256"}],"name":"MaxTotalSupplyUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"count","type":"uint256"}],"name":"MaxWalletClaimCountUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"address","name":"saleRecipient","type":"address"}],"name":"SaleRecipientForTokenUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"claimConditionIndex","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"claimer","type":"address"},{"indexed":false,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantityClaimed","type":"uint256"}],"name":"TokensClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"startTokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"endTokenId","type":"uint256"},{"indexed":false,"internalType":"string","name":"baseURI","type":"string"}],"name":"TokensLazyMinted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"wallet","type":"address"},{"indexed":false,"internalType":"uint256","name":"count","type":"uint256"}],"name":"WalletClaimCountUpdated","type":"event"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"bytes32[]","name":"proofs","type":"bytes32[]"},{"internalType":"uint256","name":"proofMaxQuantityPerTransaction","type":"uint256"}],"name":"claim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"string","name":"baseURIForTokens","type":"string"}],"name":"lazyMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerTransaction","type":"uint256"},{"internalType":"uint256","name":"waitTimeInSecondsBetweenClaims","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"internalType":"struct IDropClaimCondition_V2.ClaimCondition[]","name":"phases","type":"tuple[]"},{"internalType":"bool","name":"resetClaimEligibility","type":"bool"}],"name":"setClaimConditions","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
