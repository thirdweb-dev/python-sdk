# This script will generate python ABIs from the /abi directory

# TWRegistry
abi-gen --language Python -o thirdweb/abi --abis abi/TWRegistry.json


# TW Factory
abi-gen --language Python -o thirdweb/abi --abis abi/TWFactory.json


# Token
abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC20.json


# NFT Collection
abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC721.json


# Edition
abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC1155.json


# Marketplace
abi-gen --language Python -o thirdweb/abi --abis abi/Marketplace.json

