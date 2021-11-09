"""Generated wrapper for Market Solidity contract."""

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
from thirdweb_web3 import Web3
from thirdweb_web3.contract import ContractFunction
from thirdweb_web3.datastructures import AttributeDict
from thirdweb_web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for Market below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        MarketValidator,
    )
except ImportError:

    class MarketValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class MarketListing(TypedDict):
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

    seller: str

    assetContract: str

    tokenId: int

    quantity: int

    currency: str

    pricePerToken: int

    saleStart: int

    saleEnd: int

    tokensPerBuyer: int

    tokenType: int


class DefaultAdminRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the DEFAULT_ADMIN_ROLE method."""

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


class ListerRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the LISTER_ROLE method."""

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


class PauserRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the PAUSER_ROLE method."""

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


class ContractUri_Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the _contractURI method."""

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


class AddToListingMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the addToListing method."""

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

    def validate_and_normalize_inputs(self, listing_id: int, quantity: int):
        """Validate the inputs to the addToListing method."""
        self.validator.assert_valid(
            method_name="addToListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="addToListing",
            parameter_name="_quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        return (listing_id, quantity)

    def call(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, quantity).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity).estimateGas(
            tx_params.as_dict()
        )


class BoughtFromListingMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the boughtFromListing method."""

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

    def validate_and_normalize_inputs(self, index_0: int, index_1: str):
        """Validate the inputs to the boughtFromListing method."""
        self.validator.assert_valid(
            method_name="boughtFromListing",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        self.validator.assert_valid(
            method_name="boughtFromListing",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        return (index_0, index_1)

    def call(
        self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0, index_1).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, index_1: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(
            index_0, index_1
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(
            tx_params.as_dict()
        )


class BuyMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the buy method."""

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

    def validate_and_normalize_inputs(self, listing_id: int, quantity: int):
        """Validate the inputs to the buy method."""
        self.validator.assert_valid(
            method_name="buy",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="buy",
            parameter_name="_quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        return (listing_id, quantity)

    def call(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, quantity).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity).estimateGas(
            tx_params.as_dict()
        )


class ContractUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractURI method."""

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


class GetAllListingsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getAllListings method."""

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
    ) -> List[MarketListing]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            MarketListing(
                listingId=element[0],
                seller=element[1],
                assetContract=element[2],
                tokenId=element[3],
                quantity=element[4],
                currency=element[5],
                pricePerToken=element[6],
                saleStart=element[7],
                saleEnd=element[8],
                tokensPerBuyer=element[9],
                tokenType=element[10],
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
    ) -> MarketListing:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(listing_id).call(
            tx_params.as_dict()
        )
        return MarketListing(
            listingId=returned[0],
            seller=returned[1],
            assetContract=returned[2],
            tokenId=returned[3],
            quantity=returned[4],
            currency=returned[5],
            pricePerToken=returned[6],
            saleStart=returned[7],
            saleEnd=returned[8],
            tokensPerBuyer=returned[9],
            tokenType=returned[10],
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


class GetListingsByAssetMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getListingsByAsset method."""

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
        self, asset_contract: str, token_id: int
    ):
        """Validate the inputs to the getListingsByAsset method."""
        self.validator.assert_valid(
            method_name="getListingsByAsset",
            parameter_name="_assetContract",
            argument_value=asset_contract,
        )
        asset_contract = self.validate_and_checksum_address(asset_contract)
        self.validator.assert_valid(
            method_name="getListingsByAsset",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        return (asset_contract, token_id)

    def call(
        self,
        asset_contract: str,
        token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> List[MarketListing]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (asset_contract, token_id) = self.validate_and_normalize_inputs(
            asset_contract, token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(asset_contract, token_id).call(
            tx_params.as_dict()
        )
        return [
            MarketListing(
                listingId=element[0],
                seller=element[1],
                assetContract=element[2],
                tokenId=element[3],
                quantity=element[4],
                currency=element[5],
                pricePerToken=element[6],
                saleStart=element[7],
                saleEnd=element[8],
                tokensPerBuyer=element[9],
                tokenType=element[10],
            )
            for element in returned
        ]

    def send_transaction(
        self,
        asset_contract: str,
        token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (asset_contract, token_id) = self.validate_and_normalize_inputs(
            asset_contract, token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_contract, token_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        asset_contract: str,
        token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (asset_contract, token_id) = self.validate_and_normalize_inputs(
            asset_contract, token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            asset_contract, token_id
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        asset_contract: str,
        token_id: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (asset_contract, token_id) = self.validate_and_normalize_inputs(
            asset_contract, token_id
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_contract, token_id).estimateGas(
            tx_params.as_dict()
        )


class GetListingsByAssetContractMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getListingsByAssetContract method."""

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

    def validate_and_normalize_inputs(self, asset_contract: str):
        """Validate the inputs to the getListingsByAssetContract method."""
        self.validator.assert_valid(
            method_name="getListingsByAssetContract",
            parameter_name="_assetContract",
            argument_value=asset_contract,
        )
        asset_contract = self.validate_and_checksum_address(asset_contract)
        return asset_contract

    def call(
        self, asset_contract: str, tx_params: Optional[TxParams] = None
    ) -> List[MarketListing]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (asset_contract) = self.validate_and_normalize_inputs(asset_contract)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(asset_contract).call(
            tx_params.as_dict()
        )
        return [
            MarketListing(
                listingId=element[0],
                seller=element[1],
                assetContract=element[2],
                tokenId=element[3],
                quantity=element[4],
                currency=element[5],
                pricePerToken=element[6],
                saleStart=element[7],
                saleEnd=element[8],
                tokensPerBuyer=element[9],
                tokenType=element[10],
            )
            for element in returned
        ]

    def send_transaction(
        self, asset_contract: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (asset_contract) = self.validate_and_normalize_inputs(asset_contract)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_contract).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, asset_contract: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (asset_contract) = self.validate_and_normalize_inputs(asset_contract)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_contract).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, asset_contract: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (asset_contract) = self.validate_and_normalize_inputs(asset_contract)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_contract).estimateGas(
            tx_params.as_dict()
        )


class GetListingsBySellerMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getListingsBySeller method."""

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

    def validate_and_normalize_inputs(self, seller: str):
        """Validate the inputs to the getListingsBySeller method."""
        self.validator.assert_valid(
            method_name="getListingsBySeller",
            parameter_name="_seller",
            argument_value=seller,
        )
        seller = self.validate_and_checksum_address(seller)
        return seller

    def call(
        self, seller: str, tx_params: Optional[TxParams] = None
    ) -> List[MarketListing]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (seller) = self.validate_and_normalize_inputs(seller)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(seller).call(tx_params.as_dict())
        return [
            MarketListing(
                listingId=element[0],
                seller=element[1],
                assetContract=element[2],
                tokenId=element[3],
                quantity=element[4],
                currency=element[5],
                pricePerToken=element[6],
                saleStart=element[7],
                saleEnd=element[8],
                tokensPerBuyer=element[9],
                tokenType=element[10],
            )
            for element in returned
        ]

    def send_transaction(
        self, seller: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (seller) = self.validate_and_normalize_inputs(seller)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(seller).transact(tx_params.as_dict())

    def build_transaction(
        self, seller: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (seller) = self.validate_and_normalize_inputs(seller)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(seller).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, seller: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (seller) = self.validate_and_normalize_inputs(seller)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(seller).estimateGas(tx_params.as_dict())


class GetRoleAdminMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getRoleAdmin method."""

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

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleAdmin method."""
        self.validator.assert_valid(
            method_name="getRoleAdmin",
            parameter_name="role",
            argument_value=role,
        )
        return role

    def call(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())


class GetRoleMemberMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getRoleMember method."""

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
        self, role: Union[bytes, str], index: int
    ):
        """Validate the inputs to the getRoleMember method."""
        self.validator.assert_valid(
            method_name="getRoleMember",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="getRoleMember",
            parameter_name="index",
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return (role, index)

    def call(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, index).call(
            tx_params.as_dict()
        )
        return str(returned)

    def send_transaction(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        index: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, index) = self.validate_and_normalize_inputs(role, index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, index).estimateGas(
            tx_params.as_dict()
        )


class GetRoleMemberCountMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getRoleMemberCount method."""

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

    def validate_and_normalize_inputs(self, role: Union[bytes, str]):
        """Validate the inputs to the getRoleMemberCount method."""
        self.validator.assert_valid(
            method_name="getRoleMemberCount",
            parameter_name="role",
            argument_value=role,
        )
        return role

    def call(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).transact(tx_params.as_dict())

    def build_transaction(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, role: Union[bytes, str], tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (role) = self.validate_and_normalize_inputs(role)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role).estimateGas(tx_params.as_dict())


class GrantRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the grantRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the grantRole method."""
        self.validator.assert_valid(
            method_name="grantRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="grantRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class HasRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the hasRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the hasRole method."""
        self.validator.assert_valid(
            method_name="hasRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="hasRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(role, account).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class IsTrustedForwarderMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isTrustedForwarder method."""

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

    def validate_and_normalize_inputs(self, forwarder: str):
        """Validate the inputs to the isTrustedForwarder method."""
        self.validator.assert_valid(
            method_name="isTrustedForwarder",
            parameter_name="forwarder",
            argument_value=forwarder,
        )
        forwarder = self.validate_and_checksum_address(forwarder)
        return forwarder

    def call(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(forwarder).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).transact(tx_params.as_dict())

    def build_transaction(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, forwarder: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (forwarder) = self.validate_and_normalize_inputs(forwarder)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(forwarder).estimateGas(
            tx_params.as_dict()
        )


class ListMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the list method."""

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
        asset_contract: str,
        token_id: int,
        currency: str,
        price_per_token: int,
        quantity: int,
        tokens_per_buyer: int,
        seconds_until_start: int,
        seconds_until_end: int,
    ):
        """Validate the inputs to the list method."""
        self.validator.assert_valid(
            method_name="list",
            parameter_name="_assetContract",
            argument_value=asset_contract,
        )
        asset_contract = self.validate_and_checksum_address(asset_contract)
        self.validator.assert_valid(
            method_name="list",
            parameter_name="_tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="list",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name="list",
            parameter_name="_pricePerToken",
            argument_value=price_per_token,
        )
        # safeguard against fractional inputs
        price_per_token = int(price_per_token)
        self.validator.assert_valid(
            method_name="list",
            parameter_name="_quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name="list",
            parameter_name="_tokensPerBuyer",
            argument_value=tokens_per_buyer,
        )
        # safeguard against fractional inputs
        tokens_per_buyer = int(tokens_per_buyer)
        self.validator.assert_valid(
            method_name="list",
            parameter_name="_secondsUntilStart",
            argument_value=seconds_until_start,
        )
        # safeguard against fractional inputs
        seconds_until_start = int(seconds_until_start)
        self.validator.assert_valid(
            method_name="list",
            parameter_name="_secondsUntilEnd",
            argument_value=seconds_until_end,
        )
        # safeguard against fractional inputs
        seconds_until_end = int(seconds_until_end)
        return (
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        )

    def call(
        self,
        asset_contract: str,
        token_id: int,
        currency: str,
        price_per_token: int,
        quantity: int,
        tokens_per_buyer: int,
        seconds_until_start: int,
        seconds_until_end: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ) = self.validate_and_normalize_inputs(
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        asset_contract: str,
        token_id: int,
        currency: str,
        price_per_token: int,
        quantity: int,
        tokens_per_buyer: int,
        seconds_until_start: int,
        seconds_until_end: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ) = self.validate_and_normalize_inputs(
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        asset_contract: str,
        token_id: int,
        currency: str,
        price_per_token: int,
        quantity: int,
        tokens_per_buyer: int,
        seconds_until_start: int,
        seconds_until_end: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ) = self.validate_and_normalize_inputs(
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        asset_contract: str,
        token_id: int,
        currency: str,
        price_per_token: int,
        quantity: int,
        tokens_per_buyer: int,
        seconds_until_start: int,
        seconds_until_end: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ) = self.validate_and_normalize_inputs(
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            asset_contract,
            token_id,
            currency,
            price_per_token,
            quantity,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ).estimateGas(tx_params.as_dict())


class ListingsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the listings method."""

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

    def validate_and_normalize_inputs(self, index_0: int):
        """Validate the inputs to the listings method."""
        self.validator.assert_valid(
            method_name="listings",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[int, str, str, int, int, str, int, int, int, int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index_0).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
            returned[2],
            returned[3],
            returned[4],
            returned[5],
            returned[6],
            returned[7],
            returned[8],
            returned[9],
            returned[10],
        )

    def send_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(
            tx_params.as_dict()
        )


class MarketFeeBpsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the marketFeeBps method."""

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


class MulticallMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the multicall method."""

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

    def validate_and_normalize_inputs(self, data: List[Union[bytes, str]]):
        """Validate the inputs to the multicall method."""
        self.validator.assert_valid(
            method_name="multicall",
            parameter_name="data",
            argument_value=data,
        )
        return data

    def call(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> List[Union[bytes, str]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(data).call(tx_params.as_dict())
        return [Union[bytes, str](element) for element in returned]

    def send_transaction(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).transact(tx_params.as_dict())

    def build_transaction(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        data: List[Union[bytes, str]],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (data) = self.validate_and_normalize_inputs(data)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(data).estimateGas(tx_params.as_dict())


class OnErc1155BatchReceivedMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the onERC1155BatchReceived method."""

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
        index_0: str,
        index_1: str,
        index_2: List[int],
        index_3: List[int],
        index_4: Union[bytes, str],
    ):
        """Validate the inputs to the onERC1155BatchReceived method."""
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="index_2",
            argument_value=index_2,
        )
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="index_3",
            argument_value=index_3,
        )
        self.validator.assert_valid(
            method_name="onERC1155BatchReceived",
            parameter_name="index_4",
            argument_value=index_4,
        )
        return (index_0, index_1, index_2, index_3, index_4)

    def call(
        self,
        index_0: str,
        index_1: str,
        index_2: List[int],
        index_3: List[int],
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: List[int],
        index_3: List[int],
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: List[int],
        index_3: List[int],
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        index_0: str,
        index_1: str,
        index_2: List[int],
        index_3: List[int],
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).estimateGas(tx_params.as_dict())


class OnErc1155ReceivedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the onERC1155Received method."""

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
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
    ):
        """Validate the inputs to the onERC1155Received method."""
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_2",
            argument_value=index_2,
        )
        # safeguard against fractional inputs
        index_2 = int(index_2)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_3",
            argument_value=index_3,
        )
        # safeguard against fractional inputs
        index_3 = int(index_3)
        self.validator.assert_valid(
            method_name="onERC1155Received",
            parameter_name="index_4",
            argument_value=index_4,
        )
        return (index_0, index_1, index_2, index_3, index_4)

    def call(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: int,
        index_4: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
            index_4,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3, index_4
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3, index_4
        ).estimateGas(tx_params.as_dict())


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
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: Union[bytes, str],
    ):
        """Validate the inputs to the onERC721Received method."""
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="index_0",
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="index_1",
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="index_2",
            argument_value=index_2,
        )
        # safeguard against fractional inputs
        index_2 = int(index_2)
        self.validator.assert_valid(
            method_name="onERC721Received",
            parameter_name="index_3",
            argument_value=index_3,
        )
        return (index_0, index_1, index_2, index_3)

    def call(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            index_0, index_1, index_2, index_3
        ).call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            index_0,
            index_1,
            index_2,
            index_3,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        index_0: str,
        index_1: str,
        index_2: int,
        index_3: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            index_0,
            index_1,
            index_2,
            index_3,
        ) = self.validate_and_normalize_inputs(
            index_0, index_1, index_2, index_3
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            index_0, index_1, index_2, index_3
        ).estimateGas(tx_params.as_dict())


class PausedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the paused method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return bool(returned)

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


class RenounceRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the renounceRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the renounceRole method."""
        self.validator.assert_valid(
            method_name="renounceRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="renounceRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class RestrictedListerRoleOnlyMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the restrictedListerRoleOnly method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return bool(returned)

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


class RevokeRoleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the revokeRole method."""

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
        self, role: Union[bytes, str], account: str
    ):
        """Validate the inputs to the revokeRole method."""
        self.validator.assert_valid(
            method_name="revokeRole",
            parameter_name="role",
            argument_value=role,
        )
        self.validator.assert_valid(
            method_name="revokeRole",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (role, account)

    def call(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(role, account).call(tx_params.as_dict())

    def send_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        role: Union[bytes, str],
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (role, account) = self.validate_and_normalize_inputs(role, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(role, account).estimateGas(
            tx_params.as_dict()
        )


class SetContractUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setContractURI method."""

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

    def validate_and_normalize_inputs(self, uri: str):
        """Validate the inputs to the setContractURI method."""
        self.validator.assert_valid(
            method_name="setContractURI",
            parameter_name="_URI",
            argument_value=uri,
        )
        return uri

    def call(self, uri: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(uri).call(tx_params.as_dict())

    def send_transaction(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).transact(tx_params.as_dict())

    def build_transaction(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).estimateGas(tx_params.as_dict())


class SetMarketFeeBpsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setMarketFeeBps method."""

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

    def validate_and_normalize_inputs(self, fee_bps: int):
        """Validate the inputs to the setMarketFeeBps method."""
        self.validator.assert_valid(
            method_name="setMarketFeeBps",
            parameter_name="feeBps",
            argument_value=fee_bps,
        )
        return fee_bps

    def call(self, fee_bps: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (fee_bps) = self.validate_and_normalize_inputs(fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(fee_bps).call(tx_params.as_dict())

    def send_transaction(
        self, fee_bps: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (fee_bps) = self.validate_and_normalize_inputs(fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(fee_bps).transact(tx_params.as_dict())

    def build_transaction(
        self, fee_bps: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (fee_bps) = self.validate_and_normalize_inputs(fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(fee_bps).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, fee_bps: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (fee_bps) = self.validate_and_normalize_inputs(fee_bps)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(fee_bps).estimateGas(
            tx_params.as_dict()
        )


class SetRestrictedListerRoleOnlyMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setRestrictedListerRoleOnly method."""

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

    def validate_and_normalize_inputs(self, restricted: bool):
        """Validate the inputs to the setRestrictedListerRoleOnly method."""
        self.validator.assert_valid(
            method_name="setRestrictedListerRoleOnly",
            parameter_name="restricted",
            argument_value=restricted,
        )
        return restricted

    def call(
        self, restricted: bool, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (restricted) = self.validate_and_normalize_inputs(restricted)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(restricted).call(tx_params.as_dict())

    def send_transaction(
        self, restricted: bool, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (restricted) = self.validate_and_normalize_inputs(restricted)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(restricted).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, restricted: bool, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (restricted) = self.validate_and_normalize_inputs(restricted)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(restricted).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, restricted: bool, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (restricted) = self.validate_and_normalize_inputs(restricted)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(restricted).estimateGas(
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


class UnlistMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the unlist method."""

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

    def validate_and_normalize_inputs(self, listing_id: int, quantity: int):
        """Validate the inputs to the unlist method."""
        self.validator.assert_valid(
            method_name="unlist",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="unlist",
            parameter_name="_quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        return (listing_id, quantity)

    def call(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, quantity).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        listing_id: int,
        quantity: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, quantity) = self.validate_and_normalize_inputs(
            listing_id, quantity
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, quantity).estimateGas(
            tx_params.as_dict()
        )


class UpdateListingParamsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the updateListingParams method."""

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
        price_per_token: int,
        currency: str,
        tokens_per_buyer: int,
        seconds_until_start: int,
        seconds_until_end: int,
    ):
        """Validate the inputs to the updateListingParams method."""
        self.validator.assert_valid(
            method_name="updateListingParams",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="updateListingParams",
            parameter_name="_pricePerToken",
            argument_value=price_per_token,
        )
        # safeguard against fractional inputs
        price_per_token = int(price_per_token)
        self.validator.assert_valid(
            method_name="updateListingParams",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name="updateListingParams",
            parameter_name="_tokensPerBuyer",
            argument_value=tokens_per_buyer,
        )
        # safeguard against fractional inputs
        tokens_per_buyer = int(tokens_per_buyer)
        self.validator.assert_valid(
            method_name="updateListingParams",
            parameter_name="_secondsUntilStart",
            argument_value=seconds_until_start,
        )
        # safeguard against fractional inputs
        seconds_until_start = int(seconds_until_start)
        self.validator.assert_valid(
            method_name="updateListingParams",
            parameter_name="_secondsUntilEnd",
            argument_value=seconds_until_end,
        )
        # safeguard against fractional inputs
        seconds_until_end = int(seconds_until_end)
        return (
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        )

    def call(
        self,
        listing_id: int,
        price_per_token: int,
        currency: str,
        tokens_per_buyer: int,
        seconds_until_start: int,
        seconds_until_end: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        price_per_token: int,
        currency: str,
        tokens_per_buyer: int,
        seconds_until_start: int,
        seconds_until_end: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        listing_id: int,
        price_per_token: int,
        currency: str,
        tokens_per_buyer: int,
        seconds_until_start: int,
        seconds_until_end: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        listing_id: int,
        price_per_token: int,
        currency: str,
        tokens_per_buyer: int,
        seconds_until_start: int,
        seconds_until_end: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id,
            price_per_token,
            currency,
            tokens_per_buyer,
            seconds_until_start,
            seconds_until_end,
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Market:
    """Wrapper class for Market Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    default_admin_role: DefaultAdminRoleMethod
    """Constructor-initialized instance of
    :class:`DefaultAdminRoleMethod`.
    """

    lister_role: ListerRoleMethod
    """Constructor-initialized instance of
    :class:`ListerRoleMethod`.
    """

    pauser_role: PauserRoleMethod
    """Constructor-initialized instance of
    :class:`PauserRoleMethod`.
    """

    contract_uri_: ContractUri_Method
    """Constructor-initialized instance of
    :class:`ContractUri_Method`.
    """

    add_to_listing: AddToListingMethod
    """Constructor-initialized instance of
    :class:`AddToListingMethod`.
    """

    bought_from_listing: BoughtFromListingMethod
    """Constructor-initialized instance of
    :class:`BoughtFromListingMethod`.
    """

    buy: BuyMethod
    """Constructor-initialized instance of
    :class:`BuyMethod`.
    """

    contract_uri: ContractUriMethod
    """Constructor-initialized instance of
    :class:`ContractUriMethod`.
    """

    get_all_listings: GetAllListingsMethod
    """Constructor-initialized instance of
    :class:`GetAllListingsMethod`.
    """

    get_listing: GetListingMethod
    """Constructor-initialized instance of
    :class:`GetListingMethod`.
    """

    get_listings_by_asset: GetListingsByAssetMethod
    """Constructor-initialized instance of
    :class:`GetListingsByAssetMethod`.
    """

    get_listings_by_asset_contract: GetListingsByAssetContractMethod
    """Constructor-initialized instance of
    :class:`GetListingsByAssetContractMethod`.
    """

    get_listings_by_seller: GetListingsBySellerMethod
    """Constructor-initialized instance of
    :class:`GetListingsBySellerMethod`.
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

    is_trusted_forwarder: IsTrustedForwarderMethod
    """Constructor-initialized instance of
    :class:`IsTrustedForwarderMethod`.
    """

    _list: ListMethod
    """Constructor-initialized instance of
    :class:`ListMethod`.
    """

    listings: ListingsMethod
    """Constructor-initialized instance of
    :class:`ListingsMethod`.
    """

    market_fee_bps: MarketFeeBpsMethod
    """Constructor-initialized instance of
    :class:`MarketFeeBpsMethod`.
    """

    multicall: MulticallMethod
    """Constructor-initialized instance of
    :class:`MulticallMethod`.
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

    paused: PausedMethod
    """Constructor-initialized instance of
    :class:`PausedMethod`.
    """

    renounce_role: RenounceRoleMethod
    """Constructor-initialized instance of
    :class:`RenounceRoleMethod`.
    """

    restricted_lister_role_only: RestrictedListerRoleOnlyMethod
    """Constructor-initialized instance of
    :class:`RestrictedListerRoleOnlyMethod`.
    """

    revoke_role: RevokeRoleMethod
    """Constructor-initialized instance of
    :class:`RevokeRoleMethod`.
    """

    set_contract_uri: SetContractUriMethod
    """Constructor-initialized instance of
    :class:`SetContractUriMethod`.
    """

    set_market_fee_bps: SetMarketFeeBpsMethod
    """Constructor-initialized instance of
    :class:`SetMarketFeeBpsMethod`.
    """

    set_restricted_lister_role_only: SetRestrictedListerRoleOnlyMethod
    """Constructor-initialized instance of
    :class:`SetRestrictedListerRoleOnlyMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    total_listings: TotalListingsMethod
    """Constructor-initialized instance of
    :class:`TotalListingsMethod`.
    """

    unlist: UnlistMethod
    """Constructor-initialized instance of
    :class:`UnlistMethod`.
    """

    update_listing_params: UpdateListingParamsMethod
    """Constructor-initialized instance of
    :class:`UpdateListingParamsMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: MarketValidator = None,
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
            validator = MarketValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=Market.abi()
        ).functions

        self.default_admin_role = DefaultAdminRoleMethod(
            web3_or_provider, contract_address, functions.DEFAULT_ADMIN_ROLE
        )

        self.lister_role = ListerRoleMethod(
            web3_or_provider, contract_address, functions.LISTER_ROLE
        )

        self.pauser_role = PauserRoleMethod(
            web3_or_provider, contract_address, functions.PAUSER_ROLE
        )

        self.contract_uri_ = ContractUri_Method(
            web3_or_provider, contract_address, functions._contractURI
        )

        self.add_to_listing = AddToListingMethod(
            web3_or_provider,
            contract_address,
            functions.addToListing,
            validator,
        )

        self.bought_from_listing = BoughtFromListingMethod(
            web3_or_provider,
            contract_address,
            functions.boughtFromListing,
            validator,
        )

        self.buy = BuyMethod(
            web3_or_provider, contract_address, functions.buy, validator
        )

        self.contract_uri = ContractUriMethod(
            web3_or_provider, contract_address, functions.contractURI
        )

        self.get_all_listings = GetAllListingsMethod(
            web3_or_provider, contract_address, functions.getAllListings
        )

        self.get_listing = GetListingMethod(
            web3_or_provider, contract_address, functions.getListing, validator
        )

        self.get_listings_by_asset = GetListingsByAssetMethod(
            web3_or_provider,
            contract_address,
            functions.getListingsByAsset,
            validator,
        )

        self.get_listings_by_asset_contract = GetListingsByAssetContractMethod(
            web3_or_provider,
            contract_address,
            functions.getListingsByAssetContract,
            validator,
        )

        self.get_listings_by_seller = GetListingsBySellerMethod(
            web3_or_provider,
            contract_address,
            functions.getListingsBySeller,
            validator,
        )

        self.get_role_admin = GetRoleAdminMethod(
            web3_or_provider,
            contract_address,
            functions.getRoleAdmin,
            validator,
        )

        self.get_role_member = GetRoleMemberMethod(
            web3_or_provider,
            contract_address,
            functions.getRoleMember,
            validator,
        )

        self.get_role_member_count = GetRoleMemberCountMethod(
            web3_or_provider,
            contract_address,
            functions.getRoleMemberCount,
            validator,
        )

        self.grant_role = GrantRoleMethod(
            web3_or_provider, contract_address, functions.grantRole, validator
        )

        self.has_role = HasRoleMethod(
            web3_or_provider, contract_address, functions.hasRole, validator
        )

        self.is_trusted_forwarder = IsTrustedForwarderMethod(
            web3_or_provider,
            contract_address,
            functions.isTrustedForwarder,
            validator,
        )

        self._list = ListMethod(
            web3_or_provider, contract_address, functions.list, validator
        )

        self.listings = ListingsMethod(
            web3_or_provider, contract_address, functions.listings, validator
        )

        self.market_fee_bps = MarketFeeBpsMethod(
            web3_or_provider, contract_address, functions.marketFeeBps
        )

        self.multicall = MulticallMethod(
            web3_or_provider, contract_address, functions.multicall, validator
        )

        self.on_erc1155_batch_received = OnErc1155BatchReceivedMethod(
            web3_or_provider,
            contract_address,
            functions.onERC1155BatchReceived,
            validator,
        )

        self.on_erc1155_received = OnErc1155ReceivedMethod(
            web3_or_provider,
            contract_address,
            functions.onERC1155Received,
            validator,
        )

        self.on_erc721_received = OnErc721ReceivedMethod(
            web3_or_provider,
            contract_address,
            functions.onERC721Received,
            validator,
        )

        self.paused = PausedMethod(
            web3_or_provider, contract_address, functions.paused
        )

        self.renounce_role = RenounceRoleMethod(
            web3_or_provider,
            contract_address,
            functions.renounceRole,
            validator,
        )

        self.restricted_lister_role_only = RestrictedListerRoleOnlyMethod(
            web3_or_provider,
            contract_address,
            functions.restrictedListerRoleOnly,
        )

        self.revoke_role = RevokeRoleMethod(
            web3_or_provider, contract_address, functions.revokeRole, validator
        )

        self.set_contract_uri = SetContractUriMethod(
            web3_or_provider,
            contract_address,
            functions.setContractURI,
            validator,
        )

        self.set_market_fee_bps = SetMarketFeeBpsMethod(
            web3_or_provider,
            contract_address,
            functions.setMarketFeeBps,
            validator,
        )

        self.set_restricted_lister_role_only = (
            SetRestrictedListerRoleOnlyMethod(
                web3_or_provider,
                contract_address,
                functions.setRestrictedListerRoleOnly,
                validator,
            )
        )

        self.supports_interface = SupportsInterfaceMethod(
            web3_or_provider,
            contract_address,
            functions.supportsInterface,
            validator,
        )

        self.total_listings = TotalListingsMethod(
            web3_or_provider, contract_address, functions.totalListings
        )

        self.unlist = UnlistMethod(
            web3_or_provider, contract_address, functions.unlist, validator
        )

        self.update_listing_params = UpdateListingParamsMethod(
            web3_or_provider,
            contract_address,
            functions.updateListingParams,
            validator,
        )

    def get_listing_update_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ListingUpdate event.

        :param tx_hash: hash of transaction emitting ListingUpdate event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Market.abi(),
            )
            .events.ListingUpdate()
            .processReceipt(tx_receipt)
        )

    def get_market_fee_update_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for MarketFeeUpdate event.

        :param tx_hash: hash of transaction emitting MarketFeeUpdate event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Market.abi(),
            )
            .events.MarketFeeUpdate()
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
                abi=Market.abi(),
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
                abi=Market.abi(),
            )
            .events.NewSale()
            .processReceipt(tx_receipt)
        )

    def get_paused_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Paused event.

        :param tx_hash: hash of transaction emitting Paused event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Market.abi(),
            )
            .events.Paused()
            .processReceipt(tx_receipt)
        )

    def get_restricted_lister_role_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RestrictedListerRoleUpdated event.

        :param tx_hash: hash of transaction emitting
            RestrictedListerRoleUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Market.abi(),
            )
            .events.RestrictedListerRoleUpdated()
            .processReceipt(tx_receipt)
        )

    def get_role_admin_changed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleAdminChanged event.

        :param tx_hash: hash of transaction emitting RoleAdminChanged event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Market.abi(),
            )
            .events.RoleAdminChanged()
            .processReceipt(tx_receipt)
        )

    def get_role_granted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleGranted event.

        :param tx_hash: hash of transaction emitting RoleGranted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Market.abi(),
            )
            .events.RoleGranted()
            .processReceipt(tx_receipt)
        )

    def get_role_revoked_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for RoleRevoked event.

        :param tx_hash: hash of transaction emitting RoleRevoked event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Market.abi(),
            )
            .events.RoleRevoked()
            .processReceipt(tx_receipt)
        )

    def get_unpaused_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Unpaused event.

        :param tx_hash: hash of transaction emitting Unpaused event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=Market.abi(),
            )
            .events.Unpaused()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address payable","name":"_controlCenter","type":"address"},{"internalType":"address","name":"_trustedForwarder","type":"address"},{"internalType":"string","name":"_uri","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"seller","type":"address"},{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"saleStart","type":"uint256"},{"internalType":"uint256","name":"saleEnd","type":"uint256"},{"internalType":"uint256","name":"tokensPerBuyer","type":"uint256"},{"internalType":"enum Market.TokenType","name":"tokenType","type":"uint8"}],"indexed":false,"internalType":"struct Market.Listing","name":"listing","type":"tuple"}],"name":"ListingUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint128","name":"newFee","type":"uint128"}],"name":"MarketFeeUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"indexed":true,"internalType":"address","name":"seller","type":"address"},{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"saleStart","type":"uint256"},{"internalType":"uint256","name":"saleEnd","type":"uint256"},{"internalType":"uint256","name":"tokensPerBuyer","type":"uint256"},{"internalType":"enum Market.TokenType","name":"tokenType","type":"uint8"}],"indexed":false,"internalType":"struct Market.Listing","name":"listing","type":"tuple"}],"name":"NewListing","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"indexed":true,"internalType":"address","name":"seller","type":"address"},{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":false,"internalType":"address","name":"buyer","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantity","type":"uint256"},{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"saleStart","type":"uint256"},{"internalType":"uint256","name":"saleEnd","type":"uint256"},{"internalType":"uint256","name":"tokensPerBuyer","type":"uint256"},{"internalType":"enum Market.TokenType","name":"tokenType","type":"uint8"}],"indexed":false,"internalType":"struct Market.Listing","name":"listing","type":"tuple"}],"name":"NewSale","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"restricted","type":"bool"}],"name":"RestrictedListerRoleUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"LISTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PAUSER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"uint256","name":"_quantity","type":"uint256"}],"name":"addToListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"},{"internalType":"address","name":"index_1","type":"address"}],"name":"boughtFromListing","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"uint256","name":"_quantity","type":"uint256"}],"name":"buy","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllListings","outputs":[{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"saleStart","type":"uint256"},{"internalType":"uint256","name":"saleEnd","type":"uint256"},{"internalType":"uint256","name":"tokensPerBuyer","type":"uint256"},{"internalType":"enum Market.TokenType","name":"tokenType","type":"uint8"}],"internalType":"struct Market.Listing[]","name":"allListings","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"}],"name":"getListing","outputs":[{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"saleStart","type":"uint256"},{"internalType":"uint256","name":"saleEnd","type":"uint256"},{"internalType":"uint256","name":"tokensPerBuyer","type":"uint256"},{"internalType":"enum Market.TokenType","name":"tokenType","type":"uint8"}],"internalType":"struct Market.Listing","name":"listing","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_assetContract","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getListingsByAsset","outputs":[{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"saleStart","type":"uint256"},{"internalType":"uint256","name":"saleEnd","type":"uint256"},{"internalType":"uint256","name":"tokensPerBuyer","type":"uint256"},{"internalType":"enum Market.TokenType","name":"tokenType","type":"uint8"}],"internalType":"struct Market.Listing[]","name":"tokenListings","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_assetContract","type":"address"}],"name":"getListingsByAssetContract","outputs":[{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"saleStart","type":"uint256"},{"internalType":"uint256","name":"saleEnd","type":"uint256"},{"internalType":"uint256","name":"tokensPerBuyer","type":"uint256"},{"internalType":"enum Market.TokenType","name":"tokenType","type":"uint8"}],"internalType":"struct Market.Listing[]","name":"tokenListings","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_seller","type":"address"}],"name":"getListingsBySeller","outputs":[{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"saleStart","type":"uint256"},{"internalType":"uint256","name":"saleEnd","type":"uint256"},{"internalType":"uint256","name":"tokensPerBuyer","type":"uint256"},{"internalType":"enum Market.TokenType","name":"tokenType","type":"uint8"}],"internalType":"struct Market.Listing[]","name":"sellerListings","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_assetContract","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"uint256","name":"_tokensPerBuyer","type":"uint256"},{"internalType":"uint256","name":"_secondsUntilStart","type":"uint256"},{"internalType":"uint256","name":"_secondsUntilEnd","type":"uint256"}],"name":"list","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"listings","outputs":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"uint256","name":"saleStart","type":"uint256"},{"internalType":"uint256","name":"saleEnd","type":"uint256"},{"internalType":"uint256","name":"tokensPerBuyer","type":"uint256"},{"internalType":"enum Market.TokenType","name":"tokenType","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"marketFeeBps","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256[]","name":"index_2","type":"uint256[]"},{"internalType":"uint256[]","name":"index_3","type":"uint256[]"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155BatchReceived","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"uint256","name":"index_3","type":"uint256"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"bytes","name":"index_3","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"restrictedListerRoleOnly","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_URI","type":"string"}],"name":"setContractURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint128","name":"feeBps","type":"uint128"}],"name":"setMarketFeeBps","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"restricted","type":"bool"}],"name":"setRestrictedListerRoleOnly","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalListings","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"uint256","name":"_quantity","type":"uint256"}],"name":"unlist","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_tokensPerBuyer","type":"uint256"},{"internalType":"uint256","name":"_secondsUntilStart","type":"uint256"},{"internalType":"uint256","name":"_secondsUntilEnd","type":"uint256"}],"name":"updateListingParams","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
