// Do not modify the existing settings
module.exports = {
  networks: {
    hardhat: {
      forking: {
        url: `https://ethereum.rpc.thirdweb.com/39a3c037d7a88e6692c6681bccfd1f1cf36370324c4051a83acd0edcffb20708`,
      },
      chainId: 1,
      initialBaseFeePerGas: 0, // Allow 0 gas fees when testing
      throwOnTransactionFailures: true, // Brownie expects transactions to throw on revert
      throwOnCallFailures: true, // Brownie expects calls to throw on failure
    },
  },
};
