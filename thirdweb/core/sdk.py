from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.provider_handler import ProviderHandler
from thirdweb.contracts import Token, Edition, NFTCollection

from eth_account.account import LocalAccount
from typing import Any, Dict, Optional, Type, Union
from web3 import Web3

from thirdweb.types.sdk import SDKOptions


class ThirdwebSDK(ProviderHandler):
    __contract_cache: Dict[str, Union[NFTCollection, Edition, Token]] = {}

    def __init__(
        self,
        provider: Web3,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        super().__init__(provider, signer, options)

    def get_nft_collection(self, address: str):
        return self.get_contract(address, NFTCollection)

    def get_edition(self, address: str):
        return self.get_contract(address, Edition)

    def get_token(self, address: str) -> Token:
        return self.get_contract(address, Token)

    def get_contract(
        self,
        address: str,
        contract_type: Union[Type[NFTCollection], Type[Edition], Type[Token]],
    ) -> Any:
        if address in self.__contract_cache:
            return self.__contract_cache[address]

        contract = contract_type(
            self.__provider, address, self.__signer, self.__options
        )

        self.__contract_cache[address] = contract
        return contract

    def update_provider(self, provider: Web3):
        super().update_provider(provider)

        for contract in self.__contract_cache.values():
            contract.on_provider_updated(provider)

    def update_signer(self, signer: Optional[LocalAccount]):
        super().update_signer(signer)

        for contract in self.__contract_cache.values():
            contract.on_signer_updated(signer)
