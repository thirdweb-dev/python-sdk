"""Generated wrapper for Marketplace Solidity contract."""

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
# constructor for Marketplace below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        MarketplaceValidator,
    )
except ImportError:

    class MarketplaceValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IMarketplaceListing(TypedDict):
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

    tokenOwner: str

    assetContract: str

    tokenId: int

    startTime: int

    endTime: int

    quantity: int

    currency: str

    reservePricePerToken: int

    buyoutPricePerToken: int

    tokenType: int

    listingType: int


class IMarketplaceListingParameters(TypedDict):
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

    startTime: int

    secondsUntilEndTime: int

    quantityToList: int

    currencyToAccept: str

    reservePricePerToken: int

    buyoutPricePerToken: int

    listingType: int


class DefaultAdminRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the DEFAULT_ADMIN_ROLE method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class MaxBpsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the MAX_BPS method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class AcceptOfferMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the acceptOffer method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, listing_id: int, offeror: str, currency: str, price_per_token: int):
        """Validate the inputs to the acceptOffer method."""
        self.validator.assert_valid(
            method_name='acceptOffer',
            parameter_name='_listingId',
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name='acceptOffer',
            parameter_name='_offeror',
            argument_value=offeror,
        )
        offeror = self.validate_and_checksum_address(offeror)
        self.validator.assert_valid(
            method_name='acceptOffer',
            parameter_name='_currency',
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name='acceptOffer',
            parameter_name='_pricePerToken',
            argument_value=price_per_token,
        )
        # safeguard against fractional inputs
        price_per_token = int(price_per_token)
        return (listing_id, offeror, currency, price_per_token)

    def call(self, listing_id: int, offeror: str, currency: str, price_per_token: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, offeror, currency, price_per_token) = self.validate_and_normalize_inputs(listing_id, offeror, currency, price_per_token)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, offeror, currency, price_per_token).call(tx_params.as_dict())

    def send_transaction(self, listing_id: int, offeror: str, currency: str, price_per_token: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, offeror, currency, price_per_token) = self.validate_and_normalize_inputs(listing_id, offeror, currency, price_per_token)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, offeror, currency, price_per_token).transact(tx_params.as_dict())

    def build_transaction(self, listing_id: int, offeror: str, currency: str, price_per_token: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, offeror, currency, price_per_token) = self.validate_and_normalize_inputs(listing_id, offeror, currency, price_per_token)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, offeror, currency, price_per_token).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, listing_id: int, offeror: str, currency: str, price_per_token: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, offeror, currency, price_per_token) = self.validate_and_normalize_inputs(listing_id, offeror, currency, price_per_token)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, offeror, currency, price_per_token).estimateGas(tx_params.as_dict())

class BidBufferBpsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the bidBufferBps method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class BuyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the buy method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, listing_id: int, buy_for: str, quantity_to_buy: int, currency: str, total_price: int):
        """Validate the inputs to the buy method."""
        self.validator.assert_valid(
            method_name='buy',
            parameter_name='_listingId',
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name='buy',
            parameter_name='_buyFor',
            argument_value=buy_for,
        )
        buy_for = self.validate_and_checksum_address(buy_for)
        self.validator.assert_valid(
            method_name='buy',
            parameter_name='_quantityToBuy',
            argument_value=quantity_to_buy,
        )
        # safeguard against fractional inputs
        quantity_to_buy = int(quantity_to_buy)
        self.validator.assert_valid(
            method_name='buy',
            parameter_name='_currency',
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name='buy',
            parameter_name='_totalPrice',
            argument_value=total_price,
        )
        # safeguard against fractional inputs
        total_price = int(total_price)
        return (listing_id, buy_for, quantity_to_buy, currency, total_price)

    def call(self, listing_id: int, buy_for: str, quantity_to_buy: int, currency: str, total_price: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, buy_for, quantity_to_buy, currency, total_price) = self.validate_and_normalize_inputs(listing_id, buy_for, quantity_to_buy, currency, total_price)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, buy_for, quantity_to_buy, currency, total_price).call(tx_params.as_dict())

    def send_transaction(self, listing_id: int, buy_for: str, quantity_to_buy: int, currency: str, total_price: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, buy_for, quantity_to_buy, currency, total_price) = self.validate_and_normalize_inputs(listing_id, buy_for, quantity_to_buy, currency, total_price)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, buy_for, quantity_to_buy, currency, total_price).transact(tx_params.as_dict())

    def build_transaction(self, listing_id: int, buy_for: str, quantity_to_buy: int, currency: str, total_price: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, buy_for, quantity_to_buy, currency, total_price) = self.validate_and_normalize_inputs(listing_id, buy_for, quantity_to_buy, currency, total_price)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, buy_for, quantity_to_buy, currency, total_price).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, listing_id: int, buy_for: str, quantity_to_buy: int, currency: str, total_price: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, buy_for, quantity_to_buy, currency, total_price) = self.validate_and_normalize_inputs(listing_id, buy_for, quantity_to_buy, currency, total_price)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, buy_for, quantity_to_buy, currency, total_price).estimateGas(tx_params.as_dict())

class CancelDirectListingMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the cancelDirectListing method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, listing_id: int):
        """Validate the inputs to the cancelDirectListing method."""
        self.validator.assert_valid(
            method_name='cancelDirectListing',
            parameter_name='_listingId',
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        return (listing_id)

    def call(self, listing_id: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id).call(tx_params.as_dict())

    def send_transaction(self, listing_id: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).transact(tx_params.as_dict())

    def build_transaction(self, listing_id: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, listing_id: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).estimateGas(tx_params.as_dict())

class CloseAuctionMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the closeAuction method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, listing_id: int, close_for: str):
        """Validate the inputs to the closeAuction method."""
        self.validator.assert_valid(
            method_name='closeAuction',
            parameter_name='_listingId',
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name='closeAuction',
            parameter_name='_closeFor',
            argument_value=close_for,
        )
        close_for = self.validate_and_checksum_address(close_for)
        return (listing_id, close_for)

    def call(self, listing_id: int, close_for: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, close_for) = self.validate_and_normalize_inputs(listing_id, close_for)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, close_for).call(tx_params.as_dict())

    def send_transaction(self, listing_id: int, close_for: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, close_for) = self.validate_and_normalize_inputs(listing_id, close_for)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, close_for).transact(tx_params.as_dict())

    def build_transaction(self, listing_id: int, close_for: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, close_for) = self.validate_and_normalize_inputs(listing_id, close_for)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, close_for).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, listing_id: int, close_for: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, close_for) = self.validate_and_normalize_inputs(listing_id, close_for)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, close_for).estimateGas(tx_params.as_dict())

class ContractTypeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the contractType method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class ContractUriMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the contractURI method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class ContractVersionMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the contractVersion method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class CreateListingMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the createListing method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, params: IMarketplaceListingParameters):
        """Validate the inputs to the createListing method."""
        self.validator.assert_valid(
            method_name='createListing',
            parameter_name='_params',
            argument_value=params,
        )
        return (params)

    def call(self, params: IMarketplaceListingParameters, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(params).call(tx_params.as_dict())

    def send_transaction(self, params: IMarketplaceListingParameters, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).transact(tx_params.as_dict())

    def build_transaction(self, params: IMarketplaceListingParameters, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, params: IMarketplaceListingParameters, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).estimateGas(tx_params.as_dict())

class GetPlatformFeeInfoMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getPlatformFeeInfo method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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
        return (returned[0],returned[1],)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class GetRoleAdminMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRoleAdmin method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleAdmin method."""
        self.validator.assert_valid(
            method_name='getRoleAdmin',
            parameter_name='role',
            argument_value=role,
        )
        return (role)

    def call(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())

class GetRoleMemberMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRoleMember method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], index: int):
        """Validate the inputs to the getRoleMember method."""
        self.validator.assert_valid(
            method_name='getRoleMember',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='getRoleMember',
            parameter_name='index',
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (role, index)

    def call(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, index).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], index: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).estimateGas(tx_params.as_dict())

class GetRoleMemberCountMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRoleMemberCount method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleMemberCount method."""
        self.validator.assert_valid(
            method_name='getRoleMemberCount',
            parameter_name='role',
            argument_value=role,
        )
        return (role)

    def call(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())

class GrantRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the grantRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the grantRole method."""
        self.validator.assert_valid(
            method_name='grantRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='grantRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class HasRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the hasRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the hasRole method."""
        self.validator.assert_valid(
            method_name='hasRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='hasRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, account).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class InitializeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the initialize method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, default_admin: str, contract_uri: str, trusted_forwarders: List[str], platform_fee_recipient: str, platform_fee_bps: int):
        """Validate the inputs to the initialize method."""
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_defaultAdmin',
            argument_value=default_admin,
        )
        default_admin = self.validate_and_checksum_address(default_admin)
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_contractURI',
            argument_value=contract_uri,
        )
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_trustedForwarders',
            argument_value=trusted_forwarders,
        )
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_platformFeeRecipient',
            argument_value=platform_fee_recipient,
        )
        platform_fee_recipient = self.validate_and_checksum_address(platform_fee_recipient)
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_platformFeeBps',
            argument_value=platform_fee_bps,
        )
        # safeguard against fractional inputs
        platform_fee_bps = int(platform_fee_bps)
        return (default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps)

    def call(self, default_admin: str, contract_uri: str, trusted_forwarders: List[str], platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps).call(tx_params.as_dict())

    def send_transaction(self, default_admin: str, contract_uri: str, trusted_forwarders: List[str], platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps).transact(tx_params.as_dict())

    def build_transaction(self, default_admin: str, contract_uri: str, trusted_forwarders: List[str], platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, default_admin: str, contract_uri: str, trusted_forwarders: List[str], platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps).estimateGas(tx_params.as_dict())

class IsTrustedForwarderMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isTrustedForwarder method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, forwarder: str):
        """Validate the inputs to the isTrustedForwarder method."""
        self.validator.assert_valid(
            method_name='isTrustedForwarder',
            parameter_name='forwarder',
            argument_value=forwarder,
        )
        forwarder = self.validate_and_checksum_address(forwarder)
        return (forwarder)

    def call(self, forwarder: str, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(forwarder).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, forwarder: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).transact(tx_params.as_dict())

    def build_transaction(self, forwarder: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, forwarder: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).estimateGas(tx_params.as_dict())

class ListingsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the listings method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the listings method."""
        self.validator.assert_valid(
            method_name='listings',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> Tuple[int, str, str, int, int, int, int, str, int, int, int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (returned[0],returned[1],returned[2],returned[3],returned[4],returned[5],returned[6],returned[7],returned[8],returned[9],returned[10],returned[11],)

    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class MulticallMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the multicall method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, data: List[Union[bytes, str]]):
        """Validate the inputs to the multicall method."""
        self.validator.assert_valid(
            method_name='multicall',
            parameter_name='data',
            argument_value=data,
        )
        return (data)

    def call(self, data: List[Union[bytes, str]], tx_params: Optional[TxParams] = None) -> List[Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data).call(tx_params.as_dict())
        return [Union[bytes, str](element) for element in returned]

    def send_transaction(self, data: List[Union[bytes, str]], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).transact(tx_params.as_dict())

    def build_transaction(self, data: List[Union[bytes, str]], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, data: List[Union[bytes, str]], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).estimateGas(tx_params.as_dict())

class OfferMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the offer method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, listing_id: int, quantity_wanted: int, currency: str, price_per_token: int, expiration_timestamp: int):
        """Validate the inputs to the offer method."""
        self.validator.assert_valid(
            method_name='offer',
            parameter_name='_listingId',
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name='offer',
            parameter_name='_quantityWanted',
            argument_value=quantity_wanted,
        )
        # safeguard against fractional inputs
        quantity_wanted = int(quantity_wanted)
        self.validator.assert_valid(
            method_name='offer',
            parameter_name='_currency',
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name='offer',
            parameter_name='_pricePerToken',
            argument_value=price_per_token,
        )
        # safeguard against fractional inputs
        price_per_token = int(price_per_token)
        self.validator.assert_valid(
            method_name='offer',
            parameter_name='_expirationTimestamp',
            argument_value=expiration_timestamp,
        )
        # safeguard against fractional inputs
        expiration_timestamp = int(expiration_timestamp)
        return (listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp)

    def call(self, listing_id: int, quantity_wanted: int, currency: str, price_per_token: int, expiration_timestamp: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp) = self.validate_and_normalize_inputs(listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp).call(tx_params.as_dict())

    def send_transaction(self, listing_id: int, quantity_wanted: int, currency: str, price_per_token: int, expiration_timestamp: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp) = self.validate_and_normalize_inputs(listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp).transact(tx_params.as_dict())

    def build_transaction(self, listing_id: int, quantity_wanted: int, currency: str, price_per_token: int, expiration_timestamp: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp) = self.validate_and_normalize_inputs(listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, listing_id: int, quantity_wanted: int, currency: str, price_per_token: int, expiration_timestamp: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp) = self.validate_and_normalize_inputs(listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity_wanted, currency, price_per_token, expiration_timestamp).estimateGas(tx_params.as_dict())

class OffersMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the offers method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int, index_1: str):
        """Validate the inputs to the offers method."""
        self.validator.assert_valid(
            method_name='offers',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        self.validator.assert_valid(
            method_name='offers',
            parameter_name='index_1',
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        return (index_0, index_1)

    def call(self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None) -> Tuple[int, str, int, str, int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1).call(tx_params.as_dict())
        return (returned[0],returned[1],returned[2],returned[3],returned[4],returned[5],)

    def send_transaction(self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(tx_params.as_dict())

class OnErc1155BatchReceivedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the onERC1155BatchReceived method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str, index_1: str, index_2: List[int], index_3: List[int], index_4: Union[bytes, str]):
        """Validate the inputs to the onERC1155BatchReceived method."""
        self.validator.assert_valid(
            method_name='onERC1155BatchReceived',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name='onERC1155BatchReceived',
            parameter_name='index_1',
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name='onERC1155BatchReceived',
            parameter_name='index_2',
            argument_value=index_2,
        )
        self.validator.assert_valid(
            method_name='onERC1155BatchReceived',
            parameter_name='index_3',
            argument_value=index_3,
        )
        self.validator.assert_valid(
            method_name='onERC1155BatchReceived',
            parameter_name='index_4',
            argument_value=index_4,
        )
        return (index_0, index_1, index_2, index_3, index_4)

    def call(self, index_0: str, index_1: str, index_2: List[int], index_3: List[int], index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1, index_2, index_3, index_4).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, index_0: str, index_1: str, index_2: List[int], index_3: List[int], index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, index_1: str, index_2: List[int], index_3: List[int], index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, index_1: str, index_2: List[int], index_3: List[int], index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).estimateGas(tx_params.as_dict())

class OnErc1155ReceivedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the onERC1155Received method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str, index_1: str, index_2: int, index_3: int, index_4: Union[bytes, str]):
        """Validate the inputs to the onERC1155Received method."""
        self.validator.assert_valid(
            method_name='onERC1155Received',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name='onERC1155Received',
            parameter_name='index_1',
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name='onERC1155Received',
            parameter_name='index_2',
            argument_value=index_2,
        )
        # safeguard against fractional inputs
        index_2 = int(index_2)
        self.validator.assert_valid(
            method_name='onERC1155Received',
            parameter_name='index_3',
            argument_value=index_3,
        )
        # safeguard against fractional inputs
        index_3 = int(index_3)
        self.validator.assert_valid(
            method_name='onERC1155Received',
            parameter_name='index_4',
            argument_value=index_4,
        )
        return (index_0, index_1, index_2, index_3, index_4)

    def call(self, index_0: str, index_1: str, index_2: int, index_3: int, index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1, index_2, index_3, index_4).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, index_0: str, index_1: str, index_2: int, index_3: int, index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, index_1: str, index_2: int, index_3: int, index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, index_1: str, index_2: int, index_3: int, index_4: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1, index_2, index_3, index_4) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3, index_4).estimateGas(tx_params.as_dict())

class OnErc721ReceivedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the onERC721Received method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: str, index_1: str, index_2: int, index_3: Union[bytes, str]):
        """Validate the inputs to the onERC721Received method."""
        self.validator.assert_valid(
            method_name='onERC721Received',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name='onERC721Received',
            parameter_name='index_1',
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name='onERC721Received',
            parameter_name='index_2',
            argument_value=index_2,
        )
        # safeguard against fractional inputs
        index_2 = int(index_2)
        self.validator.assert_valid(
            method_name='onERC721Received',
            parameter_name='index_3',
            argument_value=index_3,
        )
        return (index_0, index_1, index_2, index_3)

    def call(self, index_0: str, index_1: str, index_2: int, index_3: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1, index_2, index_3) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1, index_2, index_3).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(self, index_0: str, index_1: str, index_2: int, index_3: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1, index_2, index_3) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, index_1: str, index_2: int, index_3: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1, index_2, index_3) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, index_1: str, index_2: int, index_3: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1, index_2, index_3) = self.validate_and_normalize_inputs(index_0, index_1, index_2, index_3)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1, index_2, index_3).estimateGas(tx_params.as_dict())

class RenounceRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the renounceRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the renounceRole method."""
        self.validator.assert_valid(
            method_name='renounceRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='renounceRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class RevokeRoleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the revokeRole method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, role: Union[bytes, str], account: str):
        """Validate the inputs to the revokeRole method."""
        self.validator.assert_valid(
            method_name='revokeRole',
            parameter_name='role',
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name='revokeRole',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(tx_params.as_dict())

    def build_transaction(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, role: Union[bytes, str], account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(tx_params.as_dict())

class SetAuctionBuffersMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setAuctionBuffers method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, time_buffer: int, bid_buffer_bps: int):
        """Validate the inputs to the setAuctionBuffers method."""
        self.validator.assert_valid(
            method_name='setAuctionBuffers',
            parameter_name='_timeBuffer',
            argument_value=time_buffer,
        )
        # safeguard against fractional inputs
        time_buffer = int(time_buffer)
        self.validator.assert_valid(
            method_name='setAuctionBuffers',
            parameter_name='_bidBufferBps',
            argument_value=bid_buffer_bps,
        )
        # safeguard against fractional inputs
        bid_buffer_bps = int(bid_buffer_bps)
        return (time_buffer, bid_buffer_bps)

    def call(self, time_buffer: int, bid_buffer_bps: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (time_buffer, bid_buffer_bps) = self.validate_and_normalize_inputs(time_buffer, bid_buffer_bps)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(time_buffer, bid_buffer_bps).call(tx_params.as_dict())

    def send_transaction(self, time_buffer: int, bid_buffer_bps: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (time_buffer, bid_buffer_bps) = self.validate_and_normalize_inputs(time_buffer, bid_buffer_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time_buffer, bid_buffer_bps).transact(tx_params.as_dict())

    def build_transaction(self, time_buffer: int, bid_buffer_bps: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (time_buffer, bid_buffer_bps) = self.validate_and_normalize_inputs(time_buffer, bid_buffer_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time_buffer, bid_buffer_bps).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, time_buffer: int, bid_buffer_bps: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (time_buffer, bid_buffer_bps) = self.validate_and_normalize_inputs(time_buffer, bid_buffer_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time_buffer, bid_buffer_bps).estimateGas(tx_params.as_dict())

class SetContractUriMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setContractURI method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, uri: str):
        """Validate the inputs to the setContractURI method."""
        self.validator.assert_valid(
            method_name='setContractURI',
            parameter_name='_uri',
            argument_value=uri,
        )
        return (uri)

    def call(self, uri: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(uri).call(tx_params.as_dict())

    def send_transaction(self, uri: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).transact(tx_params.as_dict())

    def build_transaction(self, uri: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, uri: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).estimateGas(tx_params.as_dict())

class SetPlatformFeeInfoMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setPlatformFeeInfo method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, platform_fee_recipient: str, platform_fee_bps: int):
        """Validate the inputs to the setPlatformFeeInfo method."""
        self.validator.assert_valid(
            method_name='setPlatformFeeInfo',
            parameter_name='_platformFeeRecipient',
            argument_value=platform_fee_recipient,
        )
        platform_fee_recipient = self.validate_and_checksum_address(platform_fee_recipient)
        self.validator.assert_valid(
            method_name='setPlatformFeeInfo',
            parameter_name='_platformFeeBps',
            argument_value=platform_fee_bps,
        )
        # safeguard against fractional inputs
        platform_fee_bps = int(platform_fee_bps)
        return (platform_fee_recipient, platform_fee_bps)

    def call(self, platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(platform_fee_recipient, platform_fee_bps).call(tx_params.as_dict())

    def send_transaction(self, platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(platform_fee_recipient, platform_fee_bps).transact(tx_params.as_dict())

    def build_transaction(self, platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(platform_fee_recipient, platform_fee_bps).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, platform_fee_recipient: str, platform_fee_bps: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (platform_fee_recipient, platform_fee_bps) = self.validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(platform_fee_recipient, platform_fee_bps).estimateGas(tx_params.as_dict())

class SupportsInterfaceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the supportsInterface method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, interface_id: Union[bytes, str]):
        """Validate the inputs to the supportsInterface method."""
        self.validator.assert_valid(
            method_name='supportsInterface',
            parameter_name='interfaceId',
            argument_value=interface_id,
        )
        return (interface_id)

    def call(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(interface_id).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).transact(tx_params.as_dict())

    def build_transaction(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).estimateGas(tx_params.as_dict())

class TimeBufferMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the timeBuffer method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class TotalListingsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the totalListings method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
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

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
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

class UpdateListingMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the updateListing method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, listing_id: int, quantity_to_list: int, reserve_price_per_token: int, buyout_price_per_token: int, currency_to_accept: str, start_time: int, seconds_until_end_time: int):
        """Validate the inputs to the updateListing method."""
        self.validator.assert_valid(
            method_name='updateListing',
            parameter_name='_listingId',
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name='updateListing',
            parameter_name='_quantityToList',
            argument_value=quantity_to_list,
        )
        # safeguard against fractional inputs
        quantity_to_list = int(quantity_to_list)
        self.validator.assert_valid(
            method_name='updateListing',
            parameter_name='_reservePricePerToken',
            argument_value=reserve_price_per_token,
        )
        # safeguard against fractional inputs
        reserve_price_per_token = int(reserve_price_per_token)
        self.validator.assert_valid(
            method_name='updateListing',
            parameter_name='_buyoutPricePerToken',
            argument_value=buyout_price_per_token,
        )
        # safeguard against fractional inputs
        buyout_price_per_token = int(buyout_price_per_token)
        self.validator.assert_valid(
            method_name='updateListing',
            parameter_name='_currencyToAccept',
            argument_value=currency_to_accept,
        )
        currency_to_accept = self.validate_and_checksum_address(currency_to_accept)
        self.validator.assert_valid(
            method_name='updateListing',
            parameter_name='_startTime',
            argument_value=start_time,
        )
        # safeguard against fractional inputs
        start_time = int(start_time)
        self.validator.assert_valid(
            method_name='updateListing',
            parameter_name='_secondsUntilEndTime',
            argument_value=seconds_until_end_time,
        )
        # safeguard against fractional inputs
        seconds_until_end_time = int(seconds_until_end_time)
        return (listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time)

    def call(self, listing_id: int, quantity_to_list: int, reserve_price_per_token: int, buyout_price_per_token: int, currency_to_accept: str, start_time: int, seconds_until_end_time: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time) = self.validate_and_normalize_inputs(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time).call(tx_params.as_dict())

    def send_transaction(self, listing_id: int, quantity_to_list: int, reserve_price_per_token: int, buyout_price_per_token: int, currency_to_accept: str, start_time: int, seconds_until_end_time: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time) = self.validate_and_normalize_inputs(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time).transact(tx_params.as_dict())

    def build_transaction(self, listing_id: int, quantity_to_list: int, reserve_price_per_token: int, buyout_price_per_token: int, currency_to_accept: str, start_time: int, seconds_until_end_time: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time) = self.validate_and_normalize_inputs(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, listing_id: int, quantity_to_list: int, reserve_price_per_token: int, buyout_price_per_token: int, currency_to_accept: str, start_time: int, seconds_until_end_time: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time) = self.validate_and_normalize_inputs(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time).estimateGas(tx_params.as_dict())

class WinningBidMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the winningBid method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the winningBid method."""
        self.validator.assert_valid(
            method_name='winningBid',
            parameter_name='index_0',
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return (index_0)

    def call(self, index_0: int, tx_params: Optional[TxParams] = None) -> Tuple[int, str, int, str, int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (returned[0],returned[1],returned[2],returned[3],returned[4],returned[5],)

    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Marketplace:
    """Wrapper class for Marketplace Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """
    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

    max_bps: MaxBpsMethod
    """Constructor-initialized instance of
    :class:`MaxBpsMethod`.
    """

    accept_offer: AcceptOfferMethod
    """Constructor-initialized instance of
    :class:`AcceptOfferMethod`.
    """

    bid_buffer_bps: BidBufferBpsMethod
    """Constructor-initialized instance of
    :class:`BidBufferBpsMethod`.
    """

    buy: BuyMethod
    """Constructor-initialized instance of
    :class:`BuyMethod`.
    """

    cancel_direct_listing: CancelDirectListingMethod
    """Constructor-initialized instance of
    :class:`CancelDirectListingMethod`.
    """

    close_auction: CloseAuctionMethod
    """Constructor-initialized instance of
    :class:`CloseAuctionMethod`.
    """

    contract_type: ContractTypeMethod
    """Constructor-initialized instance of
    :class:`ContractTypeMethod`.
    """

    contract_uri: ContractUriMethod
    """Constructor-initialized instance of
    :class:`ContractUriMethod`.
    """

    contract_version: ContractVersionMethod
    """Constructor-initialized instance of
    :class:`ContractVersionMethod`.
    """

    create_listing: CreateListingMethod
    """Constructor-initialized instance of
    :class:`CreateListingMethod`.
    """

    get_platform_fee_info: GetPlatformFeeInfoMethod
    """Constructor-initialized instance of
    :class:`GetPlatformFeeInfoMethod`.
    """

    get_role_admin: GetRoleAdminMethod
    """Constructor-initialized instance of
    :class:`GetRoleAdminMethod`.
    """

    get_role_member: GetRoleMemberMethod
    """Constructor-initialized instance of
    :class:`GetRoleMemberMethod`.
    """

    get_role_member_count: GetRoleMemberCountMethod
    """Constructor-initialized instance of
    :class:`GetRoleMemberCountMethod`.
    """

    grant_role: GrantRoleMethod
    """Constructor-initialized instance of
    :class:`GrantRoleMethod`.
    """

    has_role: HasRoleMethod
    """Constructor-initialized instance of
    :class:`HasRoleMethod`.
    """

    initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
    """

    is_trusted_forwarder: IsTrustedForwarderMethod
    """Constructor-initialized instance of
    :class:`IsTrustedForwarderMethod`.
    """

    listings: ListingsMethod
    """Constructor-initialized instance of
    :class:`ListingsMethod`.
    """

    multicall: MulticallMethod
    """Constructor-initialized instance of
    :class:`MulticallMethod`.
    """

    offer: OfferMethod
    """Constructor-initialized instance of
    :class:`OfferMethod`.
    """

    offers: OffersMethod
    """Constructor-initialized instance of
    :class:`OffersMethod`.
    """

    on_erc1155_batch_received: OnErc1155BatchReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc1155BatchReceivedMethod`.
    """

    on_erc1155_received: OnErc1155ReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc1155ReceivedMethod`.
    """

    on_erc721_received: OnErc721ReceivedMethod
    """Constructor-initialized instance of
    :class:`OnErc721ReceivedMethod`.
    """

    renounce_role: RenounceRoleMethod
    """Constructor-initialized instance of
    :class:`RenounceRoleMethod`.
    """

    revoke_role: RevokeRoleMethod
    """Constructor-initialized instance of
    :class:`RevokeRoleMethod`.
    """

    set_auction_buffers: SetAuctionBuffersMethod
    """Constructor-initialized instance of
    :class:`SetAuctionBuffersMethod`.
    """

    set_contract_uri: SetContractUriMethod
    """Constructor-initialized instance of
    :class:`SetContractUriMethod`.
    """

    set_platform_fee_info: SetPlatformFeeInfoMethod
    """Constructor-initialized instance of
    :class:`SetPlatformFeeInfoMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    time_buffer: TimeBufferMethod
    """Constructor-initialized instance of
    :class:`TimeBufferMethod`.
    """

    total_listings: TotalListingsMethod
    """Constructor-initialized instance of
    :class:`TotalListingsMethod`.
    """

    update_listing: UpdateListingMethod
    """Constructor-initialized instance of
    :class:`UpdateListingMethod`.
    """

    winning_bid: WinningBidMethod
    """Constructor-initialized instance of
    :class:`WinningBidMethod`.
    """


    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: MarketplaceValidator = None,
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
            validator = MarketplaceValidator(web3_or_provider, contract_address)

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
                         middleware['function'], layer=middleware['layer'],
                    )
            except ValueError as value_error:
                if value_error.args == ("You can't add the same un-named instance twice",):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=Marketplace.abi()).functions

        self.default_admin_role = DefaultAdminRoleMethod(web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE)

        self.max_bps = MaxBpsMethod(web3_or_provider, contract_address, functions.MAX_BPS)

        self.accept_offer = AcceptOfferMethod(web3_or_provider, contract_address, functions.acceptOffer, validator)

        self.bid_buffer_bps = BidBufferBpsMethod(web3_or_provider, contract_address, functions.bidBufferBps)

        self.buy = BuyMethod(web3_or_provider, contract_address, functions.buy, validator)

        self.cancel_direct_listing = CancelDirectListingMethod(web3_or_provider, contract_address, functions.cancelDirectListing, validator)

        self.close_auction = CloseAuctionMethod(web3_or_provider, contract_address, functions.closeAuction, validator)

        self.contract_type = ContractTypeMethod(web3_or_provider, contract_address, functions.contractType)

        self.contract_uri = ContractUriMethod(web3_or_provider, contract_address, functions.contractURI)

        self.contract_version = ContractVersionMethod(web3_or_provider, contract_address, functions.contractVersion)

        self.create_listing = CreateListingMethod(web3_or_provider, contract_address, functions.createListing, validator)

        self.get_platform_fee_info = GetPlatformFeeInfoMethod(web3_or_provider, contract_address, functions.getPlatformFeeInfo)

        self.get_role_admin = GetRoleAdminMethod(web3_or_provider, contract_address, functions.getRoleAdmin, validator)

        self.get_role_member = GetRoleMemberMethod(web3_or_provider, contract_address, functions.getRoleMember, validator)

        self.get_role_member_count = GetRoleMemberCountMethod(web3_or_provider, contract_address, functions.getRoleMemberCount, validator)

        self.grant_role = GrantRoleMethod(web3_or_provider, contract_address, functions.grantRole, validator)

        self.has_role = HasRoleMethod(web3_or_provider, contract_address, functions.hasRole, validator)

        self.initialize = InitializeMethod(web3_or_provider, contract_address, functions.initialize, validator)

        self.is_trusted_forwarder = IsTrustedForwarderMethod(web3_or_provider, contract_address, functions.isTrustedForwarder, validator)

        self.listings = ListingsMethod(web3_or_provider, contract_address, functions.listings, validator)

        self.multicall = MulticallMethod(web3_or_provider, contract_address, functions.multicall, validator)

        self.offer = OfferMethod(web3_or_provider, contract_address, functions.offer, validator)

        self.offers = OffersMethod(web3_or_provider, contract_address, functions.offers, validator)

        self.on_erc1155_batch_received = OnErc1155BatchReceivedMethod(web3_or_provider, contract_address, functions.onERC1155BatchReceived, validator)

        self.on_erc1155_received = OnErc1155ReceivedMethod(web3_or_provider, contract_address, functions.onERC1155Received, validator)

        self.on_erc721_received = OnErc721ReceivedMethod(web3_or_provider, contract_address, functions.onERC721Received, validator)

        self.renounce_role = RenounceRoleMethod(web3_or_provider, contract_address, functions.renounceRole, validator)

        self.revoke_role = RevokeRoleMethod(web3_or_provider, contract_address, functions.revokeRole, validator)

        self.set_auction_buffers = SetAuctionBuffersMethod(web3_or_provider, contract_address, functions.setAuctionBuffers, validator)

        self.set_contract_uri = SetContractUriMethod(web3_or_provider, contract_address, functions.setContractURI, validator)

        self.set_platform_fee_info = SetPlatformFeeInfoMethod(web3_or_provider, contract_address, functions.setPlatformFeeInfo, validator)

        self.supports_interface = SupportsInterfaceMethod(web3_or_provider, contract_address, functions.supportsInterface, validator)

        self.time_buffer = TimeBufferMethod(web3_or_provider, contract_address, functions.timeBuffer)

        self.total_listings = TotalListingsMethod(web3_or_provider, contract_address, functions.totalListings)

        self.update_listing = UpdateListingMethod(web3_or_provider, contract_address, functions.updateListing, validator)

        self.winning_bid = WinningBidMethod(web3_or_provider, contract_address, functions.winningBid, validator)

    def get_auction_buffers_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AuctionBuffersUpdated event.

        :param tx_hash: hash of transaction emitting AuctionBuffersUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.AuctionBuffersUpdated().processReceipt(tx_receipt)
    def get_auction_closed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AuctionClosed event.

        :param tx_hash: hash of transaction emitting AuctionClosed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.AuctionClosed().processReceipt(tx_receipt)
    def get_initialized_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Initialized event.

        :param tx_hash: hash of transaction emitting Initialized event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.Initialized().processReceipt(tx_receipt)
    def get_listing_added_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ListingAdded event.

        :param tx_hash: hash of transaction emitting ListingAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.ListingAdded().processReceipt(tx_receipt)
    def get_listing_removed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ListingRemoved event.

        :param tx_hash: hash of transaction emitting ListingRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.ListingRemoved().processReceipt(tx_receipt)
    def get_listing_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ListingUpdated event.

        :param tx_hash: hash of transaction emitting ListingUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.ListingUpdated().processReceipt(tx_receipt)
    def get_new_offer_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NewOffer event.

        :param tx_hash: hash of transaction emitting NewOffer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.NewOffer().processReceipt(tx_receipt)
    def get_new_sale_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NewSale event.

        :param tx_hash: hash of transaction emitting NewSale event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.NewSale().processReceipt(tx_receipt)
    def get_platform_fee_info_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PlatformFeeInfoUpdated event.

        :param tx_hash: hash of transaction emitting PlatformFeeInfoUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.PlatformFeeInfoUpdated().processReceipt(tx_receipt)
    def get_role_admin_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleAdminChanged event.

        :param tx_hash: hash of transaction emitting RoleAdminChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.RoleAdminChanged().processReceipt(tx_receipt)
    def get_role_granted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleGranted event.

        :param tx_hash: hash of transaction emitting RoleGranted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.RoleGranted().processReceipt(tx_receipt)
    def get_role_revoked_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleRevoked event.

        :param tx_hash: hash of transaction emitting RoleRevoked event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Marketplace.abi()).events.RoleRevoked().processReceipt(tx_receipt)

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_nativeTokenWrapper","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timeBuffer","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"bidBufferBps","type":"uint256"}],"name":"AuctionBuffersUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"closer","type":"address"},{"indexed":true,"internalType":"bool","name":"cancelled","type":"bool"},{"indexed":false,"internalType":"address","name":"auctionCreator","type":"address"},{"indexed":false,"internalType":"address","name":"winningBidder","type":"address"}],"name":"AuctionClosed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"indexed":true,"internalType":"address","name":"lister","type":"address"},{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"endTime","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"reservePricePerToken","type":"uint256"},{"internalType":"uint256","name":"buyoutPricePerToken","type":"uint256"},{"internalType":"enum IMarketplace.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IMarketplace.ListingType","name":"listingType","type":"uint8"}],"indexed":false,"internalType":"struct IMarketplace.Listing","name":"listing","type":"tuple"}],"name":"ListingAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"listingCreator","type":"address"}],"name":"ListingRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"listingCreator","type":"address"}],"name":"ListingUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"offeror","type":"address"},{"indexed":true,"internalType":"enum IMarketplace.ListingType","name":"listingType","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"quantityWanted","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalOfferAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"currency","type":"address"}],"name":"NewOffer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"indexed":true,"internalType":"address","name":"lister","type":"address"},{"indexed":false,"internalType":"address","name":"buyer","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantityBought","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalPricePaid","type":"uint256"}],"name":"NewSale","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"platformFeeRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"platformFeeBps","type":"uint256"}],"name":"PlatformFeeInfoUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_BPS","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_offeror","type":"address"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"}],"name":"acceptOffer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"bidBufferBps","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_buyFor","type":"address"},{"internalType":"uint256","name":"_quantityToBuy","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_totalPrice","type":"uint256"}],"name":"buy","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"}],"name":"cancelDirectListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_closeFor","type":"address"}],"name":"closeAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"contractType","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractVersion","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"secondsUntilEndTime","type":"uint256"},{"internalType":"uint256","name":"quantityToList","type":"uint256"},{"internalType":"address","name":"currencyToAccept","type":"address"},{"internalType":"uint256","name":"reservePricePerToken","type":"uint256"},{"internalType":"uint256","name":"buyoutPricePerToken","type":"uint256"},{"internalType":"enum IMarketplace.ListingType","name":"listingType","type":"uint8"}],"internalType":"struct IMarketplace.ListingParameters","name":"_params","type":"tuple"}],"name":"createListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getPlatformFeeInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_defaultAdmin","type":"address"},{"internalType":"string","name":"_contractURI","type":"string"},{"internalType":"address[]","name":"_trustedForwarders","type":"address[]"},{"internalType":"address","name":"_platformFeeRecipient","type":"address"},{"internalType":"uint256","name":"_platformFeeBps","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"listings","outputs":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"endTime","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"reservePricePerToken","type":"uint256"},{"internalType":"uint256","name":"buyoutPricePerToken","type":"uint256"},{"internalType":"enum IMarketplace.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IMarketplace.ListingType","name":"listingType","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"uint256","name":"_quantityWanted","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"},{"internalType":"uint256","name":"_expirationTimestamp","type":"uint256"}],"name":"offer","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"},{"internalType":"address","name":"index_1","type":"address"}],"name":"offers","outputs":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"offeror","type":"address"},{"internalType":"uint256","name":"quantityWanted","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"expirationTimestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256[]","name":"index_2","type":"uint256[]"},{"internalType":"uint256[]","name":"index_3","type":"uint256[]"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155BatchReceived","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"uint256","name":"index_3","type":"uint256"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"bytes","name":"index_3","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_timeBuffer","type":"uint256"},{"internalType":"uint256","name":"_bidBufferBps","type":"uint256"}],"name":"setAuctionBuffers","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_uri","type":"string"}],"name":"setContractURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_platformFeeRecipient","type":"address"},{"internalType":"uint256","name":"_platformFeeBps","type":"uint256"}],"name":"setPlatformFeeInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"timeBuffer","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalListings","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"uint256","name":"_quantityToList","type":"uint256"},{"internalType":"uint256","name":"_reservePricePerToken","type":"uint256"},{"internalType":"uint256","name":"_buyoutPricePerToken","type":"uint256"},{"internalType":"address","name":"_currencyToAccept","type":"address"},{"internalType":"uint256","name":"_startTime","type":"uint256"},{"internalType":"uint256","name":"_secondsUntilEndTime","type":"uint256"}],"name":"updateListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"winningBid","outputs":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"offeror","type":"address"},{"internalType":"uint256","name":"quantityWanted","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"expirationTimestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
