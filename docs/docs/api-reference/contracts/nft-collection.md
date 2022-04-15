<a id="contracts.nft_collection"></a>

# contracts.nft\_collection

Interface for interacting with an nft collection contract

<a id="contracts.nft_collection.NFTCollection"></a>

## NFTCollection Objects

```python
class NFTCollection(ERC721[TokenERC721])
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

**Arguments**:

- `to`: wallet address to mint the NFTs to
- `metadatas`: list of metadata of the NFTs to mint

**Returns**:

receipts, ids, and metadatas for each mint

