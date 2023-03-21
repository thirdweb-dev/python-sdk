"""Generated wrapper for DirectListingsLogic Solidity contract."""

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
# constructor for DirectListingsLogic below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        DirectListingsLogicValidator,
    )
except ImportError:

    class DirectListingsLogicValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IDirectListingsListing(TypedDict):
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

    listingId: int

    listingCreator: str

    assetContract: str

    tokenId: int

    quantity: int

    currency: str

    pricePerToken: int

    startTimestamp: int

    endTimestamp: int

    reserved: bool

    tokenType: int

    status: int


class IDirectListingsListingParameters(TypedDict):
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

    tokenId: int

    quantity: int

    currency: str

    pricePerToken: int

    startTimestamp: int

    endTimestamp: int

    reserved: bool


class MaxBpsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the MAX_BPS method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

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


class MsgData_Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the _msgData method."""

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


class MsgSender_Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the _msgSender method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

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


class ApproveBuyerForListingMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the approveBuyerForListing method."""

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
        self, listing_id: int, buyer: str, to_approve: bool
    ):
        """Validate the inputs to the approveBuyerForListing method."""
        self.validator.assert_valid(
            method_name="approveBuyerForListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="approveBuyerForListing",
            parameter_name="_buyer",
            argument_value=buyer,
        )
        buyer = self.validate_and_checksum_address(buyer)
        self.validator.assert_valid(
            method_name="approveBuyerForListing",
            parameter_name="_toApprove",
            argument_value=to_approve,
        )
        return (listing_id, buyer, to_approve)

    def call(
        self,
        listing_id: int,
        buyer: str,
        to_approve: bool,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, buyer, to_approve) = self.validate_and_normalize_inputs(
            listing_id, buyer, to_approve
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, buyer, to_approve).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        listing_id: int,
        buyer: str,
        to_approve: bool,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, buyer, to_approve) = self.validate_and_normalize_inputs(
            listing_id, buyer, to_approve
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, buyer, to_approve).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        listing_id: int,
        buyer: str,
        to_approve: bool,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, buyer, to_approve) = self.validate_and_normalize_inputs(
            listing_id, buyer, to_approve
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, buyer, to_approve
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        listing_id: int,
        buyer: str,
        to_approve: bool,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, buyer, to_approve) = self.validate_and_normalize_inputs(
            listing_id, buyer, to_approve
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, buyer, to_approve
        ).estimateGas(tx_params.as_dict())


class ApproveCurrencyForListingMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the approveCurrencyForListing method."""

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
        self, listing_id: int, currency: str, price_per_token_in_currency: int
    ):
        """Validate the inputs to the approveCurrencyForListing method."""
        self.validator.assert_valid(
            method_name="approveCurrencyForListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="approveCurrencyForListing",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name="approveCurrencyForListing",
            parameter_name="_pricePerTokenInCurrency",
            argument_value=price_per_token_in_currency,
        )
        # safeguard against fractional inputs
        price_per_token_in_currency = int(price_per_token_in_currency)
        return (listing_id, currency, price_per_token_in_currency)

    def call(
        self,
        listing_id: int,
        currency: str,
        price_per_token_in_currency: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            listing_id,
            currency,
            price_per_token_in_currency,
        ) = self.validate_and_normalize_inputs(
            listing_id, currency, price_per_token_in_currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            listing_id, currency, price_per_token_in_currency
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        currency: str,
        price_per_token_in_currency: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            listing_id,
            currency,
            price_per_token_in_currency,
        ) = self.validate_and_normalize_inputs(
            listing_id, currency, price_per_token_in_currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, currency, price_per_token_in_currency
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        listing_id: int,
        currency: str,
        price_per_token_in_currency: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            listing_id,
            currency,
            price_per_token_in_currency,
        ) = self.validate_and_normalize_inputs(
            listing_id, currency, price_per_token_in_currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, currency, price_per_token_in_currency
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        listing_id: int,
        currency: str,
        price_per_token_in_currency: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            listing_id,
            currency,
            price_per_token_in_currency,
        ) = self.validate_and_normalize_inputs(
            listing_id, currency, price_per_token_in_currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, currency, price_per_token_in_currency
        ).estimateGas(tx_params.as_dict())


class BuyFromListingMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the buyFromListing method."""

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
        listing_id: int,
        buy_for: str,
        quantity: int,
        currency: str,
        expected_total_price: int,
    ):
        """Validate the inputs to the buyFromListing method."""
        self.validator.assert_valid(
            method_name="buyFromListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="buyFromListing",
            parameter_name="_buyFor",
            argument_value=buy_for,
        )
        buy_for = self.validate_and_checksum_address(buy_for)
        self.validator.assert_valid(
            method_name="buyFromListing",
            parameter_name="_quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name="buyFromListing",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name="buyFromListing",
            parameter_name="_expectedTotalPrice",
            argument_value=expected_total_price,
        )
        # safeguard against fractional inputs
        expected_total_price = int(expected_total_price)
        return (listing_id, buy_for, quantity, currency, expected_total_price)

    def call(
        self,
        listing_id: int,
        buy_for: str,
        quantity: int,
        currency: str,
        expected_total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            listing_id,
            buy_for,
            quantity,
            currency,
            expected_total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, buy_for, quantity, currency, expected_total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            listing_id, buy_for, quantity, currency, expected_total_price
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        buy_for: str,
        quantity: int,
        currency: str,
        expected_total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            listing_id,
            buy_for,
            quantity,
            currency,
            expected_total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, buy_for, quantity, currency, expected_total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, buy_for, quantity, currency, expected_total_price
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        listing_id: int,
        buy_for: str,
        quantity: int,
        currency: str,
        expected_total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            listing_id,
            buy_for,
            quantity,
            currency,
            expected_total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, buy_for, quantity, currency, expected_total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, buy_for, quantity, currency, expected_total_price
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        listing_id: int,
        buy_for: str,
        quantity: int,
        currency: str,
        expected_total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            listing_id,
            buy_for,
            quantity,
            currency,
            expected_total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, buy_for, quantity, currency, expected_total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, buy_for, quantity, currency, expected_total_price
        ).estimateGas(tx_params.as_dict())


class CancelListingMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the cancelListing method."""

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

    def validate_and_normalize_inputs(self, listing_id: int):
        """Validate the inputs to the cancelListing method."""
        self.validator.assert_valid(
            method_name="cancelListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        return listing_id

    def call(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id).call(tx_params.as_dict())

    def send_transaction(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).estimateGas(
            tx_params.as_dict()
        )


class CreateListingMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the createListing method."""

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
        self, params: IDirectListingsListingParameters
    ):
        """Validate the inputs to the createListing method."""
        self.validator.assert_valid(
            method_name="createListing",
            parameter_name="_params",
            argument_value=params,
        )
        return params

    def call(
        self,
        params: IDirectListingsListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(params).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        params: IDirectListingsListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).transact(tx_params.as_dict())

    def build_transaction(
        self,
        params: IDirectListingsListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        params: IDirectListingsListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).estimateGas(tx_params.as_dict())


class CurrencyPriceForListingMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the currencyPriceForListing method."""

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

    def validate_and_normalize_inputs(self, listing_id: int, currency: str):
        """Validate the inputs to the currencyPriceForListing method."""
        self.validator.assert_valid(
            method_name="currencyPriceForListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="currencyPriceForListing",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        return (listing_id, currency)

    def call(
        self,
        listing_id: int,
        currency: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, currency) = self.validate_and_normalize_inputs(
            listing_id, currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(listing_id, currency).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self,
        listing_id: int,
        currency: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, currency) = self.validate_and_normalize_inputs(
            listing_id, currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, currency).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        listing_id: int,
        currency: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, currency) = self.validate_and_normalize_inputs(
            listing_id, currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, currency).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        listing_id: int,
        currency: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, currency) = self.validate_and_normalize_inputs(
            listing_id, currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, currency).estimateGas(
            tx_params.as_dict()
        )


class GetAllListingsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getAllListings method."""

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

    def validate_and_normalize_inputs(self, start_id: int, end_id: int):
        """Validate the inputs to the getAllListings method."""
        self.validator.assert_valid(
            method_name="getAllListings",
            parameter_name="_startId",
            argument_value=start_id,
        )
        # safeguard against fractional inputs
        start_id = int(start_id)
        self.validator.assert_valid(
            method_name="getAllListings",
            parameter_name="_endId",
            argument_value=end_id,
        )
        # safeguard against fractional inputs
        end_id = int(end_id)
        return (start_id, end_id)

    def call(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> List[IDirectListingsListing]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (start_id, end_id) = self.validate_and_normalize_inputs(
            start_id, end_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(start_id, end_id).call(
            tx_params.as_dict()
        )
        return [
            IDirectListingsListing(
                listingId=element[0],
                listingCreator=element[1],
                assetContract=element[2],
                tokenId=element[3],
                quantity=element[4],
                currency=element[5],
                pricePerToken=element[6],
                startTimestamp=element[7],
                endTimestamp=element[8],
                reserved=element[9],
                tokenType=element[10],
                status=element[11],
            )
            for element in returned
        ]

    def send_transaction(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (start_id, end_id) = self.validate_and_normalize_inputs(
            start_id, end_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start_id, end_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (start_id, end_id) = self.validate_and_normalize_inputs(
            start_id, end_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start_id, end_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (start_id, end_id) = self.validate_and_normalize_inputs(
            start_id, end_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start_id, end_id).estimateGas(
            tx_params.as_dict()
        )


class GetAllValidListingsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllValidListings method."""

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

    def validate_and_normalize_inputs(self, start_id: int, end_id: int):
        """Validate the inputs to the getAllValidListings method."""
        self.validator.assert_valid(
            method_name="getAllValidListings",
            parameter_name="_startId",
            argument_value=start_id,
        )
        # safeguard against fractional inputs
        start_id = int(start_id)
        self.validator.assert_valid(
            method_name="getAllValidListings",
            parameter_name="_endId",
            argument_value=end_id,
        )
        # safeguard against fractional inputs
        end_id = int(end_id)
        return (start_id, end_id)

    def call(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> List[IDirectListingsListing]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (start_id, end_id) = self.validate_and_normalize_inputs(
            start_id, end_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(start_id, end_id).call(
            tx_params.as_dict()
        )
        return [
            IDirectListingsListing(
                listingId=element[0],
                listingCreator=element[1],
                assetContract=element[2],
                tokenId=element[3],
                quantity=element[4],
                currency=element[5],
                pricePerToken=element[6],
                startTimestamp=element[7],
                endTimestamp=element[8],
                reserved=element[9],
                tokenType=element[10],
                status=element[11],
            )
            for element in returned
        ]

    def send_transaction(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (start_id, end_id) = self.validate_and_normalize_inputs(
            start_id, end_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start_id, end_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (start_id, end_id) = self.validate_and_normalize_inputs(
            start_id, end_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start_id, end_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (start_id, end_id) = self.validate_and_normalize_inputs(
            start_id, end_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start_id, end_id).estimateGas(
            tx_params.as_dict()
        )


class GetListingMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getListing method."""

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

    def validate_and_normalize_inputs(self, listing_id: int):
        """Validate the inputs to the getListing method."""
        self.validator.assert_valid(
            method_name="getListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        return listing_id

    def call(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> IDirectListingsListing:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(listing_id).call(
            tx_params.as_dict()
        )
        return IDirectListingsListing(
            listingId=returned[0],
            listingCreator=returned[1],
            assetContract=returned[2],
            tokenId=returned[3],
            quantity=returned[4],
            currency=returned[5],
            pricePerToken=returned[6],
            startTimestamp=returned[7],
            endTimestamp=returned[8],
            reserved=returned[9],
            tokenType=returned[10],
            status=returned[11],
        )

    def send_transaction(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).estimateGas(
            tx_params.as_dict()
        )


class IsBuyerApprovedForListingMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the isBuyerApprovedForListing method."""

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

    def validate_and_normalize_inputs(self, listing_id: int, buyer: str):
        """Validate the inputs to the isBuyerApprovedForListing method."""
        self.validator.assert_valid(
            method_name="isBuyerApprovedForListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="isBuyerApprovedForListing",
            parameter_name="_buyer",
            argument_value=buyer,
        )
        buyer = self.validate_and_checksum_address(buyer)
        return (listing_id, buyer)

    def call(
        self, listing_id: int, buyer: str, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, buyer) = self.validate_and_normalize_inputs(
            listing_id, buyer
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(listing_id, buyer).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self, listing_id: int, buyer: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, buyer) = self.validate_and_normalize_inputs(
            listing_id, buyer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, buyer).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, listing_id: int, buyer: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, buyer) = self.validate_and_normalize_inputs(
            listing_id, buyer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, buyer).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, listing_id: int, buyer: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, buyer) = self.validate_and_normalize_inputs(
            listing_id, buyer
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, buyer).estimateGas(
            tx_params.as_dict()
        )


class IsCurrencyApprovedForListingMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the isCurrencyApprovedForListing method."""

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

    def validate_and_normalize_inputs(self, listing_id: int, currency: str):
        """Validate the inputs to the isCurrencyApprovedForListing method."""
        self.validator.assert_valid(
            method_name="isCurrencyApprovedForListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="isCurrencyApprovedForListing",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        return (listing_id, currency)

    def call(
        self,
        listing_id: int,
        currency: str,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, currency) = self.validate_and_normalize_inputs(
            listing_id, currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(listing_id, currency).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        listing_id: int,
        currency: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, currency) = self.validate_and_normalize_inputs(
            listing_id, currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, currency).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        listing_id: int,
        currency: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, currency) = self.validate_and_normalize_inputs(
            listing_id, currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, currency).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        listing_id: int,
        currency: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, currency) = self.validate_and_normalize_inputs(
            listing_id, currency
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, currency).estimateGas(
            tx_params.as_dict()
        )


class TotalListingsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the totalListings method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

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


class UpdateListingMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the updateListing method."""

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
        self, listing_id: int, params: IDirectListingsListingParameters
    ):
        """Validate the inputs to the updateListing method."""
        self.validator.assert_valid(
            method_name="updateListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="updateListing",
            parameter_name="_params",
            argument_value=params,
        )
        return (listing_id, params)

    def call(
        self,
        listing_id: int,
        params: IDirectListingsListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, params) = self.validate_and_normalize_inputs(
            listing_id, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, params).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        params: IDirectListingsListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, params) = self.validate_and_normalize_inputs(
            listing_id, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, params).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        listing_id: int,
        params: IDirectListingsListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, params) = self.validate_and_normalize_inputs(
            listing_id, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, params).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        listing_id: int,
        params: IDirectListingsListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, params) = self.validate_and_normalize_inputs(
            listing_id, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, params).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class DirectListingsLogic:
    """Wrapper class for DirectListingsLogic Solidity contract."""

    max_bps: MaxBpsMethod
    """Constructor-initialized instance of
    :class:`MaxBpsMethod`.
    """

    msg_data_: MsgData_Method
    """Constructor-initialized instance of
    :class:`MsgData_Method`.
    """

    msg_sender_: MsgSender_Method
    """Constructor-initialized instance of
    :class:`MsgSender_Method`.
    """

    approve_buyer_for_listing: ApproveBuyerForListingMethod
    """Constructor-initialized instance of
    :class:`ApproveBuyerForListingMethod`.
    """

    approve_currency_for_listing: ApproveCurrencyForListingMethod
    """Constructor-initialized instance of
    :class:`ApproveCurrencyForListingMethod`.
    """

    buy_from_listing: BuyFromListingMethod
    """Constructor-initialized instance of
    :class:`BuyFromListingMethod`.
    """

    cancel_listing: CancelListingMethod
    """Constructor-initialized instance of
    :class:`CancelListingMethod`.
    """

    create_listing: CreateListingMethod
    """Constructor-initialized instance of
    :class:`CreateListingMethod`.
    """

    currency_price_for_listing: CurrencyPriceForListingMethod
    """Constructor-initialized instance of
    :class:`CurrencyPriceForListingMethod`.
    """

    get_all_listings: GetAllListingsMethod
    """Constructor-initialized instance of
    :class:`GetAllListingsMethod`.
    """

    get_all_valid_listings: GetAllValidListingsMethod
    """Constructor-initialized instance of
    :class:`GetAllValidListingsMethod`.
    """

    get_listing: GetListingMethod
    """Constructor-initialized instance of
    :class:`GetListingMethod`.
    """

    is_buyer_approved_for_listing: IsBuyerApprovedForListingMethod
    """Constructor-initialized instance of
    :class:`IsBuyerApprovedForListingMethod`.
    """

    is_currency_approved_for_listing: IsCurrencyApprovedForListingMethod
    """Constructor-initialized instance of
    :class:`IsCurrencyApprovedForListingMethod`.
    """

    total_listings: TotalListingsMethod
    """Constructor-initialized instance of
    :class:`TotalListingsMethod`.
    """

    update_listing: UpdateListingMethod
    """Constructor-initialized instance of
    :class:`UpdateListingMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: DirectListingsLogicValidator = None,
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
            validator = DirectListingsLogicValidator(
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
            abi=DirectListingsLogic.abi(),
        ).functions

        self.max_bps = MaxBpsMethod(
            web3_or_provider, contract_address, functions.MAX_BPS
        )

        self.msg_data_ = MsgData_Method(
            web3_or_provider, contract_address, functions._msgData
        )

        self.msg_sender_ = MsgSender_Method(
            web3_or_provider, contract_address, functions._msgSender
        )

        self.approve_buyer_for_listing = ApproveBuyerForListingMethod(
            web3_or_provider,
            contract_address,
            functions.approveBuyerForListing,
            validator,
        )

        self.approve_currency_for_listing = ApproveCurrencyForListingMethod(
            web3_or_provider,
            contract_address,
            functions.approveCurrencyForListing,
            validator,
        )

        self.buy_from_listing = BuyFromListingMethod(
            web3_or_provider,
            contract_address,
            functions.buyFromListing,
            validator,
        )

        self.cancel_listing = CancelListingMethod(
            web3_or_provider,
            contract_address,
            functions.cancelListing,
            validator,
        )

        self.create_listing = CreateListingMethod(
            web3_or_provider,
            contract_address,
            functions.createListing,
            validator,
        )

        self.currency_price_for_listing = CurrencyPriceForListingMethod(
            web3_or_provider,
            contract_address,
            functions.currencyPriceForListing,
            validator,
        )

        self.get_all_listings = GetAllListingsMethod(
            web3_or_provider,
            contract_address,
            functions.getAllListings,
            validator,
        )

        self.get_all_valid_listings = GetAllValidListingsMethod(
            web3_or_provider,
            contract_address,
            functions.getAllValidListings,
            validator,
        )

        self.get_listing = GetListingMethod(
            web3_or_provider, contract_address, functions.getListing, validator
        )

        self.is_buyer_approved_for_listing = IsBuyerApprovedForListingMethod(
            web3_or_provider,
            contract_address,
            functions.isBuyerApprovedForListing,
            validator,
        )

        self.is_currency_approved_for_listing = (
            IsCurrencyApprovedForListingMethod(
                web3_or_provider,
                contract_address,
                functions.isCurrencyApprovedForListing,
                validator,
            )
        )

        self.total_listings = TotalListingsMethod(
            web3_or_provider, contract_address, functions.totalListings
        )

        self.update_listing = UpdateListingMethod(
            web3_or_provider,
            contract_address,
            functions.updateListing,
            validator,
        )

    def get_buyer_approved_for_listing_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for BuyerApprovedForListing event.

        :param tx_hash: hash of transaction emitting BuyerApprovedForListing
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DirectListingsLogic.abi(),
            )
            .events.BuyerApprovedForListing()
            .processReceipt(tx_receipt)
        )

    def get_cancelled_listing_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for CancelledListing event.

        :param tx_hash: hash of transaction emitting CancelledListing event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DirectListingsLogic.abi(),
            )
            .events.CancelledListing()
            .processReceipt(tx_receipt)
        )

    def get_currency_approved_for_listing_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for CurrencyApprovedForListing event.

        :param tx_hash: hash of transaction emitting CurrencyApprovedForListing
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DirectListingsLogic.abi(),
            )
            .events.CurrencyApprovedForListing()
            .processReceipt(tx_receipt)
        )

    def get_new_listing_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NewListing event.

        :param tx_hash: hash of transaction emitting NewListing event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DirectListingsLogic.abi(),
            )
            .events.NewListing()
            .processReceipt(tx_receipt)
        )

    def get_new_sale_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NewSale event.

        :param tx_hash: hash of transaction emitting NewSale event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DirectListingsLogic.abi(),
            )
            .events.NewSale()
            .processReceipt(tx_receipt)
        )

    def get_updated_listing_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for UpdatedListing event.

        :param tx_hash: hash of transaction emitting UpdatedListing event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=DirectListingsLogic.abi(),
            )
            .events.UpdatedListing()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_nativeTokenWrapper","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"buyer","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"BuyerApprovedForListing","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"listingCreator","type":"address"},{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"}],"name":"CancelledListing","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"currency","type":"address"},{"indexed":false,"internalType":"uint256","name":"pricePerToken","type":"uint256"}],"name":"CurrencyApprovedForListing","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"listingCreator","type":"address"},{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"listingCreator","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint128","name":"startTimestamp","type":"uint128"},{"internalType":"uint128","name":"endTimestamp","type":"uint128"},{"internalType":"bool","name":"reserved","type":"bool"},{"internalType":"enum IDirectListings.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IDirectListings.Status","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct IDirectListings.Listing","name":"listing","type":"tuple"}],"name":"NewListing","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"listingCreator","type":"address"},{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"address","name":"buyer","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantityBought","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalPricePaid","type":"uint256"}],"name":"NewSale","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"listingCreator","type":"address"},{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"listingCreator","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint128","name":"startTimestamp","type":"uint128"},{"internalType":"uint128","name":"endTimestamp","type":"uint128"},{"internalType":"bool","name":"reserved","type":"bool"},{"internalType":"enum IDirectListings.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IDirectListings.Status","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct IDirectListings.Listing","name":"listing","type":"tuple"}],"name":"UpdatedListing","type":"event"},{"inputs":[],"name":"MAX_BPS","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_msgData","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_msgSender","outputs":[{"internalType":"address","name":"sender","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_buyer","type":"address"},{"internalType":"bool","name":"_toApprove","type":"bool"}],"name":"approveBuyerForListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerTokenInCurrency","type":"uint256"}],"name":"approveCurrencyForListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_buyFor","type":"address"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_expectedTotalPrice","type":"uint256"}],"name":"buyFromListing","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"}],"name":"cancelListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint128","name":"startTimestamp","type":"uint128"},{"internalType":"uint128","name":"endTimestamp","type":"uint128"},{"internalType":"bool","name":"reserved","type":"bool"}],"internalType":"struct IDirectListings.ListingParameters","name":"_params","type":"tuple"}],"name":"createListing","outputs":[{"internalType":"uint256","name":"listingId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"}],"name":"currencyPriceForListing","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_startId","type":"uint256"},{"internalType":"uint256","name":"_endId","type":"uint256"}],"name":"getAllListings","outputs":[{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"listingCreator","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint128","name":"startTimestamp","type":"uint128"},{"internalType":"uint128","name":"endTimestamp","type":"uint128"},{"internalType":"bool","name":"reserved","type":"bool"},{"internalType":"enum IDirectListings.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IDirectListings.Status","name":"status","type":"uint8"}],"internalType":"struct IDirectListings.Listing[]","name":"_allListings","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_startId","type":"uint256"},{"internalType":"uint256","name":"_endId","type":"uint256"}],"name":"getAllValidListings","outputs":[{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"listingCreator","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint128","name":"startTimestamp","type":"uint128"},{"internalType":"uint128","name":"endTimestamp","type":"uint128"},{"internalType":"bool","name":"reserved","type":"bool"},{"internalType":"enum IDirectListings.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IDirectListings.Status","name":"status","type":"uint8"}],"internalType":"struct IDirectListings.Listing[]","name":"_validListings","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"}],"name":"getListing","outputs":[{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"listingCreator","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint128","name":"startTimestamp","type":"uint128"},{"internalType":"uint128","name":"endTimestamp","type":"uint128"},{"internalType":"bool","name":"reserved","type":"bool"},{"internalType":"enum IDirectListings.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IDirectListings.Status","name":"status","type":"uint8"}],"internalType":"struct IDirectListings.Listing","name":"listing","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_buyer","type":"address"}],"name":"isBuyerApprovedForListing","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"}],"name":"isCurrencyApprovedForListing","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalListings","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint128","name":"startTimestamp","type":"uint128"},{"internalType":"uint128","name":"endTimestamp","type":"uint128"},{"internalType":"bool","name":"reserved","type":"bool"}],"internalType":"struct IDirectListings.ListingParameters","name":"_params","type":"tuple"}],"name":"updateListing","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
