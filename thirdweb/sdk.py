from functools import wraps
from typing import Optional

from eth_account.account import Account, LocalAccount
from thirdweb_web3 import HTTPProvider, Web3
from zero_ex.contract_wrappers import TxParams

from .errors import NoSignerException
from .modules.bundle import BundleModule
from .modules.collection import CollectionModule
from .modules.currency import CurrencyModule
from .modules.market import MarketModule
from .modules.nft import NftModule
from .modules.nft_v1 import NftModule as NftModuleV1
from .modules.pack import PackModule
from .options import SdkOptions
from .storage import IpfsStorage


def set_default_account(func):
    '''
    Sets the default account on all modules
    '''

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.client.eth.defaultAccount = args[0] if self.signer_address == "" else self.signer_address
        return func(self, *args, **kwargs)
    return wrapper


class ThirdwebSdk(object):
    client: Web3
    options: SdkOptions

    __private_key: str
    signer_address: str = ""
    __current_account: Optional[LocalAccount]

    storage: IpfsStorage

    __currency_module: Optional[CurrencyModule]
    __nft_module: Optional[NftModule]
    __pack_module: Optional[PackModule]
    __bundle_module = Optional[BundleModule]
    __market_module: Optional[MarketModule]

    def __init__(self, options: SdkOptions, url: str):
        """
        Create instance of the ThirdwebSdk
        """
        self.__currency_module = None
        self.__nft_module = None
        self.__pack_module = None
        self.__bundle_module = None
        self.__current_account = None
        self.__market_module = None

        self.options = options
        if self.options.private_key != "":
            self.set_private_key(self.options.private_key)

        self.storage = IpfsStorage(
            options.ipfs_gateway_url if options.ipfs_gateway_url
            else "https://ipfs.io/ipfs/")

        self.client = Web3(HTTPProvider(url))
        if not self.client.isConnected():
            raise Exception("Failed to connect to the web3 provider")

    def set_private_key(self, private_key=""):
        """
        Sets the Private Key used across the entire SDK. Calling this method
        will automatically reload the private key across all instantiated
        modules, which allows you to operate on behalf of multiple
        wallets by calling a single method.
        """
        if private_key == "" or private_key is None:
            raise NoSignerException()
        self.__current_account = Account.from_key(private_key)
        self.__private_key = "0x" + private_key.lstrip("0x")
        self.signer_address = self.__current_account.address

    @set_default_account
    def get_currency_module(self, address: str) -> CurrencyModule:
        """
        Returns an instance of the currency module
        """
        if self.__currency_module is not None and self.__currency_module.address == address:
            return self.__currency_module

        module = CurrencyModule(address, self.__get_client())
        self.__init_module(module)
        self.__currency_module = module
        return self.__currency_module

    @set_default_account
    def get_nft_module(self, address: str, is_v1: bool = False) -> NftModule:
        """
        Returns an instance of the nft module

        :param address: The address of the contract
        :param is_v1: Whether or not the module is a v1 module.
        """
        if self.__nft_module is not None and self.__nft_module.address == address:
            return self.__nft_module

        if is_v1:
            module = NftModuleV1(address, self.__get_client())
        else:
            module = NftModule(address, self.__get_client())
        self.__init_module(module)
        self.__nft_module = module
        return self.__nft_module

    @set_default_account
    def get_pack_module(self, address: str) -> PackModule:
        """
        Returns an instance of the pack module
        """
        if self.__pack_module is not None and self.__pack_module.address == address:
            return self.__pack_module

        module = PackModule(address, self.__get_client())
        self.__init_module(module)
        self.__pack_module = module
        return self.__pack_module

    @set_default_account
    def get_market_module(self, address: str) -> MarketModule:
        """
        Returns an instance of the market module
        """
        if self.__market_module is not None and self.__market_module.address == address:
            return self.__market_module

        module = MarketModule(address, self.__get_client())
        self.__init_module(module)
        self.__market_module = module
        return self.__market_module

    @set_default_account
    def get_collection_module(self, address: str) -> CollectionModule:
        """
        COLLECTION MODULE AND ALL ITS CLASSES WILL BE DEPRECATED SOON. USE BUNDLE MODULE INSTEAD.
        """
        return self.get_bundle_module(address)

    def get_bundle_module(self, address: str) -> BundleModule:

        if self.__bundle_module is not None and self.__bundle_module.address == address:
            return self.__bundle_module

        module = BundleModule(address, self.__get_client())
        self.__init_module(module)
        self.__bundle_module = module
        return self.__bundle_module

    def __get_client(self) -> Web3:
        return self.client

    def __get_storage(self) -> IpfsStorage:
        return self.storage

    def __get_signer_address(self) -> str:
        if self.signer_address == "":
            raise NoSignerException()
        return self.signer_address

    def __get_private_key(self) -> str:
        return self.__private_key

    def __get_transact_ops(self) -> TxParams:
        return TxParams(
            from_=self.__get_signer_address(),
            gas_price=self.client.toWei(
                self.options.max_gas_price_in_gwei, 'gwei')
        )

    def __get_account(self) -> Optional[LocalAccount]:
        return self.__current_account

    def __get_options(self) -> Optional[SdkOptions]:
        return self.options

    def __init_module(self, module):
        module.get_account = self.__get_account
        module.get_options = self.__get_options
        module.get_client = self.__get_client
        module.get_storage = self.__get_storage
        module.get_signer_address = self.__get_signer_address
        module.get_private_key = self.__get_private_key
        module.get_transact_opts = self.__get_transact_ops


NftlabsSdk = ThirdwebSdk
