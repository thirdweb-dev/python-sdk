from typing import Optional
from web3 import Web3


DEFAULT_IPFS_GATEWAY = "https://ipfs.io/ipfs/"

TW_IPFS_SERVER_URL = "https://upload.nftlabs.co"

TW_STORAGE_SERVER_URL = "https://storage.thirdweb.com"

DEFAULT_API_KEY = "39a3c037d7a88e6692c6681bccfd1f1cf36370324c4051a83acd0edcffb20708"

def get_rpc_url(network: str, client_id: Optional[str]) -> str:
  api_key = client_id if client_id is not None else DEFAULT_API_KEY
  return f"https://{network}.rpc.thirdweb.com/{api_key}"

def get_provider_for_network(network: str, client_id: str) -> Web3:
    """
    Returns a web3 provider instance for the given network.
    """

    rpc_url = ""
    if network == "mainnet" or network == "ethereum":
        rpc_url = get_rpc_url("ethereum", client_id)
    elif network == "goerli":
        rpc_url = get_rpc_url("goerli", client_id)
    elif network == "polygon":
        rpc_url = get_rpc_url("polygon", client_id)
    elif network == "mumbai":
        rpc_url = get_rpc_url("mumbai", client_id)
    elif network == "optimism":
      rpc_url = get_rpc_url("optimism", client_id)
    elif network == "optimism-goerli":
      rpc_url = get_rpc_url("optimism-goerli", client_id)
    elif network == "arbitrum":
      rpc_url = get_rpc_url("arbitrum", client_id)
    elif network == "arbitrum-goerli":
      rpc_url = get_rpc_url("arbitrum-goerli", client_id)
    elif network == "fantom":
        rpc_url = get_rpc_url("fantom", client_id)
    elif network == "avalanche":
        rpc_url = get_rpc_url("avalanche", client_id)
    else:
        if network.startswith("http"):
            rpc_url = network
        else:
            raise Exception(f"Unrecognized chain name or RPC url {network}")

    return Web3(Web3.HTTPProvider(rpc_url))
