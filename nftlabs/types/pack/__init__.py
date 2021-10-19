from dataclasses import dataclass
from datetime import datetime
from ..nft import NftMetadata
from typing import Union, List


@dataclass
class PackMetadata:
    id: int
    creator_address: str
    current_supply: int
    open_start: datetime
    metadata: NftMetadata


@dataclass
class PackNftMetadata:
    supply: int
    metadata: NftMetadata


@dataclass
class AssetAmountPair:
    token_id: int
    amount: int


@dataclass
class CreatePackArg:
    asset_contract_address: str
    metadata: Union[str, dict]
    assets: List[AssetAmountPair]
    seconds_until_open_start: int
    seconds_until_open_end: int
    rewards_per_open: int
