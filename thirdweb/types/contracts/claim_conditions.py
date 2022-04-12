from dataclasses import dataclass, field
from time import time
from typing import List
from thirdweb.constants.currency import NATIVE_TOKEN_ADDRESS
from thirdweb.types.currency import Amount, CurrencyValue, Price
from web3.constants import MAX_INT
from enum import Enum


@dataclass
class SnapshotInput:
    address: str
    max_claimable: int


@dataclass
class SnapshotProof(SnapshotInput):
    proof: str
    timestamp: int = int(time())


@dataclass
class Snapshot:
    merkle_root: str
    claims: List[SnapshotProof]


@dataclass
class ClaimConditionInput:
    start_time: int
    quantity_limit_per_transaction: int
    max_quantity: Amount = int(MAX_INT, 0)
    wait_in_seconds: int = int(MAX_INT, 0)
    currency_address: str = NATIVE_TOKEN_ADDRESS
    price: Price = 0
    merkle_root_hash: str = (
        "0x0000000000000000000000000000000000000000000000000000000000000000"
    )
    snapshot: List[SnapshotInput] = field(default_factory=lambda: [])


ClaimConditionInputList = List[ClaimConditionInput]


@dataclass
class ClaimConditionOutput:
    price: int
    max_quantity: int
    quantity_limit_per_tranaction: int
    wait_in_seconds: int
    start_time: int = int(time())
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


ClaimCondition = ClaimConditionOutput


@dataclass
class ClaimVerification:
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
    NO_ACTIVE_CLAIM_CONDITION_SET = ("There is no claim condition set.",)
    UNKNOWN = ("No claim conditions found.",)