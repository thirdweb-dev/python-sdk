"""Generated wrapper for Upgradeable Solidity contract."""

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
# constructor for Upgradeable below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        UpgradeableValidator,
    )
except ImportError:

    class UpgradeableValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class ProxiableUuidMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the proxiableUUID method."""

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


class UpgradeToMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the upgradeTo method."""

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

    def validate_and_normalize_inputs(self, new_implementation: str):
        """Validate the inputs to the upgradeTo method."""
        self.validator.assert_valid(
            method_name="upgradeTo",
            parameter_name="newImplementation",
            argument_value=new_implementation,
        )
        new_implementation = self.validate_and_checksum_address(
            new_implementation
        )
        return new_implementation

    def call(
        self, new_implementation: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_implementation) = self.validate_and_normalize_inputs(
            new_implementation
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_implementation).call(tx_params.as_dict())

    def send_transaction(
        self, new_implementation: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_implementation) = self.validate_and_normalize_inputs(
            new_implementation
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_implementation).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, new_implementation: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_implementation) = self.validate_and_normalize_inputs(
            new_implementation
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_implementation).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, new_implementation: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (new_implementation) = self.validate_and_normalize_inputs(
            new_implementation
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_implementation).estimateGas(
            tx_params.as_dict()
        )


class UpgradeToAndCallMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the upgradeToAndCall method."""

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
        self, new_implementation: str, data: Union[bytes, str]
    ):
        """Validate the inputs to the upgradeToAndCall method."""
        self.validator.assert_valid(
            method_name="upgradeToAndCall",
            parameter_name="newImplementation",
            argument_value=new_implementation,
        )
        new_implementation = self.validate_and_checksum_address(
            new_implementation
        )
        self.validator.assert_valid(
            method_name="upgradeToAndCall",
            parameter_name="data",
            argument_value=data,
        )
        return (new_implementation, data)

    def call(
        self,
        new_implementation: str,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_implementation, data) = self.validate_and_normalize_inputs(
            new_implementation, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_implementation, data).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        new_implementation: str,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_implementation, data) = self.validate_and_normalize_inputs(
            new_implementation, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_implementation, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        new_implementation: str,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_implementation, data) = self.validate_and_normalize_inputs(
            new_implementation, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            new_implementation, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        new_implementation: str,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (new_implementation, data) = self.validate_and_normalize_inputs(
            new_implementation, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_implementation, data).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Upgradeable:
    """Wrapper class for Upgradeable Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    proxiable_uuid: ProxiableUuidMethod
    """Constructor-initialized instance of
    :class:`ProxiableUuidMethod`.
    """

    upgrade_to: UpgradeToMethod
    """Constructor-initialized instance of
    :class:`UpgradeToMethod`.
    """

    upgrade_to_and_call: UpgradeToAndCallMethod
    """Constructor-initialized instance of
    :class:`UpgradeToAndCallMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: UpgradeableValidator = None,
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
            validator = UpgradeableValidator(
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
            abi=Upgradeable.abi(),
        ).functions

        self.proxiable_uuid = ProxiableUuidMethod(
            web3_or_provider, contract_address, functions.proxiableUUID
        )

        self.upgrade_to = UpgradeToMethod(
            web3_or_provider, contract_address, functions.upgradeTo, validator
        )

        self.upgrade_to_and_call = UpgradeToAndCallMethod(
            web3_or_provider,
            contract_address,
            functions.upgradeToAndCall,
            validator,
        )

    def get_admin_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AdminChanged event.

        :param tx_hash: hash of transaction emitting AdminChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Upgradeable.abi(),
            )
            .events.AdminChanged()
            .processReceipt(tx_receipt)
        )

    def get_beacon_upgraded_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for BeaconUpgraded event.

        :param tx_hash: hash of transaction emitting BeaconUpgraded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Upgradeable.abi(),
            )
            .events.BeaconUpgraded()
            .processReceipt(tx_receipt)
        )

    def get_upgraded_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Upgraded event.

        :param tx_hash: hash of transaction emitting Upgraded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Upgradeable.abi(),
            )
            .events.Upgraded()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"inputs":[],"name":"proxiableUUID","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
