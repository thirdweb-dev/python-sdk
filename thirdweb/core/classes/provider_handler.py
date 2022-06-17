import re
from typing import Optional
from pyee.base import EventEmitter
from thirdweb.constants.chains import ChainId
from thirdweb.constants.rpc import CHAIN_ID_TO_RPC_URL
from thirdweb.types.sdk import SDKOptions
from eth_account.account import LocalAccount
from web3.middleware import geth_poa_middleware
from web3 import Web3


class ProviderHandler(EventEmitter):
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

        super().__init__()

        self._update_provider(provider)
        self._update_signer(signer)
        self.__options = options

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

    def _update_provider(self, provider: Web3):
        """
        Update the active provider.

        :param provider: web3 provider instance to use
        """

        self.__provider = provider

    def _update_signer(self, signer: Optional[LocalAccount] = None):
        """
        Update the active signer.

        :param signer: optional account to use for signing transactions
        """

        self.__signer = signer

        if signer is not None:
            provider = self.get_provider()
            provider.eth.default_account = signer.address

    def _get_default_provider(self, chain_id: ChainId) -> Optional[Web3]:
        """
        Get a default provider for the given chain id using default public RPC URLs.

        :param chain_id: the chain id to get the default provider for
        """

        if chain_id in CHAIN_ID_TO_RPC_URL:
            return Web3(Web3.HTTPProvider(CHAIN_ID_TO_RPC_URL[chain_id]))
        return None
