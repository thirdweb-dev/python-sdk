from typing import Dict, Any
from thirdweb.types.contract import ContractType
from thirdweb.contracts import NFTCollection, Edition, Token


CONTRACTS_MAP: Dict[ContractType, Any] = {
    NFTCollection.contract_type: NFTCollection,
    Edition.contract_type: Edition,
    Token.contract_type: Token,
}

REMOTE_CONTRACT_NAME: Dict[ContractType, str] = {
    NFTCollection.contract_type: "TokenERC721",
    Edition.contract_type: "TokenERC1155",
    Token.contract_type: "TokenERC20",
}

REMOTE_CONTRACT_NAME_TO_CONTRACT_TYPE: Dict[str, ContractType] = {
    "TokenERC721": NFTCollection.contract_type,
    "TokenERC1155": Edition.contract_type,
    "TokenERC20": Token.contract_type,
}
