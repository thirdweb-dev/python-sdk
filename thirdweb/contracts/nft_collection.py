from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.abi import TokenERC721

from eth_account.account import LocalAccount
from web3 import Web3

from thirdweb.types.sdk import SDKOptions
from typing import Optional


class NFTCollection(BaseContract):
    def __init__(
        self,
        provider: Web3,
        address: str,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC721(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper)
