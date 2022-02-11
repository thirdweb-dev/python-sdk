import os
import time
import math

import thirdweb.options
from thirdweb import ThirdwebSdk
from thirdweb.types.nft import NewSignaturePayload


options = thirdweb.options.SdkOptions()
sdk = ThirdwebSdk(options, "https://rpc-mumbai.maticvigil.com")
# sdk = NftlabsSdk(options, "https://polygon-rpc.com")
sdk.set_private_key(os.getenv("PKEY"))
#
# currency_module = sdk.get_currency_module("0xd75807e8D122A4DDF3bCCBB67fC33D8d78955726")
#
# pprint(currency_module.get_value(1))
# pprint(currency_module.get_value(100000000000000000))
# pprint(currency_module.get_value(1000000000000000000))
# pprint(currency_module.get_value(10000000000000000000))
#
# pprint(currency_module.total_supply())
# pprint(currency_module.get())
# pprint(currency_module.get_all_role_members())
#

# nft_module = sdk.get_nft_module("0x718526F74cD27bAc8ae256D2B94dB4a8c640C283")
# print(nft_module.total_supply())

# minted_nft = nft_module.mint(arg=MintArg(name="Test 123", description="Some description"))
# print(minted_nft)

# for nft in nft_module.get_all():
#     print(nft)

# nft_module.transfer("0x26ec212ba1854F1a0c287e5B8E3e5463122EFb47", 1)
# print(nft_module.get_owned("0x26ec212ba1854F1a0c287e5B8E3e5463122EFb47"))

# minted_nfts = nft_module.mint_batch(args=[
#     MintArg(name="Test first", description="Some description batch"),
#     MintArg(name="Test second", description="Some description batch"),
# ])
# print(minted_nfts)

# nft_module.grant_role(Role.admin, "0x26ec212ba1854F1a0c287e5B8E3e5463122EFb47")

nft_module = sdk.get_nft_module("0x3C977f3401580Ad0939A05631030545663a2eF3c")

sig = nft_module.generate_signature(NewSignaturePayload(
    metadata={"name": "Test 123", "description": "Some description"},
    to="0x0000000000000000000000000000000000000000",
    mint_start_time_epoch_seconds=0,
    mint_end_time_epoch_seconds=math.floor(time.time()) + (60 * 24 * 365),
))

print(sig)

minted = nft_module.mint_with_signature(req=sig.payload, signature=sig.signature)
