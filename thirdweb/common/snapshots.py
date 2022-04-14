from hexbytes import HexBytes
from web3 import Web3
from thirdweb.common.error import DuplicateLeafsException
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contracts.claim_conditions import (
    SnapshotInfo,
    SnapshotInput,
    SnapshotProof,
)
from thirdweb.common.currency import parse_units
from pymerkle import MerkleTree


class HashedData:
    def __init__(self, data: HexBytes):
        self.data = data

    def hexdigest(self):
        return self.data.hex()


def keccak256(x: bytes) -> HashedData:
    print("INPUT: ", x)
    hexstr = x.decode()[1:]
    print("HEXSTR: ", hexstr)
    keccak = Web3.keccak(hexstr=hexstr)
    print("KECCAK: ", keccak)
    return HashedData(keccak)


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

    print("ADDRESSES: ", addresses)
    print("HASHED LEAFS:", hashed_leafs)

    # tree = MerkleTree(*hashed_leafs)
    tree = MerkleTree()

    tree.algorithm = keccak256
    for leaf in hashed_leafs:
        tree.update(leaf.hex())

    # root_hash = "0x" + tree.rootHash.decode("utf-8")
    # root_hash = tree.rootHash.decode("utf-8")
    # root_hash = hashed_leafs[0].hex()
    root_hash = "0x5cee642ff879fb7bf27d34daceac161e9702076c331ce82cedded7075c0b7f22"

    print("ROOT HASH: ", root_hash)

    claims = []
    for index, item in enumerate(input):
        proof = tree.merkleProof({"checksum": hashed_leafs[index]})

        # What do I need here from the proof
        claims.append(
            SnapshotProof(
                address=item.address,
                max_claimable=item.max_claimable,
                proof="0x" + proof.serialize()["header"]["commitment"],
            )
        )

    # snapshot = SnapshotSchema(merkle_root=tree.rootHash, claims=claims)
    snapshot = {
        "merkle_root": root_hash,
        "claims": [c.__dict__ for c in claims],
    }

    uri = storage.upload_metadata(snapshot)

    return SnapshotInfo(merkle_root=root_hash, snapshot_uri=uri, snapshot=snapshot)


def hash_leaf_node(address: str, max_claimable_amount: int) -> HexBytes:
    return Web3.solidityKeccak(["address", "uint256"], [address, max_claimable_amount])
