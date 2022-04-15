<a id="contracts.nft_drop"></a>

# contracts.nft\_drop

<a id="contracts.nft_drop.NFTDrop"></a>

## NFTDrop Objects

```python
class NFTDrop(ERC721[DropERC721])
```

<a id="contracts.nft_drop.NFTDrop.get_all_claimed"></a>

#### get\_all\_claimed

```python
def get_all_claimed(query_params: QueryAllParams = QueryAllParams()
                    ) -> List[NFTMetadataOwner]
```

Get all claimed NFTs.

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

**Returns**:

Total number of NFTs claimed from this contract

<a id="contracts.nft_drop.NFTDrop.total_unclaimed_supply"></a>

#### total\_unclaimed\_supply

```python
def total_unclaimed_supply() -> int
```

Get the total number of unclaimed NFTs in this contract

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

**Arguments**:

- `metadatas`: List of NFT metadata inputs.

**Returns**:

List of tx results with ids for created NFTs.

<a id="contracts.nft_drop.NFTDrop.claim_to"></a>

#### claim\_to

```python
def claim_to(
    destination_address: str,
    quantity: int,
    proofs: List[str] = [DEFAULT_MERKLE_ROOT]
) -> List[TxResultWithId[NFTMetadata]]
```

Claim NFTs to a destination address.

**Arguments**:

- `destination_address`: Destination address to claim to.
- `quantity`: Number of NFTs to claim.
- `proofs`: List of merkle proofs.

**Returns**:

List of tx results with ids for claimed NFTs.

<a id="contracts.nft_drop.NFTDrop.claim"></a>

#### claim

```python
def claim(
    quantity: int,
    proofs: List[str] = [DEFAULT_MERKLE_ROOT]
) -> List[TxResultWithId[NFTMetadata]]
```

Claim NFTs.

**Arguments**:

- `quantity`: Number of NFTs to claim.
- `proofs`: List of merkle proofs.

**Returns**:

List of tx results with ids for claimed NFTs.

