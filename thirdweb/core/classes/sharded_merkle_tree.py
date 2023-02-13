from typing import List, Optional, Dict
from web3 import Web3
from thirdweb.common.currency import fetch_currency_metadata, convert_quantity_to_number
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contracts.claim_conditions import ShardData, ShardedMerkleTreeInfo, SnapshotEntry, SnapshotEntryWithProof
from thirdweb.common.merkle_tree import MerkleTree

class ShardedMerkleTree:
    storage: IpfsStorage
    base_uri: str
    original_entries_uri: str
    shard_nybbles: int 
    token_decimals: int
    shards: Dict[str, ShardData]
    trees: Dict[str, MerkleTree]

    def __init__(
        self,
        storage: IpfsStorage,
        base_uri: str,
        original_entries_uri: str,
        shard_nybbles: int,
        token_decimals: int
    ):
        self.storage = storage
        self.base_uri = base_uri
        self.original_entries_uri = original_entries_uri
        self.shard_nybbles = shard_nybbles
        self.token_decimals = token_decimals
        self.shards = {}
        self.trees = {}
    
    @staticmethod
    def from_info(metadata: ShardedMerkleTreeInfo, storage: IpfsStorage) -> "ShardedMerkleTree":
        return ShardedMerkleTree(
            storage,
            metadata.base_uri,
            metadata.original_entries_uri,
            metadata.shard_nybbles,
            metadata.token_decimals
        )
    
    def fetch_and_cache_decimals(self, cache: Dict[str, int], provider: Web3, currency_address: str) -> int:
        if not currency_address:
            return 18
        
        if currency_address not in cache:
            currency_metadata = fetch_currency_metadata(provider, currency_address)
            decimals = currency_metadata.decimals
            cache[currency_address] = decimals
            return decimals
        
        return cache[currency_address]

    def hash_entry(self, entry: SnapshotEntry, token_decimals: int, currency_decimals: int) -> str:
        max_claimable = convert_quantity_to_number(entry.max_claimable, token_decimals)
        entry_price = entry.price

        if entry_price == "":
            entry_price = "unlimited"

        price = convert_quantity_to_number(entry_price, currency_decimals)

        currency_address = entry.currency_address
        if currency_address == "":
            currency_address = ZERO_ADDRESS
        
        hash: bytes = Web3.solidityKeccak(
            ["address", "uint256", "uint256", "address"], 
            [entry.address, max_claimable, price, currency_address]
        )

        return hash.hex()[2:]

    def get_proof(self, address: str, provider: Web3) -> Optional[SnapshotEntryWithProof]:
        shard_id = address[2:self.shard_nybbles+2]
        shard: ShardData = self.shards.get(shard_id)
        
        currency_decimal_map: Dict[str, int] = {}

        if shard is None:
            uri = self.base_uri + "/" + shard_id + ".json"

            raw = {}
            try:
                raw = self.storage.get(uri)
            except:
                return None

            shard_data: ShardData = ShardData.from_json(raw)
            self.shards[shard_id] = shard_data
            shard = self.shards[shard_id]

            hashed_entries: List[str] = []
            for e in shard.entries:
                currency_decimals = self.fetch_and_cache_decimals(currency_decimal_map, provider, e.currency_address)
                hash = self.hash_entry(e, self.token_decimals, currency_decimals)
                hashed_entries.append(hash)

            tree = MerkleTree()
            for leaf in hashed_entries:
                tree.add_leaf(leaf)

            tree.make_tree()
            self.trees[shard_id] = tree

        entry: Optional[SnapshotEntry] = None
        for e in shard.entries:
            if e.address.lower() == address.lower():
                entry = e
                break

        if entry is None:
            return None

        currency_decimals = self.fetch_and_cache_decimals(
            currency_decimal_map,
            provider,
            entry.currency_address
        )

        leaf = self.hash_entry(entry, self.token_decimals, currency_decimals)

        proof: List[str] = []
        current_tree = self.trees.get(shard_id)
        if current_tree is not None:
            merkle_proof = current_tree.get_proof(leaf)

            if merkle_proof is not None:
                proof = [p.get("left", p.get("right")) for p in merkle_proof]

        proof += shard.proofs

        return SnapshotEntryWithProof(
            address=entry.address,
            max_claimable=entry.max_claimable,
            price=entry.price,
            currency_address=entry.currency_address,
            proof=proof
        )