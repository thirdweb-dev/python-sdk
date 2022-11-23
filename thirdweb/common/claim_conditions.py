from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from web3 import Web3
from thirdweb.abi.drop_erc721 import IDropClaimCondition_V2ClaimCondition
from thirdweb.constants.addresses import DEFAULT_MERKLE_ROOT
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.common.currency import (
    approve_erc20_allowance,
    fetch_currency_value,
    is_native_token,
    parse_units,
)

from thirdweb.types.contracts.claim_conditions import (
    ClaimCondition,
    ClaimConditionOutput,
    ClaimVerification,
    Snapshot,
    SnapshotProof,
)


def prepare_claim(
    quantity: int,
    active_claim_condition: ClaimCondition,
    merkle_metadata: Dict[str, str],
    contract_wrapper: ContractWrapper,
    storage: IpfsStorage,
    proofs: List[str] = [DEFAULT_MERKLE_ROOT],
) -> ClaimVerification:
    address_to_claim = contract_wrapper.get_signer_address()
    token_decimals = 0

    max_claimable = 0

    try:
        if not active_claim_condition.merkle_root_hash.startswith(ZERO_ADDRESS):
            claims = fetch_snapshot(
                active_claim_condition.merkle_root_hash, merkle_metadata, storage
            )
            item = (
                next((c for c in claims if c.address == address_to_claim), None)
                if claims is not None
                else None
            )
            if item is None:
                raise Exception("No claim found for this address")
            proofs = item.proof
            max_claimable = parse_units(item.max_claimable, token_decimals)
    except Exception as e:
        if str(e) == "No claim found for this address":
            raise e

        print(
            "Failed to check claim condition merkle root hash, continuing anyway: ",
            str(e),
        )

    # TODO: OVERRIDES
    overrides: Dict[str, Any] = {}
    price = active_claim_condition.price
    currency_address = active_claim_condition.currency_address

    if price > 0:
        if is_native_token(currency_address):
            # overrides["value"] = quantity * price
            pass
        else:
            approve_erc20_allowance(contract_wrapper, currency_address, price, quantity)

    return ClaimVerification(
        proofs=proofs,
        max_quantity_per_transaction=max_claimable,
        price=price,
        currency_address=currency_address,
    )


def fetch_snapshot(
    merkle_root: str,
    merkle_metadata: Dict[str, str],
    storage: IpfsStorage,
) -> Optional[List[SnapshotProof]]:
    snapshot = None
    if not merkle_root in merkle_metadata:
        return snapshot

    snapshot_uri = merkle_metadata[merkle_root]
    if snapshot_uri:
        raw = storage.get(snapshot_uri)
        snapshot_data: Snapshot = Snapshot.from_json(raw)
        if merkle_root.lower() == snapshot_data.merkle_root.lower():
            snapshot = snapshot_data.claims

    return snapshot


@dataclass
class ClaimerProof:
    max_claimable: int
    proof: List[str]


def get_claimer_proofs(
    address_to_claim: str,
    merkle_root: str,
    token_decimals: int,
    merkle_metadata: Dict[str, str],
    storage: IpfsStorage,
) -> ClaimerProof:
    claims = fetch_snapshot(merkle_root, merkle_metadata, storage)

    if claims is None:
        return ClaimerProof(max_claimable=0, proof=[])
    item = next((c for c in claims if c.address == address_to_claim), None)

    if item is None:
        return ClaimerProof(proof=[], max_claimable=0)

    return ClaimerProof(
        proof=item.proof, max_claimable=parse_units(item.max_claimable, token_decimals)
    )




def transform_result_to_claim_condition(
    pm: IDropClaimCondition_V2ClaimCondition,
    provider: Web3,
    merkle_metadata: Dict[str, str],
    storage: IpfsStorage,
) -> ClaimCondition:
    cv = fetch_currency_value(provider, pm["currency"], pm["pricePerToken"])
    claims = fetch_snapshot(str(pm["merkleRoot"]), merkle_metadata, storage)
    return ClaimConditionOutput(
        start_time=pm["startTimestamp"],
        max_quantity=pm["maxClaimableSupply"],
        available_supply=pm["maxClaimableSupply"] - pm["supplyClaimed"],
        quantity_limit_per_tranaction=pm["quantityLimitPerTransaction"],
        wait_in_seconds=pm["waitTimeInSecondsBetweenClaims"],
        price=pm["pricePerToken"],
        currency_address=pm["currency"],
        currency_metadata=cv,
        merkle_root_hash=pm["merkleRoot"],
        snapshot=claims,
    )
