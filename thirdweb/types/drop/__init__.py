"""
Types for Drop module.
"""

from dataclasses import dataclass
from typing import Optional, Union
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Query:
    start: int = None
    count: int = None


@dataclass_json
@dataclass
class claim:
    start_timestamp: int
    max_mint_supply: int
    current_mint_supply: int
    quantity_limit_per_transaction: int
    wait_time_seconds_limit_per_transaction: int
    merkle_root: bytes
    price_per_token: int
    currency: str  # todo
