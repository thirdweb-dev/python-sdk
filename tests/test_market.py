import unittest

from thirdweb import ThirdwebSdk, SdkOptions

from .constants import (TEST_BUNDLE_CONTRACT_ADDRESS,
                        TEST_MARKET_CONTRACT_ADDRESS,
                        TEST_NFT_CONTRACT_ADDRESS)


class TestMarket(unittest.TestCase):
    def test_init_marketplace_module(self):
        """
        Test that tries to instantiate the Marketplace module
        """
        sdk = ThirdwebSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")
        market_module = sdk.get_market_module(TEST_MARKET_CONTRACT_ADDRESS)

        self.assertFalse(market_module.is_erc721(
            TEST_BUNDLE_CONTRACT_ADDRESS), "A bundle is not a 721 contract")
        self.assertTrue(market_module.is_erc721(
            TEST_NFT_CONTRACT_ADDRESS), "A nft contract is a 721 contract")

        self.assertTrue(market_module.is_erc1155(
            TEST_BUNDLE_CONTRACT_ADDRESS), "A bundle is a 1155 contract")
        self.assertFalse(market_module.is_erc1155(
            TEST_NFT_CONTRACT_ADDRESS), "A nft contract is not a 1155 contract")
