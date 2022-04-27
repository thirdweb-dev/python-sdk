<a id="contracts.edition_drop"></a>

# contracts.edition\_drop

<a id="contracts.edition_drop.EditionDrop"></a>

## EditionDrop Objects

```python
class EditionDrop(ERC1155[DropERC1155])
```

Setup a collection of NFTs with a customizable number of each NFT that are minted as users claim them.

```python
from thirdweb import ThirdwebSDK
from eth_account import Account
from web3 import Web3

# You can switch out this provider and RPC URL for your own
provider = Web3(Web3.HTTPProvider("<RPC_URL>"))
# This will create a random account to use for signing transactions
signer = Account.create()

sdk = ThirdwebSDK(provider, signer)
contract = sdk.get_edition_drop("{{contract_address}}")
```

<a id="contracts.edition_drop.EditionDrop.create_batch"></a>

#### create\_batch

```python
def create_batch(
        metadatas: List[NFTMetadataInput]
) -> List[TxResultWithId[NFTMetadata]]
```

Create a batch of NFTs.

```python
from thirdweb.types.nft import NFTMetadataInput, EditionMetadataInput

# Note that you can customize this metadata however you like
metadatas_with_supply = [
    EditionMetadataInput(
        NFTMetadataInput.from_json({
            "name": "Cool NFT",
            "description": "This is a cool NFT",
            "image": open("path/to/file.jpg", "rb"),
        }),
        100
    ),
    EditionMetadataInput(
        NFTMetadataInput.from_json({
            "name": "Cooler NFT",
            "description": "This is a cooler NFT",
            "image": open("path/to/file.jpg", "rb"),
        }),
        100
    )
]

txs = contract.create_batch(metadata_with_supply)
first_token_id = txs[0].id
first_nft = txs[0].data()
```

**Arguments**:

- `metadatas`: List of NFT metadata inputs.

**Returns**:

List of tx results with ids for created NFTs.

<a id="contracts.edition_drop.EditionDrop.claim_to"></a>

#### claim\_to

```python
def claim_to(destination_address: str,
             token_id: int,
             quantity: int,
             proofs: List[str] = [DEFAULT_MERKLE_ROOT]) -> TxReceipt
```

Claim NFTs to a destination address.

```python
address = {{wallet_address}}
token_id = 0
quantity = 1

tx = contract.claim_to(address, token_id, quantity)
receipt = tx.receipt
claimed_token_id = tx.id
claimed_nft = tx.data()
```

**Arguments**:

- `destination_address`: Destination address to claim to.
- `token_id`: token ID of the token to claim.
- `quantity`: Number of NFTs to claim.
- `proofs`: List of merkle proofs.

**Returns**:

tx receipt of the claim

<a id="contracts.edition_drop.EditionDrop.claim"></a>

#### claim

```python
def claim(token_id: int,
          quantity: int,
          proofs: List[str] = [DEFAULT_MERKLE_ROOT]) -> TxReceipt
```

Claim NFTs.

**Arguments**:

- `quantity`: Number of NFTs to claim.
- `token_id`: token ID of the token to claim.
- `proofs`: List of merkle proofs.

**Returns**:

tx receipt of the claim

