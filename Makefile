.PHONY: abi

test:
	poetry run brownie test --network hardhat

setup:
	rm -rf .venv
	poetry shell
	poetry install
	poetry run yarn add hardhat
	make abi

abi:
	abi-gen --language Python -o thirdweb/abi --abis abi/TWRegistry.json
	abi-gen --language Python -o thirdweb/abi --abis abi/TWFactory.json
	abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC20.json
	abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC721.json
	abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC1155.json
	abi-gen --language Python -o thirdweb/abi --abis abi/Marketplace.json
	abi-gen --language Python -o thirdweb/abi --abis abi/ERC165.json
	abi-gen --language Python -o thirdweb/abi --abis abi/IERC20.json
	abi-gen --language Python -o thirdweb/abi --abis abi/IERC721.json
	abi-gen --language Python -o thirdweb/abi --abis abi/IERC1155.json