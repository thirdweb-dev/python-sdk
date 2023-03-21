"""Generated wrapper for EnglishAuctionsLogic Solidity contract."""

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
# constructor for EnglishAuctionsLogic below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        EnglishAuctionsLogicValidator,
    )
except ImportError:

    class EnglishAuctionsLogicValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IEnglishAuctionsAuction(TypedDict):
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

    auctionId: int

    auctionCreator: str

    assetContract: str

    tokenId: int

    quantity: int

    currency: str

    minimumBidAmount: int

    buyoutBidAmount: int

    timeBufferInSeconds: int

    bidBufferBps: int

    startTimestamp: int

    endTimestamp: int

    tokenType: int

    status: int


class IEnglishAuctionsAuctionParameters(TypedDict):
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

    minimumBidAmount: int

    buyoutBidAmount: int

    timeBufferInSeconds: int

    bidBufferBps: int

    startTimestamp: int

    endTimestamp: int


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


class BidInAuctionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the bidInAuction method."""

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

    def validate_and_normalize_inputs(self, auction_id: int, bid_amount: int):
        """Validate the inputs to the bidInAuction method."""
        self.validator.assert_valid(
            method_name="bidInAuction",
            parameter_name="_auctionId",
            argument_value=auction_id,
        )
        # safeguard against fractional inputs
        auction_id = int(auction_id)
        self.validator.assert_valid(
            method_name="bidInAuction",
            parameter_name="_bidAmount",
            argument_value=bid_amount,
        )
        # safeguard against fractional inputs
        bid_amount = int(bid_amount)
        return (auction_id, bid_amount)

    def call(
        self,
        auction_id: int,
        bid_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (auction_id, bid_amount) = self.validate_and_normalize_inputs(
            auction_id, bid_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(auction_id, bid_amount).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        auction_id: int,
        bid_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (auction_id, bid_amount) = self.validate_and_normalize_inputs(
            auction_id, bid_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id, bid_amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        auction_id: int,
        bid_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (auction_id, bid_amount) = self.validate_and_normalize_inputs(
            auction_id, bid_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            auction_id, bid_amount
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        auction_id: int,
        bid_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (auction_id, bid_amount) = self.validate_and_normalize_inputs(
            auction_id, bid_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id, bid_amount).estimateGas(
            tx_params.as_dict()
        )


class CancelAuctionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the cancelAuction method."""

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

    def validate_and_normalize_inputs(self, auction_id: int):
        """Validate the inputs to the cancelAuction method."""
        self.validator.assert_valid(
            method_name="cancelAuction",
            parameter_name="_auctionId",
            argument_value=auction_id,
        )
        # safeguard against fractional inputs
        auction_id = int(auction_id)
        return auction_id

    def call(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(auction_id).call(tx_params.as_dict())

    def send_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).estimateGas(
            tx_params.as_dict()
        )


class CollectAuctionPayoutMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the collectAuctionPayout method."""

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

    def validate_and_normalize_inputs(self, auction_id: int):
        """Validate the inputs to the collectAuctionPayout method."""
        self.validator.assert_valid(
            method_name="collectAuctionPayout",
            parameter_name="_auctionId",
            argument_value=auction_id,
        )
        # safeguard against fractional inputs
        auction_id = int(auction_id)
        return auction_id

    def call(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(auction_id).call(tx_params.as_dict())

    def send_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).estimateGas(
            tx_params.as_dict()
        )


class CollectAuctionTokensMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the collectAuctionTokens method."""

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

    def validate_and_normalize_inputs(self, auction_id: int):
        """Validate the inputs to the collectAuctionTokens method."""
        self.validator.assert_valid(
            method_name="collectAuctionTokens",
            parameter_name="_auctionId",
            argument_value=auction_id,
        )
        # safeguard against fractional inputs
        auction_id = int(auction_id)
        return auction_id

    def call(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(auction_id).call(tx_params.as_dict())

    def send_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).estimateGas(
            tx_params.as_dict()
        )


class CreateAuctionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the createAuction method."""

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
        self, params: IEnglishAuctionsAuctionParameters
    ):
        """Validate the inputs to the createAuction method."""
        self.validator.assert_valid(
            method_name="createAuction",
            parameter_name="_params",
            argument_value=params,
        )
        return params

    def call(
        self,
        params: IEnglishAuctionsAuctionParameters,
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
        params: IEnglishAuctionsAuctionParameters,
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
        params: IEnglishAuctionsAuctionParameters,
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
        params: IEnglishAuctionsAuctionParameters,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).estimateGas(tx_params.as_dict())


class GetAllAuctionsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getAllAuctions method."""

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
        """Validate the inputs to the getAllAuctions method."""
        self.validator.assert_valid(
            method_name="getAllAuctions",
            parameter_name="_startId",
            argument_value=start_id,
        )
        # safeguard against fractional inputs
        start_id = int(start_id)
        self.validator.assert_valid(
            method_name="getAllAuctions",
            parameter_name="_endId",
            argument_value=end_id,
        )
        # safeguard against fractional inputs
        end_id = int(end_id)
        return (start_id, end_id)

    def call(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> List[IEnglishAuctionsAuction]:
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
            IEnglishAuctionsAuction(
                auctionId=element[0],
                auctionCreator=element[1],
                assetContract=element[2],
                tokenId=element[3],
                quantity=element[4],
                currency=element[5],
                minimumBidAmount=element[6],
                buyoutBidAmount=element[7],
                timeBufferInSeconds=element[8],
                bidBufferBps=element[9],
                startTimestamp=element[10],
                endTimestamp=element[11],
                tokenType=element[12],
                status=element[13],
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


class GetAllValidAuctionsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getAllValidAuctions method."""

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
        """Validate the inputs to the getAllValidAuctions method."""
        self.validator.assert_valid(
            method_name="getAllValidAuctions",
            parameter_name="_startId",
            argument_value=start_id,
        )
        # safeguard against fractional inputs
        start_id = int(start_id)
        self.validator.assert_valid(
            method_name="getAllValidAuctions",
            parameter_name="_endId",
            argument_value=end_id,
        )
        # safeguard against fractional inputs
        end_id = int(end_id)
        return (start_id, end_id)

    def call(
        self, start_id: int, end_id: int, tx_params: Optional[TxParams] = None
    ) -> List[IEnglishAuctionsAuction]:
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
            IEnglishAuctionsAuction(
                auctionId=element[0],
                auctionCreator=element[1],
                assetContract=element[2],
                tokenId=element[3],
                quantity=element[4],
                currency=element[5],
                minimumBidAmount=element[6],
                buyoutBidAmount=element[7],
                timeBufferInSeconds=element[8],
                bidBufferBps=element[9],
                startTimestamp=element[10],
                endTimestamp=element[11],
                tokenType=element[12],
                status=element[13],
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


class GetAuctionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getAuction method."""

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

    def validate_and_normalize_inputs(self, auction_id: int):
        """Validate the inputs to the getAuction method."""
        self.validator.assert_valid(
            method_name="getAuction",
            parameter_name="_auctionId",
            argument_value=auction_id,
        )
        # safeguard against fractional inputs
        auction_id = int(auction_id)
        return auction_id

    def call(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> IEnglishAuctionsAuction:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(auction_id).call(
            tx_params.as_dict()
        )
        return IEnglishAuctionsAuction(
            auctionId=returned[0],
            auctionCreator=returned[1],
            assetContract=returned[2],
            tokenId=returned[3],
            quantity=returned[4],
            currency=returned[5],
            minimumBidAmount=returned[6],
            buyoutBidAmount=returned[7],
            timeBufferInSeconds=returned[8],
            bidBufferBps=returned[9],
            startTimestamp=returned[10],
            endTimestamp=returned[11],
            tokenType=returned[12],
            status=returned[13],
        )

    def send_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).estimateGas(
            tx_params.as_dict()
        )


class GetWinningBidMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getWinningBid method."""

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

    def validate_and_normalize_inputs(self, auction_id: int):
        """Validate the inputs to the getWinningBid method."""
        self.validator.assert_valid(
            method_name="getWinningBid",
            parameter_name="_auctionId",
            argument_value=auction_id,
        )
        # safeguard against fractional inputs
        auction_id = int(auction_id)
        return auction_id

    def call(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[str, str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(auction_id).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def send_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).estimateGas(
            tx_params.as_dict()
        )


class IsAuctionExpiredMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isAuctionExpired method."""

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

    def validate_and_normalize_inputs(self, auction_id: int):
        """Validate the inputs to the isAuctionExpired method."""
        self.validator.assert_valid(
            method_name="isAuctionExpired",
            parameter_name="_auctionId",
            argument_value=auction_id,
        )
        # safeguard against fractional inputs
        auction_id = int(auction_id)
        return auction_id

    def call(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(auction_id).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, auction_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (auction_id) = self.validate_and_normalize_inputs(auction_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id).estimateGas(
            tx_params.as_dict()
        )


class IsNewWinningBidMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isNewWinningBid method."""

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

    def validate_and_normalize_inputs(self, auction_id: int, bid_amount: int):
        """Validate the inputs to the isNewWinningBid method."""
        self.validator.assert_valid(
            method_name="isNewWinningBid",
            parameter_name="_auctionId",
            argument_value=auction_id,
        )
        # safeguard against fractional inputs
        auction_id = int(auction_id)
        self.validator.assert_valid(
            method_name="isNewWinningBid",
            parameter_name="_bidAmount",
            argument_value=bid_amount,
        )
        # safeguard against fractional inputs
        bid_amount = int(bid_amount)
        return (auction_id, bid_amount)

    def call(
        self,
        auction_id: int,
        bid_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (auction_id, bid_amount) = self.validate_and_normalize_inputs(
            auction_id, bid_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(auction_id, bid_amount).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        auction_id: int,
        bid_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (auction_id, bid_amount) = self.validate_and_normalize_inputs(
            auction_id, bid_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id, bid_amount).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        auction_id: int,
        bid_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (auction_id, bid_amount) = self.validate_and_normalize_inputs(
            auction_id, bid_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            auction_id, bid_amount
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        auction_id: int,
        bid_amount: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (auction_id, bid_amount) = self.validate_and_normalize_inputs(
            auction_id, bid_amount
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(auction_id, bid_amount).estimateGas(
            tx_params.as_dict()
        )


class TotalAuctionsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the totalAuctions method."""

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


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class EnglishAuctionsLogic:
    """Wrapper class for EnglishAuctionsLogic Solidity contract."""

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

    bid_in_auction: BidInAuctionMethod
    """Constructor-initialized instance of
    :class:`BidInAuctionMethod`.
    """

    cancel_auction: CancelAuctionMethod
    """Constructor-initialized instance of
    :class:`CancelAuctionMethod`.
    """

    collect_auction_payout: CollectAuctionPayoutMethod
    """Constructor-initialized instance of
    :class:`CollectAuctionPayoutMethod`.
    """

    collect_auction_tokens: CollectAuctionTokensMethod
    """Constructor-initialized instance of
    :class:`CollectAuctionTokensMethod`.
    """

    create_auction: CreateAuctionMethod
    """Constructor-initialized instance of
    :class:`CreateAuctionMethod`.
    """

    get_all_auctions: GetAllAuctionsMethod
    """Constructor-initialized instance of
    :class:`GetAllAuctionsMethod`.
    """

    get_all_valid_auctions: GetAllValidAuctionsMethod
    """Constructor-initialized instance of
    :class:`GetAllValidAuctionsMethod`.
    """

    get_auction: GetAuctionMethod
    """Constructor-initialized instance of
    :class:`GetAuctionMethod`.
    """

    get_winning_bid: GetWinningBidMethod
    """Constructor-initialized instance of
    :class:`GetWinningBidMethod`.
    """

    is_auction_expired: IsAuctionExpiredMethod
    """Constructor-initialized instance of
    :class:`IsAuctionExpiredMethod`.
    """

    is_new_winning_bid: IsNewWinningBidMethod
    """Constructor-initialized instance of
    :class:`IsNewWinningBidMethod`.
    """

    total_auctions: TotalAuctionsMethod
    """Constructor-initialized instance of
    :class:`TotalAuctionsMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: EnglishAuctionsLogicValidator = None,
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
            validator = EnglishAuctionsLogicValidator(
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
            abi=EnglishAuctionsLogic.abi(),
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

        self.bid_in_auction = BidInAuctionMethod(
            web3_or_provider,
            contract_address,
            functions.bidInAuction,
            validator,
        )

        self.cancel_auction = CancelAuctionMethod(
            web3_or_provider,
            contract_address,
            functions.cancelAuction,
            validator,
        )

        self.collect_auction_payout = CollectAuctionPayoutMethod(
            web3_or_provider,
            contract_address,
            functions.collectAuctionPayout,
            validator,
        )

        self.collect_auction_tokens = CollectAuctionTokensMethod(
            web3_or_provider,
            contract_address,
            functions.collectAuctionTokens,
            validator,
        )

        self.create_auction = CreateAuctionMethod(
            web3_or_provider,
            contract_address,
            functions.createAuction,
            validator,
        )

        self.get_all_auctions = GetAllAuctionsMethod(
            web3_or_provider,
            contract_address,
            functions.getAllAuctions,
            validator,
        )

        self.get_all_valid_auctions = GetAllValidAuctionsMethod(
            web3_or_provider,
            contract_address,
            functions.getAllValidAuctions,
            validator,
        )

        self.get_auction = GetAuctionMethod(
            web3_or_provider, contract_address, functions.getAuction, validator
        )

        self.get_winning_bid = GetWinningBidMethod(
            web3_or_provider,
            contract_address,
            functions.getWinningBid,
            validator,
        )

        self.is_auction_expired = IsAuctionExpiredMethod(
            web3_or_provider,
            contract_address,
            functions.isAuctionExpired,
            validator,
        )

        self.is_new_winning_bid = IsNewWinningBidMethod(
            web3_or_provider,
            contract_address,
            functions.isNewWinningBid,
            validator,
        )

        self.total_auctions = TotalAuctionsMethod(
            web3_or_provider, contract_address, functions.totalAuctions
        )

    def get_auction_closed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AuctionClosed event.

        :param tx_hash: hash of transaction emitting AuctionClosed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EnglishAuctionsLogic.abi(),
            )
            .events.AuctionClosed()
            .processReceipt(tx_receipt)
        )

    def get_cancelled_auction_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for CancelledAuction event.

        :param tx_hash: hash of transaction emitting CancelledAuction event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EnglishAuctionsLogic.abi(),
            )
            .events.CancelledAuction()
            .processReceipt(tx_receipt)
        )

    def get_new_auction_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NewAuction event.

        :param tx_hash: hash of transaction emitting NewAuction event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EnglishAuctionsLogic.abi(),
            )
            .events.NewAuction()
            .processReceipt(tx_receipt)
        )

    def get_new_bid_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NewBid event.

        :param tx_hash: hash of transaction emitting NewBid event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=EnglishAuctionsLogic.abi(),
            )
            .events.NewBid()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_nativeTokenWrapper","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"auctionId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"indexed":true,"internalType":"address","name":"closer","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"address","name":"auctionCreator","type":"address"},{"indexed":false,"internalType":"address","name":"winningBidder","type":"address"}],"name":"AuctionClosed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"auctionCreator","type":"address"},{"indexed":true,"internalType":"uint256","name":"auctionId","type":"uint256"}],"name":"CancelledAuction","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"auctionCreator","type":"address"},{"indexed":true,"internalType":"uint256","name":"auctionId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"components":[{"internalType":"uint256","name":"auctionId","type":"uint256"},{"internalType":"address","name":"auctionCreator","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"minimumBidAmount","type":"uint256"},{"internalType":"uint256","name":"buyoutBidAmount","type":"uint256"},{"internalType":"uint64","name":"timeBufferInSeconds","type":"uint64"},{"internalType":"uint64","name":"bidBufferBps","type":"uint64"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"uint64","name":"endTimestamp","type":"uint64"},{"internalType":"enum IEnglishAuctions.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IEnglishAuctions.Status","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct IEnglishAuctions.Auction","name":"auction","type":"tuple"}],"name":"NewAuction","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"auctionId","type":"uint256"},{"indexed":true,"internalType":"address","name":"bidder","type":"address"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"indexed":false,"internalType":"uint256","name":"bidAmount","type":"uint256"},{"components":[{"internalType":"uint256","name":"auctionId","type":"uint256"},{"internalType":"address","name":"auctionCreator","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"minimumBidAmount","type":"uint256"},{"internalType":"uint256","name":"buyoutBidAmount","type":"uint256"},{"internalType":"uint64","name":"timeBufferInSeconds","type":"uint64"},{"internalType":"uint64","name":"bidBufferBps","type":"uint64"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"uint64","name":"endTimestamp","type":"uint64"},{"internalType":"enum IEnglishAuctions.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IEnglishAuctions.Status","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct IEnglishAuctions.Auction","name":"auction","type":"tuple"}],"name":"NewBid","type":"event"},{"inputs":[],"name":"MAX_BPS","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_msgData","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_msgSender","outputs":[{"internalType":"address","name":"sender","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_auctionId","type":"uint256"},{"internalType":"uint256","name":"_bidAmount","type":"uint256"}],"name":"bidInAuction","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_auctionId","type":"uint256"}],"name":"cancelAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_auctionId","type":"uint256"}],"name":"collectAuctionPayout","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_auctionId","type":"uint256"}],"name":"collectAuctionTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"minimumBidAmount","type":"uint256"},{"internalType":"uint256","name":"buyoutBidAmount","type":"uint256"},{"internalType":"uint64","name":"timeBufferInSeconds","type":"uint64"},{"internalType":"uint64","name":"bidBufferBps","type":"uint64"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"uint64","name":"endTimestamp","type":"uint64"}],"internalType":"struct IEnglishAuctions.AuctionParameters","name":"_params","type":"tuple"}],"name":"createAuction","outputs":[{"internalType":"uint256","name":"auctionId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_startId","type":"uint256"},{"internalType":"uint256","name":"_endId","type":"uint256"}],"name":"getAllAuctions","outputs":[{"components":[{"internalType":"uint256","name":"auctionId","type":"uint256"},{"internalType":"address","name":"auctionCreator","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"minimumBidAmount","type":"uint256"},{"internalType":"uint256","name":"buyoutBidAmount","type":"uint256"},{"internalType":"uint64","name":"timeBufferInSeconds","type":"uint64"},{"internalType":"uint64","name":"bidBufferBps","type":"uint64"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"uint64","name":"endTimestamp","type":"uint64"},{"internalType":"enum IEnglishAuctions.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IEnglishAuctions.Status","name":"status","type":"uint8"}],"internalType":"struct IEnglishAuctions.Auction[]","name":"_allAuctions","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_startId","type":"uint256"},{"internalType":"uint256","name":"_endId","type":"uint256"}],"name":"getAllValidAuctions","outputs":[{"components":[{"internalType":"uint256","name":"auctionId","type":"uint256"},{"internalType":"address","name":"auctionCreator","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"minimumBidAmount","type":"uint256"},{"internalType":"uint256","name":"buyoutBidAmount","type":"uint256"},{"internalType":"uint64","name":"timeBufferInSeconds","type":"uint64"},{"internalType":"uint64","name":"bidBufferBps","type":"uint64"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"uint64","name":"endTimestamp","type":"uint64"},{"internalType":"enum IEnglishAuctions.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IEnglishAuctions.Status","name":"status","type":"uint8"}],"internalType":"struct IEnglishAuctions.Auction[]","name":"_validAuctions","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_auctionId","type":"uint256"}],"name":"getAuction","outputs":[{"components":[{"internalType":"uint256","name":"auctionId","type":"uint256"},{"internalType":"address","name":"auctionCreator","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"minimumBidAmount","type":"uint256"},{"internalType":"uint256","name":"buyoutBidAmount","type":"uint256"},{"internalType":"uint64","name":"timeBufferInSeconds","type":"uint64"},{"internalType":"uint64","name":"bidBufferBps","type":"uint64"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"uint64","name":"endTimestamp","type":"uint64"},{"internalType":"enum IEnglishAuctions.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IEnglishAuctions.Status","name":"status","type":"uint8"}],"internalType":"struct IEnglishAuctions.Auction","name":"_auction","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_auctionId","type":"uint256"}],"name":"getWinningBid","outputs":[{"internalType":"address","name":"_bidder","type":"address"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_bidAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_auctionId","type":"uint256"}],"name":"isAuctionExpired","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_auctionId","type":"uint256"},{"internalType":"uint256","name":"_bidAmount","type":"uint256"}],"name":"isNewWinningBid","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalAuctions","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
