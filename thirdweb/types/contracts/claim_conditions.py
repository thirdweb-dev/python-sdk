from dataclasses import dataclass, field
from time import time
from typing import Any, Dict, List, Union
from thirdweb.constants.addresses import DEFAULT_MERKLE_ROOT
from thirdweb.constants.currency import NATIVE_TOKEN_ADDRESS
from thirdweb.types.currency import Amount, CurrencyValue, Price
from web3.constants import MAX_INT
from enum import Enum


@dataclass
class SnapshotAddressInput:
    address: str
    max_claimable: int = 0


@dataclass
class SnapshotProof:
    proof: str
    address: str
    max_claimable: int = 0
    timestamp: int = int(time())


@dataclass
class Snapshot:
    merkle_root: str
    claims: List[SnapshotProof]

    @staticmethod
    def from_json(self, json: Dict[str, Any]) -> "Snapshot":
        return Snapshot(
            merkle_root=json["merkleRoot"],
            claims=[
                SnapshotProof(
                    address=proof["address"],
                    max_claimable=proof["maxClaimable"],
                    proof=proof["proof"],
                    timestamp=proof["timestamp"],
                )
                for proof in json["claims"]
            ],
        )


@dataclass
class SnapshotInfo:
    merkle_root: str
    snapshot_uri: str
    snapshot: Snapshot


SnapshotInputSchema = List[SnapshotAddressInput]
SnapshotInput = SnapshotInputSchema
SnapshotSchema = Snapshot


@dataclass
class ClaimConditionInput:
    start_time: int = int(time()) - 1
    quantity_limit_per_transaction: Amount = int(MAX_INT, 0)
    max_quantity: Amount = int(MAX_INT, 0)
    wait_in_seconds: int = 0
    currency_address: str = NATIVE_TOKEN_ADDRESS
    price: Price = 0
    merkle_root_hash: str = DEFAULT_MERKLE_ROOT
    snapshot: List[SnapshotAddressInput] = field(default_factory=lambda: [])

    def set_snapshot(self, addresses: List[str]) -> "ClaimConditionInput":
        self.snapshot = [SnapshotAddressInput(address=address) for address in addresses]
        return self


ClaimConditionInputList = List[ClaimConditionInput]
FilledConditionInput = ClaimConditionInput


@dataclass
class ClaimConditionOutput:
    price: int
    max_quantity: int
    quantity_limit_per_tranaction: int
    wait_in_seconds: int
    start_time: int = int(time()) - 1
    available_supply: str = ""
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
    snapshot: List[SnapshotInput] = field(default_factory=lambda: [])


ClaimCondition = ClaimConditionOutput


@dataclass
class ClaimVerification:
    # TODO: OVERRIDES
    proofs: List[str]
    max_quantity_per_transaction: int
    price: int
    currency_address: str


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
