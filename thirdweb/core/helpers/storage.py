from typing import TextIO, BinaryIO, TypeVar, cast, Dict, Any, List

T = TypeVar("T")


def replace_file_properties_with_hashes(object: Dict[str, Any], cids: List[str]):
    for key, val in object.items():
        is_file = isinstance(val, TextIO) or isinstance(val, BinaryIO)
        if isinstance(val, dict) and not is_file:
            object[key] = replace_file_properties_with_hashes(val, cids)
            continue

        if not is_file:
            continue

        object[key] = f"ipfs://{cids.pop(0)}"

    return object


def replace_hash_with_gateway_url(
    object: Dict[str, Any], scheme: str, gateway_url: str
) -> Dict[str, Any]:
    """
    Replaces all hashes in an object with gateway URLs
    """

    for key, val in object.items():
        if isinstance(val, dict):
            object[key] = replace_hash_with_gateway_url(val, scheme, gateway_url)
        elif isinstance(val, list):
            object[key] = [
                replace_hash_with_gateway_url(item, scheme, gateway_url) for item in val
            ]
        elif isinstance(val, str):
            object[key] = resolve_gateway_url(val, scheme, gateway_url)

    return object


def resolve_gateway_url(ipfs_hash: T, scheme: str, gateway_url: str) -> T:
    """
    Resolves the gateway url for the given hash.
    """

    if not isinstance(ipfs_hash, str):
        return ipfs_hash

    return cast(T, cast(str, ipfs_hash).replace(scheme, gateway_url))
