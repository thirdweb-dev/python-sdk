"""Generated wrapper for LazyMintWithTier Solidity contract."""

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
# constructor for LazyMintWithTier below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        LazyMintWithTierValidator,
    )
except ImportError:

    class LazyMintWithTierValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class LazyMintWithTierTokenRange(TypedDict):
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

    startIdInclusive: int

    endIdNonInclusive: int


class LazyMintWithTierTierMetadata(TypedDict):
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

    tier: str

    ranges: List[LazyMintWithTierTokenRange]

    baseURIs: List[str]


class GetBaseUriCountMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getBaseURICount method."""

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


class GetBatchIdAtIndexMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getBatchIdAtIndex method."""

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

    def validate_and_normalize_inputs(self, index: int):
        """Validate the inputs to the getBatchIdAtIndex method."""
        self.validator.assert_valid(
            method_name="getBatchIdAtIndex",
            parameter_name="_index",
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return index

    def call(self, index: int, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, index: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index).transact(tx_params.as_dict())

    def build_transaction(
        self, index: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index).estimateGas(tx_params.as_dict())


class GetMetadataForAllTiersMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the getMetadataForAllTiers method."""

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
    ) -> List[LazyMintWithTierTierMetadata]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            LazyMintWithTierTierMetadata(
                tier=element[0],
                ranges=element[1],
                baseURIs=element[2],
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


class LazyMintMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the lazyMint method."""

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
        amount: int,
        base_uri_for_tokens: str,
        tier: str,
        data: Union[bytes, str],
    ):
        """Validate the inputs to the lazyMint method."""
        self.validator.assert_valid(
            method_name="lazyMint",
            parameter_name="_amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name="lazyMint",
            parameter_name="_baseURIForTokens",
            argument_value=base_uri_for_tokens,
        )
        self.validator.assert_valid(
            method_name="lazyMint",
            parameter_name="_tier",
            argument_value=tier,
        )
        self.validator.assert_valid(
            method_name="lazyMint",
            parameter_name="_data",
            argument_value=data,
        )
        return (amount, base_uri_for_tokens, tier, data)

    def call(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tier: str,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            amount,
            base_uri_for_tokens,
            tier,
            data,
        ) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens, tier, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            amount, base_uri_for_tokens, tier, data
        ).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tier: str,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            amount,
            base_uri_for_tokens,
            tier,
            data,
        ) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens, tier, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            amount, base_uri_for_tokens, tier, data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tier: str,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            amount,
            base_uri_for_tokens,
            tier,
            data,
        ) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens, tier, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            amount, base_uri_for_tokens, tier, data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tier: str,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            amount,
            base_uri_for_tokens,
            tier,
            data,
        ) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens, tier, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            amount, base_uri_for_tokens, tier, data
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class LazyMintWithTier:
    """Wrapper class for LazyMintWithTier Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    get_base_uri_count: GetBaseUriCountMethod
    """Constructor-initialized instance of
    :class:`GetBaseUriCountMethod`.
    """

    get_batch_id_at_index: GetBatchIdAtIndexMethod
    """Constructor-initialized instance of
    :class:`GetBatchIdAtIndexMethod`.
    """

    get_metadata_for_all_tiers: GetMetadataForAllTiersMethod
    """Constructor-initialized instance of
    :class:`GetMetadataForAllTiersMethod`.
    """

    lazy_mint: LazyMintMethod
    """Constructor-initialized instance of
    :class:`LazyMintMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: LazyMintWithTierValidator = None,
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
            validator = LazyMintWithTierValidator(
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
            abi=LazyMintWithTier.abi(),
        ).functions

        self.get_base_uri_count = GetBaseUriCountMethod(
            web3_or_provider, contract_address, functions.getBaseURICount
        )

        self.get_batch_id_at_index = GetBatchIdAtIndexMethod(
            web3_or_provider,
            contract_address,
            functions.getBatchIdAtIndex,
            validator,
        )

        self.get_metadata_for_all_tiers = GetMetadataForAllTiersMethod(
            web3_or_provider,
            contract_address,
            functions.getMetadataForAllTiers,
        )

        self.lazy_mint = LazyMintMethod(
            web3_or_provider, contract_address, functions.lazyMint, validator
        )

    def get_tokens_lazy_minted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensLazyMinted event.

        :param tx_hash: hash of transaction emitting TokensLazyMinted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=LazyMintWithTier.abi(),
            )
            .events.TokensLazyMinted()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"string","name":"tier","type":"string"},{"indexed":true,"internalType":"uint256","name":"startTokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"endTokenId","type":"uint256"},{"indexed":false,"internalType":"string","name":"baseURI","type":"string"},{"indexed":false,"internalType":"bytes","name":"encryptedBaseURI","type":"bytes"}],"name":"TokensLazyMinted","type":"event"},{"inputs":[],"name":"getBaseURICount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getBatchIdAtIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMetadataForAllTiers","outputs":[{"components":[{"internalType":"string","name":"tier","type":"string"},{"components":[{"internalType":"uint256","name":"startIdInclusive","type":"uint256"},{"internalType":"uint256","name":"endIdNonInclusive","type":"uint256"}],"internalType":"struct LazyMintWithTier.TokenRange[]","name":"ranges","type":"tuple[]"},{"internalType":"string[]","name":"baseURIs","type":"string[]"}],"internalType":"struct LazyMintWithTier.TierMetadata[]","name":"metadataForAllTiers","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"string","name":"_baseURIForTokens","type":"string"},{"internalType":"string","name":"_tier","type":"string"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"lazyMint","outputs":[{"internalType":"uint256","name":"batchId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
