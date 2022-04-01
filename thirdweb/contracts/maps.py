from typing import Dict, Any
from thirdweb.types.contract import ContractType
from thirdweb.contracts import NFTCollection, Edition, Token


CONTRACTS_MAP: Dict[ContractType, Any] = {
    NFTCollection.contract_type: NFTCollection,
    Edition.contract_type: Edition,
    Token.contract_type: Token,
}
