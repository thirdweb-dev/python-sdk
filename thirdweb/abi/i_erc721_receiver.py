"""Generated wrapper for IERC721Receiver Solidity contract."""

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
# constructor for IERC721Receiver below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IERC721ReceiverValidator,
    )
except ImportError:

    class IERC721ReceiverValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


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
        self, operator: str, _from: str, token_id: int, data: Union[bytes, str]
    ):
        """Validate the inputs to the onERC721Received method."""
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="operator",
            argument_value=operator,
        )
        operator = self.validate_and_checksum_address(operator)
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="from",
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="data",
            argument_value=data,
        )
        return (operator, _from, token_id, data)

    def call(
        self,
        operator: str,
        _from: str,
        token_id: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (operator, _from, token_id, data) = self.validate_and_normalize_inputs(
            operator, _from, token_id, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            operator, _from, token_id, data
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        operator: str,
        _from: str,
        token_id: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (operator, _from, token_id, data) = self.validate_and_normalize_inputs(
            operator, _from, token_id, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, token_id, data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        operator: str,
        _from: str,
        token_id: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (operator, _from, token_id, data) = self.validate_and_normalize_inputs(
            operator, _from, token_id, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, token_id, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        operator: str,
        _from: str,
        token_id: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (operator, _from, token_id, data) = self.validate_and_normalize_inputs(
            operator, _from, token_id, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            operator, _from, token_id, data
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IERC721Receiver:
    """Wrapper class for IERC721Receiver Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    on_erc721_received: OnErc721ReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc721ReceivedMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IERC721ReceiverValidator = None,
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
            validator = IERC721ReceiverValidator(
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
            abi=IERC721Receiver.abi(),
        ).functions

        self.on_erc721_received = OnErc721ReceivedMethod(
            web3_or_provider,
            contract_address,
            functions.onERC721Received,
            validator,
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
