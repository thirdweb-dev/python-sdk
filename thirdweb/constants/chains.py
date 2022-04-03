from enum import Enum

# Only include supported chains since python doesn't support enum extension
class ChainId(Enum):
    MAINNET = 1
    RINKEBY = 4
    GOERLI = 5
    POLYGON = 137
    FANTOM = 250
    LOCALHOST = 1337
    HARDHAT = 31337
    AVALANCHE = 43114
    MUMBAI = 80001
