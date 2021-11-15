import io
import os
import unittest

from nftlabs import MintArg, NftlabsSdk, SdkOptions
from nftlabs.storage import ipfs_storage


class TestStorage(unittest.TestCase):
    def test_storage(self):
        sdk = NftlabsSdk(SdkOptions(
            private_key=os.environ['PKEY']
        ), "https://rpc-mumbai.maticvigil.com")

        nft_module = sdk.get_nft_module(
            "0xEeD541b524Ae738c48211Be91EB81E97739A0A29")

        # mint by uploading a file
        with open(file='test.png', mode='rb') as f:
            print(nft_module.mint(MintArg(name="example",
                  description="example nft!", image=f, properties={})))

        # mint by providing a string
        print(nft_module.mint(MintArg(name="example", description="example nft!",
              image="ipfs://QmYWi4mkEjsL6MYoS8z2ZWPAhyDPNjPQ2pqg8MGEM1CaeQ", properties={})))


if __name__ == '__main__':
    unittest.main()
