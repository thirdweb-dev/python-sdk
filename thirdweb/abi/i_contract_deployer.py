"""Generated wrapper for IContractDeployer Solidity contract."""

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
# constructor for IContractDeployer below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IContractDeployerValidator,
    )
except ImportError:

    class IContractDeployerValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class DeployInstanceMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the deployInstance method."""

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
        contract_bytecode: Union[bytes, str],
        constructor_args: Union[bytes, str],
        salt: Union[bytes, str],
        value: int,
        publish_metadata_uri: str,
    ):
        """Validate the inputs to the deployInstance method."""
        self.validator.assert_valid(
            method_name="deployInstance",
            parameter_name="publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        self.validator.assert_valid(
            method_name="deployInstance",
            parameter_name="contractBytecode",
            argument_value=contract_bytecode,
        )
        self.validator.assert_valid(
            method_name="deployInstance",
            parameter_name="constructorArgs",
            argument_value=constructor_args,
        )
        self.validator.assert_valid(
            method_name="deployInstance",
            parameter_name="salt",
            argument_value=salt,
        )
        self.validator.assert_valid(
            method_name="deployInstance",
            parameter_name="value",
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        self.validator.assert_valid(
            method_name="deployInstance",
            parameter_name="publishMetadataUri",
            argument_value=publish_metadata_uri,
        )
        return (
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        )

    def call(
        self,
        publisher: str,
        contract_bytecode: Union[bytes, str],
        constructor_args: Union[bytes, str],
        salt: Union[bytes, str],
        value: int,
        publish_metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        ) = self.validate_and_normalize_inputs(
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        ).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self,
        publisher: str,
        contract_bytecode: Union[bytes, str],
        constructor_args: Union[bytes, str],
        salt: Union[bytes, str],
        value: int,
        publish_metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        ) = self.validate_and_normalize_inputs(
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        publisher: str,
        contract_bytecode: Union[bytes, str],
        constructor_args: Union[bytes, str],
        salt: Union[bytes, str],
        value: int,
        publish_metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        ) = self.validate_and_normalize_inputs(
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        publisher: str,
        contract_bytecode: Union[bytes, str],
        constructor_args: Union[bytes, str],
        salt: Union[bytes, str],
        value: int,
        publish_metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        ) = self.validate_and_normalize_inputs(
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            publisher,
            contract_bytecode,
            constructor_args,
            salt,
            value,
            publish_metadata_uri,
        ).estimateGas(tx_params.as_dict())


class DeployInstanceProxyMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the deployInstanceProxy method."""

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
        implementation: str,
        initialize_data: Union[bytes, str],
        salt: Union[bytes, str],
        value: int,
        publish_metadata_uri: str,
    ):
        """Validate the inputs to the deployInstanceProxy method."""
        self.validator.assert_valid(
            method_name="deployInstanceProxy",
            parameter_name="publisher",
            argument_value=publisher,
        )
        publisher = self.validate_and_checksum_address(publisher)
        self.validator.assert_valid(
            method_name="deployInstanceProxy",
            parameter_name="implementation",
            argument_value=implementation,
        )
        implementation = self.validate_and_checksum_address(implementation)
        self.validator.assert_valid(
            method_name="deployInstanceProxy",
            parameter_name="initializeData",
            argument_value=initialize_data,
        )
        self.validator.assert_valid(
            method_name="deployInstanceProxy",
            parameter_name="salt",
            argument_value=salt,
        )
        self.validator.assert_valid(
            method_name="deployInstanceProxy",
            parameter_name="value",
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        self.validator.assert_valid(
            method_name="deployInstanceProxy",
            parameter_name="publishMetadataUri",
            argument_value=publish_metadata_uri,
        )
        return (
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        )

    def call(
        self,
        publisher: str,
        implementation: str,
        initialize_data: Union[bytes, str],
        salt: Union[bytes, str],
        value: int,
        publish_metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        ) = self.validate_and_normalize_inputs(
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        ).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self,
        publisher: str,
        implementation: str,
        initialize_data: Union[bytes, str],
        salt: Union[bytes, str],
        value: int,
        publish_metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        ) = self.validate_and_normalize_inputs(
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        publisher: str,
        implementation: str,
        initialize_data: Union[bytes, str],
        salt: Union[bytes, str],
        value: int,
        publish_metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        ) = self.validate_and_normalize_inputs(
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        publisher: str,
        implementation: str,
        initialize_data: Union[bytes, str],
        salt: Union[bytes, str],
        value: int,
        publish_metadata_uri: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        ) = self.validate_and_normalize_inputs(
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            publisher,
            implementation,
            initialize_data,
            salt,
            value,
            publish_metadata_uri,
        ).estimateGas(tx_params.as_dict())


class GetContractDeployerMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getContractDeployer method."""

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

    def validate_and_normalize_inputs(self, contract: str):
        """Validate the inputs to the getContractDeployer method."""
        self.validator.assert_valid(
            method_name="getContractDeployer",
            parameter_name="_contract",
            argument_value=contract,
        )
        contract = self.validate_and_checksum_address(contract)
        return contract

    def call(self, contract: str, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (contract) = self.validate_and_normalize_inputs(contract)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(contract).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, contract: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (contract) = self.validate_and_normalize_inputs(contract)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(contract).transact(tx_params.as_dict())

    def build_transaction(
        self, contract: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (contract) = self.validate_and_normalize_inputs(contract)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(contract).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, contract: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (contract) = self.validate_and_normalize_inputs(contract)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(contract).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IContractDeployer:
    """Wrapper class for IContractDeployer Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    deploy_instance: DeployInstanceMethod
    """Constructor-initialized instance of
    :class:`DeployInstanceMethod`.
    """

    deploy_instance_proxy: DeployInstanceProxyMethod
    """Constructor-initialized instance of
    :class:`DeployInstanceProxyMethod`.
    """

    get_contract_deployer: GetContractDeployerMethod
    """Constructor-initialized instance of
    :class:`GetContractDeployerMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IContractDeployerValidator = None,
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
            validator = IContractDeployerValidator(
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
            abi=IContractDeployer.abi(),
        ).functions

        self.deploy_instance = DeployInstanceMethod(
            web3_or_provider,
            contract_address,
            functions.deployInstance,
            validator,
        )

        self.deploy_instance_proxy = DeployInstanceProxyMethod(
            web3_or_provider,
            contract_address,
            functions.deployInstanceProxy,
            validator,
        )

        self.get_contract_deployer = GetContractDeployerMethod(
            web3_or_provider,
            contract_address,
            functions.getContractDeployer,
            validator,
        )

    def get_contract_deployed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ContractDeployed event.

        :param tx_hash: hash of transaction emitting ContractDeployed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IContractDeployer.abi(),
            )
            .events.ContractDeployed()
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
                abi=IContractDeployer.abi(),
            )
            .events.Paused()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"deployer","type":"address"},{"indexed":true,"internalType":"address","name":"publisher","type":"address"},{"indexed":false,"internalType":"address","name":"deployedContract","type":"address"}],"name":"ContractDeployed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"isPaused","type":"bool"}],"name":"Paused","type":"event"},{"inputs":[{"internalType":"address","name":"publisher","type":"address"},{"internalType":"bytes","name":"contractBytecode","type":"bytes"},{"internalType":"bytes","name":"constructorArgs","type":"bytes"},{"internalType":"bytes32","name":"salt","type":"bytes32"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"string","name":"publishMetadataUri","type":"string"}],"name":"deployInstance","outputs":[{"internalType":"address","name":"deployedAddress","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"publisher","type":"address"},{"internalType":"address","name":"implementation","type":"address"},{"internalType":"bytes","name":"initializeData","type":"bytes"},{"internalType":"bytes32","name":"salt","type":"bytes32"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"string","name":"publishMetadataUri","type":"string"}],"name":"deployInstanceProxy","outputs":[{"internalType":"address","name":"deployedAddress","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_contract","type":"address"}],"name":"getContractDeployer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
