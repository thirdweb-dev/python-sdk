from eth_utils import encode_hex
from hexbytes import HexBytes
from web3 import Web3
from typing import Dict
from enum import Enum

from thirdweb.constants.addresses import DEFAULT_MERKLE_ROOT


class Role(Enum):
    ADMIN = "admin"
    TRANSFER = "transfer"
    MINTER = "minter"
    PAUSER = "pauser"
    EDITOR = "editor"
    LISTER = "lister"
    ASSET = "asset"
    UNWRAP = "unwrap"


ROLE_MAP: Dict[Role, str] = {
    Role.ADMIN: "",
    Role.TRANSFER: "TRANSFER_ROLE",
    Role.MINTER: "MINTER_ROLE",
    Role.PAUSER: "PAUSER_ROLE",
    Role.EDITOR: "EDITOR_ROLE",
    Role.LISTER: "LISTER_ROLE",
    Role.ASSET: "ASSET_ROLE",
    Role.UNWRAP: "UNWRAP_ROLE",
}

ALL_ROLES = [
    Role.ADMIN,
    Role.TRANSFER,
    Role.MINTER,
    Role.PAUSER,
    Role.EDITOR,
    Role.LISTER,
    Role.ASSET,
    Role.UNWRAP,
]


def get_role_hash(role: Role) -> HexBytes:
    if role == Role.ADMIN:
        return HexBytes(DEFAULT_MERKLE_ROOT)
    return Web3.keccak(text=ROLE_MAP[role])
