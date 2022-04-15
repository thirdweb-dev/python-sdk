<a id="core.classes.contract_platform_fee"></a>

# core.classes.contract\_platform\_fee

<a id="core.classes.contract_platform_fee.ContractPlatformFee"></a>

## ContractPlatformFee Objects

```python
class ContractPlatformFee(Generic[TPlatformFeeABI])
```

<a id="core.classes.contract_platform_fee.ContractPlatformFee.get"></a>

#### get

```python
def get() -> ContractPlatformFeeSchema
```

Get the platform fee of this contract.

**Returns**:

the platform fee.

<a id="core.classes.contract_platform_fee.ContractPlatformFee.set"></a>

#### set

```python
def set(platform_fee_info: ContractPlatformFeeSchema) -> TxReceipt
```

Set the platform fee of this contract.

**Arguments**:

- `platform_fee_info`: the platform fee info to set.

**Returns**:

the transaction receipt of setting the platform fee.

