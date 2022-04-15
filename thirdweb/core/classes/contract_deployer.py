from typing import Any, Dict, Optional

from web3 import Web3
from eth_account.account import LocalAccount
from thirdweb.constants.addresses import get_contract_address_by_chain_id
from thirdweb.constants.chains import ChainId
from thirdweb.core.classes.factory import ContractFactory
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.classes.provider_handler import ProviderHandler
from thirdweb.core.classes.registry import ContractRegistry
from thirdweb.types.contract import ContractType
from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import (
    EditionDropContractMetadata,
    NFTDropContractMetadata,
    EditionContractMetadata,
    MarketplaceContractMetadata,
    NFTCollectionContractMetadata,
    TokenContractMetadata,
)


class ContractDeployer(ProviderHandler):
    __factory: ContractFactory
    __registry: ContractRegistry

    _storage: IpfsStorage

    def __init__(
        self,
        provider: Web3,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
        storage: IpfsStorage = IpfsStorage(),
    ):
        super().__init__(provider, signer, options)
        self._storage = storage

    def deploy_nft_collection(self, metadata: NFTCollectionContractMetadata) -> str:
        """
        Deploy an NFT Collection contract.
        """

        return self._deploy_contract(ContractType.NFT_COLLECTION, metadata.to_json())

    def deploy_edition(self, metadata: EditionContractMetadata) -> str:
        """
        Deploy an Edition contract
        """

        return self._deploy_contract(ContractType.EDITION, metadata.to_json())

    def deploy_token(self, metadata: TokenContractMetadata) -> str:
        """
        Deploy a Token contract
        """

        return self._deploy_contract(ContractType.TOKEN, metadata.to_json())

    def deploy_marketplace(self, metadata: MarketplaceContractMetadata) -> str:
        """
        Deploy a Marketplace contract
        """

        return self._deploy_contract(ContractType.MARKETPLACE, metadata.to_json())

    def deploy_nft_drop(self, metadata: NFTDropContractMetadata) -> str:
        """
        Deploy an NFT Drop contract
        """

        return self._deploy_contract(ContractType.NFT_DROP, metadata.to_json())

    def deploy_edition_drop(self, metadata: EditionDropContractMetadata) -> str:
        """
        Deploy an Edition Drop contract
        """

        return self._deploy_contract(ContractType.EDITION_DROP, metadata.to_json())

    def _deploy_contract(
        self, contract_type: ContractType, contract_metadata: Dict[str, Any]
    ) -> str:
        factory = self._get_factory()
        return factory.deploy(contract_type, contract_metadata)

    def _get_registry(self) -> ContractRegistry:
        try:
            return self.__registry
        except:
            pass

        chain_id = ChainId(self.get_provider().eth.chain_id)
        registry_address = get_contract_address_by_chain_id(chain_id, "tw_registry")

        self.__registry = ContractRegistry(
            registry_address,
            self.get_provider(),
            self.get_signer(),
            self.get_options(),
        )

        return self.__registry

    def _get_factory(self) -> ContractFactory:
        try:
            return self.__factory
        except:
            pass

        chain_id = ChainId(self.get_provider().eth.chain_id)
        factory_address = get_contract_address_by_chain_id(chain_id, "tw_factory")

        self.__factory = ContractFactory(
            factory_address,
            self.get_provider(),
            self.get_signer(),
            self.get_options(),
            self._storage,
        )

        return self.__factory

    def _set_registry(self, registry: ContractRegistry):
        self.__registry = registry

    def _set_factory(self, factory: ContractFactory):
        self.__factory = factory
