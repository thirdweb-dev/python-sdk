# Make sure your environment is deactivated before running this script.

rm -rf .venv

# Make sure to select .venv as the VSCode project directory
poetry shell
poetry install

# Make sure ganache is installed globally as it is a dependency of brownie
poetry run yarn global add ganache
poetry run yarn add hardhat

bash scripts/abi/generate.sh