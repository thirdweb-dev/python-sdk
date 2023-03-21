"""Generated wrapper for VoteERC20 Solidity contract."""

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
# constructor for VoteERC20 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        VoteERC20Validator,
    )
except ImportError:

    class VoteERC20Validator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class VoteERC20Proposal(TypedDict):
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

    proposalId: int

    proposer: str

    targets: List[str]

    values: List[int]

    signatures: List[str]

    calldatas: List[Union[bytes, str]]

    startBlock: int

    endBlock: int

    description: str


class BallotTypehashMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the BALLOT_TYPEHASH method."""

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


class CountingModeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the COUNTING_MODE method."""

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


class ExtendedBallotTypehashMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the EXTENDED_BALLOT_TYPEHASH method."""

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


class CastVoteMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the castVote method."""

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

    def validate_and_normalize_inputs(self, proposal_id: int, support: int):
        """Validate the inputs to the castVote method."""
        self.validator.assert_valid(
            method_name="castVote",
            parameter_name="proposalId",
            argument_value=proposal_id,
        )
        # safeguard against fractional inputs
        proposal_id = int(proposal_id)
        self.validator.assert_valid(
            method_name="castVote",
            parameter_name="support",
            argument_value=support,
        )
        return (proposal_id, support)

    def call(
        self,
        proposal_id: int,
        support: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (proposal_id, support) = self.validate_and_normalize_inputs(
            proposal_id, support
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(proposal_id, support).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self,
        proposal_id: int,
        support: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (proposal_id, support) = self.validate_and_normalize_inputs(
            proposal_id, support
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id, support).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        proposal_id: int,
        support: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (proposal_id, support) = self.validate_and_normalize_inputs(
            proposal_id, support
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id, support).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        proposal_id: int,
        support: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (proposal_id, support) = self.validate_and_normalize_inputs(
            proposal_id, support
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id, support).estimateGas(
            tx_params.as_dict()
        )


class CastVoteBySigMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the castVoteBySig method."""

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
        proposal_id: int,
        support: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
    ):
        """Validate the inputs to the castVoteBySig method."""
        self.validator.assert_valid(
            method_name="castVoteBySig",
            parameter_name="proposalId",
            argument_value=proposal_id,
        )
        # safeguard against fractional inputs
        proposal_id = int(proposal_id)
        self.validator.assert_valid(
            method_name="castVoteBySig",
            parameter_name="support",
            argument_value=support,
        )
        self.validator.assert_valid(
            method_name="castVoteBySig",
            parameter_name="v",
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name="castVoteBySig",
            parameter_name="r",
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name="castVoteBySig",
            parameter_name="s",
            argument_value=s,
        )
        return (proposal_id, support, v, r, s)

    def call(
        self,
        proposal_id: int,
        support: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (proposal_id, support, v, r, s) = self.validate_and_normalize_inputs(
            proposal_id, support, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(proposal_id, support, v, r, s).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self,
        proposal_id: int,
        support: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (proposal_id, support, v, r, s) = self.validate_and_normalize_inputs(
            proposal_id, support, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id, support, v, r, s).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        proposal_id: int,
        support: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (proposal_id, support, v, r, s) = self.validate_and_normalize_inputs(
            proposal_id, support, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            proposal_id, support, v, r, s
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        proposal_id: int,
        support: int,
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (proposal_id, support, v, r, s) = self.validate_and_normalize_inputs(
            proposal_id, support, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            proposal_id, support, v, r, s
        ).estimateGas(tx_params.as_dict())


class CastVoteWithReasonMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the castVoteWithReason method."""

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
        self, proposal_id: int, support: int, reason: str
    ):
        """Validate the inputs to the castVoteWithReason method."""
        self.validator.assert_valid(
            method_name="castVoteWithReason",
            parameter_name="proposalId",
            argument_value=proposal_id,
        )
        # safeguard against fractional inputs
        proposal_id = int(proposal_id)
        self.validator.assert_valid(
            method_name="castVoteWithReason",
            parameter_name="support",
            argument_value=support,
        )
        self.validator.assert_valid(
            method_name="castVoteWithReason",
            parameter_name="reason",
            argument_value=reason,
        )
        return (proposal_id, support, reason)

    def call(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (proposal_id, support, reason) = self.validate_and_normalize_inputs(
            proposal_id, support, reason
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(proposal_id, support, reason).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (proposal_id, support, reason) = self.validate_and_normalize_inputs(
            proposal_id, support, reason
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id, support, reason).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (proposal_id, support, reason) = self.validate_and_normalize_inputs(
            proposal_id, support, reason
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            proposal_id, support, reason
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (proposal_id, support, reason) = self.validate_and_normalize_inputs(
            proposal_id, support, reason
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            proposal_id, support, reason
        ).estimateGas(tx_params.as_dict())


class CastVoteWithReasonAndParamsMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the castVoteWithReasonAndParams method."""

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
        proposal_id: int,
        support: int,
        reason: str,
        params: Union[bytes, str],
    ):
        """Validate the inputs to the castVoteWithReasonAndParams method."""
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParams",
            parameter_name="proposalId",
            argument_value=proposal_id,
        )
        # safeguard against fractional inputs
        proposal_id = int(proposal_id)
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParams",
            parameter_name="support",
            argument_value=support,
        )
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParams",
            parameter_name="reason",
            argument_value=reason,
        )
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParams",
            parameter_name="params",
            argument_value=params,
        )
        return (proposal_id, support, reason, params)

    def call(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        params: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            proposal_id,
            support,
            reason,
            params,
        ) = self.validate_and_normalize_inputs(
            proposal_id, support, reason, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            proposal_id, support, reason, params
        ).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        params: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            proposal_id,
            support,
            reason,
            params,
        ) = self.validate_and_normalize_inputs(
            proposal_id, support, reason, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            proposal_id, support, reason, params
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        params: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            proposal_id,
            support,
            reason,
            params,
        ) = self.validate_and_normalize_inputs(
            proposal_id, support, reason, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            proposal_id, support, reason, params
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        params: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            proposal_id,
            support,
            reason,
            params,
        ) = self.validate_and_normalize_inputs(
            proposal_id, support, reason, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            proposal_id, support, reason, params
        ).estimateGas(tx_params.as_dict())


class CastVoteWithReasonAndParamsBySigMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the castVoteWithReasonAndParamsBySig method."""

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
        proposal_id: int,
        support: int,
        reason: str,
        params: Union[bytes, str],
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
    ):
        """Validate the inputs to the castVoteWithReasonAndParamsBySig method."""
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParamsBySig",
            parameter_name="proposalId",
            argument_value=proposal_id,
        )
        # safeguard against fractional inputs
        proposal_id = int(proposal_id)
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParamsBySig",
            parameter_name="support",
            argument_value=support,
        )
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParamsBySig",
            parameter_name="reason",
            argument_value=reason,
        )
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParamsBySig",
            parameter_name="params",
            argument_value=params,
        )
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParamsBySig",
            parameter_name="v",
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParamsBySig",
            parameter_name="r",
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name="castVoteWithReasonAndParamsBySig",
            parameter_name="s",
            argument_value=s,
        )
        return (proposal_id, support, reason, params, v, r, s)

    def call(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        params: Union[bytes, str],
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            proposal_id,
            support,
            reason,
            params,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            proposal_id, support, reason, params, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            proposal_id, support, reason, params, v, r, s
        ).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        params: Union[bytes, str],
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            proposal_id,
            support,
            reason,
            params,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            proposal_id, support, reason, params, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            proposal_id, support, reason, params, v, r, s
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        params: Union[bytes, str],
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            proposal_id,
            support,
            reason,
            params,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            proposal_id, support, reason, params, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            proposal_id, support, reason, params, v, r, s
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        proposal_id: int,
        support: int,
        reason: str,
        params: Union[bytes, str],
        v: int,
        r: Union[bytes, str],
        s: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            proposal_id,
            support,
            reason,
            params,
            v,
            r,
            s,
        ) = self.validate_and_normalize_inputs(
            proposal_id, support, reason, params, v, r, s
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            proposal_id, support, reason, params, v, r, s
        ).estimateGas(tx_params.as_dict())


class ContractTypeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractType method."""

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


class ContractVersionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractVersion method."""

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


class ExecuteMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the execute method."""

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
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description_hash: Union[bytes, str],
    ):
        """Validate the inputs to the execute method."""
        self.validator.assert_valid(
            method_name="execute",
            parameter_name="targets",
            argument_value=targets,
        )
        self.validator.assert_valid(
            method_name="execute",
            parameter_name="values",
            argument_value=values,
        )
        self.validator.assert_valid(
            method_name="execute",
            parameter_name="calldatas",
            argument_value=calldatas,
        )
        self.validator.assert_valid(
            method_name="execute",
            parameter_name="descriptionHash",
            argument_value=description_hash,
        )
        return (targets, values, calldatas, description_hash)

    def call(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            targets,
            values,
            calldatas,
            description_hash,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            targets, values, calldatas, description_hash
        ).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            targets,
            values,
            calldatas,
            description_hash,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            targets, values, calldatas, description_hash
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            targets,
            values,
            calldatas,
            description_hash,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            targets, values, calldatas, description_hash
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            targets,
            values,
            calldatas,
            description_hash,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            targets, values, calldatas, description_hash
        ).estimateGas(tx_params.as_dict())


class GetAllProposalsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getAllProposals method."""

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
    ) -> List[VoteERC20Proposal]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return [
            VoteERC20Proposal(
                proposalId=element[0],
                proposer=element[1],
                targets=element[2],
                values=element[3],
                signatures=element[4],
                calldatas=element[5],
                startBlock=element[6],
                endBlock=element[7],
                description=element[8],
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


class GetVotesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getVotes method."""

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

    def validate_and_normalize_inputs(self, account: str, block_number: int):
        """Validate the inputs to the getVotes method."""
        self.validator.assert_valid(
            method_name="getVotes",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="getVotes",
            parameter_name="blockNumber",
            argument_value=block_number,
        )
        # safeguard against fractional inputs
        block_number = int(block_number)
        return (account, block_number)

    def call(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, block_number).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, block_number).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, block_number).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        account: str,
        block_number: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, block_number) = self.validate_and_normalize_inputs(
            account, block_number
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, block_number).estimateGas(
            tx_params.as_dict()
        )


class GetVotesWithParamsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getVotesWithParams method."""

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
        self, account: str, block_number: int, params: Union[bytes, str]
    ):
        """Validate the inputs to the getVotesWithParams method."""
        self.validator.assert_valid(
            method_name="getVotesWithParams",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name="getVotesWithParams",
            parameter_name="blockNumber",
            argument_value=block_number,
        )
        # safeguard against fractional inputs
        block_number = int(block_number)
        self.validator.assert_valid(
            method_name="getVotesWithParams",
            parameter_name="params",
            argument_value=params,
        )
        return (account, block_number, params)

    def call(
        self,
        account: str,
        block_number: int,
        params: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, block_number, params) = self.validate_and_normalize_inputs(
            account, block_number, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account, block_number, params).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self,
        account: str,
        block_number: int,
        params: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, block_number, params) = self.validate_and_normalize_inputs(
            account, block_number, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, block_number, params).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        account: str,
        block_number: int,
        params: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, block_number, params) = self.validate_and_normalize_inputs(
            account, block_number, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            account, block_number, params
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        account: str,
        block_number: int,
        params: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (account, block_number, params) = self.validate_and_normalize_inputs(
            account, block_number, params
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            account, block_number, params
        ).estimateGas(tx_params.as_dict())


class HasVotedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the hasVoted method."""

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

    def validate_and_normalize_inputs(self, proposal_id: int, account: str):
        """Validate the inputs to the hasVoted method."""
        self.validator.assert_valid(
            method_name="hasVoted",
            parameter_name="proposalId",
            argument_value=proposal_id,
        )
        # safeguard against fractional inputs
        proposal_id = int(proposal_id)
        self.validator.assert_valid(
            method_name="hasVoted",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (proposal_id, account)

    def call(
        self,
        proposal_id: int,
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (proposal_id, account) = self.validate_and_normalize_inputs(
            proposal_id, account
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(proposal_id, account).call(
            tx_params.as_dict()
        )
        return bool(returned)

    def send_transaction(
        self,
        proposal_id: int,
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (proposal_id, account) = self.validate_and_normalize_inputs(
            proposal_id, account
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        proposal_id: int,
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (proposal_id, account) = self.validate_and_normalize_inputs(
            proposal_id, account
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        proposal_id: int,
        account: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (proposal_id, account) = self.validate_and_normalize_inputs(
            proposal_id, account
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id, account).estimateGas(
            tx_params.as_dict()
        )


class HashProposalMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the hashProposal method."""

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
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description_hash: Union[bytes, str],
    ):
        """Validate the inputs to the hashProposal method."""
        self.validator.assert_valid(
            method_name="hashProposal",
            parameter_name="targets",
            argument_value=targets,
        )
        self.validator.assert_valid(
            method_name="hashProposal",
            parameter_name="values",
            argument_value=values,
        )
        self.validator.assert_valid(
            method_name="hashProposal",
            parameter_name="calldatas",
            argument_value=calldatas,
        )
        self.validator.assert_valid(
            method_name="hashProposal",
            parameter_name="descriptionHash",
            argument_value=description_hash,
        )
        return (targets, values, calldatas, description_hash)

    def call(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            targets,
            values,
            calldatas,
            description_hash,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            targets, values, calldatas, description_hash
        ).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            targets,
            values,
            calldatas,
            description_hash,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            targets, values, calldatas, description_hash
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            targets,
            values,
            calldatas,
            description_hash,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            targets, values, calldatas, description_hash
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description_hash: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            targets,
            values,
            calldatas,
            description_hash,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description_hash
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            targets, values, calldatas, description_hash
        ).estimateGas(tx_params.as_dict())


class InitializeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the initialize method."""

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
        name: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        token: str,
        initial_voting_delay: int,
        initial_voting_period: int,
        initial_proposal_threshold: int,
        initial_vote_quorum_fraction: int,
    ):
        """Validate the inputs to the initialize method."""
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_name",
            argument_value=name,
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_contractURI",
            argument_value=contract_uri,
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_trustedForwarders",
            argument_value=trusted_forwarders,
        )
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_token",
            argument_value=token,
        )
        token = self.validate_and_checksum_address(token)
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_initialVotingDelay",
            argument_value=initial_voting_delay,
        )
        # safeguard against fractional inputs
        initial_voting_delay = int(initial_voting_delay)
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_initialVotingPeriod",
            argument_value=initial_voting_period,
        )
        # safeguard against fractional inputs
        initial_voting_period = int(initial_voting_period)
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_initialProposalThreshold",
            argument_value=initial_proposal_threshold,
        )
        # safeguard against fractional inputs
        initial_proposal_threshold = int(initial_proposal_threshold)
        self.validator.assert_valid(
            method_name="initialize",
            parameter_name="_initialVoteQuorumFraction",
            argument_value=initial_vote_quorum_fraction,
        )
        # safeguard against fractional inputs
        initial_vote_quorum_fraction = int(initial_vote_quorum_fraction)
        return (
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        )

    def call(
        self,
        name: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        token: str,
        initial_voting_delay: int,
        initial_voting_period: int,
        initial_proposal_threshold: int,
        initial_vote_quorum_fraction: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        ) = self.validate_and_normalize_inputs(
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        name: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        token: str,
        initial_voting_delay: int,
        initial_voting_period: int,
        initial_proposal_threshold: int,
        initial_vote_quorum_fraction: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        ) = self.validate_and_normalize_inputs(
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        name: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        token: str,
        initial_voting_delay: int,
        initial_voting_period: int,
        initial_proposal_threshold: int,
        initial_vote_quorum_fraction: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        ) = self.validate_and_normalize_inputs(
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        name: str,
        contract_uri: str,
        trusted_forwarders: List[str],
        token: str,
        initial_voting_delay: int,
        initial_voting_period: int,
        initial_proposal_threshold: int,
        initial_vote_quorum_fraction: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        ) = self.validate_and_normalize_inputs(
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            name,
            contract_uri,
            trusted_forwarders,
            token,
            initial_voting_delay,
            initial_voting_period,
            initial_proposal_threshold,
            initial_vote_quorum_fraction,
        ).estimateGas(tx_params.as_dict())


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


class NameMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the name method."""

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


class ProposalDeadlineMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the proposalDeadline method."""

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

    def validate_and_normalize_inputs(self, proposal_id: int):
        """Validate the inputs to the proposalDeadline method."""
        self.validator.assert_valid(
            method_name="proposalDeadline",
            parameter_name="proposalId",
            argument_value=proposal_id,
        )
        # safeguard against fractional inputs
        proposal_id = int(proposal_id)
        return proposal_id

    def call(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(proposal_id).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).estimateGas(
            tx_params.as_dict()
        )


class ProposalIndexMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the proposalIndex method."""

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


class ProposalSnapshotMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the proposalSnapshot method."""

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

    def validate_and_normalize_inputs(self, proposal_id: int):
        """Validate the inputs to the proposalSnapshot method."""
        self.validator.assert_valid(
            method_name="proposalSnapshot",
            parameter_name="proposalId",
            argument_value=proposal_id,
        )
        # safeguard against fractional inputs
        proposal_id = int(proposal_id)
        return proposal_id

    def call(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(proposal_id).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).estimateGas(
            tx_params.as_dict()
        )


class ProposalThresholdMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the proposalThreshold method."""

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


class ProposalVotesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the proposalVotes method."""

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

    def validate_and_normalize_inputs(self, proposal_id: int):
        """Validate the inputs to the proposalVotes method."""
        self.validator.assert_valid(
            method_name="proposalVotes",
            parameter_name="proposalId",
            argument_value=proposal_id,
        )
        # safeguard against fractional inputs
        proposal_id = int(proposal_id)
        return proposal_id

    def call(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[int, int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(proposal_id).call(
            tx_params.as_dict()
        )
        return (
            returned[0],
            returned[1],
            returned[2],
        )

    def send_transaction(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).estimateGas(
            tx_params.as_dict()
        )


class ProposalsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the proposals method."""

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
        """Validate the inputs to the proposals method."""
        self.validator.assert_valid(
            method_name="proposals",
            parameter_name="index_0",
            argument_value=index_0,
        )
        # safeguard against fractional inputs
        index_0 = int(index_0)
        return index_0

    def call(
        self, index_0: int, tx_params: Optional[TxParams] = None
    ) -> Tuple[int, str, int, int, str]:
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


class ProposeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the propose method."""

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
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description: str,
    ):
        """Validate the inputs to the propose method."""
        self.validator.assert_valid(
            method_name="propose",
            parameter_name="targets",
            argument_value=targets,
        )
        self.validator.assert_valid(
            method_name="propose",
            parameter_name="values",
            argument_value=values,
        )
        self.validator.assert_valid(
            method_name="propose",
            parameter_name="calldatas",
            argument_value=calldatas,
        )
        self.validator.assert_valid(
            method_name="propose",
            parameter_name="description",
            argument_value=description,
        )
        return (targets, values, calldatas, description)

    def call(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            targets,
            values,
            calldatas,
            description,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            targets, values, calldatas, description
        ).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            targets,
            values,
            calldatas,
            description,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            targets, values, calldatas, description
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            targets,
            values,
            calldatas,
            description,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            targets, values, calldatas, description
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        targets: List[str],
        values: List[int],
        calldatas: List[Union[bytes, str]],
        description: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            targets,
            values,
            calldatas,
            description,
        ) = self.validate_and_normalize_inputs(
            targets, values, calldatas, description
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            targets, values, calldatas, description
        ).estimateGas(tx_params.as_dict())


class QuorumMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the quorum method."""

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

    def validate_and_normalize_inputs(self, block_number: int):
        """Validate the inputs to the quorum method."""
        self.validator.assert_valid(
            method_name="quorum",
            parameter_name="blockNumber",
            argument_value=block_number,
        )
        # safeguard against fractional inputs
        block_number = int(block_number)
        return block_number

    def call(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(block_number).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).estimateGas(
            tx_params.as_dict()
        )


class QuorumDenominatorMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the quorumDenominator method."""

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


class QuorumNumerator2Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the quorumNumerator method."""

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

    def validate_and_normalize_inputs(self, block_number: int):
        """Validate the inputs to the quorumNumerator method."""
        self.validator.assert_valid(
            method_name="quorumNumerator",
            parameter_name="blockNumber",
            argument_value=block_number,
        )
        # safeguard against fractional inputs
        block_number = int(block_number)
        return block_number

    def call(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(block_number).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, block_number: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (block_number) = self.validate_and_normalize_inputs(block_number)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(block_number).estimateGas(
            tx_params.as_dict()
        )


class QuorumNumerator1Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the quorumNumerator method."""

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


class RelayMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the relay method."""

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
        self, target: str, value: int, data: Union[bytes, str]
    ):
        """Validate the inputs to the relay method."""
        self.validator.assert_valid(
            method_name="relay",
            parameter_name="target",
            argument_value=target,
        )
        target = self.validate_and_checksum_address(target)
        self.validator.assert_valid(
            method_name="relay",
            parameter_name="value",
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        self.validator.assert_valid(
            method_name="relay",
            parameter_name="data",
            argument_value=data,
        )
        return (target, value, data)

    def call(
        self,
        target: str,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (target, value, data) = self.validate_and_normalize_inputs(
            target, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(target, value, data).call(tx_params.as_dict())

    def send_transaction(
        self,
        target: str,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (target, value, data) = self.validate_and_normalize_inputs(
            target, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target, value, data).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        target: str,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (target, value, data) = self.validate_and_normalize_inputs(
            target, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target, value, data).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        target: str,
        value: int,
        data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (target, value, data) = self.validate_and_normalize_inputs(
            target, value, data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(target, value, data).estimateGas(
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
            parameter_name="uri",
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


class SetProposalThresholdMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the setProposalThreshold method."""

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

    def validate_and_normalize_inputs(self, new_proposal_threshold: int):
        """Validate the inputs to the setProposalThreshold method."""
        self.validator.assert_valid(
            method_name="setProposalThreshold",
            parameter_name="newProposalThreshold",
            argument_value=new_proposal_threshold,
        )
        # safeguard against fractional inputs
        new_proposal_threshold = int(new_proposal_threshold)
        return new_proposal_threshold

    def call(
        self, new_proposal_threshold: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_proposal_threshold) = self.validate_and_normalize_inputs(
            new_proposal_threshold
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_proposal_threshold).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self, new_proposal_threshold: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_proposal_threshold) = self.validate_and_normalize_inputs(
            new_proposal_threshold
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_proposal_threshold).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, new_proposal_threshold: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_proposal_threshold) = self.validate_and_normalize_inputs(
            new_proposal_threshold
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            new_proposal_threshold
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self, new_proposal_threshold: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (new_proposal_threshold) = self.validate_and_normalize_inputs(
            new_proposal_threshold
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_proposal_threshold).estimateGas(
            tx_params.as_dict()
        )


class SetVotingDelayMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setVotingDelay method."""

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

    def validate_and_normalize_inputs(self, new_voting_delay: int):
        """Validate the inputs to the setVotingDelay method."""
        self.validator.assert_valid(
            method_name="setVotingDelay",
            parameter_name="newVotingDelay",
            argument_value=new_voting_delay,
        )
        # safeguard against fractional inputs
        new_voting_delay = int(new_voting_delay)
        return new_voting_delay

    def call(
        self, new_voting_delay: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_voting_delay) = self.validate_and_normalize_inputs(
            new_voting_delay
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_voting_delay).call(tx_params.as_dict())

    def send_transaction(
        self, new_voting_delay: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_voting_delay) = self.validate_and_normalize_inputs(
            new_voting_delay
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_voting_delay).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, new_voting_delay: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_voting_delay) = self.validate_and_normalize_inputs(
            new_voting_delay
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_voting_delay).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, new_voting_delay: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (new_voting_delay) = self.validate_and_normalize_inputs(
            new_voting_delay
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_voting_delay).estimateGas(
            tx_params.as_dict()
        )


class SetVotingPeriodMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setVotingPeriod method."""

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

    def validate_and_normalize_inputs(self, new_voting_period: int):
        """Validate the inputs to the setVotingPeriod method."""
        self.validator.assert_valid(
            method_name="setVotingPeriod",
            parameter_name="newVotingPeriod",
            argument_value=new_voting_period,
        )
        # safeguard against fractional inputs
        new_voting_period = int(new_voting_period)
        return new_voting_period

    def call(
        self, new_voting_period: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_voting_period) = self.validate_and_normalize_inputs(
            new_voting_period
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_voting_period).call(tx_params.as_dict())

    def send_transaction(
        self, new_voting_period: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_voting_period) = self.validate_and_normalize_inputs(
            new_voting_period
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_voting_period).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, new_voting_period: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_voting_period) = self.validate_and_normalize_inputs(
            new_voting_period
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_voting_period).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, new_voting_period: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (new_voting_period) = self.validate_and_normalize_inputs(
            new_voting_period
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_voting_period).estimateGas(
            tx_params.as_dict()
        )


class StateMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the state method."""

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

    def validate_and_normalize_inputs(self, proposal_id: int):
        """Validate the inputs to the state method."""
        self.validator.assert_valid(
            method_name="state",
            parameter_name="proposalId",
            argument_value=proposal_id,
        )
        # safeguard against fractional inputs
        proposal_id = int(proposal_id)
        return proposal_id

    def call(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(proposal_id).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, proposal_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (proposal_id) = self.validate_and_normalize_inputs(proposal_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(proposal_id).estimateGas(
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


class TokenMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the token method."""

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


class UpdateQuorumNumeratorMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the updateQuorumNumerator method."""

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

    def validate_and_normalize_inputs(self, new_quorum_numerator: int):
        """Validate the inputs to the updateQuorumNumerator method."""
        self.validator.assert_valid(
            method_name="updateQuorumNumerator",
            parameter_name="newQuorumNumerator",
            argument_value=new_quorum_numerator,
        )
        # safeguard against fractional inputs
        new_quorum_numerator = int(new_quorum_numerator)
        return new_quorum_numerator

    def call(
        self, new_quorum_numerator: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_quorum_numerator) = self.validate_and_normalize_inputs(
            new_quorum_numerator
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_quorum_numerator).call(tx_params.as_dict())

    def send_transaction(
        self, new_quorum_numerator: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_quorum_numerator) = self.validate_and_normalize_inputs(
            new_quorum_numerator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_quorum_numerator).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, new_quorum_numerator: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_quorum_numerator) = self.validate_and_normalize_inputs(
            new_quorum_numerator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_quorum_numerator).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, new_quorum_numerator: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (new_quorum_numerator) = self.validate_and_normalize_inputs(
            new_quorum_numerator
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_quorum_numerator).estimateGas(
            tx_params.as_dict()
        )


class VersionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the version method."""

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


class VotingDelayMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the votingDelay method."""

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


class VotingPeriodMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the votingPeriod method."""

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
class VoteERC20:
    """Wrapper class for VoteERC20 Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    ballot_typehash: BallotTypehashMethod
    """Constructor-initialized instance of
    :class:`BallotTypehashMethod`.
    """

    counting_mode: CountingModeMethod
    """Constructor-initialized instance of
    :class:`CountingModeMethod`.
    """

    extended_ballot_typehash: ExtendedBallotTypehashMethod
    """Constructor-initialized instance of
    :class:`ExtendedBallotTypehashMethod`.
    """

    cast_vote: CastVoteMethod
    """Constructor-initialized instance of
    :class:`CastVoteMethod`.
    """

    cast_vote_by_sig: CastVoteBySigMethod
    """Constructor-initialized instance of
    :class:`CastVoteBySigMethod`.
    """

    cast_vote_with_reason: CastVoteWithReasonMethod
    """Constructor-initialized instance of
    :class:`CastVoteWithReasonMethod`.
    """

    cast_vote_with_reason_and_params: CastVoteWithReasonAndParamsMethod
    """Constructor-initialized instance of
    :class:`CastVoteWithReasonAndParamsMethod`.
    """

    cast_vote_with_reason_and_params_by_sig: CastVoteWithReasonAndParamsBySigMethod
    """Constructor-initialized instance of
    :class:`CastVoteWithReasonAndParamsBySigMethod`.
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

    execute: ExecuteMethod
    """Constructor-initialized instance of
    :class:`ExecuteMethod`.
    """

    get_all_proposals: GetAllProposalsMethod
    """Constructor-initialized instance of
    :class:`GetAllProposalsMethod`.
    """

    get_votes: GetVotesMethod
    """Constructor-initialized instance of
    :class:`GetVotesMethod`.
    """

    get_votes_with_params: GetVotesWithParamsMethod
    """Constructor-initialized instance of
    :class:`GetVotesWithParamsMethod`.
    """

    has_voted: HasVotedMethod
    """Constructor-initialized instance of
    :class:`HasVotedMethod`.
    """

    hash_proposal: HashProposalMethod
    """Constructor-initialized instance of
    :class:`HashProposalMethod`.
    """

    initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
    """

    is_trusted_forwarder: IsTrustedForwarderMethod
    """Constructor-initialized instance of
    :class:`IsTrustedForwarderMethod`.
    """

    name: NameMethod
    """Constructor-initialized instance of
    :class:`NameMethod`.
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

    proposal_deadline: ProposalDeadlineMethod
    """Constructor-initialized instance of
    :class:`ProposalDeadlineMethod`.
    """

    proposal_index: ProposalIndexMethod
    """Constructor-initialized instance of
    :class:`ProposalIndexMethod`.
    """

    proposal_snapshot: ProposalSnapshotMethod
    """Constructor-initialized instance of
    :class:`ProposalSnapshotMethod`.
    """

    proposal_threshold: ProposalThresholdMethod
    """Constructor-initialized instance of
    :class:`ProposalThresholdMethod`.
    """

    proposal_votes: ProposalVotesMethod
    """Constructor-initialized instance of
    :class:`ProposalVotesMethod`.
    """

    proposals: ProposalsMethod
    """Constructor-initialized instance of
    :class:`ProposalsMethod`.
    """

    propose: ProposeMethod
    """Constructor-initialized instance of
    :class:`ProposeMethod`.
    """

    quorum: QuorumMethod
    """Constructor-initialized instance of
    :class:`QuorumMethod`.
    """

    quorum_denominator: QuorumDenominatorMethod
    """Constructor-initialized instance of
    :class:`QuorumDenominatorMethod`.
    """

    quorum_numerator2: QuorumNumerator2Method
    """Constructor-initialized instance of
    :class:`QuorumNumerator2Method`.
    """

    quorum_numerator1: QuorumNumerator1Method
    """Constructor-initialized instance of
    :class:`QuorumNumerator1Method`.
    """

    relay: RelayMethod
    """Constructor-initialized instance of
    :class:`RelayMethod`.
    """

    set_contract_uri: SetContractUriMethod
    """Constructor-initialized instance of
    :class:`SetContractUriMethod`.
    """

    set_proposal_threshold: SetProposalThresholdMethod
    """Constructor-initialized instance of
    :class:`SetProposalThresholdMethod`.
    """

    set_voting_delay: SetVotingDelayMethod
    """Constructor-initialized instance of
    :class:`SetVotingDelayMethod`.
    """

    set_voting_period: SetVotingPeriodMethod
    """Constructor-initialized instance of
    :class:`SetVotingPeriodMethod`.
    """

    state: StateMethod
    """Constructor-initialized instance of
    :class:`StateMethod`.
    """

    supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    token: TokenMethod
    """Constructor-initialized instance of
    :class:`TokenMethod`.
    """

    update_quorum_numerator: UpdateQuorumNumeratorMethod
    """Constructor-initialized instance of
    :class:`UpdateQuorumNumeratorMethod`.
    """

    version: VersionMethod
    """Constructor-initialized instance of
    :class:`VersionMethod`.
    """

    voting_delay: VotingDelayMethod
    """Constructor-initialized instance of
    :class:`VotingDelayMethod`.
    """

    voting_period: VotingPeriodMethod
    """Constructor-initialized instance of
    :class:`VotingPeriodMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: VoteERC20Validator = None,
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
            validator = VoteERC20Validator(web3_or_provider, contract_address)

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
            address=to_checksum_address(contract_address), abi=VoteERC20.abi()
        ).functions

        self.ballot_typehash = BallotTypehashMethod(
            web3_or_provider, contract_address, functions.BALLOT_TYPEHASH
        )

        self.counting_mode = CountingModeMethod(
            web3_or_provider, contract_address, functions.COUNTING_MODE
        )

        self.extended_ballot_typehash = ExtendedBallotTypehashMethod(
            web3_or_provider,
            contract_address,
            functions.EXTENDED_BALLOT_TYPEHASH,
        )

        self.cast_vote = CastVoteMethod(
            web3_or_provider, contract_address, functions.castVote, validator
        )

        self.cast_vote_by_sig = CastVoteBySigMethod(
            web3_or_provider,
            contract_address,
            functions.castVoteBySig,
            validator,
        )

        self.cast_vote_with_reason = CastVoteWithReasonMethod(
            web3_or_provider,
            contract_address,
            functions.castVoteWithReason,
            validator,
        )

        self.cast_vote_with_reason_and_params = (
            CastVoteWithReasonAndParamsMethod(
                web3_or_provider,
                contract_address,
                functions.castVoteWithReasonAndParams,
                validator,
            )
        )

        self.cast_vote_with_reason_and_params_by_sig = (
            CastVoteWithReasonAndParamsBySigMethod(
                web3_or_provider,
                contract_address,
                functions.castVoteWithReasonAndParamsBySig,
                validator,
            )
        )

        self.contract_type = ContractTypeMethod(
            web3_or_provider, contract_address, functions.contractType
        )

        self.contract_uri = ContractUriMethod(
            web3_or_provider, contract_address, functions.contractURI
        )

        self.contract_version = ContractVersionMethod(
            web3_or_provider, contract_address, functions.contractVersion
        )

        self.execute = ExecuteMethod(
            web3_or_provider, contract_address, functions.execute, validator
        )

        self.get_all_proposals = GetAllProposalsMethod(
            web3_or_provider, contract_address, functions.getAllProposals
        )

        self.get_votes = GetVotesMethod(
            web3_or_provider, contract_address, functions.getVotes, validator
        )

        self.get_votes_with_params = GetVotesWithParamsMethod(
            web3_or_provider,
            contract_address,
            functions.getVotesWithParams,
            validator,
        )

        self.has_voted = HasVotedMethod(
            web3_or_provider, contract_address, functions.hasVoted, validator
        )

        self.hash_proposal = HashProposalMethod(
            web3_or_provider,
            contract_address,
            functions.hashProposal,
            validator,
        )

        self.initialize = InitializeMethod(
            web3_or_provider, contract_address, functions.initialize, validator
        )

        self.is_trusted_forwarder = IsTrustedForwarderMethod(
            web3_or_provider,
            contract_address,
            functions.isTrustedForwarder,
            validator,
        )

        self.name = NameMethod(
            web3_or_provider, contract_address, functions.name
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

        self.proposal_deadline = ProposalDeadlineMethod(
            web3_or_provider,
            contract_address,
            functions.proposalDeadline,
            validator,
        )

        self.proposal_index = ProposalIndexMethod(
            web3_or_provider, contract_address, functions.proposalIndex
        )

        self.proposal_snapshot = ProposalSnapshotMethod(
            web3_or_provider,
            contract_address,
            functions.proposalSnapshot,
            validator,
        )

        self.proposal_threshold = ProposalThresholdMethod(
            web3_or_provider, contract_address, functions.proposalThreshold
        )

        self.proposal_votes = ProposalVotesMethod(
            web3_or_provider,
            contract_address,
            functions.proposalVotes,
            validator,
        )

        self.proposals = ProposalsMethod(
            web3_or_provider, contract_address, functions.proposals, validator
        )

        self.propose = ProposeMethod(
            web3_or_provider, contract_address, functions.propose, validator
        )

        self.quorum = QuorumMethod(
            web3_or_provider, contract_address, functions.quorum, validator
        )

        self.quorum_denominator = QuorumDenominatorMethod(
            web3_or_provider, contract_address, functions.quorumDenominator
        )

        self.quorum_numerator2 = QuorumNumerator2Method(
            web3_or_provider,
            contract_address,
            functions.quorumNumerator,
            validator,
        )

        self.quorum_numerator1 = QuorumNumerator1Method(
            web3_or_provider, contract_address, functions.quorumNumerator
        )

        self.relay = RelayMethod(
            web3_or_provider, contract_address, functions.relay, validator
        )

        self.set_contract_uri = SetContractUriMethod(
            web3_or_provider,
            contract_address,
            functions.setContractURI,
            validator,
        )

        self.set_proposal_threshold = SetProposalThresholdMethod(
            web3_or_provider,
            contract_address,
            functions.setProposalThreshold,
            validator,
        )

        self.set_voting_delay = SetVotingDelayMethod(
            web3_or_provider,
            contract_address,
            functions.setVotingDelay,
            validator,
        )

        self.set_voting_period = SetVotingPeriodMethod(
            web3_or_provider,
            contract_address,
            functions.setVotingPeriod,
            validator,
        )

        self.state = StateMethod(
            web3_or_provider, contract_address, functions.state, validator
        )

        self.supports_interface = SupportsInterfaceMethod(
            web3_or_provider,
            contract_address,
            functions.supportsInterface,
            validator,
        )

        self.token = TokenMethod(
            web3_or_provider, contract_address, functions.token
        )

        self.update_quorum_numerator = UpdateQuorumNumeratorMethod(
            web3_or_provider,
            contract_address,
            functions.updateQuorumNumerator,
            validator,
        )

        self.version = VersionMethod(
            web3_or_provider, contract_address, functions.version
        )

        self.voting_delay = VotingDelayMethod(
            web3_or_provider, contract_address, functions.votingDelay
        )

        self.voting_period = VotingPeriodMethod(
            web3_or_provider, contract_address, functions.votingPeriod
        )

    def get_initialized_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Initialized event.

        :param tx_hash: hash of transaction emitting Initialized event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=VoteERC20.abi(),
            )
            .events.Initialized()
            .processReceipt(tx_receipt)
        )

    def get_proposal_canceled_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ProposalCanceled event.

        :param tx_hash: hash of transaction emitting ProposalCanceled event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=VoteERC20.abi(),
            )
            .events.ProposalCanceled()
            .processReceipt(tx_receipt)
        )

    def get_proposal_created_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ProposalCreated event.

        :param tx_hash: hash of transaction emitting ProposalCreated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=VoteERC20.abi(),
            )
            .events.ProposalCreated()
            .processReceipt(tx_receipt)
        )

    def get_proposal_executed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ProposalExecuted event.

        :param tx_hash: hash of transaction emitting ProposalExecuted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=VoteERC20.abi(),
            )
            .events.ProposalExecuted()
            .processReceipt(tx_receipt)
        )

    def get_proposal_threshold_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ProposalThresholdSet event.

        :param tx_hash: hash of transaction emitting ProposalThresholdSet event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=VoteERC20.abi(),
            )
            .events.ProposalThresholdSet()
            .processReceipt(tx_receipt)
        )

    def get_quorum_numerator_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for QuorumNumeratorUpdated event.

        :param tx_hash: hash of transaction emitting QuorumNumeratorUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=VoteERC20.abi(),
            )
            .events.QuorumNumeratorUpdated()
            .processReceipt(tx_receipt)
        )

    def get_vote_cast_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for VoteCast event.

        :param tx_hash: hash of transaction emitting VoteCast event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=VoteERC20.abi(),
            )
            .events.VoteCast()
            .processReceipt(tx_receipt)
        )

    def get_vote_cast_with_params_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for VoteCastWithParams event.

        :param tx_hash: hash of transaction emitting VoteCastWithParams event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=VoteERC20.abi(),
            )
            .events.VoteCastWithParams()
            .processReceipt(tx_receipt)
        )

    def get_voting_delay_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for VotingDelaySet event.

        :param tx_hash: hash of transaction emitting VotingDelaySet event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=VoteERC20.abi(),
            )
            .events.VotingDelaySet()
            .processReceipt(tx_receipt)
        )

    def get_voting_period_set_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for VotingPeriodSet event.

        :param tx_hash: hash of transaction emitting VotingPeriodSet event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=VoteERC20.abi(),
            )
            .events.VotingPeriodSet()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"Empty","type":"error"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"proposalId","type":"uint256"}],"name":"ProposalCanceled","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"proposalId","type":"uint256"},{"indexed":false,"internalType":"address","name":"proposer","type":"address"},{"indexed":false,"internalType":"address[]","name":"targets","type":"address[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"},{"indexed":false,"internalType":"string[]","name":"signatures","type":"string[]"},{"indexed":false,"internalType":"bytes[]","name":"calldatas","type":"bytes[]"},{"indexed":false,"internalType":"uint256","name":"startBlock","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"endBlock","type":"uint256"},{"indexed":false,"internalType":"string","name":"description","type":"string"}],"name":"ProposalCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"proposalId","type":"uint256"}],"name":"ProposalExecuted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldProposalThreshold","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newProposalThreshold","type":"uint256"}],"name":"ProposalThresholdSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldQuorumNumerator","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newQuorumNumerator","type":"uint256"}],"name":"QuorumNumeratorUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"voter","type":"address"},{"indexed":false,"internalType":"uint256","name":"proposalId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"support","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"weight","type":"uint256"},{"indexed":false,"internalType":"string","name":"reason","type":"string"}],"name":"VoteCast","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"voter","type":"address"},{"indexed":false,"internalType":"uint256","name":"proposalId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"support","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"weight","type":"uint256"},{"indexed":false,"internalType":"string","name":"reason","type":"string"},{"indexed":false,"internalType":"bytes","name":"params","type":"bytes"}],"name":"VoteCastWithParams","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldVotingDelay","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newVotingDelay","type":"uint256"}],"name":"VotingDelaySet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldVotingPeriod","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newVotingPeriod","type":"uint256"}],"name":"VotingPeriodSet","type":"event"},{"inputs":[],"name":"BALLOT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"COUNTING_MODE","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"EXTENDED_BALLOT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"},{"internalType":"uint8","name":"support","type":"uint8"}],"name":"castVote","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"},{"internalType":"uint8","name":"support","type":"uint8"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"castVoteBySig","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"},{"internalType":"uint8","name":"support","type":"uint8"},{"internalType":"string","name":"reason","type":"string"}],"name":"castVoteWithReason","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"},{"internalType":"uint8","name":"support","type":"uint8"},{"internalType":"string","name":"reason","type":"string"},{"internalType":"bytes","name":"params","type":"bytes"}],"name":"castVoteWithReasonAndParams","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"},{"internalType":"uint8","name":"support","type":"uint8"},{"internalType":"string","name":"reason","type":"string"},{"internalType":"bytes","name":"params","type":"bytes"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"castVoteWithReasonAndParamsBySig","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"contractType","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractVersion","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address[]","name":"targets","type":"address[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"},{"internalType":"bytes[]","name":"calldatas","type":"bytes[]"},{"internalType":"bytes32","name":"descriptionHash","type":"bytes32"}],"name":"execute","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getAllProposals","outputs":[{"components":[{"internalType":"uint256","name":"proposalId","type":"uint256"},{"internalType":"address","name":"proposer","type":"address"},{"internalType":"address[]","name":"targets","type":"address[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"},{"internalType":"string[]","name":"signatures","type":"string[]"},{"internalType":"bytes[]","name":"calldatas","type":"bytes[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"endBlock","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"internalType":"struct VoteERC20.Proposal[]","name":"allProposals","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes","name":"params","type":"bytes"}],"name":"getVotesWithParams","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"},{"internalType":"address","name":"account","type":"address"}],"name":"hasVoted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"targets","type":"address[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"},{"internalType":"bytes[]","name":"calldatas","type":"bytes[]"},{"internalType":"bytes32","name":"descriptionHash","type":"bytes32"}],"name":"hashProposal","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_contractURI","type":"string"},{"internalType":"address[]","name":"_trustedForwarders","type":"address[]"},{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_initialVotingDelay","type":"uint256"},{"internalType":"uint256","name":"_initialVotingPeriod","type":"uint256"},{"internalType":"uint256","name":"_initialProposalThreshold","type":"uint256"},{"internalType":"uint256","name":"_initialVoteQuorumFraction","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256[]","name":"index_2","type":"uint256[]"},{"internalType":"uint256[]","name":"index_3","type":"uint256[]"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155BatchReceived","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"uint256","name":"index_3","type":"uint256"},{"internalType":"bytes","name":"index_4","type":"bytes"}],"name":"onERC1155Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"},{"internalType":"uint256","name":"index_2","type":"uint256"},{"internalType":"bytes","name":"index_3","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"}],"name":"proposalDeadline","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proposalIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"}],"name":"proposalSnapshot","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proposalThreshold","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"}],"name":"proposalVotes","outputs":[{"internalType":"uint256","name":"againstVotes","type":"uint256"},{"internalType":"uint256","name":"forVotes","type":"uint256"},{"internalType":"uint256","name":"abstainVotes","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index_0","type":"uint256"}],"name":"proposals","outputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"},{"internalType":"address","name":"proposer","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"endBlock","type":"uint256"},{"internalType":"string","name":"description","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"targets","type":"address[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"},{"internalType":"bytes[]","name":"calldatas","type":"bytes[]"},{"internalType":"string","name":"description","type":"string"}],"name":"propose","outputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"quorum","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"quorumDenominator","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"quorumNumerator","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"quorumNumerator","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"relay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"uri","type":"string"}],"name":"setContractURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newProposalThreshold","type":"uint256"}],"name":"setProposalThreshold","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newVotingDelay","type":"uint256"}],"name":"setVotingDelay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newVotingPeriod","type":"uint256"}],"name":"setVotingPeriod","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposalId","type":"uint256"}],"name":"state","outputs":[{"internalType":"enum IGovernorUpgradeable.ProposalState","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token","outputs":[{"internalType":"contract IVotesUpgradeable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"newQuorumNumerator","type":"uint256"}],"name":"updateQuorumNumerator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"votingDelay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"votingPeriod","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
