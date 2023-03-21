"""Generated wrapper for IPack Solidity contract."""

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
# constructor for IPack below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IPackValidator,
    )
except ImportError:

    class IPackValidator(Validator):  # type: ignore
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


class CreatePackMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the createPack method."""

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
        contents: List[ITokenBundleToken],
        num_of_reward_units: List[int],
        pack_uri: str,
        open_start_timestamp: int,
        amount_distributed_per_open: int,
        recipient: str,
    ):
        """Validate the inputs to the createPack method."""
        self.validator.assert_valid(
            method_name="createPack",
            parameter_name="contents",
            argument_value=contents,
        )
        self.validator.assert_valid(
            method_name="createPack",
            parameter_name="numOfRewardUnits",
            argument_value=num_of_reward_units,
        )
        self.validator.assert_valid(
            method_name="createPack",
            parameter_name="packUri",
            argument_value=pack_uri,
        )
        self.validator.assert_valid(
            method_name="createPack",
            parameter_name="openStartTimestamp",
            argument_value=open_start_timestamp,
        )
        self.validator.assert_valid(
            method_name="createPack",
            parameter_name="amountDistributedPerOpen",
            argument_value=amount_distributed_per_open,
        )
        self.validator.assert_valid(
            method_name="createPack",
            parameter_name="recipient",
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        return (
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        )

    def call(
        self,
        contents: List[ITokenBundleToken],
        num_of_reward_units: List[int],
        pack_uri: str,
        open_start_timestamp: int,
        amount_distributed_per_open: int,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        ) = self.validate_and_normalize_inputs(
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        ).call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self,
        contents: List[ITokenBundleToken],
        num_of_reward_units: List[int],
        pack_uri: str,
        open_start_timestamp: int,
        amount_distributed_per_open: int,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        ) = self.validate_and_normalize_inputs(
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        contents: List[ITokenBundleToken],
        num_of_reward_units: List[int],
        pack_uri: str,
        open_start_timestamp: int,
        amount_distributed_per_open: int,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        ) = self.validate_and_normalize_inputs(
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        contents: List[ITokenBundleToken],
        num_of_reward_units: List[int],
        pack_uri: str,
        open_start_timestamp: int,
        amount_distributed_per_open: int,
        recipient: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        ) = self.validate_and_normalize_inputs(
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            contents,
            num_of_reward_units,
            pack_uri,
            open_start_timestamp,
            amount_distributed_per_open,
            recipient,
        ).estimateGas(tx_params.as_dict())


class OpenPackMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the openPack method."""

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

    def validate_and_normalize_inputs(self, pack_id: int, amount_to_open: int):
        """Validate the inputs to the openPack method."""
        self.validator.assert_valid(
            method_name="openPack",
            parameter_name="packId",
            argument_value=pack_id,
        )
        # safeguard against fractional inputs
        pack_id = int(pack_id)
        self.validator.assert_valid(
            method_name="openPack",
            parameter_name="amountToOpen",
            argument_value=amount_to_open,
        )
        # safeguard against fractional inputs
        amount_to_open = int(amount_to_open)
        return (pack_id, amount_to_open)

    def call(
        self,
        pack_id: int,
        amount_to_open: int,
        tx_params: Optional[TxParams] = None,
    ) -> List[ITokenBundleToken]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (pack_id, amount_to_open) = self.validate_and_normalize_inputs(
            pack_id, amount_to_open
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(pack_id, amount_to_open).call(
            tx_params.as_dict()
        )
        return [
            ITokenBundleToken(
                assetContract=element[0],
                tokenType=element[1],
                tokenId=element[2],
                totalAmount=element[3],
            )
            for element in returned
        ]

    def send_transaction(
        self,
        pack_id: int,
        amount_to_open: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (pack_id, amount_to_open) = self.validate_and_normalize_inputs(
            pack_id, amount_to_open
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pack_id, amount_to_open).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        pack_id: int,
        amount_to_open: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (pack_id, amount_to_open) = self.validate_and_normalize_inputs(
            pack_id, amount_to_open
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            pack_id, amount_to_open
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        pack_id: int,
        amount_to_open: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (pack_id, amount_to_open) = self.validate_and_normalize_inputs(
            pack_id, amount_to_open
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pack_id, amount_to_open).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IPack:
    """Wrapper class for IPack Solidity contract."""

    create_pack: CreatePackMethod
    """Constructor-initialized instance of
    :class:`CreatePackMethod`.
    """

    open_pack: OpenPackMethod
    """Constructor-initialized instance of
    :class:`OpenPackMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IPackValidator = None,
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
            validator = IPackValidator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=IPack.abi()
        ).functions

        self.create_pack = CreatePackMethod(
            web3_or_provider, contract_address, functions.createPack, validator
        )

        self.open_pack = OpenPackMethod(
            web3_or_provider, contract_address, functions.openPack, validator
        )

    def get_pack_created_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PackCreated event.

        :param tx_hash: hash of transaction emitting PackCreated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IPack.abi(),
            )
            .events.PackCreated()
            .processReceipt(tx_receipt)
        )

    def get_pack_opened_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PackOpened event.

        :param tx_hash: hash of transaction emitting PackOpened event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IPack.abi(),
            )
            .events.PackOpened()
            .processReceipt(tx_receipt)
        )

    def get_pack_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PackUpdated event.

        :param tx_hash: hash of transaction emitting PackUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IPack.abi(),
            )
            .events.PackUpdated()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"packId","type":"uint256"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"totalPacksCreated","type":"uint256"}],"name":"PackCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"packId","type":"uint256"},{"indexed":true,"internalType":"address","name":"opener","type":"address"},{"indexed":false,"internalType":"uint256","name":"numOfPacksOpened","type":"uint256"},{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"enum ITokenBundle.TokenType","name":"tokenType","type":"uint8"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"totalAmount","type":"uint256"}],"indexed":false,"internalType":"struct ITokenBundle.Token[]","name":"rewardUnitsDistributed","type":"tuple[]"}],"name":"PackOpened","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"packId","type":"uint256"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"totalPacksCreated","type":"uint256"}],"name":"PackUpdated","type":"event"},{"inputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"enum ITokenBundle.TokenType","name":"tokenType","type":"uint8"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"totalAmount","type":"uint256"}],"internalType":"struct ITokenBundle.Token[]","name":"contents","type":"tuple[]"},{"internalType":"uint256[]","name":"numOfRewardUnits","type":"uint256[]"},{"internalType":"string","name":"packUri","type":"string"},{"internalType":"uint128","name":"openStartTimestamp","type":"uint128"},{"internalType":"uint128","name":"amountDistributedPerOpen","type":"uint128"},{"internalType":"address","name":"recipient","type":"address"}],"name":"createPack","outputs":[{"internalType":"uint256","name":"packId","type":"uint256"},{"internalType":"uint256","name":"packTotalSupply","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"packId","type":"uint256"},{"internalType":"uint256","name":"amountToOpen","type":"uint256"}],"name":"openPack","outputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"enum ITokenBundle.TokenType","name":"tokenType","type":"uint8"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"totalAmount","type":"uint256"}],"internalType":"struct ITokenBundle.Token[]","name":"","type":"tuple[]"}],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
