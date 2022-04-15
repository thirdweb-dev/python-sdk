<a id="core.classes.erc_20_signature_minting"></a>

# core.classes.erc\_20\_signature\_minting

<a id="core.classes.erc_20_signature_minting.ERC20SignatureMinting"></a>

## ERC20SignatureMinting Objects

```python
class ERC20SignatureMinting()
```

<a id="core.classes.erc_20_signature_minting.ERC20SignatureMinting.mint"></a>

#### mint

```python
def mint(signed_payload: SignedPayload20) -> TxReceipt
```

Mint a token with the given payload

**Arguments**:

- `signed_payload`: Signed payload

**Returns**:

transaction result with the token ID of the minted token

<a id="core.classes.erc_20_signature_minting.ERC20SignatureMinting.mint_batch"></a>

#### mint\_batch

```python
def mint_batch(signed_payloads: List[SignedPayload20]) -> TxReceipt
```

Mint a batch of tokens with the given payloads

**Arguments**:

- `signed_payloads`: Signed payloads

**Returns**:

transaction results with the token IDs of the minted tokens

<a id="core.classes.erc_20_signature_minting.ERC20SignatureMinting.verify"></a>

#### verify

```python
def verify(signed_payload: SignedPayload20) -> bool
```

Verify the signature of the given payload

**Arguments**:

- `signed_payload`: Signed payload

**Returns**:

True if the signature is valid, False otherwise

<a id="core.classes.erc_20_signature_minting.ERC20SignatureMinting.generate"></a>

#### generate

```python
def generate(mint_request: PayloadToSign20) -> SignedPayload20
```

Generate a signed payload from the given payload

**Arguments**:

- `mint_request`: Payload to sign

**Returns**:

Signed payload

<a id="core.classes.erc_20_signature_minting.ERC20SignatureMinting.generate_batch"></a>

#### generate\_batch

```python
def generate_batch(
        payloads_to_sign: List[PayloadToSign20]) -> List[SignedPayload20]
```

Generate a batch of signed payloads from the given payloads

**Arguments**:

- `payloads_to_sign`: Payloads to sign

**Returns**:

Signed payloads

