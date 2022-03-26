# Thirdweb Python SDK

The thirdweb SDK for Python.
## Installation

```bash
$ pip install thirdweb-sdk
```

## Repository Info

### Poetry Environment Setup

If you want to work with this repository, make sure to setup [Poetry](https://python-poetry.org/docs/), you're virtual environment, and the code styling tools.

Assuming you've installed and setup poetry, you can setup this repository with:

```bash
$ poetry shell
$ poetry install
$ poetry run yarn global add ganache
```

Alternatively, if your system can run .sh files, you can set everything up by running the following bash script:

```bash
$ bash scripts/env/setup.sh
```

### Running Tests

Before running tests, make sure you've already run `poetry shell` and are in the poetry virutal environment with all dependencies installed. 

Once you have checked that this you have all the dependencies, you can run the following:

```bash
$ poetry run brownie test
```

Currently (only temporary), since contract deployers are not yet setup in this SDK, the testing relies on contracts on testnets deployed through the thirdweb dashboard. The testing setup is configured to use the `mumbai` network currently, but this can be changed to any network by chaing the RPC URL used in `tests/fixtures/before.py`.

To properly setup testing, you'll need to add your private key to the `.env` file as follows:

```.env
PRIVATE_KEY=...
```

And then switch the test cases to use your own contract addresses for the `NFT_COLLECTION_ADDRESS`, `EDITION_ADDRESS`, and `TOKEN_ADDRESS` variables in `tests/test_nft_collection.py`, `tests/test_edition.py`, and `tests/test_token.py` files respectively.

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

Assuming you have the thirdweb contract ABIs in this directory at `/abi`, you can run the following command to generate an ABI.

```bash
$ abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC721.json
```

Alternatively, if your system can run .sh files, you can run the following to generate all ABIs at once (from your /abi folder):

```bash
$ bash scripts/abi/generate.sh
```
