from thirdweb.constants.chains import ChainId


CHAIN_ID_TO_RPC_URL = {
    ChainId.MAINNET: "https://main-rpc.linkpool.io",
    ChainId.RINKEBY: "https://rinkeby.arbitrum.io/rpc",
    ChainId.GOERLI: "https://goerli.optimism.io/",
    ChainId.POLYGON: "https://polygon-rpc.com/",
    ChainId.AVALANCHE: "https://api.avax.network/ext/bc/C/rpc",
    ChainId.MUMBAI: "https://rpc-mumbai.maticvigil.com",
    ChainId.FANTOM: "https://rpc.ftm.tools/",
    ChainId.LOCALHOST: "http://localhost:8545",
    ChainId.HARDHAT: "http://localhost:8545",
}
