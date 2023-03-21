"""Generated wrapper for IAirdropERC1155Claimable Solidity contract."""

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
# constructor for IAirdropERC1155Claimable below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IAirdropERC1155ClaimableValidator,
    )
except ImportError:

    class IAirdropERC1155ClaimableValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class ClaimMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the claim method."""

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
        receiver: str,
        quantity: int,
        token_id: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_for_wallet: int,
    ):
        """Validate the inputs to the claim method."""
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="receiver",
            argument_value=receiver,
        )
        receiver = self.validate_and_checksum_address(receiver)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="tokenId",
            argument_value=token_id,
        )
        # safeguard against fractional inputs
        token_id = int(token_id)
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="proofs",
            argument_value=proofs,
        )
        self.validator.assert_valid(
            method_name="claim",
            parameter_name="proofMaxQuantityForWallet",
            argument_value=proof_max_quantity_for_wallet,
        )
        # safeguard against fractional inputs
        proof_max_quantity_for_wallet = int(proof_max_quantity_for_wallet)
        return (
            receiver,
            quantity,
            token_id,
            proofs,
            proof_max_quantity_for_wallet,
        )

    def call(
        self,
        receiver: str,
        quantity: int,
        token_id: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_for_wallet: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            receiver,
            quantity,
            token_id,
            proofs,
            proof_max_quantity_for_wallet,
        ) = self.validate_and_normalize_inputs(
            receiver, quantity, token_id, proofs, proof_max_quantity_for_wallet
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            receiver, quantity, token_id, proofs, proof_max_quantity_for_wallet
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        receiver: str,
        quantity: int,
        token_id: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_for_wallet: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            receiver,
            quantity,
            token_id,
            proofs,
            proof_max_quantity_for_wallet,
        ) = self.validate_and_normalize_inputs(
            receiver, quantity, token_id, proofs, proof_max_quantity_for_wallet
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver, quantity, token_id, proofs, proof_max_quantity_for_wallet
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        receiver: str,
        quantity: int,
        token_id: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_for_wallet: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            receiver,
            quantity,
            token_id,
            proofs,
            proof_max_quantity_for_wallet,
        ) = self.validate_and_normalize_inputs(
            receiver, quantity, token_id, proofs, proof_max_quantity_for_wallet
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver, quantity, token_id, proofs, proof_max_quantity_for_wallet
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        receiver: str,
        quantity: int,
        token_id: int,
        proofs: List[Union[bytes, str]],
        proof_max_quantity_for_wallet: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            receiver,
            quantity,
            token_id,
            proofs,
            proof_max_quantity_for_wallet,
        ) = self.validate_and_normalize_inputs(
            receiver, quantity, token_id, proofs, proof_max_quantity_for_wallet
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            receiver, quantity, token_id, proofs, proof_max_quantity_for_wallet
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IAirdropERC1155Claimable:
    """Wrapper class for IAirdropERC1155Claimable Solidity contract."""

    claim: ClaimMethod
    """Constructor-initialized instance of
    :class:`ClaimMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IAirdropERC1155ClaimableValidator = None,
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
            validator = IAirdropERC1155ClaimableValidator(
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
            abi=IAirdropERC1155Claimable.abi(),
        ).functions

        self.claim = ClaimMethod(
            web3_or_provider, contract_address, functions.claim, validator
        )

    def get_tokens_claimed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensClaimed event.

        :param tx_hash: hash of transaction emitting TokensClaimed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IAirdropERC1155Claimable.abi(),
            )
            .events.TokensClaimed()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"claimer","type":"address"},{"indexed":true,"internalType":"address","name":"receiver","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"quantityClaimed","type":"uint256"}],"name":"TokensClaimed","type":"event"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes32[]","name":"proofs","type":"bytes32[]"},{"internalType":"uint256","name":"proofMaxQuantityForWallet","type":"uint256"}],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
