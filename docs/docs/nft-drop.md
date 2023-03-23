<a id="contracts.nft_drop"></a>

# contracts.nft\_drop

<a id="contracts.nft_drop.NFTDrop"></a>

## NFTDrop Objects

```python
class NFTDrop(ERC721Standard[DropERC721])
```

Setup a collection of one-of-one NFTs that are minted as users claim them.

```python
from thirdweb import ThirdwebSDK

# You can customize this to a supported network or your own RPC URL
network = "mumbai"

# Now we can create a new instance of the SDK
sdk = ThirdwebSDK(network)

# If you want to send transactions, you can instantiate the SDK with a private key instead:
#   sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network)

contract = sdk.get_nft_drop("{{contract_address}}")
```

<a id="contracts.nft_drop.NFTDrop.get_owned"></a>

#### get\_owned

```python
def get_owned(address: str = "") -> List[NFTMetadataOwner]
```

Get the metadata of all tokens owned by a specific address

```python
nfts = contract.get_owned("{{wallet_address}}")
print(nfts)
```

**Arguments**:

- `address`: the address to get the metadata for

**Returns**:

the metadata of all tokens owned by the address

<a id="contracts.nft_drop.NFTDrop.get_owned_token_ids"></a>

#### get\_owned\_token\_ids

```python
def get_owned_token_ids(address: str = "") -> List[int]
```

Get the token IDs owned by a specific address

**Arguments**:

- `address`: the address to get the token IDs for

**Returns**:

the token IDs owned by the address

<a id="contracts.nft_drop.NFTDrop.get_all_claimed"></a>

#### get\_all\_claimed

```python
def get_all_claimed(query_params: QueryAllParams = QueryAllParams()
                    ) -> List[NFTMetadataOwner]
```

Get all claimed NFTs.

```python
claimed_nfts = contract.get_all_claimed()
first_owner = claimed_nfts[0].owner
```

**Arguments**:

- `query_params`: Query parameters.

**Returns**:

List of nft metadatas and owners for claimed nfts.

<a id="contracts.nft_drop.NFTDrop.get_all_unclaimed"></a>

#### get\_all\_unclaimed

```python
def get_all_unclaimed(query_params: QueryAllParams = QueryAllParams()
                      ) -> List[NFTMetadata]
```

Get all unclaimed NFTs.

```python
unclaimed_nfts = contract.get_all_unclaimed()
first_nft_name = unclaimed_nfts[0].name
```

**Arguments**:

- `query_params`: Query parameters.

**Returns**:

List of nft metadatas.

<a id="contracts.nft_drop.NFTDrop.total_claimed_supply"></a>

#### total\_claimed\_supply

```python
def total_claimed_supply() -> int
```

Get the total number of NFTs claimed from this contract

```python
total_claimed = contract.total_claimed_supply()
```

**Returns**:

Total number of NFTs claimed from this contract

<a id="contracts.nft_drop.NFTDrop.total_unclaimed_supply"></a>

#### total\_unclaimed\_supply

```python
def total_unclaimed_supply() -> int
```

Get the total number of unclaimed NFTs in this contract

```python
total_unclaimed = contract.total_unclaimed_supply()
```

**Returns**:

Total number of unclaimed NFTs in this contract

<a id="contracts.nft_drop.NFTDrop.create_batch"></a>

#### create\_batch

```python
def create_batch(
        metadatas: List[NFTMetadataInput]
) -> List[TxResultWithId[NFTMetadata]]
```

Create a batch of NFTs.

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

txs = contract.create_batch(metadatas)
first_token_id = txs[0].id
first_nft = txs[0].data()
```

**Arguments**:

- `metadatas`: List of NFT metadata inputs.

**Returns**:

List of tx results with ids for created NFTs.

<a id="contracts.nft_drop.NFTDrop.claim_to"></a>

#### claim\_to

```python
def claim_to(destination_address: str,
             quantity: int) -> List[TxResultWithId[NFTMetadata]]
```

Claim NFTs to a destination address.

```python
address = {{wallet_address}}
quantity = 1

tx = contract.claim_to(address, quantity)
receipt = tx.receipt
claimed_token_id = tx.id
claimed_nft = tx.data()
```

**Arguments**:

- `destination_address`: Destination address to claim to.
- `quantity`: Number of NFTs to claim.
- `proofs`: List of merkle proofs.

**Returns**:

List of tx results with ids for claimed NFTs.

<a id="contracts.nft_drop.NFTDrop.claim"></a>

#### claim

```python
def claim(quantity: int) -> List[TxResultWithId[NFTMetadata]]
```

Claim NFTs.

**Arguments**:

- `quantity`: Number of NFTs to claim.
- `proofs`: List of merkle proofs.

**Returns**:

List of tx results with ids for claimed NFTs.

