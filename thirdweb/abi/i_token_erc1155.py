"""Generated wrapper for ITokenERC1155 Solidity contract."""

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
# constructor for ITokenERC1155 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ITokenERC1155Validator,
    )
except ImportError:

    class ITokenERC1155Validator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class ITokenERC1155MintRequest(TypedDict):
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

    to: str

    royaltyRecipient: str

    royaltyBps: int

    primarySaleRecipient: str

    tokenId: int

    uri: str

    quantity: int

    pricePerToken: int

    currency: str

    validityStartTimestamp: int

    validityEndTimestamp: int

    uid: Union[bytes, str]


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

class MintToMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the mintTo method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, to: str, token_id: int, uri: str, amount: int):
        """Validate the inputs to the mintTo method."""
        self.validator.assert_valid(
            method_name='mintTo',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='mintTo',
            parameter_name='tokenId',
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name='mintTo',
            parameter_name='uri',
            argument_value=uri,
        )
        self.validator.assert_valid(
            method_name='mintTo',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (to, token_id, uri, amount)

    def call(self, to: str, token_id: int, uri: str, amount: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (to, token_id, uri, amount) = self.validate_and_normalize_inputs(to, token_id, uri, amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(to, token_id, uri, amount).call(tx_params.as_dict())

    def send_transaction(self, to: str, token_id: int, uri: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, token_id, uri, amount) = self.validate_and_normalize_inputs(to, token_id, uri, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, token_id, uri, amount).transact(tx_params.as_dict())

    def build_transaction(self, to: str, token_id: int, uri: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, token_id, uri, amount) = self.validate_and_normalize_inputs(to, token_id, uri, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, token_id, uri, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, to: str, token_id: int, uri: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (to, token_id, uri, amount) = self.validate_and_normalize_inputs(to, token_id, uri, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, token_id, uri, amount).estimateGas(tx_params.as_dict())

class MintWithSignatureMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the mintWithSignature method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, req: ITokenERC1155MintRequest, signature: Union[bytes, str]):
        """Validate the inputs to the mintWithSignature method."""
        self.validator.assert_valid(
            method_name='mintWithSignature',
            parameter_name='req',
            argument_value=req,
        )
        self.validator.assert_valid(
            method_name='mintWithSignature',
            parameter_name='signature',
            argument_value=signature,
        )
        return (req, signature)

    def call(self, req: ITokenERC1155MintRequest, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (req, signature) = self.validate_and_normalize_inputs(req, signature)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(req, signature).call(tx_params.as_dict())

    def send_transaction(self, req: ITokenERC1155MintRequest, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (req, signature) = self.validate_and_normalize_inputs(req, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(req, signature).transact(tx_params.as_dict())

    def build_transaction(self, req: ITokenERC1155MintRequest, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (req, signature) = self.validate_and_normalize_inputs(req, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(req, signature).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, req: ITokenERC1155MintRequest, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (req, signature) = self.validate_and_normalize_inputs(req, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(req, signature).estimateGas(tx_params.as_dict())

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

class VerifyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the verify method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, req: ITokenERC1155MintRequest, signature: Union[bytes, str]):
        """Validate the inputs to the verify method."""
        self.validator.assert_valid(
            method_name='verify',
            parameter_name='req',
            argument_value=req,
        )
        self.validator.assert_valid(
            method_name='verify',
            parameter_name='signature',
            argument_value=signature,
        )
        return (req, signature)

    def call(self, req: ITokenERC1155MintRequest, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Tuple[bool, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (req, signature) = self.validate_and_normalize_inputs(req, signature)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(req, signature).call(tx_params.as_dict())
        return (returned[0],returned[1],)

    def send_transaction(self, req: ITokenERC1155MintRequest, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (req, signature) = self.validate_and_normalize_inputs(req, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(req, signature).transact(tx_params.as_dict())

    def build_transaction(self, req: ITokenERC1155MintRequest, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (req, signature) = self.validate_and_normalize_inputs(req, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(req, signature).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, req: ITokenERC1155MintRequest, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (req, signature) = self.validate_and_normalize_inputs(req, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(req, signature).estimateGas(tx_params.as_dict())

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ITokenERC1155:
    """Wrapper class for ITokenERC1155 Solidity contract.

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

    is_approved_for_all: IsApprovedForAllMethod
    """Constructor-initialized instance of
    :class:`IsApprovedForAllMethod`.
    """

    mint_to: MintToMethod
    """Constructor-initialized instance of
    :class:`MintToMethod`.
    """

    mint_with_signature: MintWithSignatureMethod
    """Constructor-initialized instance of
    :class:`MintWithSignatureMethod`.
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

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    verify: VerifyMethod
    """Constructor-initialized instance of
    :class:`VerifyMethod`.
    """


    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ITokenERC1155Validator = None,
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
            validator = ITokenERC1155Validator(web3_or_provider, contract_address)

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

        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=ITokenERC1155.abi()).functions

        self.balance_of = BalanceOfMethod(web3_or_provider, contract_address, functions.balanceOf, validator)

        self.balance_of_batch = BalanceOfBatchMethod(web3_or_provider, contract_address, functions.balanceOfBatch, validator)

        self.is_approved_for_all = IsApprovedForAllMethod(web3_or_provider, contract_address, functions.isApprovedForAll, validator)

        self.mint_to = MintToMethod(web3_or_provider, contract_address, functions.mintTo, validator)

        self.mint_with_signature = MintWithSignatureMethod(web3_or_provider, contract_address, functions.mintWithSignature, validator)

        self.safe_batch_transfer_from = SafeBatchTransferFromMethod(web3_or_provider, contract_address, functions.safeBatchTransferFrom, validator)

        self.safe_transfer_from = SafeTransferFromMethod(web3_or_provider, contract_address, functions.safeTransferFrom, validator)

        self.set_approval_for_all = SetApprovalForAllMethod(web3_or_provider, contract_address, functions.setApprovalForAll, validator)

        self.supports_interface = SupportsInterfaceMethod(web3_or_provider, contract_address, functions.supportsInterface, validator)

        self.verify = VerifyMethod(web3_or_provider, contract_address, functions.verify, validator)

    def get_approval_for_all_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ApprovalForAll event.

        :param tx_hash: hash of transaction emitting ApprovalForAll event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ITokenERC1155.abi()).events.ApprovalForAll().processReceipt(tx_receipt)
    def get_tokens_minted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensMinted event.

        :param tx_hash: hash of transaction emitting TokensMinted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ITokenERC1155.abi()).events.TokensMinted().processReceipt(tx_receipt)
    def get_tokens_minted_with_signature_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensMintedWithSignature event.

        :param tx_hash: hash of transaction emitting TokensMintedWithSignature
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ITokenERC1155.abi()).events.TokensMintedWithSignature().processReceipt(tx_receipt)
    def get_transfer_batch_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TransferBatch event.

        :param tx_hash: hash of transaction emitting TransferBatch event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ITokenERC1155.abi()).events.TransferBatch().processReceipt(tx_receipt)
    def get_transfer_single_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TransferSingle event.

        :param tx_hash: hash of transaction emitting TransferSingle event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ITokenERC1155.abi()).events.TransferSingle().processReceipt(tx_receipt)
    def get_uri_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for URI event.

        :param tx_hash: hash of transaction emitting URI event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ITokenERC1155.abi()).events.URI().processReceipt(tx_receipt)

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"mintedTo","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenIdMinted","type":"uint256"},{"indexed":false,"internalType":"string","name":"uri","type":"string"},{"indexed":false,"internalType":"uint256","name":"quantityMinted","type":"uint256"}],"name":"TokensMinted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"signer","type":"address"},{"indexed":true,"internalType":"address","name":"mintedTo","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenIdMinted","type":"uint256"},{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"address","name":"royaltyRecipient","type":"address"},{"internalType":"uint256","name":"royaltyBps","type":"uint256"},{"internalType":"address","name":"primarySaleRecipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"uri","type":"string"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint128","name":"validityStartTimestamp","type":"uint128"},{"internalType":"uint128","name":"validityEndTimestamp","type":"uint128"},{"internalType":"bytes32","name":"uid","type":"bytes32"}],"indexed":false,"internalType":"struct ITokenERC1155.MintRequest","name":"mintRequest","type":"tuple"}],"name":"TokensMintedWithSignature","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"uri","type":"string"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mintTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"address","name":"royaltyRecipient","type":"address"},{"internalType":"uint256","name":"royaltyBps","type":"uint256"},{"internalType":"address","name":"primarySaleRecipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"uri","type":"string"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint128","name":"validityStartTimestamp","type":"uint128"},{"internalType":"uint128","name":"validityEndTimestamp","type":"uint128"},{"internalType":"bytes32","name":"uid","type":"bytes32"}],"internalType":"struct ITokenERC1155.MintRequest","name":"req","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"mintWithSignature","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"address","name":"royaltyRecipient","type":"address"},{"internalType":"uint256","name":"royaltyBps","type":"uint256"},{"internalType":"address","name":"primarySaleRecipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"uri","type":"string"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint128","name":"validityStartTimestamp","type":"uint128"},{"internalType":"uint128","name":"validityEndTimestamp","type":"uint128"},{"internalType":"bytes32","name":"uid","type":"bytes32"}],"internalType":"struct ITokenERC1155.MintRequest","name":"req","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"verify","outputs":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"address","name":"signer","type":"address"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
