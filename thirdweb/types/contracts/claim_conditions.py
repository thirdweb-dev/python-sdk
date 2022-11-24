from dataclasses import dataclass, field
from time import time
from typing import Any, Dict, List
from thirdweb.constants.addresses import DEFAULT_MERKLE_ROOT
from thirdweb.constants.currency import NATIVE_TOKEN_ADDRESS
from thirdweb.types.currency import CurrencyValue
from web3.constants import ADDRESS_ZERO
from enum import Enum

@dataclass
class SnapshotEntry:
    address: str
    max_claimable: str
    price: str
    currency_address: str = ADDRESS_ZERO

@dataclass
class SnapshotEntryWithProof:
    address: str
    max_claimable: str
    price: str
    proof: List[str]
    currency_address: str = ADDRESS_ZERO

@dataclass
class ShardData:
    proofs: List[str]
    entries: List[SnapshotEntry]

    @staticmethod
    def from_json(json: Dict[str, Any]) -> "ShardData":
        entries = [
            SnapshotEntry(
                entry.get("address", ""),
                entry.get("maxClaimable", ""),
                entry.get("price", ""),
                entry.get("currencyAddress", ""),
            ) 
            for entry in json["entries"]
        ]
        return ShardData(
            json["proofs"],
            entries
        )

@dataclass
class ShardedMerkleTreeInfo:
    merkle_root: str
    base_uri: str
    original_entries_uri: str 
    shard_nybbles: int 
    token_decimals: int

    @staticmethod
    def from_json(json: Dict[str, Any]) -> "ShardedMerkleTreeInfo":
        return ShardedMerkleTreeInfo(
            json["merkleRoot"],
            json["baseUri"],
            json["originalEntriesUri"],
            json["shardNybbles"],
            json["tokenDecimals"],
        )


@dataclass
class ClaimConditionOutput:
    price: int
    max_claimable_supply: int
    max_claimable_per_wallet: int
    currency_mint_supply: int
    wait_in_seconds: int
    available_supply: int
    start_time: int = int(time()) - 1
    currency_metadata: CurrencyValue = field(
        default_factory=lambda: CurrencyValue(
            value=0,
            display_value=0,
            symbol="",
            decimals=18,
            name="",
        )
    )
    currency_address: str = NATIVE_TOKEN_ADDRESS
    merkle_root_hash: str = DEFAULT_MERKLE_ROOT


ClaimCondition = ClaimConditionOutput


@dataclass
class ClaimVerification:
    value: int
    proofs: List[str]
    max_claimable: int
    price: int
    currency_address: str
    price_in_proof: int
    currency_address_in_proof: str


class ClaimEligibility(Enum):
    NOT_ENOUGH_SUPPLY = ("There is not enough supply to claim.",)
    ADDRESS_NOT_ALLOWED = ("This address is not on the allowlist.",)
    WAIT_BEFORE_NEXT_CLAIM_TRANSACTION = (
        "Not enough time since last claim transaction. Please wait.",
    )
    ALREADY_CLAIMED = ("You have already claimed the token.",)
    NOT_ENOUGH_TOKENS = (
        "There are not enough tokens in the wallet to pay for the claim.",
    )
    NO_ACTIVE_CLAIM_PHASE = (
        "There is no active claim phase at the moment. Please check back in later.",
    )
    NO_CLAIM_CONDITION_SET = ("There is no claim condition set.",)
    UNKNOWN = ("No claim conditions found.",)
