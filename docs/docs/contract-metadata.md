<a id="core.classes.contract_metadata"></a>

# core.classes.contract\_metadata

<a id="core.classes.contract_metadata.ContractMetadata"></a>

## ContractMetadata Objects

```python
class ContractMetadata(Generic[TMetadataABI, TContractSchema])
```

<a id="core.classes.contract_metadata.ContractMetadata.get"></a>

#### get

```python
def get() -> TContractSchema
```

Get the contract metadata

```python
metadata = contract.metadata.get()
print(metadata)
```

**Returns**:

metadata associated with this contract

<a id="core.classes.contract_metadata.ContractMetadata.set"></a>

#### set

```python
def set(metadata: TContractSchema) -> TxReceipt
```

Set the contract metadata

```python
from thirdweb.types import ContractMetadataSchema

metadata = ContractMetadataSchema.from_json({
    "name": "My Contract",
    "description": "This is my contract!",
    "image": open("path/to/file.jpg", "rb")
})

receipt = contract.metadata.set(metadata)
```

**Arguments**:

- `metadata`: metadata to set

**Returns**:

transaction receipt of setting the metadata

