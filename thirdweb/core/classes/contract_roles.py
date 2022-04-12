from typing import Dict, List
from thirdweb.common.error import RoleException
from thirdweb.constants.role import Role, get_role_hash
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from web3.eth import TxReceipt


class ContractRoles:
    _contract_wrapper: ContractWrapper
    _roles: List[Role]

    def __init__(self, contract_wrapper: ContractWrapper, roles: List[Role]):
        self._contract_wrapper = contract_wrapper
        self._roles = roles

    """
    READ FUNCTIONS
    """

    def get_all(self) -> Dict[Role, List[str]]:
        """
        Get all role members on this contract.

        :returns: a dictionary of role members for each role
        """

        if len(self._roles) == 0:
            raise RoleException("This contract has no support for roles")

        roles = {}
        for role in self._roles:
            roles[role] = self.get(role)

        return roles

    def get(self, role: Role) -> List[str]:
        """
        Get all members of a role on this contract.

        :param role: role to get members of
        :returns: list of members of the role
        """

        if role not in self._roles:
            raise RoleException(f"This contract does not support role {role}")

        role_hash = get_role_hash(role)
        count = self._contract_wrapper._contract_abi.get_role_member_count.call(
            role_hash
        )

        return [
            self._contract_wrapper._contract_abi.get_role_member.call(role_hash, i)
            for i in range(count)
        ]

    def verify(self, roles: List[Role], address: str):
        for role in roles:
            members = self.get(role)
            if address.lower() not in [member.lower() for member in members]:
                raise RoleException(f"Address {address} is not a member of role {role}")

    """
    WRITE FUNCTIONS
    """

    def grant(self, role: Role, address: str) -> TxReceipt:
        """
        Grant a role to an address.

        :param role: role to grant
        :param address: address to grant the role to
        :returns: transaction receipt of granting the role
        """

        if role not in self._roles:
            raise RoleException(f"This contract does not support role {role}")

        role_hash = get_role_hash(role)
        return self._contract_wrapper.send_transaction(
            "grant_role", [role_hash, address]
        )

    def revoke(self, role: Role, address: str) -> TxReceipt:
        """
        Revoke a role from an address.

        :param role: role to revoke
        :param address: address to revoke the role from
        :returns: transaction receipt of revoking the role
        """

        if role not in self._roles:
            raise RoleException(f"This contract does not support role {role}")

        role_hash = get_role_hash(role)
        revoke_function_name = self.get_revoke_role_function_name(address)
        return self._contract_wrapper.send_transaction(
            revoke_function_name, [role_hash, address]
        )

    def get_revoke_role_function_name(self, address: str) -> str:
        signer_address = self._contract_wrapper.get_signer_address()
        if signer_address.lower() == address.lower():
            return "renounce_role"
        return "revoke_role"
