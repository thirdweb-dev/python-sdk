from enum import Enum
from typing import Optional
from dataclasses import dataclass

from thirdweb.constants.chains import ChainId


class GasSpeed(Enum):
    STANDARD = "standard"
    FAST = "fast"
    FASTEST = "fastest"


@dataclass
class GasSettings(object):
    max_price_in_gwei: int = 300
    speed: GasSpeed = GasSpeed.FASTEST


@dataclass
class ReadOnlySettings(object):
    rpc_url: str = ""
    chain_id: Optional[ChainId] = None


@dataclass
class SDKOptions(object):
    read_only_settings: Optional[ReadOnlySettings] = None
    gas_settings: GasSettings = GasSettings()
