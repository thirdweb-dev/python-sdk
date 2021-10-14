import os

import nftlabs.options
from nftlabs import NftlabsSdk

options = nftlabs.options.SdkOptions()
sdk = NftlabsSdk(options, "https://rpc-mumbai.maticvigil.com")

currency_module = sdk.get_currency_module("0xd75807e8D122A4DDF3bCCBB67fC33D8d78955726")

print(currency_module.total_supply())

print(currency_module.get())

sdk.set_private_key(os.getenv("PKEY"))

nft_module = sdk.get_nft_module("0xbDfF8fb43688fB4D2184DF8029A7238ac1413A24")
print(nft_module.total_supply())

nft_module.mint(name="Test")

