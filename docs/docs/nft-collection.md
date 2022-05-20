<a id="contracts.nft_collection"></a>

# contracts.nft\_collection

Interface for interacting with an nft collection contract

<a id="contracts.nft_collection.NFTCollection"></a>

## NFTCollection Objects

```python
class NFTCollection(ERC721[TokenERC721])
```

Create a collection of one-of-one NFTs.

```python
from thirdweb import ThirdwebSDK
from eth_account import Account

# You can customize this to a supported network or your own RPC URL
network = "mumbai"

# This will create a random account to use for signing transactions
signer = Account.create()

sdk = ThirdwebSDK(network, signer)
contract = sdk.get_nft_collection("{{contract_address}}")
```

<a id="contracts.nft_collection.NFTCollection.mint"></a>

#### mint

```python
def mint(
    metadata: Union[NFTMetadataInput,
                    str]) -> TxResultWithId[NFTMetadataOwner]
```

Mint a new NFT to the connected wallet

**Arguments**:

- `metadata`: metadata of the NFT to mint

**Returns**:

receipt, id, and metadata for the mint

<a id="contracts.nft_collection.NFTCollection.mint_to"></a>

#### mint\_to

```python
def mint_to(
    to: str, metadata: Union[NFTMetadataInput,
                             str]) -> TxResultWithId[NFTMetadataOwner]
```

Mint a new NFT to the specified wallet

```python
from thirdweb.types.nft import NFTMetadataInput

# Note that you can customize this metadata however you like
metadata = NFTMetadataInput.from_json({
    "name": "Cool NFT",
    "description": "This is a cool NFT",
    "image": open("path/to/file.jpg", "rb"),
})

# You can pass in any address here to mint the NFT to
tx = contract.mint_to("{{wallet_address}}", metadata)
receipt = tx.receipt
token_id = tx.id
nft = tx.data()
```

**Arguments**:

- `to`: wallet address to mint the NFT to
- `metadata`: metadata of the NFT to mint

**Returns**:

receipt, id, and metadata for the mint

<a id="contracts.nft_collection.NFTCollection.mint_batch"></a>

#### mint\_batch

```python
def mint_batch(
    metadatas: List[Union[NFTMetadataInput, str]]
) -> List[TxResultWithId[NFTMetadataOwner]]
```

Mint a batch of new NFTs to the connected wallet

**Arguments**:

- `metadatas`: list of metadata of the NFTs to mint

**Returns**:

receipts, ids, and metadatas for each mint

<a id="contracts.nft_collection.NFTCollection.mint_batch_to"></a>

#### mint\_batch\_to

```python
def mint_batch_to(
    to: str, metadatas: List[Union[NFTMetadataInput, str]]
) -> List[TxResultWithId[NFTMetadataOwner]]
```

Mint a batch of new NFTs to the specified wallet

```python
from thirdweb.types.nft import NFTMetadataInput

# You can customize this metadata however you like
metadatas = [
    NFTMetadataInput.from_json({
        "name": "Cool NFT",
        "description": "This is a cool NFT",
        "image": open("path/to/file.jpg", "rb"),
    }),
    NFTMetadataInput.from_json({
        "name": "Cooler NFT",
        "description": "This is a cooler NFT",
        "image": open("path/to/file.jpg", "rb"),
    }),
]

# You can pass in any address here to mint the NFT to
txs = contract.mint_batch_to("{{wallet_address}}", metadatas)
receipt = txs[0].receipt
first_token_id = txs[0].id
first_nft = txs[0].data()
```

**Arguments**:

- `to`: wallet address to mint the NFTs to
- `metadatas`: list of metadata of the NFTs to mint

**Returns**:

receipts, ids, and metadatas for each mint

