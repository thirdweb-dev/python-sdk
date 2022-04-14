from typing import Any, Dict, List, Optional, cast
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
    ClaimConditionInput,
    ClaimEligibility,
)
from thirdweb.types.currency import Amount
from thirdweb.types.settings.metadata import NFTDropContractMetadata
from web3.eth import TxReceipt
from web3.constants import MAX_INT
from time import time


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

    # def can_claim(self, quantity: int, address_to_check: Optional[str] = None) -> bool:
    #     """
    #     Check if a specified wallet can claim a specified quantity of NFTs

    #     :param quantity: The quantity of NFTs to check
    #     :param address_to_check: The wallet to check
    #     :return: True if the wallet can claim the quantity of NFTs, False otherwise
    #     """

    #     address_to_check = (
    #         address_to_check
    #         if address_to_check is not None
    #         else self._contract_wrapper.get_signer_address()
    #     )

    #     print(
    #         "REASONS: ",
    #         self.get_claim_ineligibility_reasons(quantity, address_to_check),
    #     )

    #     return (
    #         len(self.get_claim_ineligibility_reasons(quantity, address_to_check)) == 0
    #     )

    # def get_claim_ineligibility_reasons(
    #     self, quantity: int, address_to_check: Optional[str] = None
    # ) -> List[ClaimEligibility]:
    #     """
    #     Get the reasons why a wallet cannot claim a specified quantity of NFTs

    #     :param quantity: The quantity of NFTs to check
    #     :param address_to_check: The wallet to check
    #     :return: A list of reasons why the wallet cannot claim the quantity of NFTs
    #     """

    #     reasons: List[ClaimEligibility] = []
    #     quantity_with_decimals = parse_units(quantity, self._get_token_decimals())

    #     if address_to_check == None:
    #         address_to_check = self._contract_wrapper.get_signer_address()

    #     try:
    #         active_condition_index = (
    #             self._contract_wrapper._contract_abi.get_active_claim_condition_id.call()
    #         )
    #         claim_condition = self.get_active()
    #     except Exception as e:
    #         if includes_error_message(e, "no public mint condition."):
    #             reasons.append(ClaimEligibility.NO_CLAIM_CONDITION_SET)
    #             return reasons
    #         if includes_error_message(e, "no active mint condition."):
    #             reasons.append(ClaimEligibility.NO_ACTIVE_CLAIM_PHASE)
    #             return reasons
    #         reasons.append(ClaimEligibility.UNKNOWN)
    #         return reasons

    #     if claim_condition.available_supply < quantity_with_decimals:
    #         reasons.append(ClaimEligibility.NOT_ENOUGH_SUPPLY)

    #     if (
    #         claim_condition.merkle_root_hash != DEFAULT_MERKLE_ROOT
    #         and claim_condition.merkle_root_hash
    #         != b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    #     ):
    #         merkle_lower = claim_condition.merkle_root_hash
    #         metadata = self._metadata.get()
    #         proofs = get_claimer_proofs(
    #             cast(str, address_to_check),
    #             merkle_lower,
    #             self._get_token_decimals(),
    #             metadata.merkle,
    #             self._storage,
    #         )

    #         try:
    #             (
    #                 valid_merkle_proof,
    #             ) = self._contract_wrapper._contract_abi.verify_claim_merkle_proof.call(
    #                 active_condition_index,
    #                 cast(str, address_to_check),
    #                 quantity,
    #                 proofs.proof,  # type: ignore
    #                 proofs.max_claimable,
    #             )

    #             if not valid_merkle_proof:  # type: ignore
    #                 reasons.append(ClaimEligibility.ADDRESS_NOT_ALLOWED)
    #                 return reasons
    #         except:
    #             reasons.append(ClaimEligibility.ADDRESS_NOT_ALLOWED)
    #             return reasons

    #     (
    #         last_claimed_timestamp,
    #         timestamp_for_next_claim,
    #     ) = self._contract_wrapper._contract_abi.get_claim_timestamp.call(
    #         active_condition_index, cast(str, address_to_check)
    #     )

    #     now = int(time())

    #     if last_claimed_timestamp < 0 and now < timestamp_for_next_claim:
    #         if timestamp_for_next_claim == int(MAX_INT, 0):
    #             reasons.append(ClaimEligibility.ALREADY_CLAIMED)
    #         else:
    #             reasons.append(ClaimEligibility.WAIT_BEFORE_NEXT_CLAIM_TRANSACTION)

    #     if claim_condition.price > 0:
    #         total_price = claim_condition.price * quantity
    #         provider = self._contract_wrapper.get_provider()
    #         if is_native_token(claim_condition.currency_address):
    #             balance = int(provider.eth.get_balance(address_to_check))
    #             if balance < total_price:
    #                 reasons.append(ClaimEligibility.NOT_ENOUGH_TOKENS)
    #         else:
    #             abi = IERC20(provider, claim_condition.currency_address)
    #             erc20 = ContractWrapper[IERC20](
    #                 abi, provider, self._contract_wrapper.get_signer()
    #             )
    #             balance = erc20._contract_abi.balance_of.call(
    #                 cast(str, address_to_check)
    #             )
    #             if balance < total_price:
    #                 reasons.append(ClaimEligibility.NOT_ENOUGH_TOKENS)

    #     return reasons

    """
    WRITE FUNCTIONS
    """

    # def set(
    #     self,
    #     claim_condition_inputs: List[ClaimConditionInput],
    #     reset_claim_eligibility_for_all=False,
    # ) -> TxReceipt:
    #     """
    #     Set the claim conditions for this contract

    #     :param claim_condition_inputs: List of claim condition inputs
    #     :param reset_claim_eligibility_for_all: Reset claim eligibility for all wallets
    #     :return: transaction receipt of the set
    #     """

    #     snapshot_infos, sorted_conditions = process_claim_condition_inputs(
    #         claim_condition_inputs,
    #         self._get_token_decimals(),
    #         self._contract_wrapper.get_provider(),
    #         self._storage,
    #     )

    #     merkle_info: Dict[str, Any] = {}
    #     for s in snapshot_infos:
    #         merkle_info[s.merkle_root] = s.snapshot_uri

    #     metadata = self._metadata.get()
    #     encoded = []
    #     interface = self._contract_wrapper.get_contract_interface()

    #     if not metadata.merkle == merkle_info:
    #         metadata.merkle = merkle_info
    #         contract_uri = self._metadata._parse_and_upload_metadata(metadata.to_json())
    #         encoded.append(interface.encodeABI("setContractURI", [contract_uri]))

    #     print("CONDITIONS ", sorted_conditions)

    #     encoded.append(
    #         interface.encodeABI(
    #             "setClaimConditions",
    #             [sorted_conditions, reset_claim_eligibility_for_all],
    #         )
    #     )

    #     return self._contract_wrapper.multi_call(encoded)

    """
    INTERNAL FUNCTIONS
    """

    def _get_token_decimals(self) -> int:
        # TODO: Implement for TokenERC20
        return 0
