import dataclasses


@dataclasses.dataclass
class SdkOptions:
    ipfs_gateway_url: str = "https://cloudflare-ipfs.com/ipfs/"
    registry_contract_address: str = ""
    max_gas_price_in_gwei: int = 100
    gas_speed: str = "fastest"
    private_key: str = ""
    tx_timeout_in_seconds: int = 30
