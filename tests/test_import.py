import unittest

from nftlabs import NftlabsSdk, SdkOptions


class TestSum(unittest.TestCase):
    def test_init_sdk(self):
        """
        Test that tries to instatiate the SDK
        """
        sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")

if __name__ == '__main__':
    unittest.main()