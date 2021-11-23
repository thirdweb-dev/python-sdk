import unittest
from os import environ

from thirdweb import SdkOptions, ThirdwebSdk
from thirdweb.modules.bundle import BundleModule
from thirdweb.modules.collection import CollectionModule

from .constants import (TEST_BUNDLE_CONTRACT_ADDRESS,
                        TEST_CURRENCY_CONTRACT_ADDRESS,
                        TEST_NFT_CONTRACT_ADDRESS)


class TestRoles(unittest.TestCase):
    sdk: ThirdwebSdk
    module: BundleModule
    old_module: CollectionModule

    @classmethod
    def setUpClass(self):
        self.sdk = ThirdwebSdk(SdkOptions(
            private_key=environ['PKEY']
        ), "https://rpc-mumbai.maticvigil.com")
        contract_address = TEST_BUNDLE_CONTRACT_ADDRESS
        self.module = self.sdk.get_bundle_module(contract_address)
        self.old_module = self.sdk.get_collection_module(contract_address)

    def test_bundle_get_all(self):
        """
        Test that tries to instantiate the NFT module
        """
        result = self.module.get_all()
        self.assertGreater(
            len(result), 0, "There should be at least 1 token in the contract")

    def test_collection_get_all(self):
        """
        Test that tries to instantiate the Collection module
        """
        result = self.old_module.get_all()
        self.assertGreater(
            len(result), 0, "There should be at least 1 token in the contract")

    def test_bundle_create(self):
        """
        Test that tries to instantiate the Bundle  module
        """
        result = self.module.create({"name": "test"})
        self.assertIsNotNone(result, "The result should not be None")

    def test_bundle_create_with_token(self):
        """
        Test that tries to instantiate the Bundle  module
        """
        result = self.module.create_with_token(
            TEST_CURRENCY_CONTRACT_ADDRESS, 20, {})

    # def test_bundle_create_with_nft(self):
    #     """
    #     Test that tries to instantiate the Bundle  module
    #     """
    #     result = self.module.create_with_nft(TEST_NFT_CONTRACT_ADDRESS, 1, {})


if __name__ == '__main__':
    unittest.main()
