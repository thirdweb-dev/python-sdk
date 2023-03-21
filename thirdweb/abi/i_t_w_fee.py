"""Generated wrapper for ITWFee Solidity contract."""

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
# constructor for ITWFee below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ITWFeeValidator,
    )
except ImportError:

    class ITWFeeValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class GetFeeInfoMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getFeeInfo method."""

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

    def validate_and_normalize_inputs(self, proxy: str, _type: int):
        """Validate the inputs to the getFeeInfo method."""
        self.validator.assert_valid(
            method_name="getFeeInfo",
            parameter_name="_proxy",
            argument_value=proxy,
        )
        proxy = self.validate_and_checksum_address(proxy)
        self.validator.assert_valid(
            method_name="getFeeInfo",
            parameter_name="_type",
            argument_value=_type,
        )
        # safeguard against fractional inputs
        _type = int(_type)
        return (proxy, _type)

    def call(
        self, proxy: str, _type: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (proxy, _type) = self.validate_and_normalize_inputs(proxy, _type)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(proxy, _type).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self, proxy: str, _type: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (proxy, _type) = self.validate_and_normalize_inputs(proxy, _type)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proxy, _type).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, proxy: str, _type: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (proxy, _type) = self.validate_and_normalize_inputs(proxy, _type)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proxy, _type).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, proxy: str, _type: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (proxy, _type) = self.validate_and_normalize_inputs(proxy, _type)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proxy, _type).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ITWFee:
    """Wrapper class for ITWFee Solidity contract."""

    get_fee_info: GetFeeInfoMethod
    """Constructor-initialized instance of
    :class:`GetFeeInfoMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ITWFeeValidator = None,
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
            validator = ITWFeeValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=ITWFee.abi()
        ).functions

        self.get_fee_info = GetFeeInfoMethod(
            web3_or_provider, contract_address, functions.getFeeInfo, validator
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_proxy","type":"address"},{"internalType":"uint256","name":"_type","type":"uint256"}],"name":"getFeeInfo","outputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"bps","type":"uint256"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
