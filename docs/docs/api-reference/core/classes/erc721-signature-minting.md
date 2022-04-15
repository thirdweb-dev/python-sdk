<a id="core.classes.erc_721_signature_minting"></a>

# core.classes.erc\_721\_signature\_minting

<a id="core.classes.erc_721_signature_minting.ERC721SignatureMinting"></a>

## ERC721SignatureMinting Objects

```python
class ERC721SignatureMinting()
```

<a id="core.classes.erc_721_signature_minting.ERC721SignatureMinting.mint"></a>

#### mint

```python
def mint(signed_payload: SignedPayload721) -> TxResultWithId
```

Mint a token with the given payload

**Arguments**:

- `signed_payload`: Signed payload

**Returns**:

transaction result with the token ID of the minted token

<a id="core.classes.erc_721_signature_minting.ERC721SignatureMinting.mint_batch"></a>

#### mint\_batch

```python
def mint_batch(
        signed_payloads: List[SignedPayload721]) -> List[TxResultWithId]
```

Mint a batch of tokens with the given payloads

**Arguments**:

- `signed_payloads`: Signed payloads

**Returns**:

transaction results with the token IDs of the minted tokens

<a id="core.classes.erc_721_signature_minting.ERC721SignatureMinting.verify"></a>

#### verify

```python
def verify(signed_payload: SignedPayload721) -> bool
```

Verify the signature of the given payload

**Arguments**:

- `signed_payload`: Signed payload

**Returns**:

True if the signature is valid, False otherwise

<a id="core.classes.erc_721_signature_minting.ERC721SignatureMinting.generate"></a>

#### generate

```python
def generate(mint_request: PayloadToSign721) -> SignedPayload721
```

Generate a signed payload from the given payload

**Arguments**:

- `mint_request`: Payload to sign

**Returns**:

Signed payload

<a id="core.classes.erc_721_signature_minting.ERC721SignatureMinting.generate_batch"></a>

#### generate\_batch

```python
def generate_batch(
        payloads_to_sign: List[PayloadToSign721]) -> List[SignedPayload721]
```

Generate a batch of signed payloads from the given payloads

**Arguments**:

- `payloads_to_sign`: Payloads to sign

**Returns**:

Signed payloads

