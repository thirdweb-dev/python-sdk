from typing import Dict
from thirdweb.constants.chains import ChainId

DEFAULT_MERKLE_ROOT = (
    "0x0000000000000000000000000000000000000000000000000000000000000000"
)

OZ_DEFENDER_FORWARDER_ADDRESS = "0xc82BbE41f2cF04e3a8efA18F7032BDD7f6d98a81"
TWREGISTRY_ADDRESS = "0x7c487845f98938Bb955B1D5AD069d9a30e4131fd"
TWFACTORY_ADDRESS = "0x5DBC7B840baa9daBcBe9D2492E45D7244B54A2A0"

CONTRACT_ADDRESSES: Dict[ChainId, Dict[str, str]] = {
    ChainId.MAINNET: {
        "biconomy_forwarder": "0x84a0856b038eaAd1cC7E297cF34A7e72685A8693",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
        "contract_metadata_registry": "0x0000000000000000000000000000000000000000",
    },
    ChainId.RINKEBY: {
        "biconomy_forwarder": "0xFD4973FeB2031D4409fB57afEE5dF2051b171104",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
        "contract_metadata_registry": "0x1e474395f58418e9c594a79abb0152D04C229E8e",
    },
    ChainId.GOERLI: {
        "biconomy_forwarder": "0x0000000000000000000000000000000000000000",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
        "contract_metadata_registry": "0x520B80B85a3B9abfF75F77068116D759a11a455D",
    },
    ChainId.POLYGON: {
        "biconomy_forwarder": "0x86C80a8aa58e0A4fa09A69624c31Ab2a6CAD56b8",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
        "contract_metadata_registry": "0xB67D404478d91F1C94bc607b8945cBe159B86Df8",
    },
    ChainId.MUMBAI: {
        "biconomy_forwarder": "0x9399BB24DBB5C4b782C70c2969F58716Ebbd6a3b",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
        "contract_metadata_registry": "0x25F2Ea750BF8bE10e1139C3a19F7B4e46557D04B",
    },
    ChainId.AVALANCHE: {
        "biconomy_forwarder": "0x64CD353384109423a966dCd3Aa30D884C9b2E057",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
        "contract_metadata_registry": "0x0000000000000000000000000000000000000000",
    },
    ChainId.FANTOM: {
        "biconomy_forwarder": "0x0000000000000000000000000000000000000000",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
        "contract_metadata_registry": "0x0000000000000000000000000000000000000000",
    },
    ChainId.LOCALHOST: {
        "biconomy_forwarder": "0x0000000000000000000000000000000000000000",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
        "contract_metadata_registry": "0x0000000000000000000000000000000000000000",
    },
    ChainId.HARDHAT: {
        "biconomy_forwarder": "0x0000000000000000000000000000000000000000",
        "tw_factory": TWFACTORY_ADDRESS,
        "tw_registry": TWREGISTRY_ADDRESS,
        "contract_metadata_registry": "0x0000000000000000000000000000000000000000",
    },
}


def get_contract_address_by_chain_id(chain_id: ChainId, contract_name: str) -> str:
    return CONTRACT_ADDRESSES[chain_id][contract_name]
