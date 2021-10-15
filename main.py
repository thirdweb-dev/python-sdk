import os

import nftlabs.options
from nftlabs import NftlabsSdk
from nftlabs.modules.nft_types import MintArg
from nftlabs.types import Role

options = nftlabs.options.SdkOptions()
sdk = NftlabsSdk(options, "https://rpc-mumbai.maticvigil.com")

currency_module = sdk.get_currency_module("0xd75807e8D122A4DDF3bCCBB67fC33D8d78955726")

print(currency_module.total_supply())

print(currency_module.get())

sdk.set_private_key(os.getenv("PKEY"))

nft_module = sdk.get_nft_module("0xbDfF8fb43688fB4D2184DF8029A7238ac1413A24")
print(nft_module.total_supply())

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

nft_module.grant_role(Role.admin, "0x26ec212ba1854F1a0c287e5B8E3e5463122EFb47")

