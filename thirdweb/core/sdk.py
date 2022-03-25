from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.classes.provider_handler import ProviderHandler
from thirdweb.contracts import Token, Edition, NFTCollection

from eth_account.account import LocalAccount
from typing import Any, Dict, Optional, Type, Union, cast
from web3 import Web3

from thirdweb.types.sdk import SDKOptions


class ThirdwebSDK(ProviderHandler):
    __contract_cache: Dict[str, Union[NFTCollection, Edition, Token]] = {}
    __storage: IpfsStorage

    def __init__(
        self,
        provider: Web3,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
        storage: IpfsStorage = IpfsStorage(),
    ):
        super().__init__(provider, signer, options)
        self.__storage = storage

    def get_nft_collection(self, address: str) -> NFTCollection:
        return cast(NFTCollection, self.get_contract(address, NFTCollection))

    def get_edition(self, address: str) -> Edition:
        return cast(Edition, self.get_contract(address, Edition))

    def get_token(self, address: str) -> Token:
        return cast(Token, self.get_contract(address, Token))

    def get_contract(
        self,
        address: str,
        contract_type: Union[Type[NFTCollection], Type[Edition], Type[Token]],
    ) -> Union[NFTCollection, Edition, Token]:
        if address in self.__contract_cache:
            return self.__contract_cache[address]

        contract = contract_type(
            self.get_provider(),
            address,
            self.__storage,
            self.get_signer(),
            self.get_options(),
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
