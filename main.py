import os

import nftlabs.options
from nftlabs import NftlabsSdk
from pprint import pprint
from nftlabs.types.nft import MintArg
from nftlabs.types import Role

options = nftlabs.options.SdkOptions()
sdk = NftlabsSdk(options, "https://rpc-mumbai.maticvigil.com")
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

pack_module = sdk.get_pack_module("0x1E12bFfa725a6dC19530eccf059111524476EAc2")
print(pack_module.get_all_role_members())
