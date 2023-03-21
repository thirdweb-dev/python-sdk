"""Generated wrapper for IAirdropERC20 Solidity contract."""

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
# constructor for IAirdropERC20 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IAirdropERC20Validator,
    )
except ImportError:

    class IAirdropERC20Validator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IAirdropERC20AirdropContent(TypedDict):
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

    tokenAddress: str

    tokenOwner: str

    recipient: str

    amount: int


class AddAirdropRecipientsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the addAirdropRecipients method."""

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
        self, contents: List[IAirdropERC20AirdropContent]
    ):
        """Validate the inputs to the addAirdropRecipients method."""
        self.validator.assert_valid(
            method_name="addAirdropRecipients",
            parameter_name="_contents",
            argument_value=contents,
        )
        return contents

    def call(
        self,
        contents: List[IAirdropERC20AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (contents) = self.validate_and_normalize_inputs(contents)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(contents).call(tx_params.as_dict())

    def send_transaction(
        self,
        contents: List[IAirdropERC20AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (contents) = self.validate_and_normalize_inputs(contents)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(contents).transact(tx_params.as_dict())

    def build_transaction(
        self,
        contents: List[IAirdropERC20AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (contents) = self.validate_and_normalize_inputs(contents)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(contents).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        contents: List[IAirdropERC20AirdropContent],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (contents) = self.validate_and_normalize_inputs(contents)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(contents).estimateGas(
            tx_params.as_dict()
        )


class AirdropMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the airdrop method."""

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

    def validate_and_normalize_inputs(self, payments_to_process: int):
        """Validate the inputs to the airdrop method."""
        self.validator.assert_valid(
            method_name="airdrop",
            parameter_name="paymentsToProcess",
            argument_value=payments_to_process,
        )
        # safeguard against fractional inputs
        payments_to_process = int(payments_to_process)
        return payments_to_process

    def call(
        self, payments_to_process: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (payments_to_process) = self.validate_and_normalize_inputs(
            payments_to_process
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(payments_to_process).call(tx_params.as_dict())

    def send_transaction(
        self, payments_to_process: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (payments_to_process) = self.validate_and_normalize_inputs(
            payments_to_process
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(payments_to_process).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, payments_to_process: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (payments_to_process) = self.validate_and_normalize_inputs(
            payments_to_process
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(payments_to_process).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, payments_to_process: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (payments_to_process) = self.validate_and_normalize_inputs(
            payments_to_process
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(payments_to_process).estimateGas(
            tx_params.as_dict()
        )


class GetAllAirdropPaymentsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllAirdropPayments method."""

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
    ) -> List[IAirdropERC20AirdropContent]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            IAirdropERC20AirdropContent(
                tokenAddress=element[0],
                tokenOwner=element[1],
                recipient=element[2],
                amount=element[3],
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


class GetAllAirdropPaymentsFailedMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllAirdropPaymentsFailed method."""

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
    ) -> List[IAirdropERC20AirdropContent]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            IAirdropERC20AirdropContent(
                tokenAddress=element[0],
                tokenOwner=element[1],
                recipient=element[2],
                amount=element[3],
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


class GetAllAirdropPaymentsPendingMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllAirdropPaymentsPending method."""

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
    ) -> List[IAirdropERC20AirdropContent]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            IAirdropERC20AirdropContent(
                tokenAddress=element[0],
                tokenOwner=element[1],
                recipient=element[2],
                amount=element[3],
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


class GetAllAirdropPaymentsProcessedMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllAirdropPaymentsProcessed method."""

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
    ) -> List[IAirdropERC20AirdropContent]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            IAirdropERC20AirdropContent(
                tokenAddress=element[0],
                tokenOwner=element[1],
                recipient=element[2],
                amount=element[3],
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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IAirdropERC20:
    """Wrapper class for IAirdropERC20 Solidity contract."""

    add_airdrop_recipients: AddAirdropRecipientsMethod
    """Constructor-initialized instance of
    :class:`AddAirdropRecipientsMethod`.
    """

    airdrop: AirdropMethod
    """Constructor-initialized instance of
    :class:`AirdropMethod`.
    """

    get_all_airdrop_payments: GetAllAirdropPaymentsMethod
    """Constructor-initialized instance of
    :class:`GetAllAirdropPaymentsMethod`.
    """

    get_all_airdrop_payments_failed: GetAllAirdropPaymentsFailedMethod
    """Constructor-initialized instance of
    :class:`GetAllAirdropPaymentsFailedMethod`.
    """

    get_all_airdrop_payments_pending: GetAllAirdropPaymentsPendingMethod
    """Constructor-initialized instance of
    :class:`GetAllAirdropPaymentsPendingMethod`.
    """

    get_all_airdrop_payments_processed: GetAllAirdropPaymentsProcessedMethod
    """Constructor-initialized instance of
    :class:`GetAllAirdropPaymentsProcessedMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IAirdropERC20Validator = None,
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
            validator = IAirdropERC20Validator(
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
            abi=IAirdropERC20.abi(),
        ).functions

        self.add_airdrop_recipients = AddAirdropRecipientsMethod(
            web3_or_provider,
            contract_address,
            functions.addAirdropRecipients,
            validator,
        )

        self.airdrop = AirdropMethod(
            web3_or_provider, contract_address, functions.airdrop, validator
        )

        self.get_all_airdrop_payments = GetAllAirdropPaymentsMethod(
            web3_or_provider, contract_address, functions.getAllAirdropPayments
        )

        self.get_all_airdrop_payments_failed = (
            GetAllAirdropPaymentsFailedMethod(
                web3_or_provider,
                contract_address,
                functions.getAllAirdropPaymentsFailed,
            )
        )

        self.get_all_airdrop_payments_pending = (
            GetAllAirdropPaymentsPendingMethod(
                web3_or_provider,
                contract_address,
                functions.getAllAirdropPaymentsPending,
            )
        )

        self.get_all_airdrop_payments_processed = (
            GetAllAirdropPaymentsProcessedMethod(
                web3_or_provider,
                contract_address,
                functions.getAllAirdropPaymentsProcessed,
            )
        )

    def get_airdrop_payment_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AirdropPayment event.

        :param tx_hash: hash of transaction emitting AirdropPayment event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IAirdropERC20.abi(),
            )
            .events.AirdropPayment()
            .processReceipt(tx_receipt)
        )

    def get_recipients_added_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RecipientsAdded event.

        :param tx_hash: hash of transaction emitting RecipientsAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IAirdropERC20.abi(),
            )
            .events.RecipientsAdded()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"indexed":false,"internalType":"struct IAirdropERC20.AirdropContent","name":"content","type":"tuple"}],"name":"AirdropPayment","type":"event"},{"anonymous":false,"inputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"indexed":false,"internalType":"struct IAirdropERC20.AirdropContent[]","name":"_contents","type":"tuple[]"}],"name":"RecipientsAdded","type":"event"},{"inputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC20.AirdropContent[]","name":"_contents","type":"tuple[]"}],"name":"addAirdropRecipients","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"paymentsToProcess","type":"uint256"}],"name":"airdrop","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllAirdropPayments","outputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC20.AirdropContent[]","name":"contents","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllAirdropPaymentsFailed","outputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC20.AirdropContent[]","name":"contents","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllAirdropPaymentsPending","outputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC20.AirdropContent[]","name":"contents","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllAirdropPaymentsProcessed","outputs":[{"components":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IAirdropERC20.AirdropContent[]","name":"contents","type":"tuple[]"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
