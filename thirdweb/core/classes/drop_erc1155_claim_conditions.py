from typing import Any, Dict, List, Optional, cast
from thirdweb.abi.drop_erc1155 import DropERC1155
from thirdweb.abi.drop_erc721 import DropERC721
from thirdweb.abi.ierc20 import IERC20
from thirdweb.common.claim_conditions import (
    get_claimer_proofs,
    process_claim_condition_inputs,
    transform_result_to_claim_condition,
)
from thirdweb.common.currency import is_native_token, parse_units
from thirdweb.common.error import includes_error_message
from thirdweb.constants.addresses import DEFAULT_MERKLE_ROOT
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contracts.claim_conditions import (
    ClaimCondition,
)
from thirdweb.types.currency import Amount
from thirdweb.types.settings.metadata import EditionDropContractMetadata
from web3.eth import TxReceipt
from web3.constants import MAX_INT
from time import time


class DropERC1155ClaimConditions:
    _contract_wrapper: ContractWrapper[DropERC1155]
    _metadata: ContractMetadata[DropERC1155, EditionDropContractMetadata]
    _storage: IpfsStorage

    def __init__(
        self,
        contract_wrapper: ContractWrapper[DropERC1155],
        metadata: ContractMetadata[DropERC1155, EditionDropContractMetadata],
        storage: IpfsStorage,
    ):
        self._contract_wrapper = contract_wrapper
        self._metadata = metadata
        self._storage = storage

    """
    READ FUNCTIONS
    """

    def get_active(self, token_id: int) -> ClaimCondition:
        """
        Get the currently active claim condition

        :param token_id: token ID of the token to get the active claim condition for.
        :return: The currently active claim condition
        """

        id = self._contract_wrapper._contract_abi.get_active_claim_condition_id.call(
            token_id
        )
        mc = self._contract_wrapper._contract_abi.get_claim_condition_by_id.call(
            token_id, id
        )
        metadata = self._metadata.get()
        return transform_result_to_claim_condition(
            mc,
            self._contract_wrapper.get_provider(),
            metadata.merkle,
            self._storage,
        )

    def get_all(self, token_id: int) -> List[ClaimCondition]:
        """
        Get all claim conditions on this contract

        :param token_id: token ID of the token to get all claim conditions for.
        :return: A list of all claim conditions on this contract
        """

        # Is this the correct order?
        start_id, count = self._contract_wrapper._contract_abi.claim_condition.call(
            token_id
        )
        conditions = []
        for i in range(start_id + count):
            conditions.append(
                self._contract_wrapper._contract_abi.get_claim_condition_by_id.call(
                    token_id, i
                )
            )
        metadata = self._metadata.get()
        return [
            transform_result_to_claim_condition(
                c, self._contract_wrapper.get_provider(), metadata.merkle, self._storage
            )
            for c in conditions
        ]
