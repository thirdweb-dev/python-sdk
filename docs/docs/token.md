<a id="contracts.token"></a>

# contracts.token

Interface for interacting with a token contract

<a id="contracts.token.Token"></a>

## Token Objects

```python
class Token(ERC20Standard)
```

Create a standard crypto token or cryptocurrency.

```python
from thirdweb import ThirdwebSDK

# You can customize this to a supported network or your own RPC URL
network = "mumbai"

# Now we can create a new instance of the SDK
sdk = ThirdwebSDK(network)

# If you want to send transactions, you can instantiate the SDK with a private key instead:
#   sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network)

contract = sdk.get_token("{{contract_address}}")
```

<a id="contracts.token.Token.get_vote_balance"></a>

#### get\_vote\_balance

```python
def get_vote_balance() -> CurrencyValue
```

Get the connected wallets voting power in this token.

**Returns**:

vote balance of the connected wallet

<a id="contracts.token.Token.get_vote_balance_of"></a>

#### get\_vote\_balance\_of

```python
def get_vote_balance_of(account: str) -> CurrencyValue
```

Get the voting power of the specified wallet in this token.

**Arguments**:

- `account`: wallet address to check the balance of

**Returns**:

vote balance of the specified wallet

<a id="contracts.token.Token.get_delegation"></a>

#### get\_delegation

```python
def get_delegation() -> str
```

Get the connected wallets delegatee address for this token.

**Returns**:

delegation address of the connected wallet

<a id="contracts.token.Token.get_delegation_of"></a>

#### get\_delegation\_of

```python
def get_delegation_of(account: str) -> str
```

Get a specified wallets delegatee for this token.

**Arguments**:

- `account`: wallet address to check the delegation of

**Returns**:

delegation address of the specified wallet

<a id="contracts.token.Token.mint"></a>

#### mint

```python
def mint(amount: Price) -> TxReceipt
```

Mint tokens to the connected wallet.

**Arguments**:

- `amount`: amount of tokens to mint

**Returns**:

transaction receipt of the mint

<a id="contracts.token.Token.mint_to"></a>

#### mint\_to

```python
def mint_to(to: str, amount: Price) -> TxReceipt
```

Mint tokens to a specified wallet.

```python
contract.mint_to("{{wallet_address}}", 1)
```

**Arguments**:

- `to`: wallet address to mint tokens to
- `amount`: amount of tokens to mint

**Returns**:

transaction receipt of the mint

<a id="contracts.token.Token.mint_batch_to"></a>

#### mint\_batch\_to

```python
def mint_batch_to(args: List[TokenAmount]) -> TxReceipt
```

Mint tokens to a list of wallets.

```python
from thirdweb.types.currency import TokenAmount

args = [
    TokenAmount("{{wallet_address}}", 1),
    TokenAmount("{{wallet_address}}", 2),
]

contract.mint_batch_to(args)
```

**Arguments**:

- `args`: list of wallet addresses and amounts to mint

**Returns**:

transaction receipt of the mint

<a id="contracts.token.Token.delegate_to"></a>

#### delegate\_to

```python
def delegate_to(delegatee_address: str) -> TxReceipt
```

Delegate the connected wallets tokens to a specified wallet.

**Arguments**:

- `delegatee_address`: wallet address to delegate tokens to

**Returns**:

transaction receipt of the delegation

