# thirdweb.abi.ierc721 package

## Module contents

Generated wrapper for IERC721 Solidity contract.


### _class_ thirdweb.abi.ierc721.ApproveMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the approve method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(to, token_id, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(to, token_id, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(to, token_id, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(to, token_id, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(to, token_id)
Validate the inputs to the approve method.


### _class_ thirdweb.abi.ierc721.BalanceOfMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the balanceOf method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(owner, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(owner, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(owner, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(owner, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(owner)
Validate the inputs to the balanceOf method.


### _class_ thirdweb.abi.ierc721.GetApprovedMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getApproved method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(token_id, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(token_id, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(token_id, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(token_id, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(token_id)
Validate the inputs to the getApproved method.


### _class_ thirdweb.abi.ierc721.IERC721(web3_or_provider, contract_address, validator=None)
Bases: `object`

Wrapper class for IERC721 Solidity contract.

All method parameters of type `bytes` should be encoded as UTF-8,
which can be accomplished via `str.encode("utf_8")`.


#### \__init__(web3_or_provider, contract_address, validator=None)
Get an instance of wrapper for smart contract.


* **Parameters**

    
    * **web3_or_provider** (`Union`[`Web3`, `BaseProvider`]) – Either an instance of `web3.Web3` or
    `web3.providers.base.BaseProvider`


    * **contract_address** (`str`) – where the contract has been deployed


    * **validator** (`Optional`[`IERC721Validator`]) – for validation of method inputs.



#### _static_ abi()
Return the ABI to the underlying contract.


#### approve(_: thirdweb.abi.ierc721.ApproveMetho_ )
Constructor-initialized instance of
`ApproveMethod`.


#### balance_of(_: thirdweb.abi.ierc721.BalanceOfMetho_ )
Constructor-initialized instance of
`BalanceOfMethod`.


#### get_approval_event(tx_hash)
Get log entry for Approval event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Approval event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_approval_for_all_event(tx_hash)
Get log entry for ApprovalForAll event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting ApprovalForAll event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_approved(_: thirdweb.abi.ierc721.GetApprovedMetho_ )
Constructor-initialized instance of
`GetApprovedMethod`.


#### get_transfer_event(tx_hash)
Get log entry for Transfer event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Transfer event



* **Return type**

    `Tuple`[`AttributeDict`]



#### is_approved_for_all(_: thirdweb.abi.ierc721.IsApprovedForAllMetho_ )
Constructor-initialized instance of
`IsApprovedForAllMethod`.


#### owner_of(_: thirdweb.abi.ierc721.OwnerOfMetho_ )
Constructor-initialized instance of
`OwnerOfMethod`.


#### safe_transfer_from1(_: thirdweb.abi.ierc721.SafeTransferFrom1Metho_ )
Constructor-initialized instance of
`SafeTransferFrom1Method`.


#### safe_transfer_from2(_: thirdweb.abi.ierc721.SafeTransferFrom2Metho_ )
Constructor-initialized instance of
`SafeTransferFrom2Method`.


#### set_approval_for_all(_: thirdweb.abi.ierc721.SetApprovalForAllMetho_ )
Constructor-initialized instance of
`SetApprovalForAllMethod`.


#### supports_interface(_: thirdweb.abi.ierc721.SupportsInterfaceMetho_ )
Constructor-initialized instance of
`SupportsInterfaceMethod`.


#### transfer_from(_: thirdweb.abi.ierc721.TransferFromMetho_ )
Constructor-initialized instance of
`TransferFromMethod`.


### _class_ thirdweb.abi.ierc721.IERC721Validator(web3_or_provider, contract_address)
Bases: `zero_ex.contract_wrappers.bases.Validator`

No-op input validator.


### _class_ thirdweb.abi.ierc721.IsApprovedForAllMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the isApprovedForAll method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(owner, operator, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(owner, operator, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(owner, operator, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(owner, operator, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(owner, operator)
Validate the inputs to the isApprovedForAll method.


### _class_ thirdweb.abi.ierc721.OwnerOfMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the ownerOf method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(token_id, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(token_id, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(token_id, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(token_id, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(token_id)
Validate the inputs to the ownerOf method.


### _class_ thirdweb.abi.ierc721.SafeTransferFrom1Method(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the safeTransferFrom method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_from, to, token_id, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_from, to, token_id, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_from, to, token_id, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_from, to, token_id, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_from, to, token_id)
Validate the inputs to the safeTransferFrom method.


### _class_ thirdweb.abi.ierc721.SafeTransferFrom2Method(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the safeTransferFrom method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_from, to, token_id, data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_from, to, token_id, data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_from, to, token_id, data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_from, to, token_id, data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_from, to, token_id, data)
Validate the inputs to the safeTransferFrom method.


### _class_ thirdweb.abi.ierc721.SetApprovalForAllMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setApprovalForAll method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(operator, approved, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(operator, approved, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(operator, approved, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(operator, approved, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(operator, approved)
Validate the inputs to the setApprovalForAll method.


### _class_ thirdweb.abi.ierc721.SupportsInterfaceMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the supportsInterface method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(interface_id, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(interface_id, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(interface_id, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(interface_id, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(interface_id)
Validate the inputs to the supportsInterface method.


### _class_ thirdweb.abi.ierc721.TransferFromMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the transferFrom method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_from, to, token_id, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_from, to, token_id, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_from, to, token_id, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_from, to, token_id, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_from, to, token_id)
Validate the inputs to the transferFrom method.
