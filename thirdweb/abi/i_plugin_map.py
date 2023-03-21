"""Generated wrapper for IPluginMap Solidity contract."""

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
# constructor for IPluginMap below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IPluginMapValidator,
    )
except ImportError:

    class IPluginMapValidator(Validator):  # type: ignore
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
            parameter_name="pluginAddress",
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

    def validate_and_normalize_inputs(
        self, function_selector: Union[bytes, str]
    ):
        """Validate the inputs to the getPluginForFunction method."""
        self.validator.assert_valid(
            method_name="getPluginForFunction",
            parameter_name="functionSelector",
            argument_value=function_selector,
        )
        return function_selector

    def call(
        self,
        function_selector: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (function_selector) = self.validate_and_normalize_inputs(
            function_selector
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(function_selector).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self,
        function_selector: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (function_selector) = self.validate_and_normalize_inputs(
            function_selector
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(function_selector).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        function_selector: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (function_selector) = self.validate_and_normalize_inputs(
            function_selector
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(function_selector).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        function_selector: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (function_selector) = self.validate_and_normalize_inputs(
            function_selector
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(function_selector).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IPluginMap:
    """Wrapper class for IPluginMap Solidity contract."""

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

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IPluginMapValidator = None,
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
            validator = IPluginMapValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=IPluginMap.abi()
        ).functions

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
                abi=IPluginMap.abi(),
            )
            .events.PluginSet()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"indexed":true,"internalType":"string","name":"functionSignature","type":"string"},{"indexed":true,"internalType":"address","name":"pluginAddress","type":"address"}],"name":"PluginSet","type":"event"},{"inputs":[{"internalType":"address","name":"pluginAddress","type":"address"}],"name":"getAllFunctionsOfPlugin","outputs":[{"internalType":"bytes4[]","name":"","type":"bytes4[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllPlugins","outputs":[{"components":[{"internalType":"bytes4","name":"functionSelector","type":"bytes4"},{"internalType":"string","name":"functionSignature","type":"string"},{"internalType":"address","name":"pluginAddress","type":"address"}],"internalType":"struct IPluginMap.Plugin[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"functionSelector","type":"bytes4"}],"name":"getPluginForFunction","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
