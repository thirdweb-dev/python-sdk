"""Generated wrapper for DropERC1155 Solidity contract."""

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
# constructor for DropERC1155 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        DropERC1155Validator,
    )
except ImportError:

    class DropERC1155Validator(  # type: ignore
        Validator
    ):
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

    quantityLimitPerTransaction: int

    waitTimeInSecondsBetweenClaims: int

    merkleRoot: Union[bytes, str]

    pricePerToken: int

    currency: str


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

class BalanceOfMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the balanceOf method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, _id: int):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name='balanceOf',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='balanceOf',
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (account, _id)

    def call(self, account: str, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, _id) = self.validate_and_normalize_inputs(account, _id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, _id).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, account: str, _id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, _id) = self.validate_and_normalize_inputs(account, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id).transact(tx_params.as_dict())

    def build_transaction(self, account: str, _id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, _id) = self.validate_and_normalize_inputs(account, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, _id) = self.validate_and_normalize_inputs(account, _id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id).estimateGas(tx_params.as_dict())

class BalanceOfBatchMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the balanceOfBatch method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, accounts: List[str], ids: List[int]):
        """Validate the inputs to the balanceOfBatch method."""
        self.validator.assert_valid(
            method_name='balanceOfBatch',
            parameter_name='accounts',
            argument_value=accounts,
        )
        self.validator.assert_valid(
            method_name='balanceOfBatch',
            parameter_name='ids',
            argument_value=ids,
        )
        return (accounts, ids)

    def call(self, accounts: List[str], ids: List[int], tx_params: Optional[TxParams] = None) -> List[int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (accounts, ids) = self.validate_and_normalize_inputs(accounts, ids)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(accounts, ids).call(tx_params.as_dict())
        return [int(element) for element in returned]

    def send_transaction(self, accounts: List[str], ids: List[int], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (accounts, ids) = self.validate_and_normalize_inputs(accounts, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(accounts, ids).transact(tx_params.as_dict())

    def build_transaction(self, accounts: List[str], ids: List[int], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (accounts, ids) = self.validate_and_normalize_inputs(accounts, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(accounts, ids).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, accounts: List[str], ids: List[int], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (accounts, ids) = self.validate_and_normalize_inputs(accounts, ids)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(accounts, ids).estimateGas(tx_params.as_dict())

class BurnMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the burn method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, _id: int, value: int):
        """Validate the inputs to the burn method."""
        self.validator.assert_valid(
            method_name='burn',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='burn',
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name='burn',
            parameter_name='value',
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        return (account, _id, value)

    def call(self, account: str, _id: int, value: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, _id, value) = self.validate_and_normalize_inputs(account, _id, value)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, _id, value).call(tx_params.as_dict())

    def send_transaction(self, account: str, _id: int, value: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, _id, value) = self.validate_and_normalize_inputs(account, _id, value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id, value).transact(tx_params.as_dict())

    def build_transaction(self, account: str, _id: int, value: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, _id, value) = self.validate_and_normalize_inputs(account, _id, value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id, value).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, _id: int, value: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, _id, value) = self.validate_and_normalize_inputs(account, _id, value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id, value).estimateGas(tx_params.as_dict())

class BurnBatchMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the burnBatch method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, ids: List[int], values: List[int]):
        """Validate the inputs to the burnBatch method."""
        self.validator.assert_valid(
            method_name='burnBatch',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='burnBatch',
            parameter_name='ids',
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name='burnBatch',
            parameter_name='values',
            argument_value=values,
        )
        return (account, ids, values)

    def call(self, account: str, ids: List[int], values: List[int], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, ids, values) = self.validate_and_normalize_inputs(account, ids, values)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, ids, values).call(tx_params.as_dict())

    def send_transaction(self, account: str, ids: List[int], values: List[int], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, ids, values) = self.validate_and_normalize_inputs(account, ids, values)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, ids, values).transact(tx_params.as_dict())

    def build_transaction(self, account: str, ids: List[int], values: List[int], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, ids, values) = self.validate_and_normalize_inputs(account, ids, values)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, ids, values).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, ids: List[int], values: List[int], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, ids, values) = self.validate_and_normalize_inputs(account, ids, values)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, ids, values).estimateGas(tx_params.as_dict())

class ClaimMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the claim method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, receiver: str, token_id: int, quantity: int, currency: str, price_per_token: int, proofs: List[Union[bytes, str]], proof_max_quantity_per_transaction: int):
        """Validate the inputs to the claim method."""
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='_receiver',
            argument_value=receiver,
        )
        receiver = self.validate_and_checksum_address(receiver)
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='_quantity',
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='_currency',
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='_pricePerToken',
            argument_value=price_per_token,
        )
        # safeguard against fractional inputs
        price_per_token = int(price_per_token)
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='_proofs',
            argument_value=proofs,
        )
        self.validator.assert_valid(
            method_name='claim',
            parameter_name='_proofMaxQuantityPerTransaction',
            argument_value=proof_max_quantity_per_transaction,
        )
        # safeguard against fractional inputs
        proof_max_quantity_per_transaction = int(proof_max_quantity_per_transaction)
        return (receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction)

    def call(self, receiver: str, token_id: int, quantity: int, currency: str, price_per_token: int, proofs: List[Union[bytes, str]], proof_max_quantity_per_transaction: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction) = self.validate_and_normalize_inputs(receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction).call(tx_params.as_dict())

    def send_transaction(self, receiver: str, token_id: int, quantity: int, currency: str, price_per_token: int, proofs: List[Union[bytes, str]], proof_max_quantity_per_transaction: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction) = self.validate_and_normalize_inputs(receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction).transact(tx_params.as_dict())

    def build_transaction(self, receiver: str, token_id: int, quantity: int, currency: str, price_per_token: int, proofs: List[Union[bytes, str]], proof_max_quantity_per_transaction: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction) = self.validate_and_normalize_inputs(receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, receiver: str, token_id: int, quantity: int, currency: str, price_per_token: int, proofs: List[Union[bytes, str]], proof_max_quantity_per_transaction: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction) = self.validate_and_normalize_inputs(receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(receiver, token_id, quantity, currency, price_per_token, proofs, proof_max_quantity_per_transaction).estimateGas(tx_params.as_dict())

class ClaimConditionMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the claimCondition method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the claimCondition method."""
        self.validator.assert_valid(
            method_name='claimCondition',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (returned[0],returned[1],)

    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

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

class GetActiveClaimConditionIdMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getActiveClaimConditionId method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the getActiveClaimConditionId method."""
        self.validator.assert_valid(
            method_name='getActiveClaimConditionId',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (token_id)

    def call(self, token_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id).call(tx_params.as_dict())
        return int(returned)

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

class GetClaimConditionByIdMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getClaimConditionById method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int, condition_id: int):
        """Validate the inputs to the getClaimConditionById method."""
        self.validator.assert_valid(
            method_name='getClaimConditionById',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='getClaimConditionById',
            parameter_name='_conditionId',
            argument_value=condition_id,
        )
        # safeguard against fractional inputs
        condition_id = int(condition_id)
        return (token_id, condition_id)

    def call(self, token_id: int, condition_id: int, tx_params: Optional[TxParams] = None) -> IDropClaimConditionClaimCondition:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, condition_id) = self.validate_and_normalize_inputs(token_id, condition_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id, condition_id).call(tx_params.as_dict())
        return IDropClaimConditionClaimCondition(startTimestamp=returned[0],maxClaimableSupply=returned[1],supplyClaimed=returned[2],quantityLimitPerTransaction=returned[3],waitTimeInSecondsBetweenClaims=returned[4],merkleRoot=returned[5],pricePerToken=returned[6],currency=returned[7],)

    def send_transaction(self, token_id: int, condition_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, condition_id) = self.validate_and_normalize_inputs(token_id, condition_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, condition_id).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, condition_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, condition_id) = self.validate_and_normalize_inputs(token_id, condition_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, condition_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, condition_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id, condition_id) = self.validate_and_normalize_inputs(token_id, condition_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, condition_id).estimateGas(tx_params.as_dict())

class GetClaimTimestampMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getClaimTimestamp method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int, condition_id: int, claimer: str):
        """Validate the inputs to the getClaimTimestamp method."""
        self.validator.assert_valid(
            method_name='getClaimTimestamp',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='getClaimTimestamp',
            parameter_name='_conditionId',
            argument_value=condition_id,
        )
        # safeguard against fractional inputs
        condition_id = int(condition_id)
        self.validator.assert_valid(
            method_name='getClaimTimestamp',
            parameter_name='_claimer',
            argument_value=claimer,
        )
        claimer = self.validate_and_checksum_address(claimer)
        return (token_id, condition_id, claimer)

    def call(self, token_id: int, condition_id: int, claimer: str, tx_params: Optional[TxParams] = None) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, condition_id, claimer) = self.validate_and_normalize_inputs(token_id, condition_id, claimer)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id, condition_id, claimer).call(tx_params.as_dict())
        return (returned[0],returned[1],)

    def send_transaction(self, token_id: int, condition_id: int, claimer: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, condition_id, claimer) = self.validate_and_normalize_inputs(token_id, condition_id, claimer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, condition_id, claimer).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, condition_id: int, claimer: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, condition_id, claimer) = self.validate_and_normalize_inputs(token_id, condition_id, claimer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, condition_id, claimer).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, condition_id: int, claimer: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id, condition_id, claimer) = self.validate_and_normalize_inputs(token_id, condition_id, claimer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, condition_id, claimer).estimateGas(tx_params.as_dict())

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

class GetPlatformFeeInfoMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getPlatformFeeInfo method."""

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

class InitializeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the initialize method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, default_admin: str, name: str, symbol: str, contract_uri: str, trusted_forwarders: List[str], sale_recipient: str, royalty_recipient: str, royalty_bps: int, platform_fee_bps: int, platform_fee_recipient: str):
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
            parameter_name='_saleRecipient',
            argument_value=sale_recipient,
        )
        sale_recipient = self.validate_and_checksum_address(sale_recipient)
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
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_platformFeeBps',
            argument_value=platform_fee_bps,
        )
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_platformFeeRecipient',
            argument_value=platform_fee_recipient,
        )
        platform_fee_recipient = self.validate_and_checksum_address(platform_fee_recipient)
        return (default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient)

    def call(self, default_admin: str, name: str, symbol: str, contract_uri: str, trusted_forwarders: List[str], sale_recipient: str, royalty_recipient: str, royalty_bps: int, platform_fee_bps: int, platform_fee_recipient: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient) = self.validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient).call(tx_params.as_dict())

    def send_transaction(self, default_admin: str, name: str, symbol: str, contract_uri: str, trusted_forwarders: List[str], sale_recipient: str, royalty_recipient: str, royalty_bps: int, platform_fee_bps: int, platform_fee_recipient: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient) = self.validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient).transact(tx_params.as_dict())

    def build_transaction(self, default_admin: str, name: str, symbol: str, contract_uri: str, trusted_forwarders: List[str], sale_recipient: str, royalty_recipient: str, royalty_bps: int, platform_fee_bps: int, platform_fee_recipient: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient) = self.validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, default_admin: str, name: str, symbol: str, contract_uri: str, trusted_forwarders: List[str], sale_recipient: str, royalty_recipient: str, royalty_bps: int, platform_fee_bps: int, platform_fee_recipient: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient) = self.validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient).estimateGas(tx_params.as_dict())

class IsApprovedForAllMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isApprovedForAll method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, operator: str):
        """Validate the inputs to the isApprovedForAll method."""
        self.validator.assert_valid(
            method_name='isApprovedForAll',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='isApprovedForAll',
            parameter_name='operator',
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return (account, operator)

    def call(self, account: str, operator: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, operator) = self.validate_and_normalize_inputs(account, operator)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, operator).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, account: str, operator: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, operator) = self.validate_and_normalize_inputs(account, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, operator).transact(tx_params.as_dict())

    def build_transaction(self, account: str, operator: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, operator) = self.validate_and_normalize_inputs(account, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, operator).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, operator: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, operator) = self.validate_and_normalize_inputs(account, operator)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, operator).estimateGas(tx_params.as_dict())

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

class LazyMintMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the lazyMint method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, amount: int, base_uri_for_tokens: str):
        """Validate the inputs to the lazyMint method."""
        self.validator.assert_valid(
            method_name='lazyMint',
            parameter_name='_amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name='lazyMint',
            parameter_name='_baseURIForTokens',
            argument_value=base_uri_for_tokens,
        )
        return (amount, base_uri_for_tokens)

    def call(self, amount: int, base_uri_for_tokens: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (amount, base_uri_for_tokens) = self.validate_and_normalize_inputs(amount, base_uri_for_tokens)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(amount, base_uri_for_tokens).call(tx_params.as_dict())

    def send_transaction(self, amount: int, base_uri_for_tokens: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount, base_uri_for_tokens) = self.validate_and_normalize_inputs(amount, base_uri_for_tokens)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, base_uri_for_tokens).transact(tx_params.as_dict())

    def build_transaction(self, amount: int, base_uri_for_tokens: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount, base_uri_for_tokens) = self.validate_and_normalize_inputs(amount, base_uri_for_tokens)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, base_uri_for_tokens).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, amount: int, base_uri_for_tokens: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (amount, base_uri_for_tokens) = self.validate_and_normalize_inputs(amount, base_uri_for_tokens)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, base_uri_for_tokens).estimateGas(tx_params.as_dict())

class MaxTotalSupplyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the maxTotalSupply method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the maxTotalSupply method."""
        self.validator.assert_valid(
            method_name='maxTotalSupply',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class MaxWalletClaimCountMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the maxWalletClaimCount method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the maxWalletClaimCount method."""
        self.validator.assert_valid(
            method_name='maxWalletClaimCount',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

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

class PrimarySaleRecipientMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the primarySaleRecipient method."""

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

class SafeBatchTransferFromMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the safeBatchTransferFrom method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _from: str, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str]):
        """Validate the inputs to the safeBatchTransferFrom method."""
        self.validator.assert_valid(
            method_name='safeBatchTransferFrom',
            parameter_name='from',
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name='safeBatchTransferFrom',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='safeBatchTransferFrom',
            parameter_name='ids',
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name='safeBatchTransferFrom',
            parameter_name='amounts',
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name='safeBatchTransferFrom',
            parameter_name='data',
            argument_value=data,
        )
        return (_from, to, ids, amounts, data)

    def call(self, _from: str, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, ids, amounts, data) = self.validate_and_normalize_inputs(_from, to, ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, ids, amounts, data).call(tx_params.as_dict())

    def send_transaction(self, _from: str, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, ids, amounts, data) = self.validate_and_normalize_inputs(_from, to, ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, ids, amounts, data).transact(tx_params.as_dict())

    def build_transaction(self, _from: str, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, ids, amounts, data) = self.validate_and_normalize_inputs(_from, to, ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, ids, amounts, data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _from: str, to: str, ids: List[int], amounts: List[int], data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, ids, amounts, data) = self.validate_and_normalize_inputs(_from, to, ids, amounts, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, ids, amounts, data).estimateGas(tx_params.as_dict())

class SafeTransferFromMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the safeTransferFrom method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _from: str, to: str, _id: int, amount: int, data: Union[bytes, str]):
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
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name='safeTransferFrom',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name='safeTransferFrom',
            parameter_name='data',
            argument_value=data,
        )
        return (_from, to, _id, amount, data)

    def call(self, _from: str, to: str, _id: int, amount: int, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, _id, amount, data) = self.validate_and_normalize_inputs(_from, to, _id, amount, data)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(_from, to, _id, amount, data).call(tx_params.as_dict())

    def send_transaction(self, _from: str, to: str, _id: int, amount: int, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, _id, amount, data) = self.validate_and_normalize_inputs(_from, to, _id, amount, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, _id, amount, data).transact(tx_params.as_dict())

    def build_transaction(self, _from: str, to: str, _id: int, amount: int, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, _id, amount, data) = self.validate_and_normalize_inputs(_from, to, _id, amount, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, _id, amount, data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _from: str, to: str, _id: int, amount: int, data: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, _id, amount, data) = self.validate_and_normalize_inputs(_from, to, _id, amount, data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, _id, amount, data).estimateGas(tx_params.as_dict())

class SaleRecipientMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the saleRecipient method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the saleRecipient method."""
        self.validator.assert_valid(
            method_name='saleRecipient',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

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

class SetClaimConditionsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setClaimConditions method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int, phases: List[IDropClaimConditionClaimCondition], reset_claim_eligibility: bool):
        """Validate the inputs to the setClaimConditions method."""
        self.validator.assert_valid(
            method_name='setClaimConditions',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='setClaimConditions',
            parameter_name='_phases',
            argument_value=phases,
        )
        self.validator.assert_valid(
            method_name='setClaimConditions',
            parameter_name='_resetClaimEligibility',
            argument_value=reset_claim_eligibility,
        )
        return (token_id, phases, reset_claim_eligibility)

    def call(self, token_id: int, phases: List[IDropClaimConditionClaimCondition], reset_claim_eligibility: bool, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(token_id, phases, reset_claim_eligibility)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, phases, reset_claim_eligibility).call(tx_params.as_dict())

    def send_transaction(self, token_id: int, phases: List[IDropClaimConditionClaimCondition], reset_claim_eligibility: bool, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(token_id, phases, reset_claim_eligibility)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, phases, reset_claim_eligibility).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, phases: List[IDropClaimConditionClaimCondition], reset_claim_eligibility: bool, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(token_id, phases, reset_claim_eligibility)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, phases, reset_claim_eligibility).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, phases: List[IDropClaimConditionClaimCondition], reset_claim_eligibility: bool, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id, phases, reset_claim_eligibility) = self.validate_and_normalize_inputs(token_id, phases, reset_claim_eligibility)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, phases, reset_claim_eligibility).estimateGas(tx_params.as_dict())

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

class SetMaxTotalSupplyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setMaxTotalSupply method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int, max_total_supply: int):
        """Validate the inputs to the setMaxTotalSupply method."""
        self.validator.assert_valid(
            method_name='setMaxTotalSupply',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='setMaxTotalSupply',
            parameter_name='_maxTotalSupply',
            argument_value=max_total_supply,
        )
        # safeguard against fractional inputs
        max_total_supply = int(max_total_supply)
        return (token_id, max_total_supply)

    def call(self, token_id: int, max_total_supply: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, max_total_supply) = self.validate_and_normalize_inputs(token_id, max_total_supply)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, max_total_supply).call(tx_params.as_dict())

    def send_transaction(self, token_id: int, max_total_supply: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, max_total_supply) = self.validate_and_normalize_inputs(token_id, max_total_supply)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, max_total_supply).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, max_total_supply: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, max_total_supply) = self.validate_and_normalize_inputs(token_id, max_total_supply)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, max_total_supply).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, max_total_supply: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id, max_total_supply) = self.validate_and_normalize_inputs(token_id, max_total_supply)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, max_total_supply).estimateGas(tx_params.as_dict())

class SetMaxWalletClaimCountMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setMaxWalletClaimCount method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int, count: int):
        """Validate the inputs to the setMaxWalletClaimCount method."""
        self.validator.assert_valid(
            method_name='setMaxWalletClaimCount',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='setMaxWalletClaimCount',
            parameter_name='_count',
            argument_value=count,
        )
        # safeguard against fractional inputs
        count = int(count)
        return (token_id, count)

    def call(self, token_id: int, count: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, count) = self.validate_and_normalize_inputs(token_id, count)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, count).call(tx_params.as_dict())

    def send_transaction(self, token_id: int, count: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, count) = self.validate_and_normalize_inputs(token_id, count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, count).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, count: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, count) = self.validate_and_normalize_inputs(token_id, count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, count).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, count: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id, count) = self.validate_and_normalize_inputs(token_id, count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, count).estimateGas(tx_params.as_dict())

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

class SetPlatformFeeInfoMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setPlatformFeeInfo method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, platform_fee_recipient: str, platform_fee_bps: int):
        """Validate the inputs to the setPlatformFeeInfo method."""
        self.validator.assert_valid(
            method_name='setPlatformFeeInfo',
            parameter_name='_platformFeeRecipient',
            argument_value=platform_fee_recipient,
        )
        platform_fee_recipient = self.validate_and_checksum_address(platform_fee_recipient)
        self.validator.assert_valid(
            method_name='setPlatformFeeInfo',
            parameter_name='_platformFeeBps',
            argument_value=platform_fee_bps,
        )
        # safeguard against fractional inputs
        platform_fee_bps = int(platform_fee_bps)
        return (platform_fee_recipient, platform_fee_bps)

    def call(self, platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(platform_fee_recipient, platform_fee_bps).call(tx_params.as_dict())

    def send_transaction(self, platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(platform_fee_recipient, platform_fee_bps).transact(tx_params.as_dict())

    def build_transaction(self, platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(platform_fee_recipient, platform_fee_bps).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(platform_fee_recipient, platform_fee_bps).estimateGas(tx_params.as_dict())

class SetPrimarySaleRecipientMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setPrimarySaleRecipient method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, sale_recipient: str):
        """Validate the inputs to the setPrimarySaleRecipient method."""
        self.validator.assert_valid(
            method_name='setPrimarySaleRecipient',
            parameter_name='_saleRecipient',
            argument_value=sale_recipient,
        )
        sale_recipient = self.validate_and_checksum_address(sale_recipient)
        return (sale_recipient)

    def call(self, sale_recipient: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (sale_recipient) = self.validate_and_normalize_inputs(sale_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(sale_recipient).call(tx_params.as_dict())

    def send_transaction(self, sale_recipient: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (sale_recipient) = self.validate_and_normalize_inputs(sale_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sale_recipient).transact(tx_params.as_dict())

    def build_transaction(self, sale_recipient: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (sale_recipient) = self.validate_and_normalize_inputs(sale_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sale_recipient).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, sale_recipient: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (sale_recipient) = self.validate_and_normalize_inputs(sale_recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sale_recipient).estimateGas(tx_params.as_dict())

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

class SetWalletClaimCountMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setWalletClaimCount method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int, claimer: str, count: int):
        """Validate the inputs to the setWalletClaimCount method."""
        self.validator.assert_valid(
            method_name='setWalletClaimCount',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='setWalletClaimCount',
            parameter_name='_claimer',
            argument_value=claimer,
        )
        claimer = self.validate_and_checksum_address(claimer)
        self.validator.assert_valid(
            method_name='setWalletClaimCount',
            parameter_name='_count',
            argument_value=count,
        )
        # safeguard against fractional inputs
        count = int(count)
        return (token_id, claimer, count)

    def call(self, token_id: int, claimer: str, count: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, claimer, count) = self.validate_and_normalize_inputs(token_id, claimer, count)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, claimer, count).call(tx_params.as_dict())

    def send_transaction(self, token_id: int, claimer: str, count: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, claimer, count) = self.validate_and_normalize_inputs(token_id, claimer, count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, claimer, count).transact(tx_params.as_dict())

    def build_transaction(self, token_id: int, claimer: str, count: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, claimer, count) = self.validate_and_normalize_inputs(token_id, claimer, count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, claimer, count).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_id: int, claimer: str, count: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_id, claimer, count) = self.validate_and_normalize_inputs(token_id, claimer, count)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, claimer, count).estimateGas(tx_params.as_dict())

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

class TotalSupplyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the totalSupply method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the totalSupply method."""
        self.validator.assert_valid(
            method_name='totalSupply',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class UriMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the uri method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the uri method."""
        self.validator.assert_valid(
            method_name='uri',
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

class VerifyClaimMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the verifyClaim method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, condition_id: int, claimer: str, token_id: int, quantity: int, currency: str, price_per_token: int, verify_max_quantity_per_transaction: bool):
        """Validate the inputs to the verifyClaim method."""
        self.validator.assert_valid(
            method_name='verifyClaim',
            parameter_name='_conditionId',
            argument_value=condition_id,
        )
        # safeguard against fractional inputs
        condition_id = int(condition_id)
        self.validator.assert_valid(
            method_name='verifyClaim',
            parameter_name='_claimer',
            argument_value=claimer,
        )
        claimer = self.validate_and_checksum_address(claimer)
        self.validator.assert_valid(
            method_name='verifyClaim',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='verifyClaim',
            parameter_name='_quantity',
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name='verifyClaim',
            parameter_name='_currency',
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name='verifyClaim',
            parameter_name='_pricePerToken',
            argument_value=price_per_token,
        )
        # safeguard against fractional inputs
        price_per_token = int(price_per_token)
        self.validator.assert_valid(
            method_name='verifyClaim',
            parameter_name='verifyMaxQuantityPerTransaction',
            argument_value=verify_max_quantity_per_transaction,
        )
        return (condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction)

    def call(self, condition_id: int, claimer: str, token_id: int, quantity: int, currency: str, price_per_token: int, verify_max_quantity_per_transaction: bool, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction) = self.validate_and_normalize_inputs(condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction).call(tx_params.as_dict())

    def send_transaction(self, condition_id: int, claimer: str, token_id: int, quantity: int, currency: str, price_per_token: int, verify_max_quantity_per_transaction: bool, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction) = self.validate_and_normalize_inputs(condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction).transact(tx_params.as_dict())

    def build_transaction(self, condition_id: int, claimer: str, token_id: int, quantity: int, currency: str, price_per_token: int, verify_max_quantity_per_transaction: bool, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction) = self.validate_and_normalize_inputs(condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, condition_id: int, claimer: str, token_id: int, quantity: int, currency: str, price_per_token: int, verify_max_quantity_per_transaction: bool, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction) = self.validate_and_normalize_inputs(condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id, claimer, token_id, quantity, currency, price_per_token, verify_max_quantity_per_transaction).estimateGas(tx_params.as_dict())

class VerifyClaimMerkleProofMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the verifyClaimMerkleProof method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, condition_id: int, claimer: str, token_id: int, quantity: int, proofs: List[Union[bytes, str]], proof_max_quantity_per_transaction: int):
        """Validate the inputs to the verifyClaimMerkleProof method."""
        self.validator.assert_valid(
            method_name='verifyClaimMerkleProof',
            parameter_name='_conditionId',
            argument_value=condition_id,
        )
        # safeguard against fractional inputs
        condition_id = int(condition_id)
        self.validator.assert_valid(
            method_name='verifyClaimMerkleProof',
            parameter_name='_claimer',
            argument_value=claimer,
        )
        claimer = self.validate_and_checksum_address(claimer)
        self.validator.assert_valid(
            method_name='verifyClaimMerkleProof',
            parameter_name='_tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='verifyClaimMerkleProof',
            parameter_name='_quantity',
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name='verifyClaimMerkleProof',
            parameter_name='_proofs',
            argument_value=proofs,
        )
        self.validator.assert_valid(
            method_name='verifyClaimMerkleProof',
            parameter_name='_proofMaxQuantityPerTransaction',
            argument_value=proof_max_quantity_per_transaction,
        )
        # safeguard against fractional inputs
        proof_max_quantity_per_transaction = int(proof_max_quantity_per_transaction)
        return (condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction)

    def call(self, condition_id: int, claimer: str, token_id: int, quantity: int, proofs: List[Union[bytes, str]], proof_max_quantity_per_transaction: int, tx_params: Optional[TxParams] = None) -> Tuple[bool, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction) = self.validate_and_normalize_inputs(condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction).call(tx_params.as_dict())
        return (returned[0],returned[1],)

    def send_transaction(self, condition_id: int, claimer: str, token_id: int, quantity: int, proofs: List[Union[bytes, str]], proof_max_quantity_per_transaction: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction) = self.validate_and_normalize_inputs(condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction).transact(tx_params.as_dict())

    def build_transaction(self, condition_id: int, claimer: str, token_id: int, quantity: int, proofs: List[Union[bytes, str]], proof_max_quantity_per_transaction: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction) = self.validate_and_normalize_inputs(condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, condition_id: int, claimer: str, token_id: int, quantity: int, proofs: List[Union[bytes, str]], proof_max_quantity_per_transaction: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction) = self.validate_and_normalize_inputs(condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(condition_id, claimer, token_id, quantity, proofs, proof_max_quantity_per_transaction).estimateGas(tx_params.as_dict())

class WalletClaimCountMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the walletClaimCount method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int, index_1: str):
        """Validate the inputs to the walletClaimCount method."""
        self.validator.assert_valid(
            method_name='walletClaimCount',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        self.validator.assert_valid(
            method_name='walletClaimCount',
            parameter_name='index_1',
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        return (index_0, index_1)

    def call(self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(tx_params.as_dict())

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class DropERC1155:
    """Wrapper class for DropERC1155 Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """
    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    balance_of_batch: BalanceOfBatchMethod
    """Constructor-initialized instance of
    :class:`BalanceOfBatchMethod`.
    """

    burn: BurnMethod
    """Constructor-initialized instance of
    :class:`BurnMethod`.
    """

    burn_batch: BurnBatchMethod
    """Constructor-initialized instance of
    :class:`BurnBatchMethod`.
    """

    claim: ClaimMethod
    """Constructor-initialized instance of
    :class:`ClaimMethod`.
    """

    claim_condition: ClaimConditionMethod
    """Constructor-initialized instance of
    :class:`ClaimConditionMethod`.
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

    get_active_claim_condition_id: GetActiveClaimConditionIdMethod
    """Constructor-initialized instance of
    :class:`GetActiveClaimConditionIdMethod`.
    """

    get_claim_condition_by_id: GetClaimConditionByIdMethod
    """Constructor-initialized instance of
    :class:`GetClaimConditionByIdMethod`.
    """

    get_claim_timestamp: GetClaimTimestampMethod
    """Constructor-initialized instance of
    :class:`GetClaimTimestampMethod`.
    """

    get_default_royalty_info: GetDefaultRoyaltyInfoMethod
    """Constructor-initialized instance of
    :class:`GetDefaultRoyaltyInfoMethod`.
    """

    get_platform_fee_info: GetPlatformFeeInfoMethod
    """Constructor-initialized instance of
    :class:`GetPlatformFeeInfoMethod`.
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

    grant_role: GrantRoleMethod
    """Constructor-initialized instance of
    :class:`GrantRoleMethod`.
    """

    has_role: HasRoleMethod
    """Constructor-initialized instance of
    :class:`HasRoleMethod`.
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

    lazy_mint: LazyMintMethod
    """Constructor-initialized instance of
    :class:`LazyMintMethod`.
    """

    max_total_supply: MaxTotalSupplyMethod
    """Constructor-initialized instance of
    :class:`MaxTotalSupplyMethod`.
    """

    max_wallet_claim_count: MaxWalletClaimCountMethod
    """Constructor-initialized instance of
    :class:`MaxWalletClaimCountMethod`.
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

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    primary_sale_recipient: PrimarySaleRecipientMethod
    """Constructor-initialized instance of
    :class:`PrimarySaleRecipientMethod`.
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

    safe_batch_transfer_from: SafeBatchTransferFromMethod
    """Constructor-initialized instance of
    :class:`SafeBatchTransferFromMethod`.
    """

    safe_transfer_from: SafeTransferFromMethod
    """Constructor-initialized instance of
    :class:`SafeTransferFromMethod`.
    """

    sale_recipient: SaleRecipientMethod
    """Constructor-initialized instance of
    :class:`SaleRecipientMethod`.
    """

    set_approval_for_all: SetApprovalForAllMethod
    """Constructor-initialized instance of
    :class:`SetApprovalForAllMethod`.
    """

    set_claim_conditions: SetClaimConditionsMethod
    """Constructor-initialized instance of
    :class:`SetClaimConditionsMethod`.
    """

    set_contract_uri: SetContractUriMethod
    """Constructor-initialized instance of
    :class:`SetContractUriMethod`.
    """

    set_default_royalty_info: SetDefaultRoyaltyInfoMethod
    """Constructor-initialized instance of
    :class:`SetDefaultRoyaltyInfoMethod`.
    """

    set_max_total_supply: SetMaxTotalSupplyMethod
    """Constructor-initialized instance of
    :class:`SetMaxTotalSupplyMethod`.
    """

    set_max_wallet_claim_count: SetMaxWalletClaimCountMethod
    """Constructor-initialized instance of
    :class:`SetMaxWalletClaimCountMethod`.
    """

    set_owner: SetOwnerMethod
    """Constructor-initialized instance of
    :class:`SetOwnerMethod`.
    """

    set_platform_fee_info: SetPlatformFeeInfoMethod
    """Constructor-initialized instance of
    :class:`SetPlatformFeeInfoMethod`.
    """

    set_primary_sale_recipient: SetPrimarySaleRecipientMethod
    """Constructor-initialized instance of
    :class:`SetPrimarySaleRecipientMethod`.
    """

    set_royalty_info_for_token: SetRoyaltyInfoForTokenMethod
    """Constructor-initialized instance of
    :class:`SetRoyaltyInfoForTokenMethod`.
    """

    set_wallet_claim_count: SetWalletClaimCountMethod
    """Constructor-initialized instance of
    :class:`SetWalletClaimCountMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    symbol: SymbolMethod
    """Constructor-initialized instance of
    :class:`SymbolMethod`.
    """

    total_supply: TotalSupplyMethod
    """Constructor-initialized instance of
    :class:`TotalSupplyMethod`.
    """

    uri: UriMethod
    """Constructor-initialized instance of
    :class:`UriMethod`.
    """

    verify_claim: VerifyClaimMethod
    """Constructor-initialized instance of
    :class:`VerifyClaimMethod`.
    """

    verify_claim_merkle_proof: VerifyClaimMerkleProofMethod
    """Constructor-initialized instance of
    :class:`VerifyClaimMerkleProofMethod`.
    """

    wallet_claim_count: WalletClaimCountMethod
    """Constructor-initialized instance of
    :class:`WalletClaimCountMethod`.
    """


    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: DropERC1155Validator = None,
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
            validator = DropERC1155Validator(web3_or_provider, contract_address)

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

        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=DropERC1155.abi()).functions

        self.default_admin_role = DefaultAdminRoleMethod(web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE)

        self.balance_of = BalanceOfMethod(web3_or_provider, contract_address, functions.balanceOf, validator)

        self.balance_of_batch = BalanceOfBatchMethod(web3_or_provider, contract_address, functions.balanceOfBatch, validator)

        self.burn = BurnMethod(web3_or_provider, contract_address, functions.burn, validator)

        self.burn_batch = BurnBatchMethod(web3_or_provider, contract_address, functions.burnBatch, validator)

        self.claim = ClaimMethod(web3_or_provider, contract_address, functions.claim, validator)

        self.claim_condition = ClaimConditionMethod(web3_or_provider, contract_address, functions.claimCondition, validator)

        self.contract_type = ContractTypeMethod(web3_or_provider, contract_address, functions.contractType)

        self.contract_uri = ContractUriMethod(web3_or_provider, contract_address, functions.contractURI)

        self.contract_version = ContractVersionMethod(web3_or_provider, contract_address, functions.contractVersion)

        self.get_active_claim_condition_id = GetActiveClaimConditionIdMethod(web3_or_provider, contract_address, functions.getActiveClaimConditionId, validator)

        self.get_claim_condition_by_id = GetClaimConditionByIdMethod(web3_or_provider, contract_address, functions.getClaimConditionById, validator)

        self.get_claim_timestamp = GetClaimTimestampMethod(web3_or_provider, contract_address, functions.getClaimTimestamp, validator)

        self.get_default_royalty_info = GetDefaultRoyaltyInfoMethod(web3_or_provider, contract_address, functions.getDefaultRoyaltyInfo)

        self.get_platform_fee_info = GetPlatformFeeInfoMethod(web3_or_provider, contract_address, functions.getPlatformFeeInfo)

        self.get_role_admin = GetRoleAdminMethod(web3_or_provider, contract_address, functions.getRoleAdmin, validator)

        self.get_role_member = GetRoleMemberMethod(web3_or_provider, contract_address, functions.getRoleMember, validator)

        self.get_role_member_count = GetRoleMemberCountMethod(web3_or_provider, contract_address, functions.getRoleMemberCount, validator)

        self.get_royalty_info_for_token = GetRoyaltyInfoForTokenMethod(web3_or_provider, contract_address, functions.getRoyaltyInfoForToken, validator)

        self.grant_role = GrantRoleMethod(web3_or_provider, contract_address, functions.grantRole, validator)

        self.has_role = HasRoleMethod(web3_or_provider, contract_address, functions.hasRole, validator)

        self.initialize = InitializeMethod(web3_or_provider, contract_address, functions.initialize, validator)

        self.is_approved_for_all = IsApprovedForAllMethod(web3_or_provider, contract_address, functions.isApprovedForAll, validator)

        self.is_trusted_forwarder = IsTrustedForwarderMethod(web3_or_provider, contract_address, functions.isTrustedForwarder, validator)

        self.lazy_mint = LazyMintMethod(web3_or_provider, contract_address, functions.lazyMint, validator)

        self.max_total_supply = MaxTotalSupplyMethod(web3_or_provider, contract_address, functions.maxTotalSupply, validator)

        self.max_wallet_claim_count = MaxWalletClaimCountMethod(web3_or_provider, contract_address, functions.maxWalletClaimCount, validator)

        self.multicall = MulticallMethod(web3_or_provider, contract_address, functions.multicall, validator)

        self.name = NameMethod(web3_or_provider, contract_address, functions.name)

        self.next_token_id_to_mint = NextTokenIdToMintMethod(web3_or_provider, contract_address, functions.nextTokenIdToMint)

        self.owner = OwnerMethod(web3_or_provider, contract_address, functions.owner)

        self.primary_sale_recipient = PrimarySaleRecipientMethod(web3_or_provider, contract_address, functions.primarySaleRecipient)

        self.renounce_role = RenounceRoleMethod(web3_or_provider, contract_address, functions.renounceRole, validator)

        self.revoke_role = RevokeRoleMethod(web3_or_provider, contract_address, functions.revokeRole, validator)

        self.royalty_info = RoyaltyInfoMethod(web3_or_provider, contract_address, functions.royaltyInfo, validator)

        self.safe_batch_transfer_from = SafeBatchTransferFromMethod(web3_or_provider, contract_address, functions.safeBatchTransferFrom, validator)

        self.safe_transfer_from = SafeTransferFromMethod(web3_or_provider, contract_address, functions.safeTransferFrom, validator)

        self.sale_recipient = SaleRecipientMethod(web3_or_provider, contract_address, functions.saleRecipient, validator)

        self.set_approval_for_all = SetApprovalForAllMethod(web3_or_provider, contract_address, functions.setApprovalForAll, validator)

        self.set_claim_conditions = SetClaimConditionsMethod(web3_or_provider, contract_address, functions.setClaimConditions, validator)

        self.set_contract_uri = SetContractUriMethod(web3_or_provider, contract_address, functions.setContractURI, validator)

        self.set_default_royalty_info = SetDefaultRoyaltyInfoMethod(web3_or_provider, contract_address, functions.setDefaultRoyaltyInfo, validator)

        self.set_max_total_supply = SetMaxTotalSupplyMethod(web3_or_provider, contract_address, functions.setMaxTotalSupply, validator)

        self.set_max_wallet_claim_count = SetMaxWalletClaimCountMethod(web3_or_provider, contract_address, functions.setMaxWalletClaimCount, validator)

        self.set_owner = SetOwnerMethod(web3_or_provider, contract_address, functions.setOwner, validator)

        self.set_platform_fee_info = SetPlatformFeeInfoMethod(web3_or_provider, contract_address, functions.setPlatformFeeInfo, validator)

        self.set_primary_sale_recipient = SetPrimarySaleRecipientMethod(web3_or_provider, contract_address, functions.setPrimarySaleRecipient, validator)

        self.set_royalty_info_for_token = SetRoyaltyInfoForTokenMethod(web3_or_provider, contract_address, functions.setRoyaltyInfoForToken, validator)

        self.set_wallet_claim_count = SetWalletClaimCountMethod(web3_or_provider, contract_address, functions.setWalletClaimCount, validator)

        self.supports_interface = SupportsInterfaceMethod(web3_or_provider, contract_address, functions.supportsInterface, validator)

        self.symbol = SymbolMethod(web3_or_provider, contract_address, functions.symbol)

        self.total_supply = TotalSupplyMethod(web3_or_provider, contract_address, functions.totalSupply, validator)

        self.uri = UriMethod(web3_or_provider, contract_address, functions.uri, validator)

        self.verify_claim = VerifyClaimMethod(web3_or_provider, contract_address, functions.verifyClaim, validator)

        self.verify_claim_merkle_proof = VerifyClaimMerkleProofMethod(web3_or_provider, contract_address, functions.verifyClaimMerkleProof, validator)

        self.wallet_claim_count = WalletClaimCountMethod(web3_or_provider, contract_address, functions.walletClaimCount, validator)

    def get_approval_for_all_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ApprovalForAll event.

        :param tx_hash: hash of transaction emitting ApprovalForAll event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.ApprovalForAll().processReceipt(tx_receipt)
    def get_claim_conditions_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ClaimConditionsUpdated event.

        :param tx_hash: hash of transaction emitting ClaimConditionsUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.ClaimConditionsUpdated().processReceipt(tx_receipt)
    def get_default_royalty_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for DefaultRoyalty event.

        :param tx_hash: hash of transaction emitting DefaultRoyalty event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.DefaultRoyalty().processReceipt(tx_receipt)
    def get_max_total_supply_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for MaxTotalSupplyUpdated event.

        :param tx_hash: hash of transaction emitting MaxTotalSupplyUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.MaxTotalSupplyUpdated().processReceipt(tx_receipt)
    def get_max_wallet_claim_count_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for MaxWalletClaimCountUpdated event.

        :param tx_hash: hash of transaction emitting MaxWalletClaimCountUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.MaxWalletClaimCountUpdated().processReceipt(tx_receipt)
    def get_owner_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OwnerUpdated event.

        :param tx_hash: hash of transaction emitting OwnerUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.OwnerUpdated().processReceipt(tx_receipt)
    def get_platform_fee_info_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PlatformFeeInfoUpdated event.

        :param tx_hash: hash of transaction emitting PlatformFeeInfoUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.PlatformFeeInfoUpdated().processReceipt(tx_receipt)
    def get_primary_sale_recipient_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PrimarySaleRecipientUpdated event.

        :param tx_hash: hash of transaction emitting
            PrimarySaleRecipientUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.PrimarySaleRecipientUpdated().processReceipt(tx_receipt)
    def get_role_admin_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleAdminChanged event.

        :param tx_hash: hash of transaction emitting RoleAdminChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.RoleAdminChanged().processReceipt(tx_receipt)
    def get_role_granted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleGranted event.

        :param tx_hash: hash of transaction emitting RoleGranted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.RoleGranted().processReceipt(tx_receipt)
    def get_role_revoked_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleRevoked event.

        :param tx_hash: hash of transaction emitting RoleRevoked event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.RoleRevoked().processReceipt(tx_receipt)
    def get_royalty_for_token_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoyaltyForToken event.

        :param tx_hash: hash of transaction emitting RoyaltyForToken event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.RoyaltyForToken().processReceipt(tx_receipt)
    def get_tokens_claimed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensClaimed event.

        :param tx_hash: hash of transaction emitting TokensClaimed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.TokensClaimed().processReceipt(tx_receipt)
    def get_tokens_lazy_minted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensLazyMinted event.

        :param tx_hash: hash of transaction emitting TokensLazyMinted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.TokensLazyMinted().processReceipt(tx_receipt)
    def get_transfer_batch_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TransferBatch event.

        :param tx_hash: hash of transaction emitting TransferBatch event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.TransferBatch().processReceipt(tx_receipt)
    def get_transfer_single_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TransferSingle event.

        :param tx_hash: hash of transaction emitting TransferSingle event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.TransferSingle().processReceipt(tx_receipt)
    def get_uri_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for URI event.

        :param tx_hash: hash of transaction emitting URI event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.URI().processReceipt(tx_receipt)
    def get_wallet_claim_count_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for WalletClaimCountUpdated event.

        :param tx_hash: hash of transaction emitting WalletClaimCountUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DropERC1155.abi()).events.WalletClaimCountUpdated().processReceipt(tx_receipt)

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_thirdwebFee","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerTransaction","type":"uint256"},{"internalType":"uint256","name":"waitTimeInSecondsBetweenClaims","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"indexed":false,"internalType":"struct IDropClaimCondition.ClaimCondition[]","name":"claimConditions","type":"tuple[]"}],"name":"ClaimConditionsUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"newRoyaltyRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"newRoyaltyBps","type":"uint256"}],"name":"DefaultRoyalty","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"maxTotalSupply","type":"uint256"}],"name":"MaxTotalSupplyUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"count","type":"uint256"}],"name":"MaxWalletClaimCountUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"prevOwner","type":"address"},{"indexed":false,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"platformFeeRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"platformFeeBps","type":"uint256"}],"name":"PlatformFeeInfoUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"recipient","type":"address"}],"name":"PrimarySaleRecipientUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"address","name":"royaltyRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"royaltyBps","type":"uint256"}],"name":"RoyaltyForToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"claimConditionIndex","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"claimer","type":"address"},{"indexed":false,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantityClaimed","type":"uint256"}],"name":"TokensClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"startTokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"endTokenId","type":"uint256"},{"indexed":false,"internalType":"string","name":"baseURI","type":"string"}],"name":"TokensLazyMinted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"wallet","type":"address"},{"indexed":false,"internalType":"uint256","name":"count","type":"uint256"}],"name":"WalletClaimCountUpdated","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"burnBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_receiver","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"},{"internalType":"bytes32[]","name":"_proofs","type":"bytes32[]"},{"internalType":"uint256","name":"_proofMaxQuantityPerTransaction","type":"uint256"}],"name":"claim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"claimCondition","outputs":[{"internalType":"uint256","name":"currentStartId","type":"uint256"},{"internalType":"uint256","name":"count","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractType","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractVersion","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getActiveClaimConditionId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_conditionId","type":"uint256"}],"name":"getClaimConditionById","outputs":[{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerTransaction","type":"uint256"},{"internalType":"uint256","name":"waitTimeInSecondsBetweenClaims","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"internalType":"struct IDropClaimCondition.ClaimCondition","name":"condition","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_conditionId","type":"uint256"},{"internalType":"address","name":"_claimer","type":"address"}],"name":"getClaimTimestamp","outputs":[{"internalType":"uint256","name":"lastClaimTimestamp","type":"uint256"},{"internalType":"uint256","name":"nextValidClaimTimestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getDefaultRoyaltyInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPlatformFeeInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getRoyaltyInfoForToken","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_defaultAdmin","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"string","name":"_contractURI","type":"string"},{"internalType":"address[]","name":"_trustedForwarders","type":"address[]"},{"internalType":"address","name":"_saleRecipient","type":"address"},{"internalType":"address","name":"_royaltyRecipient","type":"address"},{"internalType":"uint128","name":"_royaltyBps","type":"uint128"},{"internalType":"uint128","name":"_platformFeeBps","type":"uint128"},{"internalType":"address","name":"_platformFeeRecipient","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"string","name":"_baseURIForTokens","type":"string"}],"name":"lazyMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"maxTotalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"maxWalletClaimCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextTokenIdToMint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"primarySaleRecipient","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"salePrice","type":"uint256"}],"name":"royaltyInfo","outputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"royaltyAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"saleRecipient","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"components":[{"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"internalType":"uint256","name":"maxClaimableSupply","type":"uint256"},{"internalType":"uint256","name":"supplyClaimed","type":"uint256"},{"internalType":"uint256","name":"quantityLimitPerTransaction","type":"uint256"},{"internalType":"uint256","name":"waitTimeInSecondsBetweenClaims","type":"uint256"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"}],"internalType":"struct IDropClaimCondition.ClaimCondition[]","name":"_phases","type":"tuple[]"},{"internalType":"bool","name":"_resetClaimEligibility","type":"bool"}],"name":"setClaimConditions","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_uri","type":"string"}],"name":"setContractURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_royaltyRecipient","type":"address"},{"internalType":"uint256","name":"_royaltyBps","type":"uint256"}],"name":"setDefaultRoyaltyInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_maxTotalSupply","type":"uint256"}],"name":"setMaxTotalSupply","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_count","type":"uint256"}],"name":"setMaxWalletClaimCount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newOwner","type":"address"}],"name":"setOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_platformFeeRecipient","type":"address"},{"internalType":"uint256","name":"_platformFeeBps","type":"uint256"}],"name":"setPlatformFeeInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_saleRecipient","type":"address"}],"name":"setPrimarySaleRecipient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_bps","type":"uint256"}],"name":"setRoyaltyInfoForToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"address","name":"_claimer","type":"address"},{"internalType":"uint256","name":"_count","type":"uint256"}],"name":"setWalletClaimCount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"uri","outputs":[{"internalType":"string","name":"_tokenURI","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_conditionId","type":"uint256"},{"internalType":"address","name":"_claimer","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"},{"internalType":"bool","name":"verifyMaxQuantityPerTransaction","type":"bool"}],"name":"verifyClaim","outputs":[],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_conditionId","type":"uint256"},{"internalType":"address","name":"_claimer","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"bytes32[]","name":"_proofs","type":"bytes32[]"},{"internalType":"uint256","name":"_proofMaxQuantityPerTransaction","type":"uint256"}],"name":"verifyClaimMerkleProof","outputs":[{"internalType":"bool","name":"validMerkleProof","type":"bool"},{"internalType":"uint256","name":"merkleProofIndex","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"},{"internalType":"address","name":"index_1","type":"address"}],"name":"walletClaimCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
