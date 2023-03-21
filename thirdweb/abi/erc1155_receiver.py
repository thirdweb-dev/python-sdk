"""Generated wrapper for ERC1155Receiver Solidity contract."""

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
# constructor for ERC1155Receiver below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ERC1155ReceiverValidator,
    )
except ImportError:

    class ERC1155ReceiverValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


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
        operator: str,
        _from: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
    ):
        """Validate the inputs to the onERC1155BatchReceived method."""
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="ids",
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="values",
            argument_value=values,
        )
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="data",
            argument_value=data,
        )
        return (operator, _from, ids, values, data)

    def call(
        self,
        operator: str,
        _from: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            operator,
            _from,
            ids,
            values,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            operator, _from, ids, values, data
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        operator: str,
        _from: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            operator,
            _from,
            ids,
            values,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, ids, values, data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        operator: str,
        _from: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            operator,
            _from,
            ids,
            values,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, ids, values, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        operator: str,
        _from: str,
        ids: List[int],
        values: List[int],
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            operator,
            _from,
            ids,
            values,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, ids, values, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, ids, values, data
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
        operator: str,
        _from: str,
        _id: int,
        value: int,
        data: Union[bytes, str],
    ):
        """Validate the inputs to the onERC1155Received method."""
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="value",
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="data",
            argument_value=data,
        )
        return (operator, _from, _id, value, data)

    def call(
        self,
        operator: str,
        _from: str,
        _id: int,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            operator,
            _from,
            _id,
            value,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, _id, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            operator, _from, _id, value, data
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        operator: str,
        _from: str,
        _id: int,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            operator,
            _from,
            _id,
            value,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, _id, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, _id, value, data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        operator: str,
        _from: str,
        _id: int,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            operator,
            _from,
            _id,
            value,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, _id, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, _id, value, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        operator: str,
        _from: str,
        _id: int,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            operator,
            _from,
            _id,
            value,
            data,
        ) = self.validate_and_normalize_inputs(
            operator, _from, _id, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, _id, value, data
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
class ERC1155Receiver:
    """Wrapper class for ERC1155Receiver Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    on_erc1155_batch_received: OnErc1155BatchReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc1155BatchReceivedMethod`.
    """

    on_erc1155_received: OnErc1155ReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc1155ReceivedMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ERC1155ReceiverValidator = None,
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
            validator = ERC1155ReceiverValidator(
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
            abi=ERC1155Receiver.abi(),
        ).functions

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

        self.supports_interface = SupportsInterfaceMethod(
            web3_or_provider,
            contract_address,
            functions.supportsInterface,
            validator,
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"onERC1155BatchReceived","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"onERC1155Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
