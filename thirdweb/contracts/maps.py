from typing import Any, Dict, Union

# from thirdweb.abi.token_erc1155.bytecode import bytecode as TOKEN_ERC1155_BYTECODE
# from thirdweb.abi.token_erc20.bytecode import bytecode as TOKEN_ERC20_BYTECODE
# from thirdweb.abi.token_erc721.bytecode import bytecode as TOKEN_ERC721_BYTECODE
from thirdweb.types.contract import ContractType
from thirdweb.contracts import (
    NFTCollection,
    Edition,
    Token,
    Marketplace,
    NFTDrop,
    EditionDrop,
    Multiwrap,
)


CONTRACTS_MAP: Dict[ContractType, Union[NFTCollection, Edition, Token]] = {
    NFTCollection.contract_type: NFTCollection,  # type: ignore
    Edition.contract_type: Edition,  # type: ignore
    Token.contract_type: Token,  # type: ignore
    Marketplace.contract_type: Marketplace,  # type: ignore
    NFTDrop.contract_type: NFTDrop,  # type: ignore
    EditionDrop.contract_type: EditionDrop,  # type: ignore
    Multiwrap.contract_type: Multiwrap,  # type: ignore
}

REMOTE_CONTRACT_NAME: Dict[ContractType, str] = {
    NFTCollection.contract_type: "TokenERC721",
    Edition.contract_type: "TokenERC1155",
    Token.contract_type: "TokenERC20",
    Marketplace.contract_type: "Marketplace",
    NFTDrop.contract_type: "DropERC721",
    EditionDrop.contract_type: "DropERC1155",
    Multiwrap.contract_type: "Multiwrap",
}

REMOTE_CONTRACT_NAME_TO_CONTRACT_TYPE: Dict[str, ContractType] = {
    "TokenERC721": NFTCollection.contract_type,
    "TokenERC1155": Edition.contract_type,
    "TokenERC20": Token.contract_type,
    "Marketplace": Marketplace.contract_type,
    "DropERC721": NFTDrop.contract_type,
    "DropERC1155": EditionDrop.contract_type,
    "Multiwrap": Multiwrap.contract_type,
}
