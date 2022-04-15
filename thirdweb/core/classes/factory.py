from typing import Dict, List, Optional, Any, cast
from eth_typing import Address
from eth_utils import encode_hex
from web3 import Web3
from thirdweb.abi.t_w_factory import TWFactory
from thirdweb.constants.addresses import (
    CONTRACT_ADDRESSES,
    OZ_DEFENDER_FORWARDER_ADDRESS,
)
from thirdweb.constants.chains import ChainId
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.contracts import (
    NFTCollection,
    Edition,
    Token,
    NFTDrop,
    EditionDrop,
    Marketplace,
)
from thirdweb.contracts.maps import (
    CONTRACTS_MAP,
    REMOTE_CONTRACT_NAME,
)
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from eth_account.account import LocalAccount

from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import (
    NFTDropContractMetadata,
    EditionDropContractMetadata,
    MarketplaceContractMetadata,
    TokenContractMetadata,
)


class ContractFactory(ContractWrapper[TWFactory]):
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

    def deploy(
        self, contract_type: ContractType, contract_metadata: Dict[str, Any]
    ) -> str:
        # First, we upload the contract metadata to IPFS
        contract_uri = self._storage.upload_metadata(
            contract_metadata,
            self._contract_abi.contract_address,
            self.get_signer_address(),
        )

        # Then, we get setup the contract interface for the contract we want to deploy
        contract = CONTRACTS_MAP[contract_type]
        interface = self.get_provider().eth.contract(
            address=cast(Address, self._contract_abi.contract_address),
            abi=contract._abi_type.abi(),
        )

        # Next, we encode all the initialize function arguments and pass them to the proxy deploy
        deploy_arguments = self.get_deploy_arguments(
            contract_type, contract_metadata, contract_uri
        )

        encoded_function = interface.encodeABI(
            fn_name="initialize", args=deploy_arguments
        )
        contract_name = REMOTE_CONTRACT_NAME[contract_type]
        encoded_type = encode_hex(contract_name).ljust(66, "0")
        receipt = self.send_transaction(
            "deploy_proxy", [encoded_type, encoded_function]
        )

        events = self.get_events("ProxyDeployed", receipt)
        if len(events) == 0 or events[0].get("event") != "ProxyDeployed":
            raise Exception("No proxy deployed event found")

        address = cast(Any, events[0].get("args")).get("proxy")
        return address

    def get_deploy_arguments(
        self,
        contract_type: ContractType,
        contract_metadata: Dict[str, Any],
        contract_uri: str,
    ) -> List[Any]:
        trusted_forwarders = self._get_default_trusted_forwarders()
        if "trusted_forwarders" in contract_metadata:
            trusted_forwarders = contract_metadata["trusted_forwarders"]

        if (
            contract_type == NFTCollection.contract_type
            or contract_type == NFTDrop.contract_type
        ):
            metadata = NFTDropContractMetadata.from_json(contract_metadata)
            return [
                self.get_signer_address(),
                metadata.name,
                metadata.symbol,
                contract_uri,
                trusted_forwarders,
                metadata.primary_sale_recipient,
                metadata.fee_recipient,
                metadata.seller_fee_basis_points,
                metadata.platform_fee_basis_points,
                metadata.platform_fee_recipient,
            ]

        if (
            contract_type == Edition.contract_type
            or contract_type == EditionDrop.contract_type
        ):
            metadata = EditionDropContractMetadata.from_json(contract_metadata)
            return [
                self.get_signer_address(),
                metadata.name,
                metadata.symbol,
                contract_uri,
                trusted_forwarders,
                metadata.primary_sale_recipient,
                metadata.fee_recipient,
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
        if contract_type == Marketplace.contract_type:
            metadata = MarketplaceContractMetadata.from_json(contract_metadata)

            return [
                self.get_signer_address(),
                contract_uri,
                trusted_forwarders,
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

            if biconomy_forwarder_address != ZERO_ADDRESS:
                return [OZ_DEFENDER_FORWARDER_ADDRESS, biconomy_forwarder_address]
        return [OZ_DEFENDER_FORWARDER_ADDRESS]
