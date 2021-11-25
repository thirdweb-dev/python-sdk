"""
Types for Pack module.
"""

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
    """CreatePackArg assembles the parameters used to create a new Pack

    Args:
        asset_contract_address: The address of the asset being put in the pack
        metadata: The metadata of the pack (name, description, image, etc)
        assets: The list of assets (pair of [id, amount]) to list in in the pack
        rewards_per_open: The number of tokens that will be awarded when opening the pack
        seconds_until_open_start: The number of seconds the pack is allowed to be opened
    """
    asset_contract_address: str
    metadata: Union[str, dict]
    assets: List[AssetAmountPair]
    rewards_per_open: int = 1
    seconds_until_open_start: int = 0
