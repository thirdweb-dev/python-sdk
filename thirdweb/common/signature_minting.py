from typing import Optional
from eth_utils import encode_hex


def resolve_or_generate_id(request_uid: Optional[str]) -> str:
    # TODO: Implement encoding
    if request_uid is None:
        return encode_hex(bytes(32))
    return encode_hex(request_uid).ljust(66, "0")
