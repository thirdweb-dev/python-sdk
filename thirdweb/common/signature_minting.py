from typing import Optional
from uuid import uuid4


def resolve_or_generate_id(request_uid: Optional[str]) -> bytes:
    # TODO: Implement encoding
    if request_uid is None:
        generated_id = uuid4().hex
        return str.encode(generated_id)
    return str.encode(request_uid)
