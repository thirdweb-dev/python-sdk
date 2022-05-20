from web3 import Web3


DEFAULT_IPFS_GATEWAY = "https://gateway.ipfscdn.io/ipfs/"

TW_IPFS_SERVER_URL = "https://upload.nftlabs.co"

PINATA_IPFS_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"

DEFAULT_API_KEY = "_gg7wSSi0KMBsdKnGVfHDueq6xMB9EkC"


def get_provider_for_network(network: str) -> Web3:
    """
    Returns a web3 provider instance for the given network.
    """

    rpc_url = ""
    if network == "mainnet":
        rpc_url = f"https://eth-mainnet.g.alchemy.com/v2/{DEFAULT_API_KEY}"
    elif network == "rinkeby":
        rpc_url = f"https://eth-rinkeby.g.alchemy.com/v2/{DEFAULT_API_KEY}"
    elif network == "goerli":
        rpc_url = f"https://eth-goerli.g.alchemy.com/v2/{DEFAULT_API_KEY}"
    elif network == "polygon":
        rpc_url = f"https://polygon-mainnet.g.alchemy.com/v2/{DEFAULT_API_KEY}"
    elif network == "mumbai":
        rpc_url = f"https://polygon-mumbai.g.alchemy.com/v2/{DEFAULT_API_KEY}"
    elif network == "fantom":
        rpc_url = "rpc.ftm.tools"
    elif network == "avalanche":
        rpc_url = "https://rpc.ankr.com/avalanche"
    else:
        if network.startswith("http"):
            rpc_url = network
        else:
            raise Exception(f"Unrecognized chain name or RPC url {network}")

    return Web3(Web3.HTTPProvider(rpc_url))
