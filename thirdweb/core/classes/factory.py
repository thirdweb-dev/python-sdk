from typing import List, Optional
from brownie import ZERO_ADDRESS, chain
from web3 import Web3
from thirdweb.abi.t_w_factory import TWFactory
from thirdweb.constants.addresses import (
    CONTRACT_ADDRESSES,
    OZ_DEFENDER_FORWARDER_ADDRESS,
)
from thirdweb.constants.chains import ChainId
from thirdweb.contracts.maps import CONTRACTS_MAP
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from eth_account.account import LocalAccount

from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from thirdweb.types.sdk import SDKOptions


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

    def deploy(self, contract_type: ContractType):
        contract = CONTRACTS_MAP[contract_type]
        schema = contract.schema

    def _get_default_trusted_forwarders(self) -> List[str]:
        chain_id = ChainId(self.get_chain_id())

        if chain_id in CONTRACT_ADDRESSES:
            biconomy_forwarder_address = CONTRACT_ADDRESSES[chain_id][
                "biconomy_forwarder"
            ]
            return [OZ_DEFENDER_FORWARDER_ADDRESS, biconomy_forwarder_address]
        return [OZ_DEFENDER_FORWARDER_ADDRESS]
