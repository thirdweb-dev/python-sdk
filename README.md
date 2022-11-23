<p align="center">
<br />
<a href="https://thirdweb.com"><img src="https://github.com/thirdweb-dev/typescript-sdk/blob/main/logo.svg?raw=true" width="200" alt=""/></a>
<br />
</p>
<h1 align="center">thirdweb Python SDK</h1>
<p align="center">
<a href="https://pypi.org/project/thirdweb-sdk/"><img src="https://img.shields.io/pypi/v/thirdweb-sdk?color=red&logo=pypi&logoColor=red" alt="pypi version"/></a>
<a href="https://github.com/thirdweb-dev/python-sdk/actions"><img alt="Build Status" src="https://github.com/thirdweb-dev/python-sdk/actions/workflows/tests.yml/badge.svg"/></a>
<a href="https://discord.gg/thirdweb"><img alt="Join our Discord!" src="https://img.shields.io/discord/834227967404146718.svg?color=7289da&label=discord&logo=discord&style=flat"/></a>

</p>
<p align="center"><strong>Best in class Web3 SDK for Python 3.7+</strong></p>
<br />

## Installation

```bash
pip install thirdweb-sdk
```

## Getting Started

To start using this SDK, you just need to pass in a provider configuration.

### Instantiating the SDK

Once you have all the necessary dependencies, you can follow the following setup steps to get started with the SDK read-only functions:

```python
from thirdweb import ThirdwebSDK

# You can create a new instance of the SDK to use by just passing in a network name
sdk = ThirdwebSDK("mumbai")
```

The SDK supports the `mainnet`, `rinkeby`, `goerli`, `polygon`, `mumbai`, `fantom`, and `avalanche` networks.

Alternatively, if you want to use your own custom RPC URL, you can pass in the RPC URL directly as follows:

```python
from thirdweb import ThirdwebSDK

# Set your RPC_URL
RPC_URL = "https://rpc-mainnet.matic.network"

# And now you can instantiate the SDK with it
sdk = ThirdwebSDK(RPC_URL)
```

### Working With Contracts

Once you instantiate the SDK, you can use it to access your thirdweb contracts. You can use the SDK's contract getter functions like `get_token`, `get_edition`, `get_nft_collection`, and `get_marketplace` to get the respective SDK contract instances. To use an NFT Collection contract for example, you can do the following.

```python
# Add your NFT Collection contract address here
NFT_COLLECTION_ADDRESS = "0x.."

# And you can instantiate your contract with just one line
nft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)

# Now you can use any of the read-only SDK contract functions
nfts = nft_collection.get_all()
print(nfts)
```

### Signing Transactions

> :warning: Never commit private keys to file tracking history, or your account could be compromised.

Meanwhile, if you want to use write functions as well and connect a signer, you can use the following setup:

```python
from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput

# Learn more about securely accessing your private key: https://portal.thirdweb.com/web3-sdk/set-up-the-sdk/securing-your-private-key
PRIVATE_KEY = "<your-private-key-here>",

# Now you can create a new instance of the SDK with your private key
sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, "mumbai")

# Instantiate a new NFT Collection contract as described above.
NFT_COLLECTION_ADDRESS = "0x.."
nft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)

# Now you can use any of the SDK contract functions including write functions
nft_collection.mint(NFTMetadataInput.from_json({ "name": "Cool NFT", "description": "Minted with the Python SDK!" }))
```

## Development Environment

In this section, we'll go over the steps to get started with running the Python SDK repository locally and contributing to the code. If you aren't interested in contributing to the thirdweb Python SDK, you can ignore this section.

### Poetry Environment Setup

If you want to work with this repository, make sure to setup [Poetry](https://python-poetry.org/docs/), you're virtual environment, and the code styling tools.

Assuming you've installed and setup poetry, you can setup this repository with:

```bash
$ poetry shell
$ poetry install
$ poetry run yarn global add ganache
$ poetry run yarn add hardhat
```

Alternatively, if your system can run .sh files, you can set everything up by running the following bash script:

```bash
$ bash scripts/env/setup.sh
```

### Running Tests

Before running tests, make sure you've already run `poetry shell` and are in the poetry virutal environment with all dependencies installed.

Once you have checked that this you have all the dependencies, you can run the following:

```bash
$ poetry run brownie test --network hardhat
```

To properly setup testing, you'll also need to add your private key to the `.env` file as follows (do NOT use a private key of one of your actual wallets):

```.env
PRIVATE_KEY=...
```

### Code Style Setup

Make sure you have `mypy`, `pylint`, and `black` installed (all included in the dev dependencies with `poetry install`.

If you're working in VSCode, there a few steps to get everything working with the poetry .venv:

1. To setup poetry virtual environment inside your VSCode so it gets recognized as part of your project (import for linters), you can take the following steps from this [stack overflow answer](https://stackoverflow.com/questions/59882884/vscode-doesnt-show-poetry-virtualenvs-in-select-interpreter-option). You need to run `poetry config virtualenvs.in-project true` and then make sure you delete/create a new poetry env.
2. In `.vscode/settings.json`, you should have the following:

```json
{
  "python.linting.mypyEnabled": true,
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false
}
```

3. Make sure to set your VSCode `Python: Interpreter` setting to the Python version inside your poetry virtual environment.

### Generate Python ABI Wrappers

Use the [abi-gen](https://www.npmjs.com/package/@0x/abi-gen) package to create the Python ABIs. You can install it with the following command:

```bash
$ npm install -g @0x/abi-gen
```

Assuming you have the thirdweb contract ABIs in this directory at `/abi`, you can run the following command to generate the necessary ABIs.

```bash
$ make abi
```
