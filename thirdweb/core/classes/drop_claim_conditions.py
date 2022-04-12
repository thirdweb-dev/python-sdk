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
        """
        Get the currently active claim condition

        :return: The currently active claim condition
        """
        pass

    def get_all(self) -> List[ClaimCondition]:
        """
        Get all claim conditions on this contract

        :return: A list of all claim conditions on this contract
        """
        pass

    def can_claim(self, quantity: Amount, address_to_check: str) -> bool:
        """
        Check if a specified wallet can claim a specified quantity of NFTs

        :param quantity: The quantity of NFTs to check
        :param address_to_check: The wallet to check
        :return: True if the wallet can claim the quantity of NFTs, False otherwise
        """
        pass

    def get_claim_ineligibility_reasons(
        self, quantity: Amount, address_to_check: str
    ) -> List[ClaimEligibility]:
        """
        Get the reasons why a wallet cannot claim a specified quantity of NFTs

        :param quantity: The quantity of NFTs to check
        :param address_to_check: The wallet to check
        :return: A list of reasons why the wallet cannot claim the quantity of NFTs
        """
        pass

    """
    WRITE FUNCTIONS
    """

    def set(
        self,
        claim_condition_inputs: List[ClaimConditionInput],
        reset_claim_eligibility_for_all=False,
    ) -> TxReceipt:
        """
        Set the claim conditions for this contract

        :param claim_condition_inputs: List of claim condition inputs
        :param reset_claim_eligibility_for_all: Reset claim eligibility for all wallets
        :return: transaction receipt of the set
        """
        pass

    def update(
        self, index: int, claim_condition_input: ClaimConditionInput
    ) -> TxReceipt:
        """
        Update the claim conditions for this contract

        :param index: Index of the claim condition to update
        :param claim_condition_input: Claim condition input
        :return: transaction receipt of the update
        """
        pass

    """
    INTERNAL FUNCTIONS
    """

    def _get_token_decimals(self) -> int:
        pass
