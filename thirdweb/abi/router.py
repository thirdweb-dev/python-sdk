"""Generated wrapper for Router Solidity contract."""

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
# constructor for Router below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        RouterValidator,
    )
except ImportError:

    class RouterValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IPluginMapPlugin(TypedDict):
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

    functionSelector: Union[bytes, str]

    functionSignature: str

    pluginAddress: str


class GetPluginForFunction_Method(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the _getPluginForFunction method."""

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

    def validate_and_normalize_inputs(self, selector: Union[bytes, str]):
        """Validate the inputs to the _getPluginForFunction method."""
        self.validator.assert_valid(
            method_name="_getPluginForFunction",
            parameter_name="_selector",
            argument_value=selector,
        )
        return selector

    def call(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(selector).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(selector).transact(tx_params.as_dict())

    def build_transaction(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(selector).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(selector).estimateGas(
            tx_params.as_dict()
        )


class AddPluginMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the addPlugin method."""

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

    def validate_and_normalize_inputs(self, plugin: IPluginMapPlugin):
        """Validate the inputs to the addPlugin method."""
        self.validator.assert_valid(
            method_name="addPlugin",
            parameter_name="_plugin",
            argument_value=plugin,
        )
        return plugin

    def call(
        self, plugin: IPluginMapPlugin, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (plugin) = self.validate_and_normalize_inputs(plugin)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(plugin).call(tx_params.as_dict())

    def send_transaction(
        self, plugin: IPluginMapPlugin, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (plugin) = self.validate_and_normalize_inputs(plugin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(plugin).transact(tx_params.as_dict())

    def build_transaction(
        self, plugin: IPluginMapPlugin, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (plugin) = self.validate_and_normalize_inputs(plugin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(plugin).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, plugin: IPluginMapPlugin, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (plugin) = self.validate_and_normalize_inputs(plugin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(plugin).estimateGas(tx_params.as_dict())


class GetAllFunctionsOfPluginMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllFunctionsOfPlugin method."""

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

    def validate_and_normalize_inputs(self, plugin_address: str):
        """Validate the inputs to the getAllFunctionsOfPlugin method."""
        self.validator.assert_valid(
            method_name="getAllFunctionsOfPlugin",
            parameter_name="_pluginAddress",
            argument_value=plugin_address,
        )
        plugin_address = self.validate_and_checksum_address(plugin_address)
        return plugin_address

    def call(
        self, plugin_address: str, tx_params: Optional[TxParams] = None
    ) -> List[Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (plugin_address) = self.validate_and_normalize_inputs(plugin_address)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(plugin_address).call(
            tx_params.as_dict()
        )
        return [Union[bytes, str](element) for element in returned]

    def send_transaction(
        self, plugin_address: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (plugin_address) = self.validate_and_normalize_inputs(plugin_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(plugin_address).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, plugin_address: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (plugin_address) = self.validate_and_normalize_inputs(plugin_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(plugin_address).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, plugin_address: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (plugin_address) = self.validate_and_normalize_inputs(plugin_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(plugin_address).estimateGas(
            tx_params.as_dict()
        )


class GetAllPluginsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getAllPlugins method."""

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
    ) -> List[IPluginMapPlugin]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            IPluginMapPlugin(
                functionSelector=element[0],
                functionSignature=element[1],
                pluginAddress=element[2],
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


class GetPluginForFunctionMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getPluginForFunction method."""

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

    def validate_and_normalize_inputs(self, selector: Union[bytes, str]):
        """Validate the inputs to the getPluginForFunction method."""
        self.validator.assert_valid(
            method_name="getPluginForFunction",
            parameter_name="_selector",
            argument_value=selector,
        )
        return selector

    def call(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(selector).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(selector).transact(tx_params.as_dict())

    def build_transaction(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(selector).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(selector).estimateGas(
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


class PluginMapMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the pluginMap method."""

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


class RemovePluginMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the removePlugin method."""

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

    def validate_and_normalize_inputs(self, selector: Union[bytes, str]):
        """Validate the inputs to the removePlugin method."""
        self.validator.assert_valid(
            method_name="removePlugin",
            parameter_name="_selector",
            argument_value=selector,
        )
        return selector

    def call(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(selector).call(tx_params.as_dict())

    def send_transaction(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(selector).transact(tx_params.as_dict())

    def build_transaction(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(selector).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, selector: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (selector) = self.validate_and_normalize_inputs(selector)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(selector).estimateGas(
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


class UpdatePluginMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the updatePlugin method."""

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

    def validate_and_normalize_inputs(self, plugin: IPluginMapPlugin):
        """Validate the inputs to the updatePlugin method."""
        self.validator.assert_valid(
            method_name="updatePlugin",
            parameter_name="_plugin",
            argument_value=plugin,
        )
        return plugin

    def call(
        self, plugin: IPluginMapPlugin, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (plugin) = self.validate_and_normalize_inputs(plugin)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(plugin).call(tx_params.as_dict())

    def send_transaction(
        self, plugin: IPluginMapPlugin, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (plugin) = self.validate_and_normalize_inputs(plugin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(plugin).transact(tx_params.as_dict())

    def build_transaction(
        self, plugin: IPluginMapPlugin, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (plugin) = self.validate_and_normalize_inputs(plugin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(plugin).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, plugin: IPluginMapPlugin, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (plugin) = self.validate_and_normalize_inputs(plugin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(plugin).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Router:
    """Wrapper class for Router Solidity contract."""

    get_plugin_for_function_: GetPluginForFunction_Method
    """Constructor-initialized instance of
    :class:`GetPluginForFunction_Method`.
    """

    add_plugin: AddPluginMethod
    """Constructor-initialized instance of
    :class:`AddPluginMethod`.
    """

    get_all_functions_of_plugin: GetAllFunctionsOfPluginMethod
    """Constructor-initialized instance of
    :class:`GetAllFunctionsOfPluginMethod`.
    """

    get_all_plugins: GetAllPluginsMethod
    """Constructor-initialized instance of
    :class:`GetAllPluginsMethod`.
    """

    get_plugin_for_function: GetPluginForFunctionMethod
    """Constructor-initialized instance of
    :class:`GetPluginForFunctionMethod`.
    """

    multicall: MulticallMethod
    """Constructor-initialized instance of
    :class:`MulticallMethod`.
    """

    plugin_map: PluginMapMethod
    """Constructor-initialized instance of
    :class:`PluginMapMethod`.
    """

    remove_plugin: RemovePluginMethod
    """Constructor-initialized instance of
    :class:`RemovePluginMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    update_plugin: UpdatePluginMethod
    """Constructor-initialized instance of
    :class:`UpdatePluginMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: RouterValidator = None,
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
            validator = RouterValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=Router.abi()
        ).functions

        self.get_plugin_for_function_ = GetPluginForFunction_Method(
            web3_or_provider,
            contract_address,
            functions._getPluginForFunction,
            validator,
        )

        self.add_plugin = AddPluginMethod(
            web3_or_provider, contract_address, functions.addPlugin, validator
        )

        self.get_all_functions_of_plugin = GetAllFunctionsOfPluginMethod(
            web3_or_provider,
            contract_address,
            functions.getAllFunctionsOfPlugin,
            validator,
        )

        self.get_all_plugins = GetAllPluginsMethod(
            web3_or_provider, contract_address, functions.getAllPlugins
        )

        self.get_plugin_for_function = GetPluginForFunctionMethod(
            web3_or_provider,
            contract_address,
            functions.getPluginForFunction,
            validator,
        )

        self.multicall = MulticallMethod(
            web3_or_provider, contract_address, functions.multicall, validator
        )

        self.plugin_map = PluginMapMethod(
            web3_or_provider, contract_address, functions.pluginMap
        )

        self.remove_plugin = RemovePluginMethod(
            web3_or_provider,
            contract_address,
            functions.removePlugin,
            validator,
        )

        self.supports_interface = SupportsInterfaceMethod(
            web3_or_provider,
            contract_address,
            functions.supportsInterface,
            validator,
        )

        self.update_plugin = UpdatePluginMethod(
            web3_or_provider,
            contract_address,
            functions.updatePlugin,
            validator,
        )

    def get_plugin_added_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PluginAdded event.

        :param tx_hash: hash of transaction emitting PluginAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Router.abi(),
            )
            .events.PluginAdded()
            .processReceipt(tx_receipt)
        )

    def get_plugin_removed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PluginRemoved event.

        :param tx_hash: hash of transaction emitting PluginRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Router.abi(),
            )
            .events.PluginRemoved()
            .processReceipt(tx_receipt)
        )

    def get_plugin_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PluginSet event.

        :param tx_hash: hash of transaction emitting PluginSet event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Router.abi(),
            )
            .events.PluginSet()
            .processReceipt(tx_receipt)
        )

    def get_plugin_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PluginUpdated event.

        :param tx_hash: hash of transaction emitting PluginUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Router.abi(),
            )
            .events.PluginUpdated()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"indexed":true,"internalType":"address","name":"pluginAddress","type":"address"}],"name":"PluginAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"indexed":true,"internalType":"address","name":"pluginAddress","type":"address"}],"name":"PluginRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"indexed":true,"internalType":"string","name":"functionSignature","type":"string"},{"indexed":true,"internalType":"address","name":"pluginAddress","type":"address"}],"name":"PluginSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"indexed":true,"internalType":"address","name":"oldPluginAddress","type":"address"},{"indexed":true,"internalType":"address","name":"newPluginAddress","type":"address"}],"name":"PluginUpdated","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"bytes4","name":"_selector","type":"bytes4"}],"name":"_getPluginForFunction","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"internalType":"string","name":"functionSignature","type":"string"},{"internalType":"address","name":"pluginAddress","type":"address"}],"internalType":"struct IPluginMap.Plugin","name":"_plugin","type":"tuple"}],"name":"addPlugin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_pluginAddress","type":"address"}],"name":"getAllFunctionsOfPlugin","outputs":[{"internalType":"bytes4[]","name":"registered","type":"bytes4[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllPlugins","outputs":[{"components":[{"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"internalType":"string","name":"functionSignature","type":"string"},{"internalType":"address","name":"pluginAddress","type":"address"}],"internalType":"struct IPluginMap.Plugin[]","name":"registered","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"_selector","type":"bytes4"}],"name":"getPluginForFunction","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"pluginMap","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"_selector","type":"bytes4"}],"name":"removePlugin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"internalType":"string","name":"functionSignature","type":"string"},{"internalType":"address","name":"pluginAddress","type":"address"}],"internalType":"struct IPluginMap.Plugin","name":"_plugin","type":"tuple"}],"name":"updatePlugin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
