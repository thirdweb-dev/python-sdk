"""Generated wrapper for IOperatorFilterRegistry Solidity contract."""

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
# constructor for IOperatorFilterRegistry below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IOperatorFilterRegistryValidator,
    )
except ImportError:

    class IOperatorFilterRegistryValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class CodeHashOfMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the codeHashOf method."""

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

    def validate_and_normalize_inputs(self, addr: str):
        """Validate the inputs to the codeHashOf method."""
        self.validator.assert_valid(
            method_name="codeHashOf",
            parameter_name="addr",
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        return addr

    def call(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(addr).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).transact(tx_params.as_dict())

    def build_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).estimateGas(tx_params.as_dict())


class CopyEntriesOfMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the copyEntriesOf method."""

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
        self, registrant: str, registrant_to_copy: str
    ):
        """Validate the inputs to the copyEntriesOf method."""
        self.validator.assert_valid(
            method_name="copyEntriesOf",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="copyEntriesOf",
            parameter_name="registrantToCopy",
            argument_value=registrant_to_copy,
        )
        registrant_to_copy = self.validate_and_checksum_address(
            registrant_to_copy
        )
        return (registrant, registrant_to_copy)

    def call(
        self,
        registrant: str,
        registrant_to_copy: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, registrant_to_copy) = self.validate_and_normalize_inputs(
            registrant, registrant_to_copy
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(registrant, registrant_to_copy).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        registrant: str,
        registrant_to_copy: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, registrant_to_copy) = self.validate_and_normalize_inputs(
            registrant, registrant_to_copy
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, registrant_to_copy
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        registrant: str,
        registrant_to_copy: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, registrant_to_copy) = self.validate_and_normalize_inputs(
            registrant, registrant_to_copy
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, registrant_to_copy
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        registrant: str,
        registrant_to_copy: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, registrant_to_copy) = self.validate_and_normalize_inputs(
            registrant, registrant_to_copy
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, registrant_to_copy
        ).estimateGas(tx_params.as_dict())


class FilteredCodeHashAtMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the filteredCodeHashAt method."""

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

    def validate_and_normalize_inputs(self, registrant: str, index: int):
        """Validate the inputs to the filteredCodeHashAt method."""
        self.validator.assert_valid(
            method_name="filteredCodeHashAt",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="filteredCodeHashAt",
            parameter_name="index",
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (registrant, index)

    def call(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(registrant, index).call(
            tx_params.as_dict()
        )
        return Union[bytes, str](returned)

    def send_transaction(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, index).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, index).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, index).estimateGas(
            tx_params.as_dict()
        )


class FilteredCodeHashesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the filteredCodeHashes method."""

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

    def validate_and_normalize_inputs(self, addr: str):
        """Validate the inputs to the filteredCodeHashes method."""
        self.validator.assert_valid(
            method_name="filteredCodeHashes",
            parameter_name="addr",
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        return addr

    def call(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> List[Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(addr).call(tx_params.as_dict())
        return [Union[bytes, str](element) for element in returned]

    def send_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).transact(tx_params.as_dict())

    def build_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).estimateGas(tx_params.as_dict())


class FilteredOperatorAtMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the filteredOperatorAt method."""

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

    def validate_and_normalize_inputs(self, registrant: str, index: int):
        """Validate the inputs to the filteredOperatorAt method."""
        self.validator.assert_valid(
            method_name="filteredOperatorAt",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="filteredOperatorAt",
            parameter_name="index",
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (registrant, index)

    def call(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(registrant, index).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, index).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, index).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, index).estimateGas(
            tx_params.as_dict()
        )


class FilteredOperatorsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the filteredOperators method."""

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

    def validate_and_normalize_inputs(self, addr: str):
        """Validate the inputs to the filteredOperators method."""
        self.validator.assert_valid(
            method_name="filteredOperators",
            parameter_name="addr",
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        return addr

    def call(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> List[str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(addr).call(tx_params.as_dict())
        return [str(element) for element in returned]

    def send_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).transact(tx_params.as_dict())

    def build_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).estimateGas(tx_params.as_dict())


class IsCodeHashFilteredMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isCodeHashFiltered method."""

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
        self, registrant: str, code_hash: Union[bytes, str]
    ):
        """Validate the inputs to the isCodeHashFiltered method."""
        self.validator.assert_valid(
            method_name="isCodeHashFiltered",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="isCodeHashFiltered",
            parameter_name="codeHash",
            argument_value=code_hash,
        )
        return (registrant, code_hash)

    def call(
        self,
        registrant: str,
        code_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, code_hash) = self.validate_and_normalize_inputs(
            registrant, code_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(registrant, code_hash).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        registrant: str,
        code_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, code_hash) = self.validate_and_normalize_inputs(
            registrant, code_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, code_hash).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        registrant: str,
        code_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, code_hash) = self.validate_and_normalize_inputs(
            registrant, code_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, code_hash).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        registrant: str,
        code_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, code_hash) = self.validate_and_normalize_inputs(
            registrant, code_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, code_hash).estimateGas(
            tx_params.as_dict()
        )


class IsCodeHashOfFilteredMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the isCodeHashOfFiltered method."""

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
        self, registrant: str, operator_with_code: str
    ):
        """Validate the inputs to the isCodeHashOfFiltered method."""
        self.validator.assert_valid(
            method_name="isCodeHashOfFiltered",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="isCodeHashOfFiltered",
            parameter_name="operatorWithCode",
            argument_value=operator_with_code,
        )
        operator_with_code = self.validate_and_checksum_address(
            operator_with_code
        )
        return (registrant, operator_with_code)

    def call(
        self,
        registrant: str,
        operator_with_code: str,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, operator_with_code) = self.validate_and_normalize_inputs(
            registrant, operator_with_code
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            registrant, operator_with_code
        ).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self,
        registrant: str,
        operator_with_code: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, operator_with_code) = self.validate_and_normalize_inputs(
            registrant, operator_with_code
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, operator_with_code
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        registrant: str,
        operator_with_code: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, operator_with_code) = self.validate_and_normalize_inputs(
            registrant, operator_with_code
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, operator_with_code
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        registrant: str,
        operator_with_code: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, operator_with_code) = self.validate_and_normalize_inputs(
            registrant, operator_with_code
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, operator_with_code
        ).estimateGas(tx_params.as_dict())


class IsOperatorAllowedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isOperatorAllowed method."""

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

    def validate_and_normalize_inputs(self, registrant: str, operator: str):
        """Validate the inputs to the isOperatorAllowed method."""
        self.validator.assert_valid(
            method_name="isOperatorAllowed",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="isOperatorAllowed",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return (registrant, operator)

    def call(
        self,
        registrant: str,
        operator: str,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, operator) = self.validate_and_normalize_inputs(
            registrant, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(registrant, operator).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        registrant: str,
        operator: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, operator) = self.validate_and_normalize_inputs(
            registrant, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, operator).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        registrant: str,
        operator: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, operator) = self.validate_and_normalize_inputs(
            registrant, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, operator).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        registrant: str,
        operator: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, operator) = self.validate_and_normalize_inputs(
            registrant, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, operator).estimateGas(
            tx_params.as_dict()
        )


class IsOperatorFilteredMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isOperatorFiltered method."""

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

    def validate_and_normalize_inputs(self, registrant: str, operator: str):
        """Validate the inputs to the isOperatorFiltered method."""
        self.validator.assert_valid(
            method_name="isOperatorFiltered",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="isOperatorFiltered",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        return (registrant, operator)

    def call(
        self,
        registrant: str,
        operator: str,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, operator) = self.validate_and_normalize_inputs(
            registrant, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(registrant, operator).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        registrant: str,
        operator: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, operator) = self.validate_and_normalize_inputs(
            registrant, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, operator).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        registrant: str,
        operator: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, operator) = self.validate_and_normalize_inputs(
            registrant, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, operator).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        registrant: str,
        operator: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, operator) = self.validate_and_normalize_inputs(
            registrant, operator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, operator).estimateGas(
            tx_params.as_dict()
        )


class IsRegisteredMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isRegistered method."""

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

    def validate_and_normalize_inputs(self, addr: str):
        """Validate the inputs to the isRegistered method."""
        self.validator.assert_valid(
            method_name="isRegistered",
            parameter_name="addr",
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        return addr

    def call(self, addr: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(addr).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).transact(tx_params.as_dict())

    def build_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).estimateGas(tx_params.as_dict())


class RegisterMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the register method."""

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

    def validate_and_normalize_inputs(self, registrant: str):
        """Validate the inputs to the register method."""
        self.validator.assert_valid(
            method_name="register",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        return registrant

    def call(
        self, registrant: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant) = self.validate_and_normalize_inputs(registrant)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(registrant).call(tx_params.as_dict())

    def send_transaction(
        self, registrant: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant) = self.validate_and_normalize_inputs(registrant)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, registrant: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant) = self.validate_and_normalize_inputs(registrant)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, registrant: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant) = self.validate_and_normalize_inputs(registrant)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant).estimateGas(
            tx_params.as_dict()
        )


class RegisterAndCopyEntriesMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the registerAndCopyEntries method."""

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
        self, registrant: str, registrant_to_copy: str
    ):
        """Validate the inputs to the registerAndCopyEntries method."""
        self.validator.assert_valid(
            method_name="registerAndCopyEntries",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="registerAndCopyEntries",
            parameter_name="registrantToCopy",
            argument_value=registrant_to_copy,
        )
        registrant_to_copy = self.validate_and_checksum_address(
            registrant_to_copy
        )
        return (registrant, registrant_to_copy)

    def call(
        self,
        registrant: str,
        registrant_to_copy: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, registrant_to_copy) = self.validate_and_normalize_inputs(
            registrant, registrant_to_copy
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(registrant, registrant_to_copy).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        registrant: str,
        registrant_to_copy: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, registrant_to_copy) = self.validate_and_normalize_inputs(
            registrant, registrant_to_copy
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, registrant_to_copy
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        registrant: str,
        registrant_to_copy: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, registrant_to_copy) = self.validate_and_normalize_inputs(
            registrant, registrant_to_copy
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, registrant_to_copy
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        registrant: str,
        registrant_to_copy: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, registrant_to_copy) = self.validate_and_normalize_inputs(
            registrant, registrant_to_copy
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, registrant_to_copy
        ).estimateGas(tx_params.as_dict())


class RegisterAndSubscribeMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the registerAndSubscribe method."""

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
        self, registrant: str, subscription: str
    ):
        """Validate the inputs to the registerAndSubscribe method."""
        self.validator.assert_valid(
            method_name="registerAndSubscribe",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="registerAndSubscribe",
            parameter_name="subscription",
            argument_value=subscription,
        )
        subscription = self.validate_and_checksum_address(subscription)
        return (registrant, subscription)

    def call(
        self,
        registrant: str,
        subscription: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, subscription) = self.validate_and_normalize_inputs(
            registrant, subscription
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(registrant, subscription).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        registrant: str,
        subscription: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, subscription) = self.validate_and_normalize_inputs(
            registrant, subscription
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, subscription).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        registrant: str,
        subscription: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, subscription) = self.validate_and_normalize_inputs(
            registrant, subscription
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, subscription
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        registrant: str,
        subscription: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, subscription) = self.validate_and_normalize_inputs(
            registrant, subscription
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, subscription).estimateGas(
            tx_params.as_dict()
        )


class SubscribeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the subscribe method."""

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
        self, registrant: str, registrant_to_subscribe: str
    ):
        """Validate the inputs to the subscribe method."""
        self.validator.assert_valid(
            method_name="subscribe",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="subscribe",
            parameter_name="registrantToSubscribe",
            argument_value=registrant_to_subscribe,
        )
        registrant_to_subscribe = self.validate_and_checksum_address(
            registrant_to_subscribe
        )
        return (registrant, registrant_to_subscribe)

    def call(
        self,
        registrant: str,
        registrant_to_subscribe: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            registrant,
            registrant_to_subscribe,
        ) = self.validate_and_normalize_inputs(
            registrant, registrant_to_subscribe
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(registrant, registrant_to_subscribe).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        registrant: str,
        registrant_to_subscribe: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            registrant,
            registrant_to_subscribe,
        ) = self.validate_and_normalize_inputs(
            registrant, registrant_to_subscribe
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, registrant_to_subscribe
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        registrant: str,
        registrant_to_subscribe: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            registrant,
            registrant_to_subscribe,
        ) = self.validate_and_normalize_inputs(
            registrant, registrant_to_subscribe
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, registrant_to_subscribe
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        registrant: str,
        registrant_to_subscribe: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            registrant,
            registrant_to_subscribe,
        ) = self.validate_and_normalize_inputs(
            registrant, registrant_to_subscribe
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, registrant_to_subscribe
        ).estimateGas(tx_params.as_dict())


class SubscriberAtMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the subscriberAt method."""

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

    def validate_and_normalize_inputs(self, registrant: str, index: int):
        """Validate the inputs to the subscriberAt method."""
        self.validator.assert_valid(
            method_name="subscriberAt",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="subscriberAt",
            parameter_name="index",
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (registrant, index)

    def call(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(registrant, index).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, index).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, index).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, registrant: str, index: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, index) = self.validate_and_normalize_inputs(
            registrant, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant, index).estimateGas(
            tx_params.as_dict()
        )


class SubscribersMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the subscribers method."""

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

    def validate_and_normalize_inputs(self, registrant: str):
        """Validate the inputs to the subscribers method."""
        self.validator.assert_valid(
            method_name="subscribers",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        return registrant

    def call(
        self, registrant: str, tx_params: Optional[TxParams] = None
    ) -> List[str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant) = self.validate_and_normalize_inputs(registrant)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(registrant).call(
            tx_params.as_dict()
        )
        return [str(element) for element in returned]

    def send_transaction(
        self, registrant: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant) = self.validate_and_normalize_inputs(registrant)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, registrant: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant) = self.validate_and_normalize_inputs(registrant)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, registrant: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant) = self.validate_and_normalize_inputs(registrant)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(registrant).estimateGas(
            tx_params.as_dict()
        )


class SubscriptionOfMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the subscriptionOf method."""

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

    def validate_and_normalize_inputs(self, addr: str):
        """Validate the inputs to the subscriptionOf method."""
        self.validator.assert_valid(
            method_name="subscriptionOf",
            parameter_name="addr",
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        return addr

    def call(self, addr: str, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(addr).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).transact(tx_params.as_dict())

    def build_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).estimateGas(tx_params.as_dict())


class UnregisterMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the unregister method."""

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

    def validate_and_normalize_inputs(self, addr: str):
        """Validate the inputs to the unregister method."""
        self.validator.assert_valid(
            method_name="unregister",
            parameter_name="addr",
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        return addr

    def call(self, addr: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(addr).call(tx_params.as_dict())

    def send_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).transact(tx_params.as_dict())

    def build_transaction(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, addr: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).estimateGas(tx_params.as_dict())


class UnsubscribeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the unsubscribe method."""

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
        self, registrant: str, copy_existing_entries: bool
    ):
        """Validate the inputs to the unsubscribe method."""
        self.validator.assert_valid(
            method_name="unsubscribe",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="unsubscribe",
            parameter_name="copyExistingEntries",
            argument_value=copy_existing_entries,
        )
        return (registrant, copy_existing_entries)

    def call(
        self,
        registrant: str,
        copy_existing_entries: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            registrant,
            copy_existing_entries,
        ) = self.validate_and_normalize_inputs(
            registrant, copy_existing_entries
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(registrant, copy_existing_entries).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        registrant: str,
        copy_existing_entries: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            registrant,
            copy_existing_entries,
        ) = self.validate_and_normalize_inputs(
            registrant, copy_existing_entries
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, copy_existing_entries
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        registrant: str,
        copy_existing_entries: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            registrant,
            copy_existing_entries,
        ) = self.validate_and_normalize_inputs(
            registrant, copy_existing_entries
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, copy_existing_entries
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        registrant: str,
        copy_existing_entries: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            registrant,
            copy_existing_entries,
        ) = self.validate_and_normalize_inputs(
            registrant, copy_existing_entries
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, copy_existing_entries
        ).estimateGas(tx_params.as_dict())


class UpdateCodeHashMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the updateCodeHash method."""

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
        self, registrant: str, codehash: Union[bytes, str], filtered: bool
    ):
        """Validate the inputs to the updateCodeHash method."""
        self.validator.assert_valid(
            method_name="updateCodeHash",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="updateCodeHash",
            parameter_name="codehash",
            argument_value=codehash,
        )
        self.validator.assert_valid(
            method_name="updateCodeHash",
            parameter_name="filtered",
            argument_value=filtered,
        )
        return (registrant, codehash, filtered)

    def call(
        self,
        registrant: str,
        codehash: Union[bytes, str],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, codehash, filtered) = self.validate_and_normalize_inputs(
            registrant, codehash, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(registrant, codehash, filtered).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        registrant: str,
        codehash: Union[bytes, str],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, codehash, filtered) = self.validate_and_normalize_inputs(
            registrant, codehash, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, codehash, filtered
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        registrant: str,
        codehash: Union[bytes, str],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, codehash, filtered) = self.validate_and_normalize_inputs(
            registrant, codehash, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, codehash, filtered
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        registrant: str,
        codehash: Union[bytes, str],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, codehash, filtered) = self.validate_and_normalize_inputs(
            registrant, codehash, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, codehash, filtered
        ).estimateGas(tx_params.as_dict())


class UpdateCodeHashesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the updateCodeHashes method."""

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
        registrant: str,
        code_hashes: List[Union[bytes, str]],
        filtered: bool,
    ):
        """Validate the inputs to the updateCodeHashes method."""
        self.validator.assert_valid(
            method_name="updateCodeHashes",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="updateCodeHashes",
            parameter_name="codeHashes",
            argument_value=code_hashes,
        )
        self.validator.assert_valid(
            method_name="updateCodeHashes",
            parameter_name="filtered",
            argument_value=filtered,
        )
        return (registrant, code_hashes, filtered)

    def call(
        self,
        registrant: str,
        code_hashes: List[Union[bytes, str]],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            registrant,
            code_hashes,
            filtered,
        ) = self.validate_and_normalize_inputs(
            registrant, code_hashes, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(registrant, code_hashes, filtered).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        registrant: str,
        code_hashes: List[Union[bytes, str]],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            registrant,
            code_hashes,
            filtered,
        ) = self.validate_and_normalize_inputs(
            registrant, code_hashes, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, code_hashes, filtered
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        registrant: str,
        code_hashes: List[Union[bytes, str]],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            registrant,
            code_hashes,
            filtered,
        ) = self.validate_and_normalize_inputs(
            registrant, code_hashes, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, code_hashes, filtered
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        registrant: str,
        code_hashes: List[Union[bytes, str]],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            registrant,
            code_hashes,
            filtered,
        ) = self.validate_and_normalize_inputs(
            registrant, code_hashes, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, code_hashes, filtered
        ).estimateGas(tx_params.as_dict())


class UpdateOperatorMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the updateOperator method."""

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
        self, registrant: str, operator: str, filtered: bool
    ):
        """Validate the inputs to the updateOperator method."""
        self.validator.assert_valid(
            method_name="updateOperator",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="updateOperator",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="updateOperator",
            parameter_name="filtered",
            argument_value=filtered,
        )
        return (registrant, operator, filtered)

    def call(
        self,
        registrant: str,
        operator: str,
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, operator, filtered) = self.validate_and_normalize_inputs(
            registrant, operator, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(registrant, operator, filtered).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        registrant: str,
        operator: str,
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, operator, filtered) = self.validate_and_normalize_inputs(
            registrant, operator, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, operator, filtered
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        registrant: str,
        operator: str,
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, operator, filtered) = self.validate_and_normalize_inputs(
            registrant, operator, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, operator, filtered
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        registrant: str,
        operator: str,
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, operator, filtered) = self.validate_and_normalize_inputs(
            registrant, operator, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, operator, filtered
        ).estimateGas(tx_params.as_dict())


class UpdateOperatorsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the updateOperators method."""

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
        self, registrant: str, operators: List[str], filtered: bool
    ):
        """Validate the inputs to the updateOperators method."""
        self.validator.assert_valid(
            method_name="updateOperators",
            parameter_name="registrant",
            argument_value=registrant,
        )
        registrant = self.validate_and_checksum_address(registrant)
        self.validator.assert_valid(
            method_name="updateOperators",
            parameter_name="operators",
            argument_value=operators,
        )
        self.validator.assert_valid(
            method_name="updateOperators",
            parameter_name="filtered",
            argument_value=filtered,
        )
        return (registrant, operators, filtered)

    def call(
        self,
        registrant: str,
        operators: List[str],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (registrant, operators, filtered) = self.validate_and_normalize_inputs(
            registrant, operators, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(registrant, operators, filtered).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        registrant: str,
        operators: List[str],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (registrant, operators, filtered) = self.validate_and_normalize_inputs(
            registrant, operators, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, operators, filtered
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        registrant: str,
        operators: List[str],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (registrant, operators, filtered) = self.validate_and_normalize_inputs(
            registrant, operators, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, operators, filtered
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        registrant: str,
        operators: List[str],
        filtered: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (registrant, operators, filtered) = self.validate_and_normalize_inputs(
            registrant, operators, filtered
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            registrant, operators, filtered
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IOperatorFilterRegistry:
    """Wrapper class for IOperatorFilterRegistry Solidity contract."""

    code_hash_of: CodeHashOfMethod
    """Constructor-initialized instance of
    :class:`CodeHashOfMethod`.
    """

    copy_entries_of: CopyEntriesOfMethod
    """Constructor-initialized instance of
    :class:`CopyEntriesOfMethod`.
    """

    filtered_code_hash_at: FilteredCodeHashAtMethod
    """Constructor-initialized instance of
    :class:`FilteredCodeHashAtMethod`.
    """

    filtered_code_hashes: FilteredCodeHashesMethod
    """Constructor-initialized instance of
    :class:`FilteredCodeHashesMethod`.
    """

    filtered_operator_at: FilteredOperatorAtMethod
    """Constructor-initialized instance of
    :class:`FilteredOperatorAtMethod`.
    """

    filtered_operators: FilteredOperatorsMethod
    """Constructor-initialized instance of
    :class:`FilteredOperatorsMethod`.
    """

    is_code_hash_filtered: IsCodeHashFilteredMethod
    """Constructor-initialized instance of
    :class:`IsCodeHashFilteredMethod`.
    """

    is_code_hash_of_filtered: IsCodeHashOfFilteredMethod
    """Constructor-initialized instance of
    :class:`IsCodeHashOfFilteredMethod`.
    """

    is_operator_allowed: IsOperatorAllowedMethod
    """Constructor-initialized instance of
    :class:`IsOperatorAllowedMethod`.
    """

    is_operator_filtered: IsOperatorFilteredMethod
    """Constructor-initialized instance of
    :class:`IsOperatorFilteredMethod`.
    """

    is_registered: IsRegisteredMethod
    """Constructor-initialized instance of
    :class:`IsRegisteredMethod`.
    """

    register: RegisterMethod
    """Constructor-initialized instance of
    :class:`RegisterMethod`.
    """

    register_and_copy_entries: RegisterAndCopyEntriesMethod
    """Constructor-initialized instance of
    :class:`RegisterAndCopyEntriesMethod`.
    """

    register_and_subscribe: RegisterAndSubscribeMethod
    """Constructor-initialized instance of
    :class:`RegisterAndSubscribeMethod`.
    """

    subscribe: SubscribeMethod
    """Constructor-initialized instance of
    :class:`SubscribeMethod`.
    """

    subscriber_at: SubscriberAtMethod
    """Constructor-initialized instance of
    :class:`SubscriberAtMethod`.
    """

    subscribers: SubscribersMethod
    """Constructor-initialized instance of
    :class:`SubscribersMethod`.
    """

    subscription_of: SubscriptionOfMethod
    """Constructor-initialized instance of
    :class:`SubscriptionOfMethod`.
    """

    unregister: UnregisterMethod
    """Constructor-initialized instance of
    :class:`UnregisterMethod`.
    """

    unsubscribe: UnsubscribeMethod
    """Constructor-initialized instance of
    :class:`UnsubscribeMethod`.
    """

    update_code_hash: UpdateCodeHashMethod
    """Constructor-initialized instance of
    :class:`UpdateCodeHashMethod`.
    """

    update_code_hashes: UpdateCodeHashesMethod
    """Constructor-initialized instance of
    :class:`UpdateCodeHashesMethod`.
    """

    update_operator: UpdateOperatorMethod
    """Constructor-initialized instance of
    :class:`UpdateOperatorMethod`.
    """

    update_operators: UpdateOperatorsMethod
    """Constructor-initialized instance of
    :class:`UpdateOperatorsMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IOperatorFilterRegistryValidator = None,
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
            validator = IOperatorFilterRegistryValidator(
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
            abi=IOperatorFilterRegistry.abi(),
        ).functions

        self.code_hash_of = CodeHashOfMethod(
            web3_or_provider, contract_address, functions.codeHashOf, validator
        )

        self.copy_entries_of = CopyEntriesOfMethod(
            web3_or_provider,
            contract_address,
            functions.copyEntriesOf,
            validator,
        )

        self.filtered_code_hash_at = FilteredCodeHashAtMethod(
            web3_or_provider,
            contract_address,
            functions.filteredCodeHashAt,
            validator,
        )

        self.filtered_code_hashes = FilteredCodeHashesMethod(
            web3_or_provider,
            contract_address,
            functions.filteredCodeHashes,
            validator,
        )

        self.filtered_operator_at = FilteredOperatorAtMethod(
            web3_or_provider,
            contract_address,
            functions.filteredOperatorAt,
            validator,
        )

        self.filtered_operators = FilteredOperatorsMethod(
            web3_or_provider,
            contract_address,
            functions.filteredOperators,
            validator,
        )

        self.is_code_hash_filtered = IsCodeHashFilteredMethod(
            web3_or_provider,
            contract_address,
            functions.isCodeHashFiltered,
            validator,
        )

        self.is_code_hash_of_filtered = IsCodeHashOfFilteredMethod(
            web3_or_provider,
            contract_address,
            functions.isCodeHashOfFiltered,
            validator,
        )

        self.is_operator_allowed = IsOperatorAllowedMethod(
            web3_or_provider,
            contract_address,
            functions.isOperatorAllowed,
            validator,
        )

        self.is_operator_filtered = IsOperatorFilteredMethod(
            web3_or_provider,
            contract_address,
            functions.isOperatorFiltered,
            validator,
        )

        self.is_registered = IsRegisteredMethod(
            web3_or_provider,
            contract_address,
            functions.isRegistered,
            validator,
        )

        self.register = RegisterMethod(
            web3_or_provider, contract_address, functions.register, validator
        )

        self.register_and_copy_entries = RegisterAndCopyEntriesMethod(
            web3_or_provider,
            contract_address,
            functions.registerAndCopyEntries,
            validator,
        )

        self.register_and_subscribe = RegisterAndSubscribeMethod(
            web3_or_provider,
            contract_address,
            functions.registerAndSubscribe,
            validator,
        )

        self.subscribe = SubscribeMethod(
            web3_or_provider, contract_address, functions.subscribe, validator
        )

        self.subscriber_at = SubscriberAtMethod(
            web3_or_provider,
            contract_address,
            functions.subscriberAt,
            validator,
        )

        self.subscribers = SubscribersMethod(
            web3_or_provider,
            contract_address,
            functions.subscribers,
            validator,
        )

        self.subscription_of = SubscriptionOfMethod(
            web3_or_provider,
            contract_address,
            functions.subscriptionOf,
            validator,
        )

        self.unregister = UnregisterMethod(
            web3_or_provider, contract_address, functions.unregister, validator
        )

        self.unsubscribe = UnsubscribeMethod(
            web3_or_provider,
            contract_address,
            functions.unsubscribe,
            validator,
        )

        self.update_code_hash = UpdateCodeHashMethod(
            web3_or_provider,
            contract_address,
            functions.updateCodeHash,
            validator,
        )

        self.update_code_hashes = UpdateCodeHashesMethod(
            web3_or_provider,
            contract_address,
            functions.updateCodeHashes,
            validator,
        )

        self.update_operator = UpdateOperatorMethod(
            web3_or_provider,
            contract_address,
            functions.updateOperator,
            validator,
        )

        self.update_operators = UpdateOperatorsMethod(
            web3_or_provider,
            contract_address,
            functions.updateOperators,
            validator,
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"codeHashOf","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"address","name":"registrantToCopy","type":"address"}],"name":"copyEntriesOf","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"filteredCodeHashAt","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"filteredCodeHashes","outputs":[{"internalType":"bytes32[]","name":"","type":"bytes32[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"filteredOperatorAt","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"filteredOperators","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"bytes32","name":"codeHash","type":"bytes32"}],"name":"isCodeHashFiltered","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"address","name":"operatorWithCode","type":"address"}],"name":"isCodeHashOfFiltered","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isOperatorAllowed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isOperatorFiltered","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"isRegistered","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"}],"name":"register","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"address","name":"registrantToCopy","type":"address"}],"name":"registerAndCopyEntries","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"address","name":"subscription","type":"address"}],"name":"registerAndSubscribe","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"address","name":"registrantToSubscribe","type":"address"}],"name":"subscribe","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"subscriberAt","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"}],"name":"subscribers","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"subscriptionOf","outputs":[{"internalType":"address","name":"registrant","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"unregister","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"bool","name":"copyExistingEntries","type":"bool"}],"name":"unsubscribe","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"bytes32","name":"codehash","type":"bytes32"},{"internalType":"bool","name":"filtered","type":"bool"}],"name":"updateCodeHash","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"bytes32[]","name":"codeHashes","type":"bytes32[]"},{"internalType":"bool","name":"filtered","type":"bool"}],"name":"updateCodeHashes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"filtered","type":"bool"}],"name":"updateOperator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"registrant","type":"address"},{"internalType":"address[]","name":"operators","type":"address[]"},{"internalType":"bool","name":"filtered","type":"bool"}],"name":"updateOperators","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
