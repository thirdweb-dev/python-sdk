import unittest

from nftlabs import NftlabsSdk, SdkOptions

from test_constants import (TEST_COLLECTION_CONTRACT_ADDRESS,
                            TEST_MARKET_CONTRACT_ADDRESS,
                            TEST_NFT_CONTRACT_ADDRESS)


class TestMarket(unittest.TestCase):
    def test_init_marketplace_module(self):
        """
        Test that tries to instantiate the Marketplace module
        """
        sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com")
        market_module = sdk.get_market_module(TEST_MARKET_CONTRACT_ADDRESS)

        self.assertFalse(market_module.is_erc721(
            TEST_COLLECTION_CONTRACT_ADDRESS), "A collection is not a 721 contract")
        self.assertTrue(market_module.is_erc721(
            TEST_NFT_CONTRACT_ADDRESS), "A nft contract is a 721 contract")

        self.assertTrue(market_module.is_erc1155(
            TEST_COLLECTION_CONTRACT_ADDRESS), "A collection is a 1155 contract")
        self.assertFalse(market_module.is_erc1155(
            TEST_NFT_CONTRACT_ADDRESS), "A nft contract is not a 1155 contract")
