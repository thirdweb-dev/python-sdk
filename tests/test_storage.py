import unittest
from nftlabs import NftlabsSdk, SdkOptions, MintArg
from nftlabs.storage import ipfs_storage
from test_constants import (TEST_NFT_CONTRACT_ADDRESS)
import os, io

class TestStorage(unittest.TestCase):
    def storage(self):
        sdk = NftlabsSdk(SdkOptions(
            private_key=environ['PKEY']
        ), "https://rpc-mumbai.maticvigil.com")

        nft_module = sdk.get_nft_module(
            "0xe76Fc319fD15a92328bAE16D3320F6ceB20759C6")

        # mint by uploading a file
        with open(file='test.png', mode='rb') as f:
            print(nft_module.mint(MintArg(name="example",
                  description="example nft!", image=f, properties={})))

        # mint by providing a string
        print(nft_module.mint(MintArg(name="example", description="example nft!",
              image="ipfs://QmYWi4mkEjsL6MYoS8z2ZWPAhyDPNjPQ2pqg8MGEM1CaeQ", properties={})))


if __name__ == '__main__':
    unittest.main()
