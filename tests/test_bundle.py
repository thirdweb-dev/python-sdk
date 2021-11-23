import unittest
from os import environ

from thirdweb import SdkOptions, ThirdwebSdk
from thirdweb.modules.bundle import BundleModule
from thirdweb.modules.currency import CurrencyModule
from thirdweb.modules.nft import NftModule

from .constants import (TEST_BUNDLE_CONTRACT_ADDRESS,
                        TEST_CURRENCY_CONTRACT_ADDRESS,
                        TEST_NFT_CONTRACT_ADDRESS)


class TestRoles(unittest.TestCase):
    sdk: ThirdwebSdk
    bundle_module: BundleModule
    nft_module: NftModule
    currency_module: CurrencyModule

    @classmethod
    def setUpClass(self):
        self.sdk = ThirdwebSdk(SdkOptions(
            private_key=environ['PKEY']
        ), "https://rpc-mumbai.maticvigil.com")
        self.bundle_module = self.sdk.get_bundle_module(
            TEST_BUNDLE_CONTRACT_ADDRESS)
        self.nft_module = self.sdk.get_nft_module(TEST_NFT_CONTRACT_ADDRESS)
        self.currency_module = self.sdk.get_currency_module(
            TEST_CURRENCY_CONTRACT_ADDRESS)

    def test_bundle_get_all(self):
        """
        Test that tries to instantiate the NFT module
        """
        result = self.bundle_module.get_all()
        self.assertGreater(
            len(result), 0, "There should be at least 1 token in the contract")

    def test_collection_get_all(self):
        """
        Test that tries to instantiate the Collection module
        """
        result = self.bundle_module.get_all()
        self.assertGreater(
            len(result), 0, "There should be at least 1 token in the contract")

    def test_bundle_create(self):
        """
        Test that tries to instantiate the Bundle  module
        """
        result = self.bundle_module.create({"name": "test"})
        self.assertIsNotNone(result, "The resulting bundle should not be None")

    # def test_bundle_create_with_token(self):
    #     """
    #     Test that tries to instantiate the Bundle  module
    #     """
    #     self.currency_module.mint(20)
    #     result = self.bundle_module.create_with_token(
    #         TEST_CURRENCY_CONTRACT_ADDRESS, 20, {})
    #     self.assertIsNotNone(result, "The resulting bundle should not be None")
    #     self.assertEqual(result, 20)

    def test_create(self):
        """
        Call create method to mint token with 0 supply
        """
        created = self.bundle_module.create(metadata={"name": "test"})
        self.assertEqual(created.metadata.name, "test")
        self.assertEqual(created.supply, 0)

    # def test_bundle_create_with_nft(self):
    #     """
    #     Test that tries to instantiate the Bundle  module
    #     """
    #     result = self.module.create_with_nft(TEST_NFT_CONTRACT_ADDRESS, 1, {})


if __name__ == '__main__':
    unittest.main()
