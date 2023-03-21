"""Generated wrapper for IMultiwrap Solidity contract."""

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
# constructor for IMultiwrap below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IMultiwrapValidator,
    )
except ImportError:

    class IMultiwrapValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class ITokenBundleToken(TypedDict):
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

    assetContract: str

    tokenType: int

    tokenId: int

    totalAmount: int


class UnwrapMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the unwrap method."""

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

    def validate_and_normalize_inputs(self, token_id: int, recipient: str):
        """Validate the inputs to the unwrap method."""
        self.validator.assert_valid(
            method_name="unwrap",
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="unwrap",
            parameter_name="recipient",
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        return (token_id, recipient)

    def call(
        self,
        token_id: int,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, recipient) = self.validate_and_normalize_inputs(
            token_id, recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, recipient).call(tx_params.as_dict())

    def send_transaction(
        self,
        token_id: int,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, recipient) = self.validate_and_normalize_inputs(
            token_id, recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        token_id: int,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, recipient) = self.validate_and_normalize_inputs(
            token_id, recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        token_id: int,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id, recipient) = self.validate_and_normalize_inputs(
            token_id, recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient).estimateGas(
            tx_params.as_dict()
        )


class WrapMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the wrap method."""

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
        wrapped_contents: List[ITokenBundleToken],
        uri_for_wrapped_token: str,
        recipient: str,
    ):
        """Validate the inputs to the wrap method."""
        self.validator.assert_valid(
            method_name="wrap",
            parameter_name="wrappedContents",
            argument_value=wrapped_contents,
        )
        self.validator.assert_valid(
            method_name="wrap",
            parameter_name="uriForWrappedToken",
            argument_value=uri_for_wrapped_token,
        )
        self.validator.assert_valid(
            method_name="wrap",
            parameter_name="recipient",
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        return (wrapped_contents, uri_for_wrapped_token, recipient)

    def call(
        self,
        wrapped_contents: List[ITokenBundleToken],
        uri_for_wrapped_token: str,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            wrapped_contents,
            uri_for_wrapped_token,
            recipient,
        ) = self.validate_and_normalize_inputs(
            wrapped_contents, uri_for_wrapped_token, recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            wrapped_contents, uri_for_wrapped_token, recipient
        ).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        wrapped_contents: List[ITokenBundleToken],
        uri_for_wrapped_token: str,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            wrapped_contents,
            uri_for_wrapped_token,
            recipient,
        ) = self.validate_and_normalize_inputs(
            wrapped_contents, uri_for_wrapped_token, recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            wrapped_contents, uri_for_wrapped_token, recipient
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        wrapped_contents: List[ITokenBundleToken],
        uri_for_wrapped_token: str,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            wrapped_contents,
            uri_for_wrapped_token,
            recipient,
        ) = self.validate_and_normalize_inputs(
            wrapped_contents, uri_for_wrapped_token, recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            wrapped_contents, uri_for_wrapped_token, recipient
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        wrapped_contents: List[ITokenBundleToken],
        uri_for_wrapped_token: str,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            wrapped_contents,
            uri_for_wrapped_token,
            recipient,
        ) = self.validate_and_normalize_inputs(
            wrapped_contents, uri_for_wrapped_token, recipient
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            wrapped_contents, uri_for_wrapped_token, recipient
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IMultiwrap:
    """Wrapper class for IMultiwrap Solidity contract."""

    unwrap: UnwrapMethod
    """Constructor-initialized instance of
    :class:`UnwrapMethod`.
    """

    wrap: WrapMethod
    """Constructor-initialized instance of
    :class:`WrapMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IMultiwrapValidator = None,
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
            validator = IMultiwrapValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=IMultiwrap.abi()
        ).functions

        self.unwrap = UnwrapMethod(
            web3_or_provider, contract_address, functions.unwrap, validator
        )

        self.wrap = WrapMethod(
            web3_or_provider, contract_address, functions.wrap, validator
        )

    def get_tokens_unwrapped_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensUnwrapped event.

        :param tx_hash: hash of transaction emitting TokensUnwrapped event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IMultiwrap.abi(),
            )
            .events.TokensUnwrapped()
            .processReceipt(tx_receipt)
        )

    def get_tokens_wrapped_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensWrapped event.

        :param tx_hash: hash of transaction emitting TokensWrapped event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IMultiwrap.abi(),
            )
            .events.TokensWrapped()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"unwrapper","type":"address"},{"indexed":true,"internalType":"address","name":"recipientOfWrappedContents","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenIdOfWrappedToken","type":"uint256"}],"name":"TokensUnwrapped","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"wrapper","type":"address"},{"indexed":true,"internalType":"address","name":"recipientOfWrappedToken","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenIdOfWrappedToken","type":"uint256"},{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"enum ITokenBundle.TokenType","name":"tokenType","type":"uint8"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"totalAmount","type":"uint256"}],"indexed":false,"internalType":"struct ITokenBundle.Token[]","name":"wrappedContents","type":"tuple[]"}],"name":"TokensWrapped","type":"event"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"unwrap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"enum ITokenBundle.TokenType","name":"tokenType","type":"uint8"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"totalAmount","type":"uint256"}],"internalType":"struct ITokenBundle.Token[]","name":"wrappedContents","type":"tuple[]"},{"internalType":"string","name":"uriForWrappedToken","type":"string"},{"internalType":"address","name":"recipient","type":"address"}],"name":"wrap","outputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"stateMutability":"payable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
