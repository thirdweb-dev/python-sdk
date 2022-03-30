import re
from typing import Optional

from thirdweb.constants.chains import ChainId
from thirdweb.constants.rpc import CHAIN_ID_TO_RPC_URL
from thirdweb.types.sdk import SDKOptions
from eth_account.account import LocalAccount
from web3.middleware import geth_poa_middleware
from web3 import Web3


class ProviderHandler(object):
    """
    The provider handler is responsible for managing the connected provider and signer
    for any class including the read-only provider.
    """

    __provider: Web3
    __signer: Optional[LocalAccount]
    __options: SDKOptions

    def __init__(
        self,
        provider: Web3,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        """
        Initialize the provider handler.

        :param provider: web3 provider instance to use
        :param signer: optional account to use for signing transactions
        :param options: optional SDKOptions instance to specify read-only RPC URL and gas settings
        """

        self.update_provider(provider)
        self.update_signer(signer)
        self.__options = options

    def update_provider(self, provider: Web3):
        """
        Update the active provider.

        :param provider: web3 provider instance to use
        """

        self.__provider = provider

        self.__provider.middleware_onion.clear()
        self.__provider.middleware_onion.inject(geth_poa_middleware, layer=0)

    def update_signer(self, signer: Optional[LocalAccount] = None):
        """
        Update the active signer.

        :param signer: optional account to use for signing transactions
        """

        self.__signer = signer

        if signer is not None:
            provider = self.get_provider()
            provider.eth.default_account = signer.address

    def is_read_only(self):
        """
        Check if there is no active signer.
        """

        return self.__signer != None

    def get_signer(self) -> Optional[LocalAccount]:
        """
        Get the active signer.

        :returns: the Account instance of the active signer, otherwise None
        """

        return self.__signer

    def get_provider(self) -> Web3:
        """
        Get the active provider.

        :returns: the Web3 instance of the active provider
        """

        return self.__provider

    def get_options(self) -> SDKOptions:
        return self.__options

    def __get_read_only_provider(self) -> Optional[Web3]:
        """
        Get a read only provider based on the read-only settings and specified provider.
        """

        # First check if there is a read-only settings instance
        if self.__options.read_only_settings is not None:
            match = re.match(
                r"^(ws|http)s?:\/\/", self.__options.read_only_settings.rpc_url
            )

            # Check if the read only RPC URL is a valid URL (websocket or http/https)
            if match is not None:
                if "https://" in match.group() or "http://" in match.group():
                    return Web3(
                        Web3.HTTPProvider(self.__options.read_only_settings.rpc_url)
                    )
                if "ws://" in match.group():
                    return Web3(
                        Web3.WebsocketProvider(
                            self.__options.read_only_settings.rpc_url
                        )
                    )

            # Otherwise try to use a default provider using default public RPC URLs using the specified chain_id
            if self.__options.read_only_settings.chain_id is not None:
                default_provider = self.__get_default_provider(
                    self.__options.read_only_settings.chain_id
                )
                if default_provider != None:
                    return default_provider

        # Finally, if nothing else works, use the connected providers chain id to get a default provider
        provider = self.get_provider()
        return self.__get_default_provider(ChainId(provider.eth.chain_id))

    def __get_default_provider(self, chain_id: ChainId) -> Optional[Web3]:
        """
        Get a default provider for the given chain id using default public RPC URLs.

        :param chain_id: the chain id to get the default provider for
        """

        if chain_id in CHAIN_ID_TO_RPC_URL:
            return Web3(Web3.HTTPProvider(CHAIN_ID_TO_RPC_URL[chain_id]))
        return None
