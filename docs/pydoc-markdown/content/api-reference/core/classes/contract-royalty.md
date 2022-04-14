<a id="core.classes.contract_royalty"></a>

# core.classes.contract\_royalty

<a id="core.classes.contract_royalty.ContractRoyalty"></a>

## ContractRoyalty Objects

```python
class ContractRoyalty(Generic[TRoyaltyABI])
```

<a id="core.classes.contract_royalty.ContractRoyalty.get_default_royalty_info"></a>

#### get\_default\_royalty\_info

```python
def get_default_royalty_info() -> ContractRoyaltySchema
```

Get the default royalty information for this contract.

**Returns**:

the default royalty information.

<a id="core.classes.contract_royalty.ContractRoyalty.get_token_royalty_info"></a>

#### get\_token\_royalty\_info

```python
def get_token_royalty_info(token_id: int) -> ContractRoyaltySchema
```

Get the royalty information for a specific token.

**Arguments**:

- `token_id`: the id of the token.

**Returns**:

the royalty information for the token.

<a id="core.classes.contract_royalty.ContractRoyalty.set_default_royalty_info"></a>

#### set\_default\_royalty\_info

```python
def set_default_royalty_info(royalty_data: ContractRoyaltySchema) -> TxReceipt
```

Set the default royalty information for this contract.

**Arguments**:

- `royalty_data`: the default royalty information.

**Returns**:

the transaction receipt of setting the royalty.

<a id="core.classes.contract_royalty.ContractRoyalty.set_token_royalty_info"></a>

#### set\_token\_royalty\_info

```python
def set_token_royalty_info(token_id: int,
                           royalty_data: ContractRoyaltySchema) -> TxReceipt
```

Set the royalty information for a specific token.

**Arguments**:

- `token_id`: the id of the token.
- `royalty_data`: the royalty information for the token.

**Returns**:

the transaction receipt of setting the royalty.

