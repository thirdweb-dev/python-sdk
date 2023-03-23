<a id="core.classes.erc_20"></a>

# core.classes.erc\_20

<a id="core.classes.erc_20.ERC20"></a>

## ERC20 Objects

```python
class ERC20(BaseContract[TokenERC20])
```

<a id="core.classes.erc_20.ERC20.get"></a>

#### get

```python
def get() -> Currency
```

Get token metadata

```python
token = contract.erc20.get()
print(token)
```

**Returns**:

token metadata

<a id="core.classes.erc_20.ERC20.balance"></a>

#### balance

```python
def balance() -> CurrencyValue
```

Get token balance

```python
balance = contract.erc20.balance()
print(balance)
```

**Returns**:

balance of the connected wallet

<a id="core.classes.erc_20.ERC20.balance_of"></a>

#### balance\_of

```python
def balance_of(address: str) -> CurrencyValue
```

Get token balance of a specific wallet

```python
address = "{{wallet_address}}"
balance = contract.erc20.balance_of(address)
print(balance)
```

**Arguments**:

- `address`: wallet address to check the balance of

**Returns**:

balance of the specified wallet

<a id="core.classes.erc_20.ERC20.total_supply"></a>

#### total\_supply

```python
def total_supply() -> CurrencyValue
```

Get the total minted supply

```python
supply = contract.erc20.total_supply()
print(supply)
```

**Returns**:

total minted supply of the token

<a id="core.classes.erc_20.ERC20.allowance"></a>

#### allowance

```python
def allowance(spender: str) -> CurrencyValue
```

Get the allowance of a specific spender

```python
spender = "{{wallet_address}}"
allowance = contract.erc20.allowance(spender)
print(allowance)
```

**Arguments**:

- `spender`: wallet address to check the allowance of

**Returns**:

allowance of the connected wallet

<a id="core.classes.erc_20.ERC20.allowance_of"></a>

#### allowance\_of

```python
def allowance_of(owner: str, spender: str) -> CurrencyValue
```

Get the allowance of a spender for a specific owner

```python
# Address of the wallet who owns the funds
address = "{{wallet_address}}"

# Address of the wallet to check the token allowance
spender = "0x..."

allowance = contract.erc20.allowance_of(address, spender)
print(allowance)
```

**Arguments**:

- `owner`: wallet address whose assets will be spent
- `spender`: wallet address to check the allowance of

**Returns**:

allowance of the specified spender for the specified owner

<a id="core.classes.erc_20.ERC20.is_transfer_restricted"></a>

#### is\_transfer\_restricted

```python
def is_transfer_restricted() -> bool
```

Check whether transfer is restricted for tokens in this module

```python
is_restricted = contract.erc20.is_transfer_restricted()
print(is_restricted)
```

**Returns**:

True if transfer is restricted, False otherwise

<a id="core.classes.erc_20.ERC20.mint"></a>

#### mint

```python
def mint(amount: Price) -> TxReceipt
```

Mint tokens

```python
address = "{{wallet_address}}"
amount = 100

receipt = contract.erc20.mint(amount)
```

**Arguments**:

- `amount`: amount of tokens to mint

**Returns**:

transaction receipt of the mint

<a id="core.classes.erc_20.ERC20.mint_to"></a>

#### mint\_to

```python
def mint_to(to: str, amount: Price) -> TxReceipt
```

Mint tokens to a specific wallet

```python
address = "{{wallet_address}}"
amount = 100

receipt = contract.erc20.mint_to(address, amount)
```

**Arguments**:

- `to`: wallet address to mint tokens to
- `amount`: amount of tokens to mint

**Returns**:

transaction receipt of the mint

<a id="core.classes.erc_20.ERC20.mint_batch_to"></a>

#### mint\_batch\_to

```python
def mint_batch_to(args: List[TokenAmount]) -> TxReceipt
```

Mint tokens to many wallets

```python
from thirdweb.types.currency import TokenAmount

args = [
    TokenAmount("{{wallet_address}}", 1),
    TokenAmount("{{wallet_address}}", 2),
]

**Arguments**:

- `args`: list of wallet addresses and amounts to mint

**Returns**:

transaction receipt of the mint

<a id="core.classes.erc_20.ERC20.transfer"></a>

#### transfer

```python
def transfer(to: str, amount: Price) -> TxReceipt
```

Transfer tokens

```python
# Address to send tokens to
to = "0x...

# Amount of tokens to transfer
amount = 0.1

contract.erc20.transfer(to, amount)
```

**Arguments**:

- `to`: wallet address to transfer the tokens to
- `amount`: amount of tokens to transfer

**Returns**:

transaction receipt of the transfer

<a id="core.classes.erc_20.ERC20.transfer_from"></a>

#### transfer\_from

```python
def transfer_from(fr: str, to: str, amount: Price) -> TxReceipt
```

Transfer tokens from a specific wallet

```python
# Address to send tokens from
fr = "{{wallet_address}}"

# Address to send tokens to
to = "0x..."

# Amount of tokens to transfer
amount = 0.1

contract.erc20.transfer_from(fr, to, amount)
```

**Arguments**:

- `fr`: wallet address to transfer the tokens from
- `to`: wallet address to transfer the tokens to
- `amount`: amount of tokens to transfer

**Returns**:

transaction receipt of the transfer

<a id="core.classes.erc_20.ERC20.set_allowance"></a>

#### set\_allowance

```python
def set_allowance(spender: str, amount: Price) -> TxReceipt
```

Approve a specific wallet to spend tokens

```python
spender = "0x..."
amount = 100
contract.erc20.set_allowance(spender, amount)
```

**Arguments**:

- `spender`: wallet address to set the allowance of
- `amount`: amount to set the allowance to

**Returns**:

transaction receipt of the allowance set

<a id="core.classes.erc_20.ERC20.transfer_batch"></a>

#### transfer\_batch

```python
def transfer_batch(args: List[TokenAmount])
```

Transfer tokens to many wallets

```python
from thirdweb.types.currency import TokenAmount

data = [
    TokenAmount("{{wallet_address}}", 0.1),
    TokenAmount("0x...", 0.2),
]

contract.erc20.transfer_batch(data)
```

**Arguments**:

- `args`: list of token amounts and addressed to transfer to

**Returns**:

transaction receipt of the transfers

<a id="core.classes.erc_20.ERC20.burn"></a>

#### burn

```python
def burn(amount: Price) -> TxReceipt
```

Burn tokens

```python
amount = 0.1
contract.erc20.burn(amount)
```

**Arguments**:

- `amount`: amount of tokens to burn

**Returns**:

transaction receipt of the burn

<a id="core.classes.erc_20.ERC20.burn_from"></a>

#### burn\_from

```python
def burn_from(holder: str, amount: Price) -> TxReceipt
```

Burn tokens from a specific wallet

```python
holder = "{{wallet_address}}"
amount = 0.1
contract.erc20.burn_from(holder, amount)
```

**Arguments**:

- `holder`: wallet address to burn the tokens from
- `amount`: amount of tokens to burn

**Returns**:

transaction receipt of the burn

