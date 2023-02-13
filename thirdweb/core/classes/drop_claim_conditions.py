from typing import List
from thirdweb.abi.drop_erc721 import DropERC721
from thirdweb.common.claim_conditions import (
    transform_result_to_claim_condition,
)
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contracts.claim_conditions import (
    ClaimCondition,
)
from thirdweb.types.settings.metadata import NFTDropContractMetadata


class DropClaimConditions:
    _contract_wrapper: ContractWrapper[DropERC721]
    _metadata: ContractMetadata[DropERC721, NFTDropContractMetadata]
    _storage: IpfsStorage

    def __init__(
        self,
        contract_wrapper: ContractWrapper[DropERC721],
        metadata: ContractMetadata[DropERC721, NFTDropContractMetadata],
        storage: IpfsStorage,
    ):
        self._contract_wrapper = contract_wrapper
        self._metadata = metadata
        self._storage = storage

    """
    READ FUNCTIONS
    """

    def get_active(self) -> ClaimCondition:
        """
        Get the currently active claim condition

        :return: The currently active claim condition
        """

        id = self._contract_wrapper._contract_abi.get_active_claim_condition_id.call()
        mc = self._contract_wrapper._contract_abi.get_claim_condition_by_id.call(id)
        metadata = self._metadata.get()
        return transform_result_to_claim_condition(
            mc,
            self._contract_wrapper.get_provider(),
            metadata.merkle,
            self._storage,
        )

    def get_all(self) -> List[ClaimCondition]:
        """
        Get all claim conditions on this contract

        :return: A list of all claim conditions on this contract
        """

        # Is this the correct order?
        start_id, count = self._contract_wrapper._contract_abi.claim_condition.call()
        conditions = []
        for i in range(start_id + count):
            conditions.append(
                self._contract_wrapper._contract_abi.get_claim_condition_by_id.call(i)
            )
        metadata = self._metadata.get()
        return [
            transform_result_to_claim_condition(
                c, self._contract_wrapper.get_provider(), metadata.merkle, self._storage
            )
            for c in conditions
        ]
