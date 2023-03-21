"""Generated wrapper for IFeeTierPlacementExtension Solidity contract."""

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
# constructor for IFeeTierPlacementExtension below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IFeeTierPlacementExtensionValidator,
    )
except ImportError:

    class IFeeTierPlacementExtensionValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class GetFeeTierMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getFeeTier method."""

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

    def validate_and_normalize_inputs(self, deployer: str, proxy: str):
        """Validate the inputs to the getFeeTier method."""
        self.validator.assert_valid(
            method_name="getFeeTier",
            parameter_name="deployer",
            argument_value=deployer,
        )
        deployer = self.validate_and_checksum_address(deployer)
        self.validator.assert_valid(
            method_name="getFeeTier",
            parameter_name="proxy",
            argument_value=proxy,
        )
        proxy = self.validate_and_checksum_address(proxy)
        return (deployer, proxy)

    def call(
        self, deployer: str, proxy: str, tx_params: Optional[TxParams] = None
    ) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (deployer, proxy) = self.validate_and_normalize_inputs(deployer, proxy)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(deployer, proxy).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self, deployer: str, proxy: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (deployer, proxy) = self.validate_and_normalize_inputs(deployer, proxy)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(deployer, proxy).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, deployer: str, proxy: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (deployer, proxy) = self.validate_and_normalize_inputs(deployer, proxy)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(deployer, proxy).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, deployer: str, proxy: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (deployer, proxy) = self.validate_and_normalize_inputs(deployer, proxy)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(deployer, proxy).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IFeeTierPlacementExtension:
    """Wrapper class for IFeeTierPlacementExtension Solidity contract."""

    get_fee_tier: GetFeeTierMethod
    """Constructor-initialized instance of
    :class:`GetFeeTierMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IFeeTierPlacementExtensionValidator = None,
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
            validator = IFeeTierPlacementExtensionValidator(
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
            abi=IFeeTierPlacementExtension.abi(),
        ).functions

        self.get_fee_tier = GetFeeTierMethod(
            web3_or_provider, contract_address, functions.getFeeTier, validator
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"deployer","type":"address"},{"internalType":"address","name":"proxy","type":"address"}],"name":"getFeeTier","outputs":[{"internalType":"uint128","name":"tierId","type":"uint128"},{"internalType":"uint128","name":"validUntilTimestamp","type":"uint128"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
