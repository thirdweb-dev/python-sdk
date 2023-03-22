<a id="contracts.multiwrap"></a>

# contracts.multiwrap

<a id="contracts.multiwrap.Multiwrap"></a>

## Multiwrap Objects

```python
class Multiwrap(ERC721Standard[MultiwrapABI])
```

Multiwrap lets you wrap any number of ERC20, ERC721, or ERC1155 tokens into
a single wrapped token bundle.

```python
from thirdweb import ThirdwebSDK

# You can customize this to a supported network or your own RPC URL
network = "mumbai"

# Now we can create a new instance of the SDK
sdk = ThirdwebSDK(network)

# If you want to send transactions, you can instantiate the SDK with a private key instead:
#   sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network)

contract = sdk.get_multiwrap("{{contract_address}}")
```

<a id="contracts.multiwrap.Multiwrap.get_wrapped_contents"></a>

#### get\_wrapped\_contents

```python
def get_wrapped_contents(wrapped_token_id: int) -> WrappedTokens
```

Get the contents of a wrapped token bundle

**Arguments**:

- `wrapped_token_id`: The ID of the wrapped token to get the contents of

**Returns**:

The contents of the wrapped token bundle
```python
token_id = 0
contents = contract.get_wrapped_contents(token_id)
print(contents.erc20_tokens)
print(contents.erc721_tokens)
print(contents.erc1155_tokens)
```

<a id="contracts.multiwrap.Multiwrap.wrap"></a>

#### wrap

```python
def wrap(
    contents: TokensToWrap,
    wrapped_token_metadata: Union[str, NFTMetadataInput],
    recipient_address: Optional[str] = None
) -> TxResultWithId[NFTMetadataOwner]
```

Wrap any number of ERC20, ERC721, or ERC1155 tokens into a single wrapped token

**Arguments**:

- `contents`: The tokens to wrap into a single wrapped token
- `wrapped_token_metadata`: The metadata to use for the wrapped token
- `recipient_address`: The optional address to send the wrapped token to

**Returns**:

The transaction receipt of the token wrapping
```python
from thirdweb.types import (
    TokensToWrap,
    ERC20Wrappable,
    ERC721Wrappable,
    ERC1155Wrappable,
    NFTMetadataInput,
)

# Contract setup goes here...

tx = contract.wrap(
    TokensToWrap(
        erc20_tokens=[
            ERC20Wrappable(contract_address="0x...", quantity=0.8),
        ],
        erc721_tokens=[
            ERC721Wrappable(contract_address="0x...", token_id=0),
        ],
        erc1155_tokens=[
            ERC1155Wrappable(contract_address="0x...", token_id=0, quantity=1),
        ]
    ),
    NFTMetadataInput(
        name="Wrapped NFT",
        description="This is a wrapped bundle of tokens and NFTs",
        image="ipfs://...",
    )
)

print(tx.receipt, tx.id)
```

<a id="contracts.multiwrap.Multiwrap.unwrap"></a>

#### unwrap

```python
def unwrap(wrapped_token_id: int,
           recipient_address: Optional[str] = None) -> TxReceipt
```

Unwrap a wrapped token bundle

**Arguments**:

- `wrapped_token_id`: The ID of the wrapped token to unwrap
- `recipient_address`: The optional address to send the unwrapped tokens to

**Returns**:

The transaction receipt of the token unwrapping
```python
tx = contract.unwrap(wrapped_token_id, receipientAddress)
```

