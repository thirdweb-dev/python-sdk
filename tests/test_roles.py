import unittest
from os import environ

from thirdweb import SdkOptions, ThirdwebSdk
from thirdweb.types.role import Role

from .constants import (TEST_BUNDLE_CONTRACT_ADDRESS,
                        TEST_COMPANION_WALLET_ADDRESS,
                        TEST_CURRENCY_CONTRACT_ADDRESS,
                        TEST_MARKET_CONTRACT_ADDRESS,
                        TEST_NFT_CONTRACT_ADDRESS, TEST_PACK_CONTRACT_ADDRESS)


class TestRoles(unittest.TestCase):
    def test_grant_and_revoke_role(self):
        """
        Test that tries to instantiate the NFT module
        """
        sdk = ThirdwebSdk(SdkOptions(
            private_key=environ['PKEY']
        ), "https://rpc-mumbai.maticvigil.com")

        modules = [
            sdk.get_nft_module(
                TEST_NFT_CONTRACT_ADDRESS),
            sdk.get_market_module(
                TEST_MARKET_CONTRACT_ADDRESS),
            sdk.get_bundle_module(
                TEST_BUNDLE_CONTRACT_ADDRESS),
            sdk.get_pack_module(
                TEST_PACK_CONTRACT_ADDRESS),
            sdk.get_currency_module(
                TEST_CURRENCY_CONTRACT_ADDRESS),
        ]

        for module in modules:
            address_to_add = TEST_COMPANION_WALLET_ADDRESS
            module.grant_role(Role.admin, address_to_add)

            members = module.get_role_members(Role.admin)
            if address_to_add not in members:
                self.fail("Failed to add role to member")

            module.revoke_role(Role.admin, address_to_add)
            members = module.get_role_members(Role.admin)
            if address_to_add in members:
                self.fail("Failed to remove role from member")


if __name__ == '__main__':
    unittest.main()
