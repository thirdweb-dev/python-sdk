from thirdweb import ThirdwebSdk, SdkOptions
from dotenv import load_dotenv
import os


#network = "https://polygon-rpc.com"
network = "https://rinkeby-light.eth.linkpool.io/"
sdk = ThirdwebSdk(SdkOptions(), network)

load_dotenv()
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

sdk.set_private_key(PRIVATE_KEY)

bundle_smart_contract_address = "0xC92702c53620DcA7B0d2898e361333957f547525"
#nft_module = sdk.get_

pack_contract = "0xEA9e245C4663AC7A82Df0329A1a480C4729adC52"
pack_module = sdk.get_pack_module(pack_contract)

# pack_module.create(CreatePackArg(
#     asset_contract_address= bundle_smart_contract_address,
#     metadata=('packme'),
#     assets= [AssetAmountPair(amount=1, token_id=1), AssetAmountPair(amount=1, token_id=0)],
#     rewards_per_open=1,
#     seconds_until_open_start=0,
# ))

pack_module.deposit_link(1)
print(pack_module.open_pack(1))
