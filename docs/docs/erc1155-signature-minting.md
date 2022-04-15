<a id="core.classes.erc_1155_signature_minting"></a>

# core.classes.erc\_1155\_signature\_minting

<a id="core.classes.erc_1155_signature_minting.ERC1155SignatureMinting"></a>

## ERC1155SignatureMinting Objects

```python
class ERC1155SignatureMinting()
```

<a id="core.classes.erc_1155_signature_minting.ERC1155SignatureMinting.mint"></a>

#### mint

```python
def mint(signed_payload: SignedPayload1155) -> TxResultWithId
```

Mint a token with the given payload

**Arguments**:

- `signed_payload`: Signed payload

**Returns**:

transaction result with the token ID of the minted token

<a id="core.classes.erc_1155_signature_minting.ERC1155SignatureMinting.mint_batch"></a>

#### mint\_batch

```python
def mint_batch(
        signed_payloads: List[SignedPayload1155]) -> List[TxResultWithId]
```

Mint a batch of tokens with the given payloads

**Arguments**:

- `signed_payloads`: Signed payloads

**Returns**:

transaction results with the token IDs of the minted tokens

<a id="core.classes.erc_1155_signature_minting.ERC1155SignatureMinting.verify"></a>

#### verify

```python
def verify(signed_payload: SignedPayload1155) -> bool
```

Verify the signature of the given payload

**Arguments**:

- `signed_payload`: Signed payload

**Returns**:

True if the signature is valid, False otherwise

<a id="core.classes.erc_1155_signature_minting.ERC1155SignatureMinting.generate"></a>

#### generate

```python
def generate(mint_request: PayloadToSign1155) -> SignedPayload1155
```

Generate a signed payload from the given payload

**Arguments**:

- `mint_request`: Payload to sign

**Returns**:

Signed payload

<a id="core.classes.erc_1155_signature_minting.ERC1155SignatureMinting.generate_batch"></a>

#### generate\_batch

```python
def generate_batch(
        payloads_to_sign: List[PayloadToSign1155]) -> List[SignedPayload1155]
```

Generate a batch of signed payloads from the given payloads

**Arguments**:

- `payloads_to_sign`: Payloads to sign

**Returns**:

Signed payloads

