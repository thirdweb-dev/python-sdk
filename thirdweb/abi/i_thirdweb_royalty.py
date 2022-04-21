"""Generated wrapper for IThirdwebRoyalty Solidity contract."""

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
# constructor for IThirdwebRoyalty below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IThirdwebRoyaltyValidator,
    )
except ImportError:

    class IThirdwebRoyaltyValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class GetDefaultRoyaltyInfoMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getDefaultRoyaltyInfo method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

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


class GetRoyaltyInfoForTokenMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getRoyaltyInfoForToken method."""

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

    def validate_and_normalize_inputs(self, token_id: int):
        """Validate the inputs to the getRoyaltyInfoForToken method."""
        self.validator.assert_valid(
            method_name="getRoyaltyInfoForToken",
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return token_id

    def call(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).transact(tx_params.as_dict())

    def build_transaction(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id) = self.validate_and_normalize_inputs(token_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id).estimateGas(
            tx_params.as_dict()
        )


class RoyaltyInfoMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the royaltyInfo method."""

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

    def validate_and_normalize_inputs(self, token_id: int, sale_price: int):
        """Validate the inputs to the royaltyInfo method."""
        self.validator.assert_valid(
            method_name="royaltyInfo",
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="royaltyInfo",
            parameter_name="salePrice",
            argument_value=sale_price,
        )
        # safeguard against fractional inputs
        sale_price = int(sale_price)
        return (token_id, sale_price)

    def call(
        self,
        token_id: int,
        sale_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, sale_price) = self.validate_and_normalize_inputs(
            token_id, sale_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token_id, sale_price).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self,
        token_id: int,
        sale_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, sale_price) = self.validate_and_normalize_inputs(
            token_id, sale_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, sale_price).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        token_id: int,
        sale_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, sale_price) = self.validate_and_normalize_inputs(
            token_id, sale_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, sale_price).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        token_id: int,
        sale_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id, sale_price) = self.validate_and_normalize_inputs(
            token_id, sale_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, sale_price).estimateGas(
            tx_params.as_dict()
        )


class SetDefaultRoyaltyInfoMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setDefaultRoyaltyInfo method."""

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
        self, royalty_recipient: str, royalty_bps: int
    ):
        """Validate the inputs to the setDefaultRoyaltyInfo method."""
        self.validator.assert_valid(
            method_name="setDefaultRoyaltyInfo",
            parameter_name="_royaltyRecipient",
            argument_value=royalty_recipient,
        )
        royalty_recipient = self.validate_and_checksum_address(
            royalty_recipient
        )
        self.validator.assert_valid(
            method_name="setDefaultRoyaltyInfo",
            parameter_name="_royaltyBps",
            argument_value=royalty_bps,
        )
        # safeguard against fractional inputs
        royalty_bps = int(royalty_bps)
        return (royalty_recipient, royalty_bps)

    def call(
        self,
        royalty_recipient: str,
        royalty_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(
            royalty_recipient, royalty_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(royalty_recipient, royalty_bps).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        royalty_recipient: str,
        royalty_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(
            royalty_recipient, royalty_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            royalty_recipient, royalty_bps
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        royalty_recipient: str,
        royalty_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(
            royalty_recipient, royalty_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            royalty_recipient, royalty_bps
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        royalty_recipient: str,
        royalty_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (royalty_recipient, royalty_bps) = self.validate_and_normalize_inputs(
            royalty_recipient, royalty_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            royalty_recipient, royalty_bps
        ).estimateGas(tx_params.as_dict())


class SetRoyaltyInfoForTokenMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setRoyaltyInfoForToken method."""

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
        self, token_id: int, recipient: str, bps: int
    ):
        """Validate the inputs to the setRoyaltyInfoForToken method."""
        self.validator.assert_valid(
            method_name="setRoyaltyInfoForToken",
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="setRoyaltyInfoForToken",
            parameter_name="recipient",
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        self.validator.assert_valid(
            method_name="setRoyaltyInfoForToken",
            parameter_name="bps",
            argument_value=bps,
        )
        # safeguard against fractional inputs
        bps = int(bps)
        return (token_id, recipient, bps)

    def call(
        self,
        token_id: int,
        recipient: str,
        bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token_id, recipient, bps) = self.validate_and_normalize_inputs(
            token_id, recipient, bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token_id, recipient, bps).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        token_id: int,
        recipient: str,
        bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_id, recipient, bps) = self.validate_and_normalize_inputs(
            token_id, recipient, bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient, bps).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        token_id: int,
        recipient: str,
        bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_id, recipient, bps) = self.validate_and_normalize_inputs(
            token_id, recipient, bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            token_id, recipient, bps
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        token_id: int,
        recipient: str,
        bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (token_id, recipient, bps) = self.validate_and_normalize_inputs(
            token_id, recipient, bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_id, recipient, bps).estimateGas(
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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IThirdwebRoyalty:
    """Wrapper class for IThirdwebRoyalty Solidity contract."""

    get_default_royalty_info: GetDefaultRoyaltyInfoMethod
    """Constructor-initialized instance of
    :class:`GetDefaultRoyaltyInfoMethod`.
    """

    get_royalty_info_for_token: GetRoyaltyInfoForTokenMethod
    """Constructor-initialized instance of
    :class:`GetRoyaltyInfoForTokenMethod`.
    """

    royalty_info: RoyaltyInfoMethod
    """Constructor-initialized instance of
    :class:`RoyaltyInfoMethod`.
    """

    set_default_royalty_info: SetDefaultRoyaltyInfoMethod
    """Constructor-initialized instance of
    :class:`SetDefaultRoyaltyInfoMethod`.
    """

    set_royalty_info_for_token: SetRoyaltyInfoForTokenMethod
    """Constructor-initialized instance of
    :class:`SetRoyaltyInfoForTokenMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IThirdwebRoyaltyValidator = None,
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
            validator = IThirdwebRoyaltyValidator(
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
            abi=IThirdwebRoyalty.abi(),
        ).functions

        self.get_default_royalty_info = GetDefaultRoyaltyInfoMethod(
            web3_or_provider, contract_address, functions.getDefaultRoyaltyInfo
        )

        self.get_royalty_info_for_token = GetRoyaltyInfoForTokenMethod(
            web3_or_provider,
            contract_address,
            functions.getRoyaltyInfoForToken,
            validator,
        )

        self.royalty_info = RoyaltyInfoMethod(
            web3_or_provider,
            contract_address,
            functions.royaltyInfo,
            validator,
        )

        self.set_default_royalty_info = SetDefaultRoyaltyInfoMethod(
            web3_or_provider,
            contract_address,
            functions.setDefaultRoyaltyInfo,
            validator,
        )

        self.set_royalty_info_for_token = SetRoyaltyInfoForTokenMethod(
            web3_or_provider,
            contract_address,
            functions.setRoyaltyInfoForToken,
            validator,
        )

        self.supports_interface = SupportsInterfaceMethod(
            web3_or_provider,
            contract_address,
            functions.supportsInterface,
            validator,
        )

    def get_default_royalty_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for DefaultRoyalty event.

        :param tx_hash: hash of transaction emitting DefaultRoyalty event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IThirdwebRoyalty.abi(),
            )
            .events.DefaultRoyalty()
            .processReceipt(tx_receipt)
        )

    def get_royalty_for_token_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoyaltyForToken event.

        :param tx_hash: hash of transaction emitting RoyaltyForToken event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IThirdwebRoyalty.abi(),
            )
            .events.RoyaltyForToken()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"newRoyaltyRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"newRoyaltyBps","type":"uint256"}],"name":"DefaultRoyalty","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"address","name":"royaltyRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"royaltyBps","type":"uint256"}],"name":"RoyaltyForToken","type":"event"},{"inputs":[],"name":"getDefaultRoyaltyInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getRoyaltyInfoForToken","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"salePrice","type":"uint256"}],"name":"royaltyInfo","outputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"royaltyAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_royaltyRecipient","type":"address"},{"internalType":"uint256","name":"_royaltyBps","type":"uint256"}],"name":"setDefaultRoyaltyInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"bps","type":"uint256"}],"name":"setRoyaltyInfoForToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
