"""Generated wrapper for ContractPublisher Solidity contract."""

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
# constructor for ContractPublisher below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ContractPublisherValidator,
    )
except ImportError:

    class ContractPublisherValidator(Validator):  # type: ignore
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

    def validate_and_normalize_inputs(self, publisher: str):
        """Validate the inputs to the getAllPublishedContracts method."""
        self.validator.assert_valid(
            method_name="getAllPublishedContracts",
            parameter_name="_publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        return publisher

    def call(
        self, publisher: str, tx_params: Optional[TxParams] = None
    ) -> List[IContractPublisherCustomContractInstance]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (publisher) = self.validate_and_normalize_inputs(publisher)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(publisher).call(tx_params.as_dict())
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
        self, publisher: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (publisher) = self.validate_and_normalize_inputs(publisher)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher).transact(tx_params.as_dict())

    def build_transaction(
        self, publisher: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (publisher) = self.validate_and_normalize_inputs(publisher)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, publisher: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (publisher) = self.validate_and_normalize_inputs(publisher)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher).estimateGas(
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

    def validate_and_normalize_inputs(self, publisher: str, contract_id: str):
        """Validate the inputs to the getPublishedContract method."""
        self.validator.assert_valid(
            method_name="getPublishedContract",
            parameter_name="_publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        self.validator.assert_valid(
            method_name="getPublishedContract",
            parameter_name="_contractId",
            argument_value=contract_id,
        )
        return (publisher, contract_id)

    def call(
        self,
        publisher: str,
        contract_id: str,
        tx_params: Optional[TxParams] = None,
    ) -> IContractPublisherCustomContractInstance:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (publisher, contract_id) = self.validate_and_normalize_inputs(
            publisher, contract_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(publisher, contract_id).call(
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

    def validate_and_normalize_inputs(self, publisher: str, contract_id: str):
        """Validate the inputs to the getPublishedContractVersions method."""
        self.validator.assert_valid(
            method_name="getPublishedContractVersions",
            parameter_name="_publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        self.validator.assert_valid(
            method_name="getPublishedContractVersions",
            parameter_name="_contractId",
            argument_value=contract_id,
        )
        return (publisher, contract_id)

    def call(
        self,
        publisher: str,
        contract_id: str,
        tx_params: Optional[TxParams] = None,
    ) -> List[IContractPublisherCustomContractInstance]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (publisher, contract_id) = self.validate_and_normalize_inputs(
            publisher, contract_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(publisher, contract_id).call(
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

    def validate_and_normalize_inputs(self, compiler_metadata_uri: str):
        """Validate the inputs to the getPublishedUriFromCompilerUri method."""
        self.validator.assert_valid(
            method_name="getPublishedUriFromCompilerUri",
            parameter_name="compilerMetadataUri",
            argument_value=compiler_metadata_uri,
        )
        return compiler_metadata_uri

    def call(
        self, compiler_metadata_uri: str, tx_params: Optional[TxParams] = None
    ) -> List[str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (compiler_metadata_uri) = self.validate_and_normalize_inputs(
            compiler_metadata_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(compiler_metadata_uri).call(
            tx_params.as_dict()
        )
        return [str(element) for element in returned]

    def send_transaction(
        self, compiler_metadata_uri: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (compiler_metadata_uri) = self.validate_and_normalize_inputs(
            compiler_metadata_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(compiler_metadata_uri).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, compiler_metadata_uri: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (compiler_metadata_uri) = self.validate_and_normalize_inputs(
            compiler_metadata_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(compiler_metadata_uri).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, compiler_metadata_uri: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (compiler_metadata_uri) = self.validate_and_normalize_inputs(
            compiler_metadata_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(compiler_metadata_uri).estimateGas(
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

    def validate_and_normalize_inputs(self, publisher: str):
        """Validate the inputs to the getPublisherProfileUri method."""
        self.validator.assert_valid(
            method_name="getPublisherProfileUri",
            parameter_name="publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        return publisher

    def call(
        self, publisher: str, tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (publisher) = self.validate_and_normalize_inputs(publisher)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(publisher).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, publisher: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (publisher) = self.validate_and_normalize_inputs(publisher)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher).transact(tx_params.as_dict())

    def build_transaction(
        self, publisher: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (publisher) = self.validate_and_normalize_inputs(publisher)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, publisher: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (publisher) = self.validate_and_normalize_inputs(publisher)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher).estimateGas(
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


class IsPausedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isPaused method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return bool(returned)

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


class PrevPublisherMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the prevPublisher method."""

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
            parameter_name="_publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="_contractId",
            argument_value=contract_id,
        )
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="_publishMetadataUri",
            argument_value=publish_metadata_uri,
        )
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="_compilerMetadataUri",
            argument_value=compiler_metadata_uri,
        )
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="_bytecodeHash",
            argument_value=bytecode_hash,
        )
        self.validator.assert_valid(
            method_name="publishContract",
            parameter_name="_implementation",
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


class SetPauseMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setPause method."""

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

    def validate_and_normalize_inputs(self, pause: bool):
        """Validate the inputs to the setPause method."""
        self.validator.assert_valid(
            method_name="setPause",
            parameter_name="_pause",
            argument_value=pause,
        )
        return pause

    def call(self, pause: bool, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (pause) = self.validate_and_normalize_inputs(pause)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(pause).call(tx_params.as_dict())

    def send_transaction(
        self, pause: bool, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (pause) = self.validate_and_normalize_inputs(pause)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pause).transact(tx_params.as_dict())

    def build_transaction(
        self, pause: bool, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (pause) = self.validate_and_normalize_inputs(pause)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pause).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, pause: bool, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (pause) = self.validate_and_normalize_inputs(pause)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pause).estimateGas(tx_params.as_dict())


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

    def validate_and_normalize_inputs(self, publisher: str, uri: str):
        """Validate the inputs to the setPublisherProfileUri method."""
        self.validator.assert_valid(
            method_name="setPublisherProfileUri",
            parameter_name="publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        self.validator.assert_valid(
            method_name="setPublisherProfileUri",
            parameter_name="uri",
            argument_value=uri,
        )
        return (publisher, uri)

    def call(
        self, publisher: str, uri: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (publisher, uri) = self.validate_and_normalize_inputs(publisher, uri)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(publisher, uri).call(tx_params.as_dict())

    def send_transaction(
        self, publisher: str, uri: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (publisher, uri) = self.validate_and_normalize_inputs(publisher, uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher, uri).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, publisher: str, uri: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (publisher, uri) = self.validate_and_normalize_inputs(publisher, uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher, uri).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, publisher: str, uri: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (publisher, uri) = self.validate_and_normalize_inputs(publisher, uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(publisher, uri).estimateGas(
            tx_params.as_dict()
        )


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
            parameter_name="_publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        self.validator.assert_valid(
            method_name="unpublishContract",
            parameter_name="_contractId",
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
class ContractPublisher:
    """Wrapper class for ContractPublisher Solidity contract."""

    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

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

    grant_role: GrantRoleMethod
    """Constructor-initialized instance of
    :class:`GrantRoleMethod`.
    """

    has_role: HasRoleMethod
    """Constructor-initialized instance of
    :class:`HasRoleMethod`.
    """

    is_paused: IsPausedMethod
    """Constructor-initialized instance of
    :class:`IsPausedMethod`.
    """

    is_trusted_forwarder: IsTrustedForwarderMethod
    """Constructor-initialized instance of
    :class:`IsTrustedForwarderMethod`.
    """

    multicall: MulticallMethod
    """Constructor-initialized instance of
    :class:`MulticallMethod`.
    """

    prev_publisher: PrevPublisherMethod
    """Constructor-initialized instance of
    :class:`PrevPublisherMethod`.
    """

    publish_contract: PublishContractMethod
    """Constructor-initialized instance of
    :class:`PublishContractMethod`.
    """

    renounce_role: RenounceRoleMethod
    """Constructor-initialized instance of
    :class:`RenounceRoleMethod`.
    """

    revoke_role: RevokeRoleMethod
    """Constructor-initialized instance of
    :class:`RevokeRoleMethod`.
    """

    set_pause: SetPauseMethod
    """Constructor-initialized instance of
    :class:`SetPauseMethod`.
    """

    set_publisher_profile_uri: SetPublisherProfileUriMethod
    """Constructor-initialized instance of
    :class:`SetPublisherProfileUriMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    unpublish_contract: UnpublishContractMethod
    """Constructor-initialized instance of
    :class:`UnpublishContractMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ContractPublisherValidator = None,
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
            validator = ContractPublisherValidator(
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
            abi=ContractPublisher.abi(),
        ).functions

        self.default_admin_role = DefaultAdminRoleMethod(
            web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE
        )

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

        self.grant_role = GrantRoleMethod(
            web3_or_provider, contract_address, functions.grantRole, validator
        )

        self.has_role = HasRoleMethod(
            web3_or_provider, contract_address, functions.hasRole, validator
        )

        self.is_paused = IsPausedMethod(
            web3_or_provider, contract_address, functions.isPaused
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

        self.prev_publisher = PrevPublisherMethod(
            web3_or_provider, contract_address, functions.prevPublisher
        )

        self.publish_contract = PublishContractMethod(
            web3_or_provider,
            contract_address,
            functions.publishContract,
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

        self.set_pause = SetPauseMethod(
            web3_or_provider, contract_address, functions.setPause, validator
        )

        self.set_publisher_profile_uri = SetPublisherProfileUriMethod(
            web3_or_provider,
            contract_address,
            functions.setPublisherProfileUri,
            validator,
        )

        self.supports_interface = SupportsInterfaceMethod(
            web3_or_provider,
            contract_address,
            functions.supportsInterface,
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
                abi=ContractPublisher.abi(),
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
                abi=ContractPublisher.abi(),
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
                abi=ContractPublisher.abi(),
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
                abi=ContractPublisher.abi(),
            )
            .events.PublisherProfileUpdated()
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
                abi=ContractPublisher.abi(),
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
                abi=ContractPublisher.abi(),
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
                abi=ContractPublisher.abi(),
            )
            .events.RoleRevoked()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_trustedForwarder","type":"address"},{"internalType":"contract IContractPublisher","name":"_prevPublisher","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"publisher","type":"address"},{"components":[{"internalType":"string","name":"contractId","type":"string"},{"internalType":"uint256","name":"publishTimestamp","type":"uint256"},{"internalType":"string","name":"publishMetadataUri","type":"string"},{"internalType":"bytes32","name":"bytecodeHash","type":"bytes32"},{"internalType":"address","name":"implementation","type":"address"}],"indexed":false,"internalType":"struct IContractPublisher.CustomContractInstance","name":"publishedContract","type":"tuple"}],"name":"ContractPublished","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"publisher","type":"address"},{"indexed":true,"internalType":"string","name":"contractId","type":"string"}],"name":"ContractUnpublished","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"isPaused","type":"bool"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"publisher","type":"address"},{"indexed":false,"internalType":"string","name":"prevURI","type":"string"},{"indexed":false,"internalType":"string","name":"newURI","type":"string"}],"name":"PublisherProfileUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_publisher","type":"address"}],"name":"getAllPublishedContracts","outputs":[{"components":[{"internalType":"string","name":"contractId","type":"string"},{"internalType":"uint256","name":"publishTimestamp","type":"uint256"},{"internalType":"string","name":"publishMetadataUri","type":"string"},{"internalType":"bytes32","name":"bytecodeHash","type":"bytes32"},{"internalType":"address","name":"implementation","type":"address"}],"internalType":"struct IContractPublisher.CustomContractInstance[]","name":"published","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_publisher","type":"address"},{"internalType":"string","name":"_contractId","type":"string"}],"name":"getPublishedContract","outputs":[{"components":[{"internalType":"string","name":"contractId","type":"string"},{"internalType":"uint256","name":"publishTimestamp","type":"uint256"},{"internalType":"string","name":"publishMetadataUri","type":"string"},{"internalType":"bytes32","name":"bytecodeHash","type":"bytes32"},{"internalType":"address","name":"implementation","type":"address"}],"internalType":"struct IContractPublisher.CustomContractInstance","name":"published","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_publisher","type":"address"},{"internalType":"string","name":"_contractId","type":"string"}],"name":"getPublishedContractVersions","outputs":[{"components":[{"internalType":"string","name":"contractId","type":"string"},{"internalType":"uint256","name":"publishTimestamp","type":"uint256"},{"internalType":"string","name":"publishMetadataUri","type":"string"},{"internalType":"bytes32","name":"bytecodeHash","type":"bytes32"},{"internalType":"address","name":"implementation","type":"address"}],"internalType":"struct IContractPublisher.CustomContractInstance[]","name":"published","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"compilerMetadataUri","type":"string"}],"name":"getPublishedUriFromCompilerUri","outputs":[{"internalType":"string[]","name":"publishedMetadataUris","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"publisher","type":"address"}],"name":"getPublisherProfileUri","outputs":[{"internalType":"string","name":"uri","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPaused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"prevPublisher","outputs":[{"internalType":"contract IContractPublisher","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_publisher","type":"address"},{"internalType":"string","name":"_contractId","type":"string"},{"internalType":"string","name":"_publishMetadataUri","type":"string"},{"internalType":"string","name":"_compilerMetadataUri","type":"string"},{"internalType":"bytes32","name":"_bytecodeHash","type":"bytes32"},{"internalType":"address","name":"_implementation","type":"address"}],"name":"publishContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_pause","type":"bool"}],"name":"setPause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"publisher","type":"address"},{"internalType":"string","name":"uri","type":"string"}],"name":"setPublisherProfileUri","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_publisher","type":"address"},{"internalType":"string","name":"_contractId","type":"string"}],"name":"unpublishContract","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
