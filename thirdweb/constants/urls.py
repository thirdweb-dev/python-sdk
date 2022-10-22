from web3 import Web3


DEFAULT_IPFS_GATEWAY = "https://gateway.ipfscdn.io/ipfs/"

TW_IPFS_SERVER_URL = "https://upload.nftlabs.co"

PINATA_IPFS_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"

DEFAULT_API_KEY = "39a3c037d7a88e6692c6681bccfd1f1cf36370324c4051a83acd0edcffb20708"

def get_rpc_url(network: str) -> str:
  return f"https://{network}.rpc.thirdweb.com/{DEFAULT_API_KEY}"

def get_provider_for_network(network: str) -> Web3:
    """
    Returns a web3 provider instance for the given network.
    """

    rpc_url = ""
    if network == "mainnet" or network == "ethereum":
        rpc_url = get_rpc_url("ethereum")
    elif network == "goerli":
        rpc_url = get_rpc_url("goerli")
    elif network == "polygon":
        rpc_url = get_rpc_url("polygon")
    elif network == "mumbai":
        rpc_url = get_rpc_url("mumbai")
    elif network == "optimism":
      rpc_url = getRpcUrl("optimism");
    elif network == "optimism-goerli":
      rpc_url = getRpcUrl("optimism-goerli");
    elif network == "arbitrum":
      rpc_url = getRpcUrl("arbitrum");
    elif network == "arbitrum-goerli":
      rpc_url = getRpcUrl("arbitrum-goerli");
    elif network == "fantom":
        rpc_url = get_rpc_url("fantom")
    elif network == "avalanche":
        rpc_url = get_rpc_url("avalanche")
    else:
        if network.startswith("http"):
            rpc_url = network
        else:
            raise Exception(f"Unrecognized chain name or RPC url {network}")

    return Web3(Web3.HTTPProvider(rpc_url))
