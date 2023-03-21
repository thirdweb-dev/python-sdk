"""Generated wrapper for IOffers Solidity contract."""

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
# constructor for IOffers below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IOffersValidator,
    )
except ImportError:

    class IOffersValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IOffersOffer(TypedDict):
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

    offerId: int

    offeror: str

    assetContract: str

    tokenId: int

    quantity: int

    currency: str

    totalPrice: int

    expirationTimestamp: int

    tokenType: int

    status: int


class IOffersOfferParams(TypedDict):
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

    totalPrice: int

    expirationTimestamp: int


class AcceptOfferMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the acceptOffer method."""

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

    def validate_and_normalize_inputs(self, offer_id: int):
        """Validate the inputs to the acceptOffer method."""
        self.validator.assert_valid(
            method_name="acceptOffer",
            parameter_name="_offerId",
            argument_value=offer_id,
        )
        # safeguard against fractional inputs
        offer_id = int(offer_id)
        return offer_id

    def call(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(offer_id).call(tx_params.as_dict())

    def send_transaction(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(offer_id).transact(tx_params.as_dict())

    def build_transaction(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(offer_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(offer_id).estimateGas(
            tx_params.as_dict()
        )


class CancelOfferMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the cancelOffer method."""

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

    def validate_and_normalize_inputs(self, offer_id: int):
        """Validate the inputs to the cancelOffer method."""
        self.validator.assert_valid(
            method_name="cancelOffer",
            parameter_name="_offerId",
            argument_value=offer_id,
        )
        # safeguard against fractional inputs
        offer_id = int(offer_id)
        return offer_id

    def call(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(offer_id).call(tx_params.as_dict())

    def send_transaction(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(offer_id).transact(tx_params.as_dict())

    def build_transaction(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(offer_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(offer_id).estimateGas(
            tx_params.as_dict()
        )


class GetAllOffersMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getAllOffers method."""

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
        """Validate the inputs to the getAllOffers method."""
        self.validator.assert_valid(
            method_name="getAllOffers",
            parameter_name="_startId",
            argument_value=start_id,
        )
        # safeguard against fractional inputs
        start_id = int(start_id)
        self.validator.assert_valid(
            method_name="getAllOffers",
            parameter_name="_endId",
            argument_value=end_id,
        )
        # safeguard against fractional inputs
        end_id = int(end_id)
        return (start_id, end_id)

    def call(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> List[IOffersOffer]:
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
            IOffersOffer(
                offerId=element[0],
                offeror=element[1],
                assetContract=element[2],
                tokenId=element[3],
                quantity=element[4],
                currency=element[5],
                totalPrice=element[6],
                expirationTimestamp=element[7],
                tokenType=element[8],
                status=element[9],
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


class GetAllValidOffersMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getAllValidOffers method."""

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
        """Validate the inputs to the getAllValidOffers method."""
        self.validator.assert_valid(
            method_name="getAllValidOffers",
            parameter_name="_startId",
            argument_value=start_id,
        )
        # safeguard against fractional inputs
        start_id = int(start_id)
        self.validator.assert_valid(
            method_name="getAllValidOffers",
            parameter_name="_endId",
            argument_value=end_id,
        )
        # safeguard against fractional inputs
        end_id = int(end_id)
        return (start_id, end_id)

    def call(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> List[IOffersOffer]:
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
            IOffersOffer(
                offerId=element[0],
                offeror=element[1],
                assetContract=element[2],
                tokenId=element[3],
                quantity=element[4],
                currency=element[5],
                totalPrice=element[6],
                expirationTimestamp=element[7],
                tokenType=element[8],
                status=element[9],
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


class GetOfferMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getOffer method."""

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

    def validate_and_normalize_inputs(self, offer_id: int):
        """Validate the inputs to the getOffer method."""
        self.validator.assert_valid(
            method_name="getOffer",
            parameter_name="_offerId",
            argument_value=offer_id,
        )
        # safeguard against fractional inputs
        offer_id = int(offer_id)
        return offer_id

    def call(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> IOffersOffer:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(offer_id).call(tx_params.as_dict())
        return IOffersOffer(
            offerId=returned[0],
            offeror=returned[1],
            assetContract=returned[2],
            tokenId=returned[3],
            quantity=returned[4],
            currency=returned[5],
            totalPrice=returned[6],
            expirationTimestamp=returned[7],
            tokenType=returned[8],
            status=returned[9],
        )

    def send_transaction(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(offer_id).transact(tx_params.as_dict())

    def build_transaction(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(offer_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, offer_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (offer_id) = self.validate_and_normalize_inputs(offer_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(offer_id).estimateGas(
            tx_params.as_dict()
        )


class MakeOfferMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the makeOffer method."""

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

    def validate_and_normalize_inputs(self, params: IOffersOfferParams):
        """Validate the inputs to the makeOffer method."""
        self.validator.assert_valid(
            method_name="makeOffer",
            parameter_name="_params",
            argument_value=params,
        )
        return params

    def call(
        self, params: IOffersOfferParams, tx_params: Optional[TxParams] = None
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
        self, params: IOffersOfferParams, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).transact(tx_params.as_dict())

    def build_transaction(
        self, params: IOffersOfferParams, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, params: IOffersOfferParams, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IOffers:
    """Wrapper class for IOffers Solidity contract."""

    accept_offer: AcceptOfferMethod
    """Constructor-initialized instance of
    :class:`AcceptOfferMethod`.
    """

    cancel_offer: CancelOfferMethod
    """Constructor-initialized instance of
    :class:`CancelOfferMethod`.
    """

    get_all_offers: GetAllOffersMethod
    """Constructor-initialized instance of
    :class:`GetAllOffersMethod`.
    """

    get_all_valid_offers: GetAllValidOffersMethod
    """Constructor-initialized instance of
    :class:`GetAllValidOffersMethod`.
    """

    get_offer: GetOfferMethod
    """Constructor-initialized instance of
    :class:`GetOfferMethod`.
    """

    make_offer: MakeOfferMethod
    """Constructor-initialized instance of
    :class:`MakeOfferMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IOffersValidator = None,
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
            validator = IOffersValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=IOffers.abi()
        ).functions

        self.accept_offer = AcceptOfferMethod(
            web3_or_provider,
            contract_address,
            functions.acceptOffer,
            validator,
        )

        self.cancel_offer = CancelOfferMethod(
            web3_or_provider,
            contract_address,
            functions.cancelOffer,
            validator,
        )

        self.get_all_offers = GetAllOffersMethod(
            web3_or_provider,
            contract_address,
            functions.getAllOffers,
            validator,
        )

        self.get_all_valid_offers = GetAllValidOffersMethod(
            web3_or_provider,
            contract_address,
            functions.getAllValidOffers,
            validator,
        )

        self.get_offer = GetOfferMethod(
            web3_or_provider, contract_address, functions.getOffer, validator
        )

        self.make_offer = MakeOfferMethod(
            web3_or_provider, contract_address, functions.makeOffer, validator
        )

    def get_accepted_offer_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AcceptedOffer event.

        :param tx_hash: hash of transaction emitting AcceptedOffer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IOffers.abi(),
            )
            .events.AcceptedOffer()
            .processReceipt(tx_receipt)
        )

    def get_cancelled_offer_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for CancelledOffer event.

        :param tx_hash: hash of transaction emitting CancelledOffer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IOffers.abi(),
            )
            .events.CancelledOffer()
            .processReceipt(tx_receipt)
        )

    def get_new_offer_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NewOffer event.

        :param tx_hash: hash of transaction emitting NewOffer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IOffers.abi(),
            )
            .events.NewOffer()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"offeror","type":"address"},{"indexed":true,"internalType":"uint256","name":"offerId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"address","name":"seller","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantityBought","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalPricePaid","type":"uint256"}],"name":"AcceptedOffer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"offeror","type":"address"},{"indexed":true,"internalType":"uint256","name":"offerId","type":"uint256"}],"name":"CancelledOffer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"offeror","type":"address"},{"indexed":true,"internalType":"uint256","name":"offerId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"components":[{"internalType":"uint256","name":"offerId","type":"uint256"},{"internalType":"address","name":"offeror","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"totalPrice","type":"uint256"},{"internalType":"uint256","name":"expirationTimestamp","type":"uint256"},{"internalType":"enum IOffers.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IOffers.Status","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct IOffers.Offer","name":"offer","type":"tuple"}],"name":"NewOffer","type":"event"},{"inputs":[{"internalType":"uint256","name":"_offerId","type":"uint256"}],"name":"acceptOffer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_offerId","type":"uint256"}],"name":"cancelOffer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_startId","type":"uint256"},{"internalType":"uint256","name":"_endId","type":"uint256"}],"name":"getAllOffers","outputs":[{"components":[{"internalType":"uint256","name":"offerId","type":"uint256"},{"internalType":"address","name":"offeror","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"totalPrice","type":"uint256"},{"internalType":"uint256","name":"expirationTimestamp","type":"uint256"},{"internalType":"enum IOffers.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IOffers.Status","name":"status","type":"uint8"}],"internalType":"struct IOffers.Offer[]","name":"offers","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_startId","type":"uint256"},{"internalType":"uint256","name":"_endId","type":"uint256"}],"name":"getAllValidOffers","outputs":[{"components":[{"internalType":"uint256","name":"offerId","type":"uint256"},{"internalType":"address","name":"offeror","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"totalPrice","type":"uint256"},{"internalType":"uint256","name":"expirationTimestamp","type":"uint256"},{"internalType":"enum IOffers.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IOffers.Status","name":"status","type":"uint8"}],"internalType":"struct IOffers.Offer[]","name":"offers","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_offerId","type":"uint256"}],"name":"getOffer","outputs":[{"components":[{"internalType":"uint256","name":"offerId","type":"uint256"},{"internalType":"address","name":"offeror","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"totalPrice","type":"uint256"},{"internalType":"uint256","name":"expirationTimestamp","type":"uint256"},{"internalType":"enum IOffers.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IOffers.Status","name":"status","type":"uint8"}],"internalType":"struct IOffers.Offer","name":"offer","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"totalPrice","type":"uint256"},{"internalType":"uint256","name":"expirationTimestamp","type":"uint256"}],"internalType":"struct IOffers.OfferParams","name":"_params","type":"tuple"}],"name":"makeOffer","outputs":[{"internalType":"uint256","name":"offerId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
