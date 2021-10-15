import enum
from eth_hash.auto import keccak


class Role(enum.Enum):
    admin = ""
    minter = "MINTER_ROLE"
    transfer = "TRANSFER_ROLE"
    pauser = "PAUSER_ROLE"

    def get_hash(self) -> bytes:
        if self.name == "admin":
            return b"\x00" * 32

        r = str(self.value)
        return keccak(str.encode(r))
