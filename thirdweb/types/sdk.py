from enum import Enum
from web3 import Web3
from dataclasses import dataclass

class GasSpeed(Enum):
    STANDARD = "standard"
    FAST = "fast"
    FASTEST = "fastest"

@dataclass
class GasSettings(object):
    max_price_in_gwei: int = 300
    speed: GasSpeed = GasSpeed.FASTEST

@dataclass
class SDKOptions(object):
    read_only_rpc_url: str = ""
    gas_settings: GasSettings = GasSettings()
