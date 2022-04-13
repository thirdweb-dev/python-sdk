from typing import List
from web3 import Web3
from thirdweb.common.error import DuplicateLeafsException
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contracts.claim_conditions import (
    SnapshotAddressInput,
    SnapshotInfo,
    SnapshotInput,
    SnapshotProof,
    SnapshotSchema,
)
from thirdweb.common.currency import parse_units
from pymerkle import MerkleTree


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

    # Need to use keccak256 encoding
    tree = MerkleTree(*hashed_leafs, hash_type="sha3_256")

    claims = []
    for index, item in enumerate(input):
        proof = tree.merkleProof({"checksum": hashed_leafs[index]})

        # What do I need here from the proof
        claims.append(
            SnapshotProof(
                address=item.address,
                max_claimable=item.max_claimable,
                proof=proof.serialize()["commitment"],
            )
        )

    snapshot = SnapshotSchema(merkle_root=tree.rootHash, claims=claims)
    uri = storage.upload_metadata(snapshot)

    return SnapshotInfo(merkle_root=tree.rootHash, snapshot_uri=uri, snapshot=snapshot)


def hash_leaf_node(address: str, max_claimable_amount: int) -> str:
    return Web3.solidityKeccak(["address", "uint256"], [address, max_claimable_amount])
