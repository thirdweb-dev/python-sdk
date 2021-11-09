from enum import Enum
from eth_hash.auto import keccak


class Role(Enum):
    admin = ""
    minter = "MINTER_ROLE"
    transfer = "TRANSFER_ROLE"
    pauser = "PAUSER_ROLE"
    lister = "LISTER_ROLE"

    def get_hash(self) -> bytes:
        if self.name == "admin":
            return b"\x00" * 32

        r = str(self.value)
        return keccak(str.encode(r))
