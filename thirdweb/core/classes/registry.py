from typing import List, Optional, cast
from eth_utils import is_address
from web3 import Web3
from eth_account.account import LocalAccount
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.abi import TWRegistry
from thirdweb.types.sdk import SDKOptions


class ContractRegistry(ContractWrapper):
    def __init__(
        self,
        registry_address: str,
        provider: Web3,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        abi = TWRegistry(provider, registry_address)
        super().__init__(abi, provider, signer, options)

    def get_contract_addresses(self, address: str) -> List[str]:
        """
        Get all the contract addresses registered for a given address.

        :param address: address to get the contract addresses for
        :returns: list of contract addresses
        """

        contract_addresses = self._get_abi().get_all.call(address)
        return [
            address
            for address in contract_addresses
            if address != ZERO_ADDRESS and is_address(address)
        ]

    def _get_abi(self) -> TWRegistry:
        return cast(TWRegistry, self._contract_abi)
