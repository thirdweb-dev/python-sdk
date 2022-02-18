# Examples

### Generating a dynamic NFT that can be minted by anyone for 24h

```python
# get your NFT Module
nft_module = sdk.get_nft_module("0x....")

# Generate a dynamic NFT and sign it with the connected wallet
# This is generally done on the server side
sig = nft_module.generate_signature(NewSignaturePayload(
    metadata={"name": "Cool NFT", "description": "My cool NFT description"},
    to=ZeroAddress, # will be minted to a specific address or ZeroAddress for whoever mints it first 
    mint_start_time_epoch_seconds=math.floor(time.time()), # can minted anytime from now
    mint_end_time_epoch_seconds=math.floor(time.time()) + (60 * 60 * 24), # to 24h from now
))

# Now anyone can mint the generated NFT as long as they have the correct signature
minted = nft_module.mint_with_signature(req=sig.payload, signature=sig.signature)
```