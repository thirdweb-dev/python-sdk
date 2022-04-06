from typing import Any, Dict, Union

# from thirdweb.abi.token_erc1155.bytecode import bytecode as TOKEN_ERC1155_BYTECODE
# from thirdweb.abi.token_erc20.bytecode import bytecode as TOKEN_ERC20_BYTECODE
# from thirdweb.abi.token_erc721.bytecode import bytecode as TOKEN_ERC721_BYTECODE
from thirdweb.types.contract import ContractType
from thirdweb.contracts import NFTCollection, Edition, Token, Marketplace


CONTRACTS_MAP: Dict[ContractType, Union[NFTCollection, Edition, Token]] = {
    NFTCollection.contract_type: NFTCollection,  # type: ignore
    Edition.contract_type: Edition,  # type: ignore
    Token.contract_type: Token,  # type: ignore
    Marketplace.contract_type: Marketplace,  # type: ignore
}

CONTRACT_BYTECODE: Dict[ContractType, str] = {
    NFTCollection.contract_type: "",
    Edition.contract_type: "",
    Token.contract_type: "",
    Marketplace.contract_type: "",
}

REMOTE_CONTRACT_NAME: Dict[ContractType, str] = {
    NFTCollection.contract_type: "TokenERC721",
    Edition.contract_type: "TokenERC1155",
    Token.contract_type: "TokenERC20",
    Marketplace.contract_type: "Marketplace",
}

REMOTE_CONTRACT_NAME_TO_CONTRACT_TYPE: Dict[str, ContractType] = {
    "TokenERC721": NFTCollection.contract_type,
    "TokenERC1155": Edition.contract_type,
    "TokenERC20": Token.contract_type,
    "Marketplace": Marketplace.contract_type,
}
