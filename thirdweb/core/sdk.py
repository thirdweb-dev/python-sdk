from .classes.provider_handler import ProviderHandler
from eth_account.account import LocalAccount
from typing import Any, Dict, Optional
from web3 import Web3

from thirdweb.types.sdk import SDKOptions


class ThirdwebSDK(ProviderHandler):
    __contract_cache: Dict[str, Any] = {}

    def __init__(
        self,
        provider: Web3,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        super().__init__(provider, signer, options)

    def get_nft_collection(self, address: str):
        pass

    def get_edition(self):
        pass

    def get_token(self):
        pass

    def update_provider(self, provider: Web3):
        super().update_provider(provider)

        for contract in self.__contract_cache.values():
            contract.update_provider(provider)
