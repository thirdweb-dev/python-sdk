import os
import unittest

from thirdweb import MintArg, ThirdwebSdk, SdkOptions


class TestStorage(unittest.TestCase):
    def test_storage(self):
        sdk = ThirdwebSdk(SdkOptions(
            private_key=os.environ['PKEY']
        ), "https://rpc-mumbai.maticvigil.com")

        nft_module = sdk.get_nft_module(
            "0xEeD541b524Ae738c48211Be91EB81E97739A0A29")

        # mint by uploading a file
        with open(file='tests/test.png', mode='rb') as f:
            content = f.read()
            module = nft_module.mint(MintArg(name="example",
                                             description="example nft!", image=content, properties={}))
            self.assertTrue(module.image.startswith(
                "ipfs://"), "Image files are expected to be uploaded when set in the image property")

        # mint by providing a string
        actual_image = "ipfs://QmYWi4mkEjsL6MYoS8z2ZWPAhyDPNjPQ2pqg8MGEM1CaeQ"
        module = nft_module.mint(MintArg(name="example", description="example nft!",
                                         image=actual_image, properties={}))
        self.assertEqual(module.image, actual_image,
                         "String image properties should be uploaded as-is")


if __name__ == '__main__':
    unittest.main()
