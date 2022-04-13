from typing import Any, Dict, List, Optional

from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.common.currency import (
    approve_erc20_allowance,
    is_native_token,
    parse_units,
)

from thirdweb.types.contracts.claim_conditions import (
    ClaimCondition,
    ClaimVerification,
    Snapshot,
    SnapshotProof,
)

DEFAULT_MERKLE_ROOT = (
    "0x0000000000000000000000000000000000000000000000000000000000000000"
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
    merkle_root: str, merkle_metadata: Dict[str, str], storage: IpfsStorage
) -> Optional[List[SnapshotProof]]:
    snapshot_uri = merkle_metadata[merkle_root]
    snapshot = None
    if snapshot_uri:
        raw = storage.get(snapshot_uri)
        snapshot_data: Snapshot = Snapshot.from_json(raw)
        if merkle_root.lower() == snapshot_data.merkle_root.lower():
            snapshot = snapshot_data.claims

    return snapshot
