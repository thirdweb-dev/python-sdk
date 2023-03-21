"""Generated wrapper for TokenBundle Solidity contract."""

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
# constructor for TokenBundle below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        TokenBundleValidator,
    )
except ImportError:

    class TokenBundleValidator(Validator):  # type: ignore
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


class GetTokenCountOfBundleMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getTokenCountOfBundle method."""

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

    def validate_and_normalize_inputs(self, bundle_id: int):
        """Validate the inputs to the getTokenCountOfBundle method."""
        self.validator.assert_valid(
            method_name="getTokenCountOfBundle",
            parameter_name="_bundleId",
            argument_value=bundle_id,
        )
        # safeguard against fractional inputs
        bundle_id = int(bundle_id)
        return bundle_id

    def call(
        self, bundle_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(bundle_id).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, bundle_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).transact(tx_params.as_dict())

    def build_transaction(
        self, bundle_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, bundle_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).estimateGas(
            tx_params.as_dict()
        )


class GetTokenOfBundleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getTokenOfBundle method."""

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

    def validate_and_normalize_inputs(self, bundle_id: int, index: int):
        """Validate the inputs to the getTokenOfBundle method."""
        self.validator.assert_valid(
            method_name="getTokenOfBundle",
            parameter_name="_bundleId",
            argument_value=bundle_id,
        )
        # safeguard against fractional inputs
        bundle_id = int(bundle_id)
        self.validator.assert_valid(
            method_name="getTokenOfBundle",
            parameter_name="index",
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (bundle_id, index)

    def call(
        self, bundle_id: int, index: int, tx_params: Optional[TxParams] = None
    ) -> ITokenBundleToken:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (bundle_id, index) = self.validate_and_normalize_inputs(
            bundle_id, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(bundle_id, index).call(
            tx_params.as_dict()
        )
        return ITokenBundleToken(
            assetContract=returned[0],
            tokenType=returned[1],
            tokenId=returned[2],
            totalAmount=returned[3],
        )

    def send_transaction(
        self, bundle_id: int, index: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (bundle_id, index) = self.validate_and_normalize_inputs(
            bundle_id, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id, index).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, bundle_id: int, index: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (bundle_id, index) = self.validate_and_normalize_inputs(
            bundle_id, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id, index).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, bundle_id: int, index: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (bundle_id, index) = self.validate_and_normalize_inputs(
            bundle_id, index
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id, index).estimateGas(
            tx_params.as_dict()
        )


class GetUriOfBundleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getUriOfBundle method."""

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

    def validate_and_normalize_inputs(self, bundle_id: int):
        """Validate the inputs to the getUriOfBundle method."""
        self.validator.assert_valid(
            method_name="getUriOfBundle",
            parameter_name="_bundleId",
            argument_value=bundle_id,
        )
        # safeguard against fractional inputs
        bundle_id = int(bundle_id)
        return bundle_id

    def call(
        self, bundle_id: int, tx_params: Optional[TxParams] = None
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(bundle_id).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, bundle_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).transact(tx_params.as_dict())

    def build_transaction(
        self, bundle_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, bundle_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (bundle_id) = self.validate_and_normalize_inputs(bundle_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bundle_id).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class TokenBundle:
    """Wrapper class for TokenBundle Solidity contract."""

    get_token_count_of_bundle: GetTokenCountOfBundleMethod
    """Constructor-initialized instance of
    :class:`GetTokenCountOfBundleMethod`.
    """

    get_token_of_bundle: GetTokenOfBundleMethod
    """Constructor-initialized instance of
    :class:`GetTokenOfBundleMethod`.
    """

    get_uri_of_bundle: GetUriOfBundleMethod
    """Constructor-initialized instance of
    :class:`GetUriOfBundleMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: TokenBundleValidator = None,
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
            validator = TokenBundleValidator(
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
            abi=TokenBundle.abi(),
        ).functions

        self.get_token_count_of_bundle = GetTokenCountOfBundleMethod(
            web3_or_provider,
            contract_address,
            functions.getTokenCountOfBundle,
            validator,
        )

        self.get_token_of_bundle = GetTokenOfBundleMethod(
            web3_or_provider,
            contract_address,
            functions.getTokenOfBundle,
            validator,
        )

        self.get_uri_of_bundle = GetUriOfBundleMethod(
            web3_or_provider,
            contract_address,
            functions.getUriOfBundle,
            validator,
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"uint256","name":"_bundleId","type":"uint256"}],"name":"getTokenCountOfBundle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_bundleId","type":"uint256"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getTokenOfBundle","outputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"enum ITokenBundle.TokenType","name":"tokenType","type":"uint8"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"totalAmount","type":"uint256"}],"internalType":"struct ITokenBundle.Token","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_bundleId","type":"uint256"}],"name":"getUriOfBundle","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
