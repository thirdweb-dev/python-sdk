# This script will generate python ABIs from the /abi directory

# Token
abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC20.json


# NFT Collection
abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC721.json


# Edition
abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC1155.json


# TWRegistry
abi-gen --language Python -o thirdweb/abi --abis abi/TWRegistry.json
sed -i '' "s/Union[bytes, str](returned)/cast(Union[bytes, str], (returned))/g" thirdweb/abi/t_w_registry/__init__.py

# TW Factory
abi-gen --language Python -o thirdweb/abi --abis abi/TWFactory.json
