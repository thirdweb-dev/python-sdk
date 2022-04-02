# This script will generate python ABIs from the /abi directory

# Token
abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC20.json
mkdir -p thirdweb/abi/token_erc20/bytecode && echo -n "bytecode = " > thirdweb/abi/token_erc20/bytecode/__init__.py
cat abi/TokenERC20.json | jq '.bytecode' >> thirdweb/abi/token_erc20/bytecode/__init__.py

# NFT Collection
abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC721.json
mkdir -p thirdweb/abi/token_erc721/bytecode && echo -n "bytecode = " > thirdweb/abi/token_erc721/bytecode/__init__.py
cat abi/TokenERC721.json | jq '.bytecode' >> thirdweb/abi/token_erc721/bytecode/__init__.py


# Edition
abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC1155.json
mkdir -p thirdweb/abi/token_erc1155/bytecode && echo -n "bytecode = " > thirdweb/abi/token_erc1155/bytecode/__init__.py
cat abi/TokenERC1155.json | jq '.bytecode' >> thirdweb/abi/token_erc1155/bytecode/__init__.py


# TWRegistry
abi-gen --language Python -o thirdweb/abi --abis abi/TWRegistry.json

# TW Factory
abi-gen --language Python -o thirdweb/abi --abis abi/TWFactory.json
