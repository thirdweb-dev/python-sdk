<a id="core.classes.contract_roles"></a>

# core.classes.contract\_roles

<a id="core.classes.contract_roles.ContractRoles"></a>

## ContractRoles Objects

```python
class ContractRoles()
```

<a id="core.classes.contract_roles.ContractRoles.get_all"></a>

#### get\_all

```python
def get_all() -> Dict[Role, List[str]]
```

Get all role members on this contract.

```python
all_role_members = contract.roles.get_all()
print(all_role_members)
```

**Returns**:

a dictionary of role members for each role

<a id="core.classes.contract_roles.ContractRoles.get"></a>

#### get

```python
def get(role: Role) -> List[str]
```

Get all members of a role on this contract.

```python
from thirdweb.constants.role import Role

# Select any role to filter by
role = Role.ADMIN

role_members = contract.roles.get(role)
print(role_members)
```

**Arguments**:

- `role`: role to get members of

**Returns**:

list of members of the role

<a id="core.classes.contract_roles.ContractRoles.grant"></a>

#### grant

```python
def grant(role: Role, address: str) -> TxReceipt
```

Grant a role to a wallet

```python
from thirdweb.constants.role import Role

address = "{{wallet_address}}" # Address to grant a role
role = Role.ADMIN # Select a role to grant

receipt = contract.roles.grant(role, address)
```

**Arguments**:

- `role`: role to grant
- `address`: address to grant the role to

**Returns**:

transaction receipt of granting the role

<a id="core.classes.contract_roles.ContractRoles.revoke"></a>

#### revoke

```python
def revoke(role: Role, address: str) -> TxReceipt
```

Revoke a role from a wallet

```python
from thirdweb.constants.role import Role

address = "{{wallet_address}}" # Address to revoke a role from
role = Role.MINTER # The role to revoke

receipt = contract.roles.revoke(role, address)
```

**Arguments**:

- `role`: role to revoke
- `address`: address to revoke the role from

**Returns**:

transaction receipt of revoking the role

