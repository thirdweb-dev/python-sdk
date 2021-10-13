import asyncio

import nftlabs.options
from nftlabs import NftlabsSdk

options = nftlabs.options.SdkOptions()
sdk = NftlabsSdk(options, "https://rpc-mumbai.maticvigil.com")

currency_module = sdk.get_currency_module("0xd75807e8D122A4DDF3bCCBB67fC33D8d78955726")

print(currency_module.total_supply())


print(currency_module.get())
