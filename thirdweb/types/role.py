"""
Roles
"""
from enum import Enum
from eth_hash.auto import keccak


class Role(Enum):
    '''
    The `Role` class is used to define the roles used throughout the contracts.
    '''

    '''The admin role, which has complete control over a project/module including assigning roles'''
    admin = ""

    '''The minter role, which permission to mint tokens in a contract'''
    minter = "MINTER_ROLE"

    '''The transfer role, which has permission to transfer tokens in and out of contracts'''
    transfer = "TRANSFER_ROLE"

    '''The pauser role, which has the permission to pause all changes on a module'''
    pauser = "PAUSER_ROLE"

    '''The lister role, which has permission to list items on a Market'''
    lister = "LISTER_ROLE"

    def get_hash(self) -> bytes:
        if self.name == "admin":
            return b"\x00" * 32

        r = str(self.value)
        return keccak(str.encode(r))
