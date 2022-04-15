<a id="core.classes.drop_erc1155_claim_conditions"></a>

# core.classes.drop\_erc1155\_claim\_conditions

<a id="core.classes.drop_erc1155_claim_conditions.DropERC1155ClaimConditions"></a>

## DropERC1155ClaimConditions Objects

```python
class DropERC1155ClaimConditions()
```

<a id="core.classes.drop_erc1155_claim_conditions.DropERC1155ClaimConditions.get_active"></a>

#### get\_active

```python
def get_active(token_id: int) -> ClaimCondition
```

Get the currently active claim condition

**Arguments**:

- `token_id`: token ID of the token to get the active claim condition for.

**Returns**:

The currently active claim condition

<a id="core.classes.drop_erc1155_claim_conditions.DropERC1155ClaimConditions.get_all"></a>

#### get\_all

```python
def get_all(token_id: int) -> List[ClaimCondition]
```

Get all claim conditions on this contract

**Arguments**:

- `token_id`: token ID of the token to get all claim conditions for.

**Returns**:

A list of all claim conditions on this contract

