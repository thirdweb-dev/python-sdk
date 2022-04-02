from typing import Dict, List, Optional, Any
from web3 import Web3
from thirdweb.abi.t_w_factory import TWFactory
from thirdweb.constants.addresses import (
    CONTRACT_ADDRESSES,
    OZ_DEFENDER_FORWARDER_ADDRESS,
)
from thirdweb.constants.chains import ChainId
from thirdweb.contracts import NFTCollection, Edition, Token
from thirdweb.contracts.maps import (
    CONTRACT_BYTECODE,
    CONTRACTS_MAP,
    REMOTE_CONTRACT_NAME,
)
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from eth_account.account import LocalAccount

from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import (
    EditionContractMetadata,
    NFTCollectionContractMetadata,
    TokenContractMetadata,
)


class ContractFactory(ContractWrapper):
    _storage: IpfsStorage

    def __init__(
        self,
        factory_address: str,
        provider: Web3,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
        storage: IpfsStorage = IpfsStorage(),
    ):
        abi = TWFactory(provider, factory_address)
        super().__init__(abi, provider, signer, options)
        self._storage = storage

    def deploy(self, contract_type: ContractType, contract_metadata: Dict[str, Any]):
        contract = CONTRACTS_MAP[contract_type]

        contract_uri = self._storage.upload_metadata(
            contract_metadata,
            self._contract_abi.contract_address,
            self.get_signer_address(),
        )

        interface = self.get_contract_interface()

        # TODO: Use contract factory to encode function for "initialize"
        # with get_deploy_arguments()

        deploy_arguments = self.get_deploy_arguments(
            contract_type, contract_metadata, contract_uri
        )
        encoded_function = interface.encodeABI("initialize", deploy_arguments)

        contract_name = REMOTE_CONTRACT_NAME[contract_type]
        encoded_type = contract_name.encode("utf-8")

        self.send_transaction("deploy_proxy", [encoded_type, encoded_function])

    def get_deploy_arguments(
        self,
        contract_type: ContractType,
        contract_metadata: Dict[str, Any],
        contract_uri: str,
    ) -> List[Any]:
        trusted_forwarders = self._get_default_trusted_forwarders()
        if "trusted_forwarders" in contract_metadata:
            trusted_forwarders = contract_metadata["trusted_forwarders"]

        if contract_type == NFTCollection.contract_type:
            metadata = NFTCollectionContractMetadata.from_json(contract_metadata)
            return [
                self.get_signer_address(),
                metadata.name,
                metadata.symbol,
                contract_uri,
                trusted_forwarders,
                metadata.primary_sale_recipient,
                metadata.seller_fee_basis_points,
                metadata.platform_fee_basis_points,
                metadata.platform_fee_recipient,
            ]

        if contract_type == Edition.contract_type:
            metadata = EditionContractMetadata.from_json(contract_metadata)
            return [
                self.get_signer_address(),
                metadata.name,
                metadata.symbol,
                contract_uri,
                trusted_forwarders,
                metadata.primary_sale_recipient,
                metadata.seller_fee_basis_points,
                metadata.platform_fee_basis_points,
                metadata.platform_fee_recipient,
            ]

        if contract_type == Token.contract_type:
            metadata = TokenContractMetadata.from_json(contract_metadata)
            return [
                self.get_signer_address(),
                metadata.name,
                metadata.symbol,
                contract_uri,
                trusted_forwarders,
                metadata.primary_sale_recipient,
                metadata.platform_fee_recipient,
                metadata.platform_fee_basis_points,
            ]

        return []

    def _get_default_trusted_forwarders(self) -> List[str]:
        chain_id = ChainId(self.get_chain_id())

        if chain_id in CONTRACT_ADDRESSES:
            biconomy_forwarder_address = CONTRACT_ADDRESSES[chain_id][
                "biconomy_forwarder"
            ]
            return [OZ_DEFENDER_FORWARDER_ADDRESS, biconomy_forwarder_address]
        return [OZ_DEFENDER_FORWARDER_ADDRESS]
