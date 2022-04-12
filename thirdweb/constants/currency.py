from typing import Dict
from thirdweb.types.currency import NativeToken, WrappedToken
from thirdweb.constants.chains import ChainId

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

NATIVE_TOKEN_ADDRESS = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"

NATIVE_TOKENS: Dict[ChainId, NativeToken] = {
    ChainId.MAINNET: NativeToken(
        "Ether",
        "ETH",
        18,
        WrappedToken(
            "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            "Wrapped Ether",
            "WETH",
        ),
    ),
    ChainId.RINKEBY: NativeToken(
        "Ether",
        "ETH",
        18,
        WrappedToken(
            "0xc778417E063141139Fce010982780140Aa0cD5Ab",
            "Wrapped Ether",
            "WETH",
        ),
    ),
    ChainId.GOERLI: NativeToken(
        "Ether",
        "ETH",
        18,
        WrappedToken(
            "0x0bb7509324ce409f7bbc4b701f932eaca9736ab7",
            "Wrapped Ether",
            "WETH",
        ),
    ),
    ChainId.POLYGON: NativeToken(
        "Matic",
        "MATIC",
        18,
        WrappedToken(
            "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270",
            "Wrapped Matic",
            "WMATIC",
        ),
    ),
    ChainId.MUMBAI: NativeToken(
        "Matic",
        "MATIC",
        18,
        WrappedToken(
            "0x9c3C9283D3e44854697Cd22D3Faa240Cfb032889",
            "Wrapped Matic",
            "WMATIC",
        ),
    ),
    ChainId.AVALANCHE: NativeToken(
        "Avalanche",
        "AVAX",
        18,
        WrappedToken(
            "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7",
            "Wrapped AVAX",
            "WAVAX",
        ),
    ),
    ChainId.FANTOM: NativeToken(
        "Fantom",
        "FTM",
        18,
        WrappedToken(
            "0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83",
            "Wrapped Fantom",
            "WFTM",
        ),
    ),
    ChainId.LOCALHOST: NativeToken(
        "Ether",
        "ETH",
        18,
        WrappedToken(
            "0x5FbDB2315678afecb367f032d93F642f64180aa3",
            "Wrapped Ether",
            "WETH",
        ),
    ),
    ChainId.HARDHAT: NativeToken(
        "Ether",
        "ETH",
        18,
        WrappedToken(
            "0x5FbDB2315678afecb367f032d93F642f64180aa3",
            "Wrapped Ether",
            "WETH",
        ),
    ),
}


def get_native_token_by_chain_id(chain_id: ChainId) -> NativeToken:
    return NATIVE_TOKENS[chain_id]
