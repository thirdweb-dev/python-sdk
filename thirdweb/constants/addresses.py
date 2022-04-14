from typing import Dict
from thirdweb.constants.chains import ChainId
from thirdweb.constants.currency import ZERO_ADDRESS

DEFAULT_MERKLE_ROOT = (
    "0x0000000000000000000000000000000000000000000000000000000000000000"
)

OZ_DEFENDER_FORWARDER_ADDRESS = "0xc82BbE41f2cF04e3a8efA18F7032BDD7f6d98a81"
TWREGISTRY_ADDRESS = "0x7c487845f98938Bb955B1D5AD069d9a30e4131fd"
TWFACTORY_ADDRESS = "0x11c34F062Cb10a20B9F463E12Ff9dA62D76FDf65"

CONTRACT_ADDRESSES: Dict[ChainId, Dict[str, str]] = {
    ChainId.MAINNET: {
        "biconomy_forwarder": "0x84a0856b038eaAd1cC7E297cF34A7e72685A8693",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
    },
    ChainId.RINKEBY: {
        "biconomy_forwarder": "0xFD4973FeB2031D4409fB57afEE5dF2051b171104",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
    },
    ChainId.GOERLI: {
        "biconomy_forwarder": ZERO_ADDRESS,
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
    },
    ChainId.POLYGON: {
        "biconomy_forwarder": "0x86C80a8aa58e0A4fa09A69624c31Ab2a6CAD56b8",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
    },
    ChainId.MUMBAI: {
        "biconomy_forwarder": "0x9399BB24DBB5C4b782C70c2969F58716Ebbd6a3b",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
    },
    ChainId.AVALANCHE: {
        "biconomy_forwarder": "0x64CD353384109423a966dCd3Aa30D884C9b2E057",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
    },
    ChainId.FANTOM: {
        "biconomy_forwarder": ZERO_ADDRESS,
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
    },
    ChainId.LOCALHOST: {
        "biconomy_forwarder": ZERO_ADDRESS,
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
    },
    ChainId.HARDHAT: {
        "biconomy_forwarder": ZERO_ADDRESS,
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
    },
}


def get_contract_address_by_chain_id(chain_id: ChainId, contract_name: str) -> str:
    return CONTRACT_ADDRESSES[chain_id][contract_name]
