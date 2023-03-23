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

Get the contract platform fees

```python
platform_fees = contract.platform_fee.get()
print(platform_fees.platform_fee_basis_points)
print(platform_fees.platform_fee_recipient)
```

**Returns**:

the platform fee.

<a id="core.classes.contract_platform_fee.ContractPlatformFee.set"></a>

#### set

```python
def set(platform_fee_info: ContractPlatformFeeSchema) -> TxReceipt
```

Set the contract platform fees

```python
from thirdweb.types import ContractPlatformFeeSchema

platform_fee_info = ContractPlatformFeeSchema(
    platform_fee_basis_points=100 # 1%
    platform_fee_receipient="{{wallet_address}}"
)

receipt = contract.platform_fee.set(platform_fee_info)
```

**Arguments**:

- `platform_fee_info`: the platform fee info to set.

**Returns**:

the transaction receipt of setting the platform fee.

