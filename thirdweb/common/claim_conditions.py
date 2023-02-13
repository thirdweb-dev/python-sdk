from typing import Dict, Optional, cast

from web3 import Web3
from web3.constants import MAX_INT
from thirdweb.abi.drop_erc721 import IClaimConditionClaimCondition
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.common.currency import (
    approve_erc20_allowance,
    convert_quantity_to_number,
    fetch_currency_value,
    is_native_token,
    normalize_price_value
)
from thirdweb.core.classes.sharded_merkle_tree import ShardedMerkleTree

from thirdweb.types.contracts.claim_conditions import (
    ClaimCondition,
    ClaimConditionOutput,
    ClaimVerification,
    SnapshotEntryWithProof,
    ShardedMerkleTreeInfo
)


def prepare_claim(
    address_to_claim: str,
    quantity: int,
    active_claim_condition: ClaimCondition,
    merkle_metadata: Dict[str, str],
    contract_wrapper: ContractWrapper,
    storage: IpfsStorage,
) -> ClaimVerification:
    max_claimable = active_claim_condition.max_claimable_per_wallet
    proofs = []
    price_in_proof = active_claim_condition.price
    currency_address_in_proof = active_claim_condition.currency_address
    value = 0

    max_int = int(MAX_INT, 0)

    if not active_claim_condition.merkle_root_hash.startswith(ZERO_ADDRESS):
        snapshot_entry = fetch_snapshot_entry_for_address(
            address_to_claim,
            active_claim_condition.merkle_root_hash, 
            merkle_metadata, 
            contract_wrapper.get_provider(),
            storage
        )

        if snapshot_entry is not None:
            proofs = snapshot_entry.proof
            max_claimable = convert_quantity_to_number(snapshot_entry.max_claimable, 0)

            if snapshot_entry.price == "unlimited" or snapshot_entry.price == "":
                price_in_proof = max_int
            else:
                price_in_proof = normalize_price_value(
                    contract_wrapper.get_provider(), 
                    float(snapshot_entry.price), 
                    snapshot_entry.currency_address
                )
        
            if snapshot_entry.currency_address == "":
                currency_address_in_proof = ZERO_ADDRESS
            else:
                currency_address_in_proof = snapshot_entry.currency_address

    price_per_token = price_in_proof
    if price_in_proof == max_int:
        price_per_token = active_claim_condition.price

    currency_address = active_claim_condition.currency_address
    if currency_address_in_proof != ZERO_ADDRESS:
        currency_address = currency_address_in_proof

    value = 0
    if price_per_token > 0:
        if is_native_token(currency_address):
            value = quantity * price_per_token
        else:
            approve_erc20_allowance(
                contract_wrapper, 
                currency_address, 
                price_per_token,
                quantity
            )

    return ClaimVerification(
        value=value,
        proofs=proofs,
        max_claimable=max_claimable,
        price=price_per_token,
        currency_address=currency_address,
        price_in_proof=price_in_proof,
        currency_address_in_proof=currency_address_in_proof,

    )


def fetch_snapshot_entry_for_address(
    address_to_claim: str,
    merkle_root_hash: str,
    merkle_metadata: Optional[Dict[str, str]],
    provider: Web3,
    storage: IpfsStorage,
) -> Optional[SnapshotEntryWithProof]:
    if merkle_metadata is None:
        return None
        
    merkle_root = merkle_root_hash

    snapshot_uri = merkle_metadata[merkle_root_hash]
    if snapshot_uri:
        raw = storage.get(snapshot_uri)
        metadata = ShardedMerkleTreeInfo.from_json(raw)
       
        if metadata.merkle_root == merkle_root:
            merkle_tree = ShardedMerkleTree.from_info(
                metadata,
                storage
            )
            return merkle_tree.get_proof(address_to_claim, provider)

    return None

def transform_result_to_claim_condition(
    pm: IClaimConditionClaimCondition,
    provider: Web3,
    merkle_metadata: Dict[str, str],
    storage: IpfsStorage,
) -> ClaimCondition:
    cv = fetch_currency_value(provider, pm["currency"], pm["pricePerToken"])
    return ClaimConditionOutput(
        start_time=pm["startTimestamp"],
        max_claimable_supply=pm["maxClaimableSupply"],
        max_claimable_per_wallet=pm["quantityLimitPerWallet"],
        currency_mint_supply=pm["supplyClaimed"],
        available_supply=pm["maxClaimableSupply"] - pm["supplyClaimed"],
        wait_in_seconds=0,
        price=pm["pricePerToken"],
        currency_address=pm["currency"],
        currency_metadata=cv,
        merkle_root_hash="0x" + cast(bytes, pm["merkleRoot"]).hex()
    )
