import unittest

from nftlabs import NftlabsSdk, SdkOptions


class TestSum(unittest.TestCase):
    def test_init_sdk(self):
        """
        Test that tries to instantiate the SDK
        """
        sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")

    def test_init_nft_module(self):
        """
        Test that tries to instantiate the NFT module
        """
        sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")
        nft_module = sdk.get_nft_module(
            "0xEeD541b524Ae738c48211Be91EB81E97739A0A29")

    def test_init_currency_module(self):
        """
        Test that tries to instantiate the Currency module
        """
        sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")
        currency_module = sdk.get_currency_module(
            "0xF18FEb8b2F58691d67C98dB98B360840df340e74")

    def test_init_bundle_module(self):
        """
        Test that tries to instantiate the Bundle module
        """
        sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")
        bundle_module = sdk.get_bundle_module(
            "0x6Da734b14e4CE604f1e18efb7E7f7ef022e96616")

    def test_init_pack_module(self):
        """
        Test that tries to instantiate the Pack module
        """
        sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")
        pack_module = sdk.get_pack_module(
            "0x54ec360704b2e9E4e6499a732b78094D6d78e37B")

    def test_init_marketplace_module(self):
        """
        Test that tries to instantiate the Marketplace module
        """
        sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")
        pack_module = sdk.get_market_module(
            "0xD3920A1fd0fB09EA00F8ce56d0c655CF7a50428C")


if __name__ == '__main__':
    unittest.main()
