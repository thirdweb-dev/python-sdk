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
    """
    The gas settings for the SDK.

    :param max_price_in_gwei: maximum gas price in gwei, defaults to 300
    :param speed: gas speed to use, defaults to "fastest"
    """

    max_price_in_gwei: int = 300
    speed: GasSpeed = GasSpeed.FASTEST


@dataclass
class ReadOnlySettings(object):
    """
    The read-only RPC settings for the SDK.

    :param rpc_url: URL of the RPC
    :param chain_id: optional chain ID to use for the RPC
    """

    rpc_url: str = ""
    chain_id: Optional[ChainId] = None


@dataclass
class SDKOptions(object):
    """
    Optional settings to configure the SDK

    :param read_only_settings: optional read-only RPC settings
    :param gas_settings: gas settings
    """

    read_only_settings: Optional[ReadOnlySettings] = None
    gas_settings: GasSettings = GasSettings()
