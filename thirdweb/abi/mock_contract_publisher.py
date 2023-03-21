"""Generated wrapper for MockContractPublisher Solidity contract."""

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
# constructor for MockContractPublisher below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        MockContractPublisherValidator,
    )
except ImportError:

    class MockContractPublisherValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IContractPublisherCustomContractInstance(TypedDict):
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

    contractId: str

    publishTimestamp: int

    publishMetadataUri: str

    bytecodeHash: Union[bytes, str]

    implementation: str


class GetAllPublishedContractsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllPublishedContracts method."""

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
        """Validate the inputs to the getAllPublishedContracts method."""
        self.validator.assert_valid(
            method_name="getAllPublishedContracts",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return index_0

    def call(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> List[IContractPublisherCustomContractInstance]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return [
            IContractPublisherCustomContractInstance(
                contractId=element[0],
                publishTimestamp=element[1],
                publishMetadataUri=element[2],
                bytecodeHash=element[3],
                implementation=element[4],
            )
            for element in returned
        ]

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


class GetPublishedContractMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getPublishedContract method."""

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

    def validate_and_normalize_inputs(self, index_0: str, index_1: str):
        """Validate the inputs to the getPublishedContract method."""
        self.validator.assert_valid(
            method_name="getPublishedContract",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="getPublishedContract",
            parameter_name="index_1",
            argument_value=index_1,
        )
        return (index_0, index_1)

    def call(
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
    ) -> IContractPublisherCustomContractInstance:
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
        return IContractPublisherCustomContractInstance(
            contractId=returned[0],
            publishTimestamp=returned[1],
            publishMetadataUri=returned[2],
            bytecodeHash=returned[3],
            implementation=returned[4],
        )

    def send_transaction(
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
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
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
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
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


class GetPublishedContractVersionsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getPublishedContractVersions method."""

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

    def validate_and_normalize_inputs(self, index_0: str, index_1: str):
        """Validate the inputs to the getPublishedContractVersions method."""
        self.validator.assert_valid(
            method_name="getPublishedContractVersions",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="getPublishedContractVersions",
            parameter_name="index_1",
            argument_value=index_1,
        )
        return (index_0, index_1)

    def call(
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
    ) -> List[IContractPublisherCustomContractInstance]:
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
        return [
            IContractPublisherCustomContractInstance(
                contractId=element[0],
                publishTimestamp=element[1],
                publishMetadataUri=element[2],
                bytecodeHash=element[3],
                implementation=element[4],
            )
            for element in returned
        ]

    def send_transaction(
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
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
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
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
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


class GetPublishedUriFromCompilerUriMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getPublishedUriFromCompilerUri method."""

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
        """Validate the inputs to the getPublishedUriFromCompilerUri method."""
        self.validator.assert_valid(
            method_name="getPublishedUriFromCompilerUri",
            parameter_name="index_0",
            argument_value=index_0,
        )
        return index_0

    def call(
        self, index_0: str, tx_params: Optional[TxParams] = None
    ) -> List[str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return [str(element) for element in returned]

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


class GetPublisherProfileUriMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getPublisherProfileUri method."""

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
        """Validate the inputs to the getPublisherProfileUri method."""
        self.validator.assert_valid(
            method_name="getPublisherProfileUri",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return index_0

    def call(self, index_0: str, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return str(returned)

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


class PublishContractMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the publishContract method."""

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
        publisher: str,
        contract_id: str,
        publish_metadata_uri: str,
        compiler_metadata_uri: str,
        bytecode_hash: Union[bytes, str],
        implementation: str,
    ):
        """Validate the inputs to the publishContract method."""
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="contractId",
            argument_value=contract_id,
        )
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="publishMetadataUri",
            argument_value=publish_metadata_uri,
        )
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="compilerMetadataUri",
            argument_value=compiler_metadata_uri,
        )
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="bytecodeHash",
            argument_value=bytecode_hash,
        )
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="implementation",
            argument_value=implementation,
        )
        implementation = self.validate_and_checksum_address(implementation)
        return (
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        )

    def call(
        self,
        publisher: str,
        contract_id: str,
        publish_metadata_uri: str,
        compiler_metadata_uri: str,
        bytecode_hash: Union[bytes, str],
        implementation: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        ) = self.validate_and_normalize_inputs(
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        publisher: str,
        contract_id: str,
        publish_metadata_uri: str,
        compiler_metadata_uri: str,
        bytecode_hash: Union[bytes, str],
        implementation: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        ) = self.validate_and_normalize_inputs(
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        publisher: str,
        contract_id: str,
        publish_metadata_uri: str,
        compiler_metadata_uri: str,
        bytecode_hash: Union[bytes, str],
        implementation: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        ) = self.validate_and_normalize_inputs(
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        publisher: str,
        contract_id: str,
        publish_metadata_uri: str,
        compiler_metadata_uri: str,
        bytecode_hash: Union[bytes, str],
        implementation: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        ) = self.validate_and_normalize_inputs(
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            publisher,
            contract_id,
            publish_metadata_uri,
            compiler_metadata_uri,
            bytecode_hash,
            implementation,
        ).estimateGas(tx_params.as_dict())


class SetPublisherProfileUriMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setPublisherProfileUri method."""

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

    def validate_and_normalize_inputs(self, index_0: str, index_1: str):
        """Validate the inputs to the setPublisherProfileUri method."""
        self.validator.assert_valid(
            method_name="setPublisherProfileUri",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="setPublisherProfileUri",
            parameter_name="index_1",
            argument_value=index_1,
        )
        return (index_0, index_1)

    def call(
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(index_0, index_1).call(tx_params.as_dict())

    def send_transaction(
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
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
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
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
        self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


class UnpublishContractMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the unpublishContract method."""

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

    def validate_and_normalize_inputs(self, publisher: str, contract_id: str):
        """Validate the inputs to the unpublishContract method."""
        self.validator.assert_valid(
            method_name="unpublishContract",
            parameter_name="publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        self.validator.assert_valid(
            method_name="unpublishContract",
            parameter_name="contractId",
            argument_value=contract_id,
        )
        return (publisher, contract_id)

    def call(
        self,
        publisher: str,
        contract_id: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (publisher, contract_id) = self.validate_and_normalize_inputs(
            publisher, contract_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(publisher, contract_id).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        publisher: str,
        contract_id: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (publisher, contract_id) = self.validate_and_normalize_inputs(
            publisher, contract_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher, contract_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        publisher: str,
        contract_id: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (publisher, contract_id) = self.validate_and_normalize_inputs(
            publisher, contract_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            publisher, contract_id
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        publisher: str,
        contract_id: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (publisher, contract_id) = self.validate_and_normalize_inputs(
            publisher, contract_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher, contract_id).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class MockContractPublisher:
    """Wrapper class for MockContractPublisher Solidity contract."""

    get_all_published_contracts: GetAllPublishedContractsMethod
    """Constructor-initialized instance of
    :class:`GetAllPublishedContractsMethod`.
    """

    get_published_contract: GetPublishedContractMethod
    """Constructor-initialized instance of
    :class:`GetPublishedContractMethod`.
    """

    get_published_contract_versions: GetPublishedContractVersionsMethod
    """Constructor-initialized instance of
    :class:`GetPublishedContractVersionsMethod`.
    """

    get_published_uri_from_compiler_uri: GetPublishedUriFromCompilerUriMethod
    """Constructor-initialized instance of
    :class:`GetPublishedUriFromCompilerUriMethod`.
    """

    get_publisher_profile_uri: GetPublisherProfileUriMethod
    """Constructor-initialized instance of
    :class:`GetPublisherProfileUriMethod`.
    """

    publish_contract: PublishContractMethod
    """Constructor-initialized instance of
    :class:`PublishContractMethod`.
    """

    set_publisher_profile_uri: SetPublisherProfileUriMethod
    """Constructor-initialized instance of
    :class:`SetPublisherProfileUriMethod`.
    """

    unpublish_contract: UnpublishContractMethod
    """Constructor-initialized instance of
    :class:`UnpublishContractMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: MockContractPublisherValidator = None,
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
            validator = MockContractPublisherValidator(
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
            abi=MockContractPublisher.abi(),
        ).functions

        self.get_all_published_contracts = GetAllPublishedContractsMethod(
            web3_or_provider,
            contract_address,
            functions.getAllPublishedContracts,
            validator,
        )

        self.get_published_contract = GetPublishedContractMethod(
            web3_or_provider,
            contract_address,
            functions.getPublishedContract,
            validator,
        )

        self.get_published_contract_versions = (
            GetPublishedContractVersionsMethod(
                web3_or_provider,
                contract_address,
                functions.getPublishedContractVersions,
                validator,
            )
        )

        self.get_published_uri_from_compiler_uri = (
            GetPublishedUriFromCompilerUriMethod(
                web3_or_provider,
                contract_address,
                functions.getPublishedUriFromCompilerUri,
                validator,
            )
        )

        self.get_publisher_profile_uri = GetPublisherProfileUriMethod(
            web3_or_provider,
            contract_address,
            functions.getPublisherProfileUri,
            validator,
        )

        self.publish_contract = PublishContractMethod(
            web3_or_provider,
            contract_address,
            functions.publishContract,
            validator,
        )

        self.set_publisher_profile_uri = SetPublisherProfileUriMethod(
            web3_or_provider,
            contract_address,
            functions.setPublisherProfileUri,
            validator,
        )

        self.unpublish_contract = UnpublishContractMethod(
            web3_or_provider,
            contract_address,
            functions.unpublishContract,
            validator,
        )

    def get_contract_published_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ContractPublished event.

        :param tx_hash: hash of transaction emitting ContractPublished event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=MockContractPublisher.abi(),
            )
            .events.ContractPublished()
            .processReceipt(tx_receipt)
        )

    def get_contract_unpublished_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ContractUnpublished event.

        :param tx_hash: hash of transaction emitting ContractUnpublished event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=MockContractPublisher.abi(),
            )
            .events.ContractUnpublished()
            .processReceipt(tx_receipt)
        )

    def get_paused_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Paused event.

        :param tx_hash: hash of transaction emitting Paused event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=MockContractPublisher.abi(),
            )
            .events.Paused()
            .processReceipt(tx_receipt)
        )

    def get_publisher_profile_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PublisherProfileUpdated event.

        :param tx_hash: hash of transaction emitting PublisherProfileUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=MockContractPublisher.abi(),
            )
            .events.PublisherProfileUpdated()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"publisher","type":"address"},{"components":[{"internalType":"string","name":"contractId","type":"string"},{"internalType":"uint256","name":"publishTimestamp","type":"uint256"},{"internalType":"string","name":"publishMetadataUri","type":"string"},{"internalType":"bytes32","name":"bytecodeHash","type":"bytes32"},{"internalType":"address","name":"implementation","type":"address"}],"indexed":false,"internalType":"struct IContractPublisher.CustomContractInstance","name":"publishedContract","type":"tuple"}],"name":"ContractPublished","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"publisher","type":"address"},{"indexed":true,"internalType":"string","name":"contractId","type":"string"}],"name":"ContractUnpublished","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"isPaused","type":"bool"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"publisher","type":"address"},{"indexed":false,"internalType":"string","name":"prevURI","type":"string"},{"indexed":false,"internalType":"string","name":"newURI","type":"string"}],"name":"PublisherProfileUpdated","type":"event"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"getAllPublishedContracts","outputs":[{"components":[{"internalType":"string","name":"contractId","type":"string"},{"internalType":"uint256","name":"publishTimestamp","type":"uint256"},{"internalType":"string","name":"publishMetadataUri","type":"string"},{"internalType":"bytes32","name":"bytecodeHash","type":"bytes32"},{"internalType":"address","name":"implementation","type":"address"}],"internalType":"struct IContractPublisher.CustomContractInstance[]","name":"published","type":"tuple[]"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"string","name":"index_1","type":"string"}],"name":"getPublishedContract","outputs":[{"components":[{"internalType":"string","name":"contractId","type":"string"},{"internalType":"uint256","name":"publishTimestamp","type":"uint256"},{"internalType":"string","name":"publishMetadataUri","type":"string"},{"internalType":"bytes32","name":"bytecodeHash","type":"bytes32"},{"internalType":"address","name":"implementation","type":"address"}],"internalType":"struct IContractPublisher.CustomContractInstance","name":"published","type":"tuple"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"string","name":"index_1","type":"string"}],"name":"getPublishedContractVersions","outputs":[{"components":[{"internalType":"string","name":"contractId","type":"string"},{"internalType":"uint256","name":"publishTimestamp","type":"uint256"},{"internalType":"string","name":"publishMetadataUri","type":"string"},{"internalType":"bytes32","name":"bytecodeHash","type":"bytes32"},{"internalType":"address","name":"implementation","type":"address"}],"internalType":"struct IContractPublisher.CustomContractInstance[]","name":"published","type":"tuple[]"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"string","name":"index_0","type":"string"}],"name":"getPublishedUriFromCompilerUri","outputs":[{"internalType":"string[]","name":"publishedMetadataUris","type":"string[]"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"getPublisherProfileUri","outputs":[{"internalType":"string","name":"uri","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"publisher","type":"address"},{"internalType":"string","name":"contractId","type":"string"},{"internalType":"string","name":"publishMetadataUri","type":"string"},{"internalType":"string","name":"compilerMetadataUri","type":"string"},{"internalType":"bytes32","name":"bytecodeHash","type":"bytes32"},{"internalType":"address","name":"implementation","type":"address"}],"name":"publishContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"string","name":"index_1","type":"string"}],"name":"setPublisherProfileUri","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"publisher","type":"address"},{"internalType":"string","name":"contractId","type":"string"}],"name":"unpublishContract","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
