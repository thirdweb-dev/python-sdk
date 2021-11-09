"""Generated wrapper for NFTCollection Solidity contract."""

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
from thirdweb_web3 import Web3
from thirdweb_web3.contract import ContractFunction
from thirdweb_web3.datastructures import AttributeDict
from thirdweb_web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for NFTCollection below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        NFTCollectionValidator,
    )
except ImportError:

    class NFTCollectionValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


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


class MinterRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the MINTER_ROLE method."""

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


class PauserRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the PAUSER_ROLE method."""

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


class TransferRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the TRANSFER_ROLE method."""

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


class ContractUri_Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the _contractURI method."""

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


class BurnMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the burn method."""

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
        self, account: str, _id: int, value: int
    ):
        """Validate the inputs to the burn method."""
        self.validator.assert_valid(
            method_name="burn",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="burn",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name="burn",
            parameter_name="value",
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        return (account, _id, value)

    def call(
        self,
        account: str,
        _id: int,
        value: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, _id, value) = self.validate_and_normalize_inputs(
            account, _id, value
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, _id, value).call(tx_params.as_dict())

    def send_transaction(
        self,
        account: str,
        _id: int,
        value: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, _id, value) = self.validate_and_normalize_inputs(
            account, _id, value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id, value).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        account: str,
        _id: int,
        value: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, _id, value) = self.validate_and_normalize_inputs(
            account, _id, value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id, value).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        account: str,
        _id: int,
        value: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, _id, value) = self.validate_and_normalize_inputs(
            account, _id, value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id, value).estimateGas(
            tx_params.as_dict()
        )


class BurnBatchMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the burnBatch method."""

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
        self, account: str, ids: List[int], values: List[int]
    ):
        """Validate the inputs to the burnBatch method."""
        self.validator.assert_valid(
            method_name="burnBatch",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="burnBatch",
            parameter_name="ids",
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="burnBatch",
            parameter_name="values",
            argument_value=values,
        )
        return (account, ids, values)

    def call(
        self,
        account: str,
        ids: List[int],
        values: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, ids, values) = self.validate_and_normalize_inputs(
            account, ids, values
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, ids, values).call(tx_params.as_dict())

    def send_transaction(
        self,
        account: str,
        ids: List[int],
        values: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, ids, values) = self.validate_and_normalize_inputs(
            account, ids, values
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, ids, values).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        account: str,
        ids: List[int],
        values: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, ids, values) = self.validate_and_normalize_inputs(
            account, ids, values
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, ids, values).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        account: str,
        ids: List[int],
        values: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, ids, values) = self.validate_and_normalize_inputs(
            account, ids, values
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, ids, values).estimateGas(
            tx_params.as_dict()
        )


class ContractUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractURI method."""

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


class CreateNativeTokensMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the createNativeTokens method."""

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
        to: str,
        nft_ur_is: List[str],
        nft_supplies: List[int],
        data: Union[bytes, str],
    ):
        """Validate the inputs to the createNativeTokens method."""
        self.validator.assert_valid(
            method_name="createNativeTokens",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="createNativeTokens",
            parameter_name="_nftURIs",
            argument_value=nft_ur_is,
        )
        self.validator.assert_valid(
            method_name="createNativeTokens",
            parameter_name="_nftSupplies",
            argument_value=nft_supplies,
        )
        self.validator.assert_valid(
            method_name="createNativeTokens",
            parameter_name="data",
            argument_value=data,
        )
        return (to, nft_ur_is, nft_supplies, data)

    def call(
        self,
        to: str,
        nft_ur_is: List[str],
        nft_supplies: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> List[int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            to,
            nft_ur_is,
            nft_supplies,
            data,
        ) = self.validate_and_normalize_inputs(
            to, nft_ur_is, nft_supplies, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            to, nft_ur_is, nft_supplies, data
        ).call(tx_params.as_dict())
        return [int(element) for element in returned]

    def send_transaction(
        self,
        to: str,
        nft_ur_is: List[str],
        nft_supplies: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            to,
            nft_ur_is,
            nft_supplies,
            data,
        ) = self.validate_and_normalize_inputs(
            to, nft_ur_is, nft_supplies, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            to, nft_ur_is, nft_supplies, data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        to: str,
        nft_ur_is: List[str],
        nft_supplies: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            to,
            nft_ur_is,
            nft_supplies,
            data,
        ) = self.validate_and_normalize_inputs(
            to, nft_ur_is, nft_supplies, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            to, nft_ur_is, nft_supplies, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        to: str,
        nft_ur_is: List[str],
        nft_supplies: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            to,
            nft_ur_is,
            nft_supplies,
            data,
        ) = self.validate_and_normalize_inputs(
            to, nft_ur_is, nft_supplies, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            to, nft_ur_is, nft_supplies, data
        ).estimateGas(tx_params.as_dict())


class CreatorMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the creator method."""

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

    def validate_and_normalize_inputs(self, nft_id: int):
        """Validate the inputs to the creator method."""
        self.validator.assert_valid(
            method_name="creator",
            parameter_name="_nftId",
            argument_value=nft_id,
        )
        # safeguard against fractional inputs
        nft_id = int(nft_id)
        return nft_id

    def call(self, nft_id: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(nft_id).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).transact(tx_params.as_dict())

    def build_transaction(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).estimateGas(tx_params.as_dict())


class Erc20WrappedTokensMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the erc20WrappedTokens method."""

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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the erc20WrappedTokens method."""
        self.validator.assert_valid(
            method_name="erc20WrappedTokens",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[str, int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def send_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class Erc721WrappedTokensMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the erc721WrappedTokens method."""

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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the erc721WrappedTokens method."""
        self.validator.assert_valid(
            method_name="erc721WrappedTokens",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
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


class MintMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the mint method."""

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
        self, to: str, _id: int, amount: int, data: Union[bytes, str]
    ):
        """Validate the inputs to the mint method."""
        self.validator.assert_valid(
            method_name="mint",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="mint",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name="mint",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name="mint",
            parameter_name="data",
            argument_value=data,
        )
        return (to, _id, amount, data)

    def call(
        self,
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
        (to, _id, amount, data) = self.validate_and_normalize_inputs(
            to, _id, amount, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(to, _id, amount, data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        to: str,
        _id: int,
        amount: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, _id, amount, data) = self.validate_and_normalize_inputs(
            to, _id, amount, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, _id, amount, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        to: str,
        _id: int,
        amount: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, _id, amount, data) = self.validate_and_normalize_inputs(
            to, _id, amount, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, _id, amount, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        to: str,
        _id: int,
        amount: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (to, _id, amount, data) = self.validate_and_normalize_inputs(
            to, _id, amount, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, _id, amount, data).estimateGas(
            tx_params.as_dict()
        )


class MintBatchMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the mintBatch method."""

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
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
    ):
        """Validate the inputs to the mintBatch method."""
        self.validator.assert_valid(
            method_name="mintBatch",
            parameter_name="to",
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name="mintBatch",
            parameter_name="ids",
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="mintBatch",
            parameter_name="amounts",
            argument_value=amounts,
        )
        self.validator.assert_valid(
            method_name="mintBatch",
            parameter_name="data",
            argument_value=data,
        )
        return (to, ids, amounts, data)

    def call(
        self,
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
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(
            to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(to, ids, amounts, data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(
            to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, ids, amounts, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(
            to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            to, ids, amounts, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        to: str,
        ids: List[int],
        amounts: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (to, ids, amounts, data) = self.validate_and_normalize_inputs(
            to, ids, amounts, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, ids, amounts, data).estimateGas(
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


class NextTokenIdMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the nextTokenId method."""

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


class OnErc1155BatchReceivedMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the onERC1155BatchReceived method."""

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
        index_0: str,
        index_1: str,
        index_2: List[int],
        index_3: List[int],
        index_4: Union[bytes, str],
    ):
        """Validate the inputs to the onERC1155BatchReceived method."""
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="index_2",
            argument_value=index_2,
        )
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="index_3",
            argument_value=index_3,
        )
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="index_4",
            argument_value=index_4,
        )
        return (index_0, index_1, index_2, index_3, index_4)

    def call(
        self,
        index_0: str,
        index_1: str,
        index_2: List[int],
        index_3: List[int],
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: List[int],
        index_3: List[int],
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: List[int],
        index_3: List[int],
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        index_0: str,
        index_1: str,
        index_2: List[int],
        index_3: List[int],
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).estimateGas(tx_params.as_dict())


class OnErc1155ReceivedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the onERC1155Received method."""

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
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
    ):
        """Validate the inputs to the onERC1155Received method."""
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_2",
            argument_value=index_2,
        )
        # safeguard against fractional inputs
        index_2 = int(index_2)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_3",
            argument_value=index_3,
        )
        # safeguard against fractional inputs
        index_3 = int(index_3)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_4",
            argument_value=index_4,
        )
        return (index_0, index_1, index_2, index_3, index_4)

    def call(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).estimateGas(tx_params.as_dict())


class OnErc721ReceivedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the onERC721Received method."""

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
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: Union[bytes, str],
    ):
        """Validate the inputs to the onERC721Received method."""
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="index_2",
            argument_value=index_2,
        )
        # safeguard against fractional inputs
        index_2 = int(index_2)
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="index_3",
            argument_value=index_3,
        )
        return (index_0, index_1, index_2, index_3)

    def call(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            index_0, index_1, index_2, index_3
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3
        ).estimateGas(tx_params.as_dict())


class PauseMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the pause method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

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


class PausedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the paused method."""

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


class RedeemErc20Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the redeemERC20 method."""

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

    def validate_and_normalize_inputs(self, nft_id: int, amount: int):
        """Validate the inputs to the redeemERC20 method."""
        self.validator.assert_valid(
            method_name="redeemERC20",
            parameter_name="_nftId",
            argument_value=nft_id,
        )
        # safeguard against fractional inputs
        nft_id = int(nft_id)
        self.validator.assert_valid(
            method_name="redeemERC20",
            parameter_name="_amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (nft_id, amount)

    def call(
        self, nft_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (nft_id, amount) = self.validate_and_normalize_inputs(nft_id, amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(nft_id, amount).call(tx_params.as_dict())

    def send_transaction(
        self, nft_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (nft_id, amount) = self.validate_and_normalize_inputs(nft_id, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id, amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, nft_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (nft_id, amount) = self.validate_and_normalize_inputs(nft_id, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id, amount).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, nft_id: int, amount: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (nft_id, amount) = self.validate_and_normalize_inputs(nft_id, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id, amount).estimateGas(
            tx_params.as_dict()
        )


class RedeemErc721Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the redeemERC721 method."""

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

    def validate_and_normalize_inputs(self, nft_id: int):
        """Validate the inputs to the redeemERC721 method."""
        self.validator.assert_valid(
            method_name="redeemERC721",
            parameter_name="_nftId",
            argument_value=nft_id,
        )
        # safeguard against fractional inputs
        nft_id = int(nft_id)
        return nft_id

    def call(self, nft_id: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(nft_id).call(tx_params.as_dict())

    def send_transaction(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).transact(tx_params.as_dict())

    def build_transaction(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).estimateGas(tx_params.as_dict())


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


class RoyaltyBpsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the royaltyBps method."""

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


class RoyaltyInfoMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the royaltyInfo method."""

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

    def validate_and_normalize_inputs(self, index_0: int, sale_price: int):
        """Validate the inputs to the royaltyInfo method."""
        self.validator.assert_valid(
            method_name="royaltyInfo",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        self.validator.assert_valid(
            method_name="royaltyInfo",
            parameter_name="salePrice",
            argument_value=sale_price,
        )
        # safeguard against fractional inputs
        sale_price = int(sale_price)
        return (index_0, sale_price)

    def call(
        self,
        index_0: int,
        sale_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, sale_price) = self.validate_and_normalize_inputs(
            index_0, sale_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, sale_price).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self,
        index_0: int,
        sale_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, sale_price) = self.validate_and_normalize_inputs(
            index_0, sale_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, sale_price).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        index_0: int,
        sale_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, sale_price) = self.validate_and_normalize_inputs(
            index_0, sale_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, sale_price).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        index_0: int,
        sale_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, sale_price) = self.validate_and_normalize_inputs(
            index_0, sale_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, sale_price).estimateGas(
            tx_params.as_dict()
        )


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


class SetContractUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setContractURI method."""

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

    def validate_and_normalize_inputs(self, uri: str):
        """Validate the inputs to the setContractURI method."""
        self.validator.assert_valid(
            method_name="setContractURI",
            parameter_name="_URI",
            argument_value=uri,
        )
        return uri

    def call(self, uri: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(uri).call(tx_params.as_dict())

    def send_transaction(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).transact(tx_params.as_dict())

    def build_transaction(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).estimateGas(tx_params.as_dict())


class SetRestrictedTransferMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setRestrictedTransfer method."""

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

    def validate_and_normalize_inputs(self, restricted_transfer: bool):
        """Validate the inputs to the setRestrictedTransfer method."""
        self.validator.assert_valid(
            method_name="setRestrictedTransfer",
            parameter_name="_restrictedTransfer",
            argument_value=restricted_transfer,
        )
        return restricted_transfer

    def call(
        self, restricted_transfer: bool, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (restricted_transfer) = self.validate_and_normalize_inputs(
            restricted_transfer
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(restricted_transfer).call(tx_params.as_dict())

    def send_transaction(
        self, restricted_transfer: bool, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (restricted_transfer) = self.validate_and_normalize_inputs(
            restricted_transfer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(restricted_transfer).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, restricted_transfer: bool, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (restricted_transfer) = self.validate_and_normalize_inputs(
            restricted_transfer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(restricted_transfer).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, restricted_transfer: bool, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (restricted_transfer) = self.validate_and_normalize_inputs(
            restricted_transfer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(restricted_transfer).estimateGas(
            tx_params.as_dict()
        )


class SetRoyaltyBpsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setRoyaltyBps method."""

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

    def validate_and_normalize_inputs(self, royalty_bps: int):
        """Validate the inputs to the setRoyaltyBps method."""
        self.validator.assert_valid(
            method_name="setRoyaltyBps",
            parameter_name="_royaltyBps",
            argument_value=royalty_bps,
        )
        # safeguard against fractional inputs
        royalty_bps = int(royalty_bps)
        return royalty_bps

    def call(
        self, royalty_bps: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (royalty_bps) = self.validate_and_normalize_inputs(royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(royalty_bps).call(tx_params.as_dict())

    def send_transaction(
        self, royalty_bps: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (royalty_bps) = self.validate_and_normalize_inputs(royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(royalty_bps).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, royalty_bps: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (royalty_bps) = self.validate_and_normalize_inputs(royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(royalty_bps).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, royalty_bps: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (royalty_bps) = self.validate_and_normalize_inputs(royalty_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(royalty_bps).estimateGas(
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


class TokenStateMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the tokenState method."""

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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the tokenState method."""
        self.validator.assert_valid(
            method_name="tokenState",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[str, str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def send_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class TokenUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the tokenURI method."""

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

    def validate_and_normalize_inputs(self, nft_id: int):
        """Validate the inputs to the tokenURI method."""
        self.validator.assert_valid(
            method_name="tokenURI",
            parameter_name="_nftId",
            argument_value=nft_id,
        )
        # safeguard against fractional inputs
        nft_id = int(nft_id)
        return nft_id

    def call(self, nft_id: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(nft_id).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).transact(tx_params.as_dict())

    def build_transaction(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).estimateGas(tx_params.as_dict())


class TotalSupplyMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the totalSupply method."""

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

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the totalSupply method."""
        self.validator.assert_valid(
            method_name="totalSupply",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return _id

    def call(self, _id: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, _id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).transact(tx_params.as_dict())

    def build_transaction(
        self, _id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, _id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class TransfersRestrictedMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the transfersRestricted method."""

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


class UnpauseMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the unpause method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params.as_dict())

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


class UriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the uri method."""

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

    def validate_and_normalize_inputs(self, nft_id: int):
        """Validate the inputs to the uri method."""
        self.validator.assert_valid(
            method_name="uri",
            parameter_name="_nftId",
            argument_value=nft_id,
        )
        # safeguard against fractional inputs
        nft_id = int(nft_id)
        return nft_id

    def call(self, nft_id: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(nft_id).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).transact(tx_params.as_dict())

    def build_transaction(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, nft_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (nft_id) = self.validate_and_normalize_inputs(nft_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(nft_id).estimateGas(tx_params.as_dict())


class WrapErc20Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the wrapERC20 method."""

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
        token_contract: str,
        token_amount: int,
        num_of_nfts_to_mint: int,
        nft_uri: str,
    ):
        """Validate the inputs to the wrapERC20 method."""
        self.validator.assert_valid(
            method_name="wrapERC20",
            parameter_name="_tokenContract",
            argument_value=token_contract,
        )
        token_contract = self.validate_and_checksum_address(token_contract)
        self.validator.assert_valid(
            method_name="wrapERC20",
            parameter_name="_tokenAmount",
            argument_value=token_amount,
        )
        # safeguard against fractional inputs
        token_amount = int(token_amount)
        self.validator.assert_valid(
            method_name="wrapERC20",
            parameter_name="_numOfNftsToMint",
            argument_value=num_of_nfts_to_mint,
        )
        # safeguard against fractional inputs
        num_of_nfts_to_mint = int(num_of_nfts_to_mint)
        self.validator.assert_valid(
            method_name="wrapERC20",
            parameter_name="_nftURI",
            argument_value=nft_uri,
        )
        return (token_contract, token_amount, num_of_nfts_to_mint, nft_uri)

    def call(
        self,
        token_contract: str,
        token_amount: int,
        num_of_nfts_to_mint: int,
        nft_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            token_contract,
            token_amount,
            num_of_nfts_to_mint,
            nft_uri,
        ) = self.validate_and_normalize_inputs(
            token_contract, token_amount, num_of_nfts_to_mint, nft_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            token_contract, token_amount, num_of_nfts_to_mint, nft_uri
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        token_contract: str,
        token_amount: int,
        num_of_nfts_to_mint: int,
        nft_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            token_contract,
            token_amount,
            num_of_nfts_to_mint,
            nft_uri,
        ) = self.validate_and_normalize_inputs(
            token_contract, token_amount, num_of_nfts_to_mint, nft_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_contract, token_amount, num_of_nfts_to_mint, nft_uri
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        token_contract: str,
        token_amount: int,
        num_of_nfts_to_mint: int,
        nft_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            token_contract,
            token_amount,
            num_of_nfts_to_mint,
            nft_uri,
        ) = self.validate_and_normalize_inputs(
            token_contract, token_amount, num_of_nfts_to_mint, nft_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_contract, token_amount, num_of_nfts_to_mint, nft_uri
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        token_contract: str,
        token_amount: int,
        num_of_nfts_to_mint: int,
        nft_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            token_contract,
            token_amount,
            num_of_nfts_to_mint,
            nft_uri,
        ) = self.validate_and_normalize_inputs(
            token_contract, token_amount, num_of_nfts_to_mint, nft_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_contract, token_amount, num_of_nfts_to_mint, nft_uri
        ).estimateGas(tx_params.as_dict())


class WrapErc721Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the wrapERC721 method."""

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
        self, nft_contract: str, token_id: int, nft_uri: str
    ):
        """Validate the inputs to the wrapERC721 method."""
        self.validator.assert_valid(
            method_name="wrapERC721",
            parameter_name="_nftContract",
            argument_value=nft_contract,
        )
        nft_contract = self.validate_and_checksum_address(nft_contract)
        self.validator.assert_valid(
            method_name="wrapERC721",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="wrapERC721",
            parameter_name="_nftURI",
            argument_value=nft_uri,
        )
        return (nft_contract, token_id, nft_uri)

    def call(
        self,
        nft_contract: str,
        token_id: int,
        nft_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (nft_contract, token_id, nft_uri) = self.validate_and_normalize_inputs(
            nft_contract, token_id, nft_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(nft_contract, token_id, nft_uri).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        nft_contract: str,
        token_id: int,
        nft_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (nft_contract, token_id, nft_uri) = self.validate_and_normalize_inputs(
            nft_contract, token_id, nft_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            nft_contract, token_id, nft_uri
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        nft_contract: str,
        token_id: int,
        nft_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (nft_contract, token_id, nft_uri) = self.validate_and_normalize_inputs(
            nft_contract, token_id, nft_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            nft_contract, token_id, nft_uri
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        nft_contract: str,
        token_id: int,
        nft_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (nft_contract, token_id, nft_uri) = self.validate_and_normalize_inputs(
            nft_contract, token_id, nft_uri
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            nft_contract, token_id, nft_uri
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class NFTCollection:
    """Wrapper class for NFTCollection Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

    minter_role: MinterRoleMethod
    """Constructor-initialized instance of
    :class:`MinterRoleMethod`.
    """

    pauser_role: PauserRoleMethod
    """Constructor-initialized instance of
    :class:`PauserRoleMethod`.
    """

    transfer_role: TransferRoleMethod
    """Constructor-initialized instance of
    :class:`TransferRoleMethod`.
    """

    contract_uri_: ContractUri_Method
    """Constructor-initialized instance of
    :class:`ContractUri_Method`.
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

    contract_uri: ContractUriMethod
    """Constructor-initialized instance of
    :class:`ContractUriMethod`.
    """

    create_native_tokens: CreateNativeTokensMethod
    """Constructor-initialized instance of
    :class:`CreateNativeTokensMethod`.
    """

    creator: CreatorMethod
    """Constructor-initialized instance of
    :class:`CreatorMethod`.
    """

    erc20_wrapped_tokens: Erc20WrappedTokensMethod
    """Constructor-initialized instance of
    :class:`Erc20WrappedTokensMethod`.
    """

    erc721_wrapped_tokens: Erc721WrappedTokensMethod
    """Constructor-initialized instance of
    :class:`Erc721WrappedTokensMethod`.
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

    is_approved_for_all: IsApprovedForAllMethod
    """Constructor-initialized instance of
    :class:`IsApprovedForAllMethod`.
    """

    is_trusted_forwarder: IsTrustedForwarderMethod
    """Constructor-initialized instance of
    :class:`IsTrustedForwarderMethod`.
    """

    mint: MintMethod
    """Constructor-initialized instance of
    :class:`MintMethod`.
    """

    mint_batch: MintBatchMethod
    """Constructor-initialized instance of
    :class:`MintBatchMethod`.
    """

    multicall: MulticallMethod
    """Constructor-initialized instance of
    :class:`MulticallMethod`.
    """

    next_token_id: NextTokenIdMethod
    """Constructor-initialized instance of
    :class:`NextTokenIdMethod`.
    """

    on_erc1155_batch_received: OnErc1155BatchReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc1155BatchReceivedMethod`.
    """

    on_erc1155_received: OnErc1155ReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc1155ReceivedMethod`.
    """

    on_erc721_received: OnErc721ReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc721ReceivedMethod`.
    """

    pause: PauseMethod
    """Constructor-initialized instance of
    :class:`PauseMethod`.
    """

    paused: PausedMethod
    """Constructor-initialized instance of
    :class:`PausedMethod`.
    """

    redeem_erc20: RedeemErc20Method
    """Constructor-initialized instance of
    :class:`RedeemErc20Method`.
    """

    redeem_erc721: RedeemErc721Method
    """Constructor-initialized instance of
    :class:`RedeemErc721Method`.
    """

    renounce_role: RenounceRoleMethod
    """Constructor-initialized instance of
    :class:`RenounceRoleMethod`.
    """

    revoke_role: RevokeRoleMethod
    """Constructor-initialized instance of
    :class:`RevokeRoleMethod`.
    """

    royalty_bps: RoyaltyBpsMethod
    """Constructor-initialized instance of
    :class:`RoyaltyBpsMethod`.
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

    set_approval_for_all: SetApprovalForAllMethod
    """Constructor-initialized instance of
    :class:`SetApprovalForAllMethod`.
    """

    set_contract_uri: SetContractUriMethod
    """Constructor-initialized instance of
    :class:`SetContractUriMethod`.
    """

    set_restricted_transfer: SetRestrictedTransferMethod
    """Constructor-initialized instance of
    :class:`SetRestrictedTransferMethod`.
    """

    set_royalty_bps: SetRoyaltyBpsMethod
    """Constructor-initialized instance of
    :class:`SetRoyaltyBpsMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    token_state: TokenStateMethod
    """Constructor-initialized instance of
    :class:`TokenStateMethod`.
    """

    token_uri: TokenUriMethod
    """Constructor-initialized instance of
    :class:`TokenUriMethod`.
    """

    total_supply: TotalSupplyMethod
    """Constructor-initialized instance of
    :class:`TotalSupplyMethod`.
    """

    transfers_restricted: TransfersRestrictedMethod
    """Constructor-initialized instance of
    :class:`TransfersRestrictedMethod`.
    """

    unpause: UnpauseMethod
    """Constructor-initialized instance of
    :class:`UnpauseMethod`.
    """

    uri: UriMethod
    """Constructor-initialized instance of
    :class:`UriMethod`.
    """

    wrap_erc20: WrapErc20Method
    """Constructor-initialized instance of
    :class:`WrapErc20Method`.
    """

    wrap_erc721: WrapErc721Method
    """Constructor-initialized instance of
    :class:`WrapErc721Method`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: NFTCollectionValidator = None,
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
            validator = NFTCollectionValidator(
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
            abi=NFTCollection.abi(),
        ).functions

        self.default_admin_role = DefaultAdminRoleMethod(
            web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE
        )

        self.minter_role = MinterRoleMethod(
            web3_or_provider, contract_address, functions.MINTER_ROLE
        )

        self.pauser_role = PauserRoleMethod(
            web3_or_provider, contract_address, functions.PAUSER_ROLE
        )

        self.transfer_role = TransferRoleMethod(
            web3_or_provider, contract_address, functions.TRANSFER_ROLE
        )

        self.contract_uri_ = ContractUri_Method(
            web3_or_provider, contract_address, functions._contractURI
        )

        self.balance_of = BalanceOfMethod(
            web3_or_provider, contract_address, functions.balanceOf, validator
        )

        self.balance_of_batch = BalanceOfBatchMethod(
            web3_or_provider,
            contract_address,
            functions.balanceOfBatch,
            validator,
        )

        self.burn = BurnMethod(
            web3_or_provider, contract_address, functions.burn, validator
        )

        self.burn_batch = BurnBatchMethod(
            web3_or_provider, contract_address, functions.burnBatch, validator
        )

        self.contract_uri = ContractUriMethod(
            web3_or_provider, contract_address, functions.contractURI
        )

        self.create_native_tokens = CreateNativeTokensMethod(
            web3_or_provider,
            contract_address,
            functions.createNativeTokens,
            validator,
        )

        self.creator = CreatorMethod(
            web3_or_provider, contract_address, functions.creator, validator
        )

        self.erc20_wrapped_tokens = Erc20WrappedTokensMethod(
            web3_or_provider,
            contract_address,
            functions.erc20WrappedTokens,
            validator,
        )

        self.erc721_wrapped_tokens = Erc721WrappedTokensMethod(
            web3_or_provider,
            contract_address,
            functions.erc721WrappedTokens,
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

        self.is_approved_for_all = IsApprovedForAllMethod(
            web3_or_provider,
            contract_address,
            functions.isApprovedForAll,
            validator,
        )

        self.is_trusted_forwarder = IsTrustedForwarderMethod(
            web3_or_provider,
            contract_address,
            functions.isTrustedForwarder,
            validator,
        )

        self.mint = MintMethod(
            web3_or_provider, contract_address, functions.mint, validator
        )

        self.mint_batch = MintBatchMethod(
            web3_or_provider, contract_address, functions.mintBatch, validator
        )

        self.multicall = MulticallMethod(
            web3_or_provider, contract_address, functions.multicall, validator
        )

        self.next_token_id = NextTokenIdMethod(
            web3_or_provider, contract_address, functions.nextTokenId
        )

        self.on_erc1155_batch_received = OnErc1155BatchReceivedMethod(
            web3_or_provider,
            contract_address,
            functions.onERC1155BatchReceived,
            validator,
        )

        self.on_erc1155_received = OnErc1155ReceivedMethod(
            web3_or_provider,
            contract_address,
            functions.onERC1155Received,
            validator,
        )

        self.on_erc721_received = OnErc721ReceivedMethod(
            web3_or_provider,
            contract_address,
            functions.onERC721Received,
            validator,
        )

        self.pause = PauseMethod(
            web3_or_provider, contract_address, functions.pause
        )

        self.paused = PausedMethod(
            web3_or_provider, contract_address, functions.paused
        )

        self.redeem_erc20 = RedeemErc20Method(
            web3_or_provider,
            contract_address,
            functions.redeemERC20,
            validator,
        )

        self.redeem_erc721 = RedeemErc721Method(
            web3_or_provider,
            contract_address,
            functions.redeemERC721,
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

        self.royalty_bps = RoyaltyBpsMethod(
            web3_or_provider, contract_address, functions.royaltyBps
        )

        self.royalty_info = RoyaltyInfoMethod(
            web3_or_provider,
            contract_address,
            functions.royaltyInfo,
            validator,
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

        self.set_contract_uri = SetContractUriMethod(
            web3_or_provider,
            contract_address,
            functions.setContractURI,
            validator,
        )

        self.set_restricted_transfer = SetRestrictedTransferMethod(
            web3_or_provider,
            contract_address,
            functions.setRestrictedTransfer,
            validator,
        )

        self.set_royalty_bps = SetRoyaltyBpsMethod(
            web3_or_provider,
            contract_address,
            functions.setRoyaltyBps,
            validator,
        )

        self.supports_interface = SupportsInterfaceMethod(
            web3_or_provider,
            contract_address,
            functions.supportsInterface,
            validator,
        )

        self.token_state = TokenStateMethod(
            web3_or_provider, contract_address, functions.tokenState, validator
        )

        self.token_uri = TokenUriMethod(
            web3_or_provider, contract_address, functions.tokenURI, validator
        )

        self.total_supply = TotalSupplyMethod(
            web3_or_provider,
            contract_address,
            functions.totalSupply,
            validator,
        )

        self.transfers_restricted = TransfersRestrictedMethod(
            web3_or_provider, contract_address, functions.transfersRestricted
        )

        self.unpause = UnpauseMethod(
            web3_or_provider, contract_address, functions.unpause
        )

        self.uri = UriMethod(
            web3_or_provider, contract_address, functions.uri, validator
        )

        self.wrap_erc20 = WrapErc20Method(
            web3_or_provider, contract_address, functions.wrapERC20, validator
        )

        self.wrap_erc721 = WrapErc721Method(
            web3_or_provider, contract_address, functions.wrapERC721, validator
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
                abi=NFTCollection.abi(),
            )
            .events.ApprovalForAll()
            .processReceipt(tx_receipt)
        )

    def get_erc20_redeemed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ERC20Redeemed event.

        :param tx_hash: hash of transaction emitting ERC20Redeemed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=NFTCollection.abi(),
            )
            .events.ERC20Redeemed()
            .processReceipt(tx_receipt)
        )

    def get_erc20_wrapped_token_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ERC20WrappedToken event.

        :param tx_hash: hash of transaction emitting ERC20WrappedToken event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=NFTCollection.abi(),
            )
            .events.ERC20WrappedToken()
            .processReceipt(tx_receipt)
        )

    def get_erc721_redeemed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ERC721Redeemed event.

        :param tx_hash: hash of transaction emitting ERC721Redeemed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=NFTCollection.abi(),
            )
            .events.ERC721Redeemed()
            .processReceipt(tx_receipt)
        )

    def get_erc721_wrapped_token_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ERC721WrappedToken event.

        :param tx_hash: hash of transaction emitting ERC721WrappedToken event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=NFTCollection.abi(),
            )
            .events.ERC721WrappedToken()
            .processReceipt(tx_receipt)
        )

    def get_native_tokens_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NativeTokens event.

        :param tx_hash: hash of transaction emitting NativeTokens event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=NFTCollection.abi(),
            )
            .events.NativeTokens()
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
                abi=NFTCollection.abi(),
            )
            .events.Paused()
            .processReceipt(tx_receipt)
        )

    def get_restricted_transfer_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RestrictedTransferUpdated event.

        :param tx_hash: hash of transaction emitting RestrictedTransferUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=NFTCollection.abi(),
            )
            .events.RestrictedTransferUpdated()
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
                abi=NFTCollection.abi(),
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
                abi=NFTCollection.abi(),
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
                abi=NFTCollection.abi(),
            )
            .events.RoleRevoked()
            .processReceipt(tx_receipt)
        )

    def get_royalty_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoyaltyUpdated event.

        :param tx_hash: hash of transaction emitting RoyaltyUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=NFTCollection.abi(),
            )
            .events.RoyaltyUpdated()
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
                abi=NFTCollection.abi(),
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
                abi=NFTCollection.abi(),
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
                abi=NFTCollection.abi(),
            )
            .events.URI()
            .processReceipt(tx_receipt)
        )

    def get_unpaused_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Unpaused event.

        :param tx_hash: hash of transaction emitting Unpaused event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=NFTCollection.abi(),
            )
            .events.Unpaused()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address payable","name":"_controlCenter","type":"address"},{"internalType":"address","name":"_trustedForwarder","type":"address"},{"internalType":"string","name":"_uri","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"redeemer","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"sourceOfUnderlying","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenAmountReceived","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"sharesRedeemed","type":"uint256"}],"name":"ERC20Redeemed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"creator","type":"address"},{"indexed":true,"internalType":"address","name":"sourceOfUnderlying","type":"address"},{"indexed":false,"internalType":"uint256","name":"totalAmountOfUnderlying","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"shares","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"string","name":"tokenURI","type":"string"}],"name":"ERC20WrappedToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"redeemer","type":"address"},{"indexed":true,"internalType":"address","name":"sourceOfUnderlying","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenIdOfUnderlying","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ERC721Redeemed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"creator","type":"address"},{"indexed":true,"internalType":"address","name":"sourceOfUnderlying","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenIdOfUnderlying","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"string","name":"tokenURI","type":"string"}],"name":"ERC721WrappedToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"creator","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"},{"indexed":false,"internalType":"string[]","name":"tokenURIs","type":"string[]"},{"indexed":false,"internalType":"uint256[]","name":"tokenSupplies","type":"uint256[]"}],"name":"NativeTokens","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"transferable","type":"bool"}],"name":"RestrictedTransferUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"royaltyBps","type":"uint256"}],"name":"RoyaltyUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PAUSER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TRANSFER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"burnBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"string[]","name":"_nftURIs","type":"string[]"},{"internalType":"uint256[]","name":"_nftSupplies","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"createNativeTokens","outputs":[{"internalType":"uint256[]","name":"nftIds","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_nftId","type":"uint256"}],"name":"creator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"erc20WrappedTokens","outputs":[{"internalType":"address","name":"source","type":"address"},{"internalType":"uint256","name":"shares","type":"uint256"},{"internalType":"uint256","name":"underlyingTokenAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"erc721WrappedTokens","outputs":[{"internalType":"address","name":"source","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"mintBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"nextTokenId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256[]","name":"index_2","type":"uint256[]"},{"internalType":"uint256[]","name":"index_3","type":"uint256[]"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155BatchReceived","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"uint256","name":"index_3","type":"uint256"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"bytes","name":"index_3","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_nftId","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"redeemERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_nftId","type":"uint256"}],"name":"redeemERC721","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"royaltyBps","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"},{"internalType":"uint256","name":"salePrice","type":"uint256"}],"name":"royaltyInfo","outputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"royaltyAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_URI","type":"string"}],"name":"setContractURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_restrictedTransfer","type":"bool"}],"name":"setRestrictedTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_royaltyBps","type":"uint256"}],"name":"setRoyaltyBps","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"tokenState","outputs":[{"internalType":"address","name":"creator","type":"address"},{"internalType":"string","name":"uri","type":"string"},{"internalType":"enum NFTCollection.UnderlyingType","name":"underlyingType","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_nftId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"transfersRestricted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_nftId","type":"uint256"}],"name":"uri","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenContract","type":"address"},{"internalType":"uint256","name":"_tokenAmount","type":"uint256"},{"internalType":"uint256","name":"_numOfNftsToMint","type":"uint256"},{"internalType":"string","name":"_nftURI","type":"string"}],"name":"wrapERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_nftContract","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"string","name":"_nftURI","type":"string"}],"name":"wrapERC721","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
