from eth_account import Account
from thirdweb.abi.thirdweb_contract import ThirdwebContract
from thirdweb.common.feature_detection import fetch_contract_metadata
from thirdweb.constants.addresses import get_contract_address_by_chain_id
from thirdweb.constants.urls import get_provider_for_network
from thirdweb.contracts import Marketplace
from thirdweb.contracts.custom import CustomContract
from thirdweb.contracts.edition_drop import EditionDrop
from thirdweb.contracts.nft_drop import NFTDrop
from thirdweb.core.classes.contract_deployer import ContractDeployer
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.classes.provider_handler import ProviderHandler
from thirdweb.contracts import Token, Edition, NFTCollection

from eth_account.account import LocalAccount
from typing import Dict, Optional, Type, Union, cast
from web3 import Web3

from thirdweb.types.sdk import SDKOptions


class ThirdwebSDK(ProviderHandler):
    """
    The main entry point for the Thirdweb SDK.
    """

    __contract_cache: Dict[
        str, Union[NFTCollection, Edition, Token, Marketplace, NFTDrop, EditionDrop]
    ] = {}
    storage: IpfsStorage

    deployer: ContractDeployer

    @staticmethod
    def from_private_key(
        private_key: str,
        network: str,
        options: SDKOptions = SDKOptions(),
    ) -> "ThirdwebSDK":
        signer = Account.from_key(private_key)
        sdk = ThirdwebSDK(network, signer, options)
        return sdk

    def __init__(
        self,
        network: str,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
        storage: IpfsStorage = IpfsStorage(),
    ):
        """
        Initialize the thirdweb SDK.

        :param provider: web3 provider instance to use for getting on-chain data
        :param signer: signer to use for sending transactions
        :param options: optional SDK configuration options
        :param storage: optional IPFS storage instance to use for storing data
        """

        provider = get_provider_for_network(network)
        super().__init__(provider, signer, options)
        self.storage = storage
        self.deployer = ContractDeployer(provider, signer, options, storage)

    def get_nft_collection(self, address: str) -> NFTCollection:
        """
        Returns an NFT Collection contract SDK instance

        :param address: address of the NFT Collection contract
        :returns: NFT Collection contract SDK instance
        """

        return cast(NFTCollection, self._get_contract(address, NFTCollection))

    def get_edition(self, address: str) -> Edition:
        """
        Returns an Edition contract SDK instance

        :param address: address of the Edition contract
        :returns: Edition contract SDK instance
        """

        return cast(Edition, self._get_contract(address, Edition))

    def get_token(self, address: str) -> Token:
        """
        Returns a Token contract SDK instance

        :param address: address of the Token contract
        :returns: Token contract SDK instance
        """

        return cast(Token, self._get_contract(address, Token))

    def get_marketplace(self, address: str) -> Marketplace:
        """
        Returns a Marketplace contract SDK instance

        :param address: address of the Marketplace contract
        :returns: Marketplace contract SDK instance
        """

        return cast(Marketplace, self._get_contract(address, Marketplace))

    def get_nft_drop(self, address: str) -> NFTDrop:
        """
        Returns an NFT Drop contract SDK instance

        :param address: address of the NFT Drop contract
        :returns: NFT Drop contract SDK instance
        """

        return cast(NFTDrop, self._get_contract(address, NFTDrop))

    def get_edition_drop(self, address: str) -> EditionDrop:
        """
        Returns an Edition Drop contract SDK instance

        :param address: address of the Edition Drop contract
        :returns: Edition Drop contract SDK instance
        """

        return cast(EditionDrop, self._get_contract(address, EditionDrop))

    def update_provider(self, provider: Web3):
        """
        Update the provider instance used by the SDK.

        :param provider: web3 provider instance to use for getting on-chain data
        """

        super().update_provider(provider)

        for contract in self.__contract_cache.values():
            contract.on_provider_updated(provider)

    def update_signer(self, signer: Optional[LocalAccount] = None):
        """
        Update the signer instance used by the SDK.

        :param signer: signer to use for sending transactions
        """

        super().update_signer(signer)

        for contract in self.__contract_cache.values():
            contract.on_signer_updated(signer)

    def _get_contract(
        self,
        address: str,
        contract_type: Union[
            Type[NFTCollection],
            Type[Edition],
            Type[Token],
            Type[Marketplace],
            Type[NFTDrop],
            Type[EditionDrop],
        ],
    ) -> Union[NFTCollection, Edition, Token, Marketplace, NFTDrop, EditionDrop]:
        if address in self.__contract_cache:
            return self.__contract_cache[address]

        contract = contract_type(
            self.get_provider(),
            address,
            self.storage,
            self.get_signer(),
            self.get_options(),
        )

        self.__contract_cache[address] = contract
        return contract
