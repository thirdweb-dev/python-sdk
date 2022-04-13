from thirdweb.common.error import DuplicateLeafsException
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contracts.claim_conditions import SnapshotInfo, SnapshotInput
from thirdweb.common.currency import parse_units


def create_snapshot(
    snapshot_input: SnapshotInput, token_decimals: int, storage: IpfsStorage
) -> SnapshotInfo:
    input = snapshot_input
    addresses = [i.address for i in input]
    has_duplicates = len(addresses) != len(set(addresses))
    if has_duplicates:
        raise DuplicateLeafsException()

    hashed_leafs = [
        hash_leaf_node(i.address, parse_units(i.max_claimable, token_decimals))
        for i in input
    ]

    # TODO: Implement merkle tree
    pass


def hash_leaf_node(address: str, max_claimable_amount: int) -> str:
    pass
