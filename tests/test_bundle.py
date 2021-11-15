import unittest
from os import environ

from dataclasses_json.api import A

from thirdweb import SdkOptions, ThirdwebSdk
from thirdweb.modules.bundle import BundleModule
from thirdweb.modules.collection import CollectionModule
from thirdweb.types.collection import CreateCollectionArg


class TestRoles(unittest.TestCase):
    sdk: ThirdwebSdk
    module: BundleModule
    old_module: CollectionModule

    @classmethod
    def setUpClass(self):
        self.sdk = ThirdwebSdk(SdkOptions(
            private_key=environ['PKEY']
        ), "https://rpc-mumbai.maticvigil.com")
        self.module = self.sdk.get_bundle_module(
            "0x5CF412451f4Cef34293604048238bd18D2BD1e71")
        self.old_module = self.sdk.get_collection_module(
            "0x5CF412451f4Cef34293604048238bd18D2BD1e71")

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

    # def test_collection_mint(self):
    #     """
    #     Test that tries to instantiate the Collection module
    #     """
    #     result = self.old_module.create_and_mint(meta_with_supply=CreateCollectionArg(
    #         metadata={"name": "Test"},
    #         supply=10,
    #     ))
    #     print("Minted", result)
    #     result = self.module.create_and_mint(meta_with_supply=CreateCollectionArg(
    #         metadata={"name": "Test"},
    #         supply=10,
    #     ))


if __name__ == '__main__':
    unittest.main()
