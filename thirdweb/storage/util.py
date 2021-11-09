def replace_ipfs_prefix_with_gateway(uri: str, gateway_url: str) -> str:
    if uri == "":
        return ""

    return uri.replace("ipfs://", gateway_url, 1).rstrip("/")
