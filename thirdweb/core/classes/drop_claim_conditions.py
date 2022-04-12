from typing import List
from thirdweb.abi.drop_erc721 import DropERC721
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contracts.claim_conditions import (
    ClaimCondition,
    ClaimConditionInput,
    ClaimEligibility,
)
from thirdweb.types.currency import Amount
from thirdweb.types.settings.metadata import DropContractMetadata
from web3.eth import TxReceipt


class DropClaimConditions:
    _contract_wrapper: ContractWrapper[DropERC721]
    _metadata: ContractMetadata[DropERC721, DropContractMetadata]
    _storage: IpfsStorage

    def __init__(
        self,
        contract_wrapper: ContractWrapper[DropERC721],
        metadata: ContractMetadata[DropERC721, DropContractMetadata],
        storage: IpfsStorage,
    ):
        self._contract_wrapper = contract_wrapper
        self._metadata = metadata
        self._storage = storage

    """
    READ FUNCTIONS
    """

    def get_active(self) -> ClaimCondition:
        pass

    def get_all(self) -> List[ClaimCondition]:
        pass

    def can_claim(self, quantity: Amount, address_to_check: str) -> bool:
        pass

    def get_claim_ineligibility_reasons(
        self, quantity: Amount, address_to_check: str
    ) -> List[ClaimEligibility]:
        pass

    """
    WRITE FUNCTIONS
    """

    def set(
        self,
        claim_condition_inputs: List[ClaimConditionInput],
        reset_claim_eligibility_for_all=False,
    ) -> TxReceipt:
        pass

    def update(
        self, index: int, claim_condition_input: ClaimConditionInput
    ) -> TxReceipt:
        pass

    """
    INTERNAL FUNCTIONS
    """

    def _get_token_decimals(self) -> int:
        pass
