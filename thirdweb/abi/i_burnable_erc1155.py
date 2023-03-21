"""Generated wrapper for IBurnableERC1155 Solidity contract."""

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
# constructor for IBurnableERC1155 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IBurnableERC1155Validator,
    )
except ImportError:

    class IBurnableERC1155Validator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class BurnMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the burn method."""

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
        self, account: str, _id: int, value: int
    ):
        """Validate the inputs to the burn method."""
        self.validator.assert_valid(
            method_name="burn",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="burn",
            parameter_name="id",
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        self.validator.assert_valid(
            method_name="burn",
            parameter_name="value",
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        return (account, _id, value)

    def call(
        self,
        account: str,
        _id: int,
        value: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, _id, value) = self.validate_and_normalize_inputs(
            account, _id, value
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, _id, value).call(tx_params.as_dict())

    def send_transaction(
        self,
        account: str,
        _id: int,
        value: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, _id, value) = self.validate_and_normalize_inputs(
            account, _id, value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id, value).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        account: str,
        _id: int,
        value: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, _id, value) = self.validate_and_normalize_inputs(
            account, _id, value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id, value).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        account: str,
        _id: int,
        value: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, _id, value) = self.validate_and_normalize_inputs(
            account, _id, value
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, _id, value).estimateGas(
            tx_params.as_dict()
        )


class BurnBatchMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the burnBatch method."""

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
        self, account: str, ids: List[int], values: List[int]
    ):
        """Validate the inputs to the burnBatch method."""
        self.validator.assert_valid(
            method_name="burnBatch",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="burnBatch",
            parameter_name="ids",
            argument_value=ids,
        )
        self.validator.assert_valid(
            method_name="burnBatch",
            parameter_name="values",
            argument_value=values,
        )
        return (account, ids, values)

    def call(
        self,
        account: str,
        ids: List[int],
        values: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, ids, values) = self.validate_and_normalize_inputs(
            account, ids, values
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, ids, values).call(tx_params.as_dict())

    def send_transaction(
        self,
        account: str,
        ids: List[int],
        values: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, ids, values) = self.validate_and_normalize_inputs(
            account, ids, values
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, ids, values).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        account: str,
        ids: List[int],
        values: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, ids, values) = self.validate_and_normalize_inputs(
            account, ids, values
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, ids, values).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        account: str,
        ids: List[int],
        values: List[int],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, ids, values) = self.validate_and_normalize_inputs(
            account, ids, values
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, ids, values).estimateGas(
            tx_params.as_dict()
        )


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IBurnableERC1155:
    """Wrapper class for IBurnableERC1155 Solidity contract."""

    burn: BurnMethod
    """Constructor-initialized instance of
    :class:`BurnMethod`.
    """

    burn_batch: BurnBatchMethod
    """Constructor-initialized instance of
    :class:`BurnBatchMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IBurnableERC1155Validator = None,
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
            validator = IBurnableERC1155Validator(
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
            abi=IBurnableERC1155.abi(),
        ).functions

        self.burn = BurnMethod(
            web3_or_provider, contract_address, functions.burn, validator
        )

        self.burn_batch = BurnBatchMethod(
            web3_or_provider, contract_address, functions.burnBatch, validator
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"burnBatch","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
