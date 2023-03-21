"""Generated wrapper for AirdropERC1155 Solidity contract."""

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
# constructor for AirdropERC1155 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        AirdropERC1155Validator,
    )
except ImportError:

    class AirdropERC1155Validator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IAirdropERC1155AirdropContent(TypedDict):
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

    tokenAddress: str

    tokenOwner: str

    recipient: str

    tokenId: int

    amount: int


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


class AddAirdropRecipientsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the addAirdropRecipients method."""

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
        self, contents: List[IAirdropERC1155AirdropContent]
    ):
        """Validate the inputs to the addAirdropRecipients method."""
        self.validator.assert_valid(
            method_name="addAirdropRecipients",
            parameter_name="_contents",
            argument_value=contents,
        )
        return contents

    def call(
        self,
        contents: List[IAirdropERC1155AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (contents) = self.validate_and_normalize_inputs(contents)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(contents).call(tx_params.as_dict())

    def send_transaction(
        self,
        contents: List[IAirdropERC1155AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (contents) = self.validate_and_normalize_inputs(contents)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(contents).transact(tx_params.as_dict())

    def build_transaction(
        self,
        contents: List[IAirdropERC1155AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (contents) = self.validate_and_normalize_inputs(contents)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(contents).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        contents: List[IAirdropERC1155AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (contents) = self.validate_and_normalize_inputs(contents)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(contents).estimateGas(
            tx_params.as_dict()
        )


class Airdrop1Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the airdrop method."""

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
        token_address: str,
        token_owner: str,
        contents: List[IAirdropERC1155AirdropContent],
    ):
        """Validate the inputs to the airdrop method."""
        self.validator.assert_valid(
            method_name="airdrop",
            parameter_name="_tokenAddress",
            argument_value=token_address,
        )
        token_address = self.validate_and_checksum_address(token_address)
        self.validator.assert_valid(
            method_name="airdrop",
            parameter_name="_tokenOwner",
            argument_value=token_owner,
        )
        token_owner = self.validate_and_checksum_address(token_owner)
        self.validator.assert_valid(
            method_name="airdrop",
            parameter_name="_contents",
            argument_value=contents,
        )
        return (token_address, token_owner, contents)

    def call(
        self,
        token_address: str,
        token_owner: str,
        contents: List[IAirdropERC1155AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            token_address,
            token_owner,
            contents,
        ) = self.validate_and_normalize_inputs(
            token_address, token_owner, contents
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_address, token_owner, contents).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        token_address: str,
        token_owner: str,
        contents: List[IAirdropERC1155AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            token_address,
            token_owner,
            contents,
        ) = self.validate_and_normalize_inputs(
            token_address, token_owner, contents
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_address, token_owner, contents
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        token_address: str,
        token_owner: str,
        contents: List[IAirdropERC1155AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            token_address,
            token_owner,
            contents,
        ) = self.validate_and_normalize_inputs(
            token_address, token_owner, contents
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_address, token_owner, contents
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        token_address: str,
        token_owner: str,
        contents: List[IAirdropERC1155AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            token_address,
            token_owner,
            contents,
        ) = self.validate_and_normalize_inputs(
            token_address, token_owner, contents
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_address, token_owner, contents
        ).estimateGas(tx_params.as_dict())


class Airdrop2Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the airdrop method."""

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

    def validate_and_normalize_inputs(self, payments_to_process: int):
        """Validate the inputs to the airdrop method."""
        self.validator.assert_valid(
            method_name="airdrop",
            parameter_name="paymentsToProcess",
            argument_value=payments_to_process,
        )
        # safeguard against fractional inputs
        payments_to_process = int(payments_to_process)
        return payments_to_process

    def call(
        self, payments_to_process: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (payments_to_process) = self.validate_and_normalize_inputs(
            payments_to_process
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(payments_to_process).call(tx_params.as_dict())

    def send_transaction(
        self, payments_to_process: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (payments_to_process) = self.validate_and_normalize_inputs(
            payments_to_process
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(payments_to_process).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, payments_to_process: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (payments_to_process) = self.validate_and_normalize_inputs(
            payments_to_process
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(payments_to_process).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, payments_to_process: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (payments_to_process) = self.validate_and_normalize_inputs(
            payments_to_process
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(payments_to_process).estimateGas(
            tx_params.as_dict()
        )


class ContractTypeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractType method."""

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


class ContractVersionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractVersion method."""

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


class GetAllAirdropPaymentsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllAirdropPayments method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(
        self, tx_params: Optional[TxParams] = None
    ) -> List[IAirdropERC1155AirdropContent]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            IAirdropERC1155AirdropContent(
                tokenAddress=element[0],
                tokenOwner=element[1],
                recipient=element[2],
                tokenId=element[3],
                amount=element[4],
            )
            for element in returned
        ]

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


class GetAllAirdropPaymentsFailedMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllAirdropPaymentsFailed method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(
        self, tx_params: Optional[TxParams] = None
    ) -> List[IAirdropERC1155AirdropContent]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            IAirdropERC1155AirdropContent(
                tokenAddress=element[0],
                tokenOwner=element[1],
                recipient=element[2],
                tokenId=element[3],
                amount=element[4],
            )
            for element in returned
        ]

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


class GetAllAirdropPaymentsPendingMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllAirdropPaymentsPending method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(
        self, tx_params: Optional[TxParams] = None
    ) -> List[IAirdropERC1155AirdropContent]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            IAirdropERC1155AirdropContent(
                tokenAddress=element[0],
                tokenOwner=element[1],
                recipient=element[2],
                tokenId=element[3],
                amount=element[4],
            )
            for element in returned
        ]

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


class GetAllAirdropPaymentsProcessedMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllAirdropPaymentsProcessed method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(
        self, tx_params: Optional[TxParams] = None
    ) -> List[IAirdropERC1155AirdropContent]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            IAirdropERC1155AirdropContent(
                tokenAddress=element[0],
                tokenOwner=element[1],
                recipient=element[2],
                tokenId=element[3],
                amount=element[4],
            )
            for element in returned
        ]

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


class HasRoleWithSwitchMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the hasRoleWithSwitch method."""

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
        """Validate the inputs to the hasRoleWithSwitch method."""
        self.validator.assert_valid(
            method_name="hasRoleWithSwitch",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="hasRoleWithSwitch",
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


class InitializeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the initialize method."""

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

    def validate_and_normalize_inputs(self, default_admin: str):
        """Validate the inputs to the initialize method."""
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_defaultAdmin",
            argument_value=default_admin,
        )
        default_admin = self.validate_and_checksum_address(default_admin)
        return default_admin

    def call(
        self, default_admin: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (default_admin) = self.validate_and_normalize_inputs(default_admin)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(default_admin).call(tx_params.as_dict())

    def send_transaction(
        self, default_admin: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (default_admin) = self.validate_and_normalize_inputs(default_admin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, default_admin: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (default_admin) = self.validate_and_normalize_inputs(default_admin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, default_admin: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (default_admin) = self.validate_and_normalize_inputs(default_admin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin).estimateGas(
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


class OwnerMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the owner method."""

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


class PayeeCountMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the payeeCount method."""

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


class ProcessedCountMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the processedCount method."""

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


class SetOwnerMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setOwner method."""

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

    def validate_and_normalize_inputs(self, new_owner: str):
        """Validate the inputs to the setOwner method."""
        self.validator.assert_valid(
            method_name="setOwner",
            parameter_name="_newOwner",
            argument_value=new_owner,
        )
        new_owner = self.validate_and_checksum_address(new_owner)
        return new_owner

    def call(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_owner).call(tx_params.as_dict())

    def send_transaction(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).transact(tx_params.as_dict())

    def build_transaction(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, new_owner: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class AirdropERC1155:
    """Wrapper class for AirdropERC1155 Solidity contract."""

    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

    add_airdrop_recipients: AddAirdropRecipientsMethod
    """Constructor-initialized instance of
    :class:`AddAirdropRecipientsMethod`.
    """

    airdrop1: Airdrop1Method
    """Constructor-initialized instance of
    :class:`Airdrop1Method`.
    """

    airdrop2: Airdrop2Method
    """Constructor-initialized instance of
    :class:`Airdrop2Method`.
    """

    contract_type: ContractTypeMethod
    """Constructor-initialized instance of
    :class:`ContractTypeMethod`.
    """

    contract_version: ContractVersionMethod
    """Constructor-initialized instance of
    :class:`ContractVersionMethod`.
    """

    get_all_airdrop_payments: GetAllAirdropPaymentsMethod
    """Constructor-initialized instance of
    :class:`GetAllAirdropPaymentsMethod`.
    """

    get_all_airdrop_payments_failed: GetAllAirdropPaymentsFailedMethod
    """Constructor-initialized instance of
    :class:`GetAllAirdropPaymentsFailedMethod`.
    """

    get_all_airdrop_payments_pending: GetAllAirdropPaymentsPendingMethod
    """Constructor-initialized instance of
    :class:`GetAllAirdropPaymentsPendingMethod`.
    """

    get_all_airdrop_payments_processed: GetAllAirdropPaymentsProcessedMethod
    """Constructor-initialized instance of
    :class:`GetAllAirdropPaymentsProcessedMethod`.
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

    has_role_with_switch: HasRoleWithSwitchMethod
    """Constructor-initialized instance of
    :class:`HasRoleWithSwitchMethod`.
    """

    initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
    """

    multicall: MulticallMethod
    """Constructor-initialized instance of
    :class:`MulticallMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    payee_count: PayeeCountMethod
    """Constructor-initialized instance of
    :class:`PayeeCountMethod`.
    """

    processed_count: ProcessedCountMethod
    """Constructor-initialized instance of
    :class:`ProcessedCountMethod`.
    """

    renounce_role: RenounceRoleMethod
    """Constructor-initialized instance of
    :class:`RenounceRoleMethod`.
    """

    revoke_role: RevokeRoleMethod
    """Constructor-initialized instance of
    :class:`RevokeRoleMethod`.
    """

    set_owner: SetOwnerMethod
    """Constructor-initialized instance of
    :class:`SetOwnerMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: AirdropERC1155Validator = None,
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
            validator = AirdropERC1155Validator(
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
            abi=AirdropERC1155.abi(),
        ).functions

        self.default_admin_role = DefaultAdminRoleMethod(
            web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE
        )

        self.add_airdrop_recipients = AddAirdropRecipientsMethod(
            web3_or_provider,
            contract_address,
            functions.addAirdropRecipients,
            validator,
        )

        self.airdrop1 = Airdrop1Method(
            web3_or_provider, contract_address, functions.airdrop, validator
        )

        self.airdrop2 = Airdrop2Method(
            web3_or_provider, contract_address, functions.airdrop, validator
        )

        self.contract_type = ContractTypeMethod(
            web3_or_provider, contract_address, functions.contractType
        )

        self.contract_version = ContractVersionMethod(
            web3_or_provider, contract_address, functions.contractVersion
        )

        self.get_all_airdrop_payments = GetAllAirdropPaymentsMethod(
            web3_or_provider, contract_address, functions.getAllAirdropPayments
        )

        self.get_all_airdrop_payments_failed = (
            GetAllAirdropPaymentsFailedMethod(
                web3_or_provider,
                contract_address,
                functions.getAllAirdropPaymentsFailed,
            )
        )

        self.get_all_airdrop_payments_pending = (
            GetAllAirdropPaymentsPendingMethod(
                web3_or_provider,
                contract_address,
                functions.getAllAirdropPaymentsPending,
            )
        )

        self.get_all_airdrop_payments_processed = (
            GetAllAirdropPaymentsProcessedMethod(
                web3_or_provider,
                contract_address,
                functions.getAllAirdropPaymentsProcessed,
            )
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

        self.has_role_with_switch = HasRoleWithSwitchMethod(
            web3_or_provider,
            contract_address,
            functions.hasRoleWithSwitch,
            validator,
        )

        self.initialize = InitializeMethod(
            web3_or_provider, contract_address, functions.initialize, validator
        )

        self.multicall = MulticallMethod(
            web3_or_provider, contract_address, functions.multicall, validator
        )

        self.owner = OwnerMethod(
            web3_or_provider, contract_address, functions.owner
        )

        self.payee_count = PayeeCountMethod(
            web3_or_provider, contract_address, functions.payeeCount
        )

        self.processed_count = ProcessedCountMethod(
            web3_or_provider, contract_address, functions.processedCount
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

        self.set_owner = SetOwnerMethod(
            web3_or_provider, contract_address, functions.setOwner, validator
        )

    def get_airdrop_payment_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AirdropPayment event.

        :param tx_hash: hash of transaction emitting AirdropPayment event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AirdropERC1155.abi(),
            )
            .events.AirdropPayment()
            .processReceipt(tx_receipt)
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
                abi=AirdropERC1155.abi(),
            )
            .events.Initialized()
            .processReceipt(tx_receipt)
        )

    def get_owner_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OwnerUpdated event.

        :param tx_hash: hash of transaction emitting OwnerUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AirdropERC1155.abi(),
            )
            .events.OwnerUpdated()
            .processReceipt(tx_receipt)
        )

    def get_recipients_added_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RecipientsAdded event.

        :param tx_hash: hash of transaction emitting RecipientsAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=AirdropERC1155.abi(),
            )
            .events.RecipientsAdded()
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
                abi=AirdropERC1155.abi(),
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
                abi=AirdropERC1155.abi(),
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
                abi=AirdropERC1155.abi(),
            )
            .events.RoleRevoked()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"indexed":false,"internalType":"struct IAirdropERC1155.AirdropContent","name":"content","type":"tuple"}],"name":"AirdropPayment","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prevOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerUpdated","type":"event"},{"anonymous":false,"inputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"indexed":false,"internalType":"struct IAirdropERC1155.AirdropContent[]","name":"_contents","type":"tuple[]"}],"name":"RecipientsAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC1155.AirdropContent[]","name":"_contents","type":"tuple[]"}],"name":"addAirdropRecipients","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"},{"internalType":"address","name":"_tokenOwner","type":"address"},{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC1155.AirdropContent[]","name":"_contents","type":"tuple[]"}],"name":"airdrop","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"paymentsToProcess","type":"uint256"}],"name":"airdrop","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"contractType","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"contractVersion","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"getAllAirdropPayments","outputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC1155.AirdropContent[]","name":"contents","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllAirdropPaymentsFailed","outputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC1155.AirdropContent[]","name":"contents","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllAirdropPaymentsPending","outputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC1155.AirdropContent[]","name":"contents","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllAirdropPaymentsProcessed","outputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC1155.AirdropContent[]","name":"contents","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"member","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"count","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRoleWithSwitch","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_defaultAdmin","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"payeeCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"processedCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newOwner","type":"address"}],"name":"setOwner","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
