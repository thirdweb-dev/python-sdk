from typing import List
from thirdweb.abi.drop_erc1155 import DropERC1155
from thirdweb.common.claim_conditions import (
    transform_result_to_claim_condition,
)
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contracts.claim_conditions import (
    ClaimCondition,
)
from thirdweb.types.settings.metadata import EditionDropContractMetadata


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
