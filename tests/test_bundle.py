import unittest
from os import environ

from dataclasses_json.api import A

from thirdweb import SdkOptions, ThirdwebSdk,  CreateBundleArg, Metadata
from thirdweb.modules.bundle import BundleModule
from thirdweb.modules.collection import CollectionModule
from thirdweb.types.collection import CreateCollectionArg
from typing import Union

class TestRoles(unittest.TestCase):
    sdk: ThirdwebSdk
    module: BundleModule
    old_module: CollectionModule

    @classmethod
    def setUpClass(self):
         self.sdk = ThirdwebSdk(SdkOptions(
             private_key=environ['PKEY']
         ), "https://rpc-mumbai.maticvigil.com")
         contract_address = "0x888bcEddB2af1537437420B320D6D4d60A358Cc0"
         self.module = self.sdk.get_bundle_module(contract_address)
         self.old_module = self.sdk.get_collection_module(contract_address)
  
 
    def test_bundle_get_all(self):
        """
        Test that tries to instantiate the NFT module
        """
        result = self.module.get_all()
        self.assertGreater(len(result), 0, "There should be at least 1 token in the contract")

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
        result = self.module.create_with_token("0x71C37c568F5dB15dD0dD5930a3EFF23958722690", 20, {})

    
    def test_bundle_create_with_nft(self):
        """
        Test that tries to instantiate the Bundle  module
        """
        result = self.module.create_with_nft("0xaA00E3Af449B32382BF3962A1F61bC2f5EC2a467", 1, {})



if __name__ == '__main__':
    unittest.main()
