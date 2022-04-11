# thirdweb.abi package

## Submodules

## thirdweb.abi.erc165 module

Generated wrapper for ERC165 Solidity contract.


### _class_ thirdweb.abi.erc165.ERC165(web3_or_provider, contract_address, validator=None)
Bases: `object`

Wrapper class for ERC165 Solidity contract.


#### \__init__(web3_or_provider, contract_address, validator=None)
Get an instance of wrapper for smart contract.


* **Parameters**

    
    * **web3_or_provider** (`Union`[`Web3`, `BaseProvider`]) – Either an instance of `web3.Web3` or
    `web3.providers.base.BaseProvider`


    * **contract_address** (`str`) – where the contract has been deployed


    * **validator** (`Optional`[`ERC165Validator`]) – for validation of method inputs.



#### _static_ abi()
Return the ABI to the underlying contract.


#### supports_interface(_: thirdweb.abi.erc165.SupportsInterfaceMetho_ )
Constructor-initialized instance of
`SupportsInterfaceMethod`.


### _class_ thirdweb.abi.erc165.ERC165Validator(web3_or_provider, contract_address)
Bases: `zero_ex.contract_wrappers.bases.Validator`

No-op input validator.


### _class_ thirdweb.abi.erc165.SupportsInterfaceMethod(web3_or_provider, contract_address, contract_function, validator=None)
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

## thirdweb.abi.ierc1155 module

Generated wrapper for IERC1155 Solidity contract.


### _class_ thirdweb.abi.ierc1155.BalanceOfBatchMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the balanceOfBatch method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(accounts, ids, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(accounts, ids, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `List`[`int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(accounts, ids, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(accounts, ids, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(accounts, ids)
Validate the inputs to the balanceOfBatch method.


### _class_ thirdweb.abi.ierc1155.BalanceOfMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the balanceOf method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, _id, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, _id, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, _id, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, _id, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account, _id)
Validate the inputs to the balanceOf method.


### _class_ thirdweb.abi.ierc1155.IERC1155(web3_or_provider, contract_address, validator=None)
Bases: `object`

Wrapper class for IERC1155 Solidity contract.

All method parameters of type `bytes` should be encoded as UTF-8,
which can be accomplished via `str.encode("utf_8")`.


#### \__init__(web3_or_provider, contract_address, validator=None)
Get an instance of wrapper for smart contract.


* **Parameters**

    
    * **web3_or_provider** (`Union`[`Web3`, `BaseProvider`]) – Either an instance of `web3.Web3` or
    `web3.providers.base.BaseProvider`


    * **contract_address** (`str`) – where the contract has been deployed


    * **validator** (`Optional`[`IERC1155Validator`]) – for validation of method inputs.



#### _static_ abi()
Return the ABI to the underlying contract.


#### balance_of(_: thirdweb.abi.ierc1155.BalanceOfMetho_ )
Constructor-initialized instance of
`BalanceOfMethod`.


#### balance_of_batch(_: thirdweb.abi.ierc1155.BalanceOfBatchMetho_ )
Constructor-initialized instance of
`BalanceOfBatchMethod`.


#### get_approval_for_all_event(tx_hash)
Get log entry for ApprovalForAll event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting ApprovalForAll event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_transfer_batch_event(tx_hash)
Get log entry for TransferBatch event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting TransferBatch event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_transfer_single_event(tx_hash)
Get log entry for TransferSingle event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting TransferSingle event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_uri_event(tx_hash)
Get log entry for URI event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting URI event



* **Return type**

    `Tuple`[`AttributeDict`]



#### is_approved_for_all(_: thirdweb.abi.ierc1155.IsApprovedForAllMetho_ )
Constructor-initialized instance of
`IsApprovedForAllMethod`.


#### safe_batch_transfer_from(_: thirdweb.abi.ierc1155.SafeBatchTransferFromMetho_ )
Constructor-initialized instance of
`SafeBatchTransferFromMethod`.


#### safe_transfer_from(_: thirdweb.abi.ierc1155.SafeTransferFromMetho_ )
Constructor-initialized instance of
`SafeTransferFromMethod`.


#### set_approval_for_all(_: thirdweb.abi.ierc1155.SetApprovalForAllMetho_ )
Constructor-initialized instance of
`SetApprovalForAllMethod`.


#### supports_interface(_: thirdweb.abi.ierc1155.SupportsInterfaceMetho_ )
Constructor-initialized instance of
`SupportsInterfaceMethod`.


### _class_ thirdweb.abi.ierc1155.IERC1155Validator(web3_or_provider, contract_address)
Bases: `zero_ex.contract_wrappers.bases.Validator`

No-op input validator.


### _class_ thirdweb.abi.ierc1155.IsApprovedForAllMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the isApprovedForAll method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, operator, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, operator, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, operator, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, operator, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account, operator)
Validate the inputs to the isApprovedForAll method.


### _class_ thirdweb.abi.ierc1155.SafeBatchTransferFromMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the safeBatchTransferFrom method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_from, to, ids, amounts, data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_from, to, ids, amounts, data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_from, to, ids, amounts, data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_from, to, ids, amounts, data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_from, to, ids, amounts, data)
Validate the inputs to the safeBatchTransferFrom method.


### _class_ thirdweb.abi.ierc1155.SafeTransferFromMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the safeTransferFrom method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_from, to, _id, amount, data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_from, to, _id, amount, data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_from, to, _id, amount, data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_from, to, _id, amount, data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_from, to, _id, amount, data)
Validate the inputs to the safeTransferFrom method.


### _class_ thirdweb.abi.ierc1155.SetApprovalForAllMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.ierc1155.SupportsInterfaceMethod(web3_or_provider, contract_address, contract_function, validator=None)
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

## thirdweb.abi.ierc20 module

Generated wrapper for IERC20 Solidity contract.


### _class_ thirdweb.abi.ierc20.AllowanceMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the allowance method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(owner, spender, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(owner, spender, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(owner, spender, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(owner, spender, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(owner, spender)
Validate the inputs to the allowance method.


### _class_ thirdweb.abi.ierc20.ApproveMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the approve method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(spender, amount, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(spender, amount, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(spender, amount, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(spender, amount, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(spender, amount)
Validate the inputs to the approve method.


### _class_ thirdweb.abi.ierc20.BalanceOfMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the balanceOf method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account)
Validate the inputs to the balanceOf method.


### _class_ thirdweb.abi.ierc20.IERC20(web3_or_provider, contract_address, validator=None)
Bases: `object`

Wrapper class for IERC20 Solidity contract.


#### \__init__(web3_or_provider, contract_address, validator=None)
Get an instance of wrapper for smart contract.


* **Parameters**

    
    * **web3_or_provider** (`Union`[`Web3`, `BaseProvider`]) – Either an instance of `web3.Web3` or
    `web3.providers.base.BaseProvider`


    * **contract_address** (`str`) – where the contract has been deployed


    * **validator** (`Optional`[`IERC20Validator`]) – for validation of method inputs.



#### _static_ abi()
Return the ABI to the underlying contract.


#### allowance(_: thirdweb.abi.ierc20.AllowanceMetho_ )
Constructor-initialized instance of
`AllowanceMethod`.


#### approve(_: thirdweb.abi.ierc20.ApproveMetho_ )
Constructor-initialized instance of
`ApproveMethod`.


#### balance_of(_: thirdweb.abi.ierc20.BalanceOfMetho_ )
Constructor-initialized instance of
`BalanceOfMethod`.


#### get_approval_event(tx_hash)
Get log entry for Approval event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Approval event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_transfer_event(tx_hash)
Get log entry for Transfer event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Transfer event



* **Return type**

    `Tuple`[`AttributeDict`]



#### total_supply(_: thirdweb.abi.ierc20.TotalSupplyMetho_ )
Constructor-initialized instance of
`TotalSupplyMethod`.


#### transfer(_: thirdweb.abi.ierc20.TransferMetho_ )
Constructor-initialized instance of
`TransferMethod`.


#### transfer_from(_: thirdweb.abi.ierc20.TransferFromMetho_ )
Constructor-initialized instance of
`TransferFromMethod`.


### _class_ thirdweb.abi.ierc20.IERC20Validator(web3_or_provider, contract_address)
Bases: `zero_ex.contract_wrappers.bases.Validator`

No-op input validator.


### _class_ thirdweb.abi.ierc20.TotalSupplyMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the totalSupply method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.ierc20.TransferFromMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the transferFrom method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_from, to, amount, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_from, to, amount, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_from, to, amount, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_from, to, amount, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_from, to, amount)
Validate the inputs to the transferFrom method.


### _class_ thirdweb.abi.ierc20.TransferMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the transfer method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(to, amount, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(to, amount, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(to, amount, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(to, amount, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(to, amount)
Validate the inputs to the transfer method.

## thirdweb.abi.ierc721 module

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

## thirdweb.abi.marketplace module

Generated wrapper for Marketplace Solidity contract.


### _class_ thirdweb.abi.marketplace.AcceptOfferMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the acceptOffer method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(listing_id, offeror, currency, price_per_token, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(listing_id, offeror, currency, price_per_token, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(listing_id, offeror, currency, price_per_token, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(listing_id, offeror, currency, price_per_token, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(listing_id, offeror, currency, price_per_token)
Validate the inputs to the acceptOffer method.


### _class_ thirdweb.abi.marketplace.BidBufferBpsMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the bidBufferBps method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.marketplace.BuyMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the buy method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(listing_id, buy_for, quantity_to_buy, currency, total_price, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(listing_id, buy_for, quantity_to_buy, currency, total_price, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(listing_id, buy_for, quantity_to_buy, currency, total_price, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(listing_id, buy_for, quantity_to_buy, currency, total_price, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(listing_id, buy_for, quantity_to_buy, currency, total_price)
Validate the inputs to the buy method.


### _class_ thirdweb.abi.marketplace.CancelDirectListingMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the cancelDirectListing method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(listing_id, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(listing_id, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(listing_id, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(listing_id, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(listing_id)
Validate the inputs to the cancelDirectListing method.


### _class_ thirdweb.abi.marketplace.CloseAuctionMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the closeAuction method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(listing_id, close_for, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(listing_id, close_for, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(listing_id, close_for, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(listing_id, close_for, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(listing_id, close_for)
Validate the inputs to the closeAuction method.


### _class_ thirdweb.abi.marketplace.ContractTypeMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractType method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.marketplace.ContractUriMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractURI method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.marketplace.ContractVersionMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractVersion method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.marketplace.CreateListingMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the createListing method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(params, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(params, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(params, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(params, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(params)
Validate the inputs to the createListing method.


### _class_ thirdweb.abi.marketplace.DefaultAdminRoleMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the DEFAULT_ADMIN_ROLE method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.marketplace.GetPlatformFeeInfoMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getPlatformFeeInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`str`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.marketplace.GetRoleAdminMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleAdmin method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleAdmin method.


### _class_ thirdweb.abi.marketplace.GetRoleMemberCountMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMemberCount method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleMemberCount method.


### _class_ thirdweb.abi.marketplace.GetRoleMemberMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMember method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, index, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, index, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, index, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, index, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, index)
Validate the inputs to the getRoleMember method.


### _class_ thirdweb.abi.marketplace.GrantRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the grantRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the grantRole method.


### _class_ thirdweb.abi.marketplace.HasRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the hasRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the hasRole method.


### _class_ thirdweb.abi.marketplace.IMarketplaceListing(\*args, \*\*kwargs)
Bases: `dict`

Python representation of a tuple or struct.

Solidity compiler output does not include the names of structs that appear
in method definitions.  A tuple found in an ABI may have been written in
Solidity as a literal, anonymous tuple, or it may have been written as a
named `struct`, but there is no way to tell from the compiler
output.  This class represents a tuple that appeared in a method
definition.  Its name is derived from a hash of that tuple’s field names,
and every method whose ABI refers to a tuple with that same list of field
names will have a generated wrapper method that refers to this class.

Any members of type `bytes` should be encoded as UTF-8, which can be
accomplished via `str.encode("utf_8")`


#### assetContract(_: st_ )

#### buyoutPricePerToken(_: in_ )

#### currency(_: st_ )

#### endTime(_: in_ )

#### listingId(_: in_ )

#### listingType(_: in_ )

#### quantity(_: in_ )

#### reservePricePerToken(_: in_ )

#### startTime(_: in_ )

#### tokenId(_: in_ )

#### tokenOwner(_: st_ )

#### tokenType(_: in_ )

### _class_ thirdweb.abi.marketplace.IMarketplaceListingParameters(\*args, \*\*kwargs)
Bases: `dict`

Python representation of a tuple or struct.

Solidity compiler output does not include the names of structs that appear
in method definitions.  A tuple found in an ABI may have been written in
Solidity as a literal, anonymous tuple, or it may have been written as a
named `struct`, but there is no way to tell from the compiler
output.  This class represents a tuple that appeared in a method
definition.  Its name is derived from a hash of that tuple’s field names,
and every method whose ABI refers to a tuple with that same list of field
names will have a generated wrapper method that refers to this class.

Any members of type `bytes` should be encoded as UTF-8, which can be
accomplished via `str.encode("utf_8")`


#### assetContract(_: st_ )

#### buyoutPricePerToken(_: in_ )

#### currencyToAccept(_: st_ )

#### listingType(_: in_ )

#### quantityToList(_: in_ )

#### reservePricePerToken(_: in_ )

#### secondsUntilEndTime(_: in_ )

#### startTime(_: in_ )

#### tokenId(_: in_ )

### _class_ thirdweb.abi.marketplace.InitializeMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the initialize method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(default_admin, contract_uri, trusted_forwarders, platform_fee_recipient, platform_fee_bps)
Validate the inputs to the initialize method.


### _class_ thirdweb.abi.marketplace.IsTrustedForwarderMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the isTrustedForwarder method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(forwarder, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(forwarder, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(forwarder, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(forwarder, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(forwarder)
Validate the inputs to the isTrustedForwarder method.


### _class_ thirdweb.abi.marketplace.ListingsMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the listings method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`int`, `str`, `str`, `int`, `int`, `int`, `int`, `str`, `int`, `int`, `int`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0)
Validate the inputs to the listings method.


### _class_ thirdweb.abi.marketplace.Marketplace(web3_or_provider, contract_address, validator=None)
Bases: `object`

Wrapper class for Marketplace Solidity contract.

All method parameters of type `bytes` should be encoded as UTF-8,
which can be accomplished via `str.encode("utf_8")`.


#### \__init__(web3_or_provider, contract_address, validator=None)
Get an instance of wrapper for smart contract.


* **Parameters**

    
    * **web3_or_provider** (`Union`[`Web3`, `BaseProvider`]) – Either an instance of `web3.Web3` or
    `web3.providers.base.BaseProvider`


    * **contract_address** (`str`) – where the contract has been deployed


    * **validator** (`Optional`[`MarketplaceValidator`]) – for validation of method inputs.



#### _static_ abi()
Return the ABI to the underlying contract.


#### accept_offer(_: thirdweb.abi.marketplace.AcceptOfferMetho_ )
Constructor-initialized instance of
`AcceptOfferMethod`.


#### bid_buffer_bps(_: thirdweb.abi.marketplace.BidBufferBpsMetho_ )
Constructor-initialized instance of
`BidBufferBpsMethod`.


#### buy(_: thirdweb.abi.marketplace.BuyMetho_ )
Constructor-initialized instance of
`BuyMethod`.


#### cancel_direct_listing(_: thirdweb.abi.marketplace.CancelDirectListingMetho_ )
Constructor-initialized instance of
`CancelDirectListingMethod`.


#### close_auction(_: thirdweb.abi.marketplace.CloseAuctionMetho_ )
Constructor-initialized instance of
`CloseAuctionMethod`.


#### contract_type(_: thirdweb.abi.marketplace.ContractTypeMetho_ )
Constructor-initialized instance of
`ContractTypeMethod`.


#### contract_uri(_: thirdweb.abi.marketplace.ContractUriMetho_ )
Constructor-initialized instance of
`ContractUriMethod`.


#### contract_version(_: thirdweb.abi.marketplace.ContractVersionMetho_ )
Constructor-initialized instance of
`ContractVersionMethod`.


#### create_listing(_: thirdweb.abi.marketplace.CreateListingMetho_ )
Constructor-initialized instance of
`CreateListingMethod`.


#### default_admin_role(_: thirdweb.abi.marketplace.DefaultAdminRoleMetho_ )
Constructor-initialized instance of
`DefaultAdminRoleMethod`.


#### get_auction_buffers_updated_event(tx_hash)
Get log entry for AuctionBuffersUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting AuctionBuffersUpdated
    event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_auction_closed_event(tx_hash)
Get log entry for AuctionClosed event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting AuctionClosed event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_listing_added_event(tx_hash)
Get log entry for ListingAdded event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting ListingAdded event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_listing_removed_event(tx_hash)
Get log entry for ListingRemoved event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting ListingRemoved event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_listing_updated_event(tx_hash)
Get log entry for ListingUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting ListingUpdated event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_new_offer_event(tx_hash)
Get log entry for NewOffer event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting NewOffer event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_new_sale_event(tx_hash)
Get log entry for NewSale event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting NewSale event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_platform_fee_info(_: thirdweb.abi.marketplace.GetPlatformFeeInfoMetho_ )
Constructor-initialized instance of
`GetPlatformFeeInfoMethod`.


#### get_platform_fee_info_updated_event(tx_hash)
Get log entry for PlatformFeeInfoUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting PlatformFeeInfoUpdated
    event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_admin(_: thirdweb.abi.marketplace.GetRoleAdminMetho_ )
Constructor-initialized instance of
`GetRoleAdminMethod`.


#### get_role_admin_changed_event(tx_hash)
Get log entry for RoleAdminChanged event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleAdminChanged event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_granted_event(tx_hash)
Get log entry for RoleGranted event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleGranted event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_member(_: thirdweb.abi.marketplace.GetRoleMemberMetho_ )
Constructor-initialized instance of
`GetRoleMemberMethod`.


#### get_role_member_count(_: thirdweb.abi.marketplace.GetRoleMemberCountMetho_ )
Constructor-initialized instance of
`GetRoleMemberCountMethod`.


#### get_role_revoked_event(tx_hash)
Get log entry for RoleRevoked event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleRevoked event



* **Return type**

    `Tuple`[`AttributeDict`]



#### grant_role(_: thirdweb.abi.marketplace.GrantRoleMetho_ )
Constructor-initialized instance of
`GrantRoleMethod`.


#### has_role(_: thirdweb.abi.marketplace.HasRoleMetho_ )
Constructor-initialized instance of
`HasRoleMethod`.


#### initialize(_: thirdweb.abi.marketplace.InitializeMetho_ )
Constructor-initialized instance of
`InitializeMethod`.


#### is_trusted_forwarder(_: thirdweb.abi.marketplace.IsTrustedForwarderMetho_ )
Constructor-initialized instance of
`IsTrustedForwarderMethod`.


#### listings(_: thirdweb.abi.marketplace.ListingsMetho_ )
Constructor-initialized instance of
`ListingsMethod`.


#### max_bps(_: thirdweb.abi.marketplace.MaxBpsMetho_ )
Constructor-initialized instance of
`MaxBpsMethod`.


#### multicall(_: thirdweb.abi.marketplace.MulticallMetho_ )
Constructor-initialized instance of
`MulticallMethod`.


#### offer(_: thirdweb.abi.marketplace.OfferMetho_ )
Constructor-initialized instance of
`OfferMethod`.


#### offers(_: thirdweb.abi.marketplace.OffersMetho_ )
Constructor-initialized instance of
`OffersMethod`.


#### on_erc1155_batch_received(_: thirdweb.abi.marketplace.OnErc1155BatchReceivedMetho_ )
Constructor-initialized instance of
`OnErc1155BatchReceivedMethod`.


#### on_erc1155_received(_: thirdweb.abi.marketplace.OnErc1155ReceivedMetho_ )
Constructor-initialized instance of
`OnErc1155ReceivedMethod`.


#### on_erc721_received(_: thirdweb.abi.marketplace.OnErc721ReceivedMetho_ )
Constructor-initialized instance of
`OnErc721ReceivedMethod`.


#### renounce_role(_: thirdweb.abi.marketplace.RenounceRoleMetho_ )
Constructor-initialized instance of
`RenounceRoleMethod`.


#### revoke_role(_: thirdweb.abi.marketplace.RevokeRoleMetho_ )
Constructor-initialized instance of
`RevokeRoleMethod`.


#### set_auction_buffers(_: thirdweb.abi.marketplace.SetAuctionBuffersMetho_ )
Constructor-initialized instance of
`SetAuctionBuffersMethod`.


#### set_contract_uri(_: thirdweb.abi.marketplace.SetContractUriMetho_ )
Constructor-initialized instance of
`SetContractUriMethod`.


#### set_platform_fee_info(_: thirdweb.abi.marketplace.SetPlatformFeeInfoMetho_ )
Constructor-initialized instance of
`SetPlatformFeeInfoMethod`.


#### supports_interface(_: thirdweb.abi.marketplace.SupportsInterfaceMetho_ )
Constructor-initialized instance of
`SupportsInterfaceMethod`.


#### thirdweb_fee(_: thirdweb.abi.marketplace.ThirdwebFeeMetho_ )
Constructor-initialized instance of
`ThirdwebFeeMethod`.


#### time_buffer(_: thirdweb.abi.marketplace.TimeBufferMetho_ )
Constructor-initialized instance of
`TimeBufferMethod`.


#### total_listings(_: thirdweb.abi.marketplace.TotalListingsMetho_ )
Constructor-initialized instance of
`TotalListingsMethod`.


#### update_listing(_: thirdweb.abi.marketplace.UpdateListingMetho_ )
Constructor-initialized instance of
`UpdateListingMethod`.


#### winning_bid(_: thirdweb.abi.marketplace.WinningBidMetho_ )
Constructor-initialized instance of
`WinningBidMethod`.


### _class_ thirdweb.abi.marketplace.MarketplaceValidator(web3_or_provider, contract_address)
Bases: `zero_ex.contract_wrappers.bases.Validator`

No-op input validator.


### _class_ thirdweb.abi.marketplace.MaxBpsMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the MAX_BPS method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.marketplace.MulticallMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the multicall method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `List`[`Union`[`bytes`, `str`]]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(data)
Validate the inputs to the multicall method.


### _class_ thirdweb.abi.marketplace.OfferMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the offer method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(listing_id, quantity_wanted, currency, price_per_token, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(listing_id, quantity_wanted, currency, price_per_token, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(listing_id, quantity_wanted, currency, price_per_token, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(listing_id, quantity_wanted, currency, price_per_token, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(listing_id, quantity_wanted, currency, price_per_token)
Validate the inputs to the offer method.


### _class_ thirdweb.abi.marketplace.OffersMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the offers method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, index_1, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, index_1, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`int`, `str`, `int`, `str`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, index_1, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, index_1, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0, index_1)
Validate the inputs to the offers method.


### _class_ thirdweb.abi.marketplace.OnErc1155BatchReceivedMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the onERC1155BatchReceived method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, index_1, index_2, index_3, index_4, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, index_1, index_2, index_3, index_4, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, index_1, index_2, index_3, index_4, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, index_1, index_2, index_3, index_4, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
Validate the inputs to the onERC1155BatchReceived method.


### _class_ thirdweb.abi.marketplace.OnErc1155ReceivedMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the onERC1155Received method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, index_1, index_2, index_3, index_4, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, index_1, index_2, index_3, index_4, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, index_1, index_2, index_3, index_4, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, index_1, index_2, index_3, index_4, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0, index_1, index_2, index_3, index_4)
Validate the inputs to the onERC1155Received method.


### _class_ thirdweb.abi.marketplace.OnErc721ReceivedMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the onERC721Received method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, index_1, index_2, index_3, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, index_1, index_2, index_3, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, index_1, index_2, index_3, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, index_1, index_2, index_3, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0, index_1, index_2, index_3)
Validate the inputs to the onERC721Received method.


### _class_ thirdweb.abi.marketplace.RenounceRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the renounceRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the renounceRole method.


### _class_ thirdweb.abi.marketplace.RevokeRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the revokeRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the revokeRole method.


### _class_ thirdweb.abi.marketplace.SetAuctionBuffersMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setAuctionBuffers method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(time_buffer, bid_buffer_bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(time_buffer, bid_buffer_bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(time_buffer, bid_buffer_bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(time_buffer, bid_buffer_bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(time_buffer, bid_buffer_bps)
Validate the inputs to the setAuctionBuffers method.


### _class_ thirdweb.abi.marketplace.SetContractUriMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setContractURI method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(uri, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(uri, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(uri, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(uri, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(uri)
Validate the inputs to the setContractURI method.


### _class_ thirdweb.abi.marketplace.SetPlatformFeeInfoMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setPlatformFeeInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(platform_fee_recipient, platform_fee_bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(platform_fee_recipient, platform_fee_bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
Validate the inputs to the setPlatformFeeInfo method.


### _class_ thirdweb.abi.marketplace.SupportsInterfaceMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.marketplace.ThirdwebFeeMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the thirdwebFee method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.marketplace.TimeBufferMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the timeBuffer method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.marketplace.TotalListingsMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the totalListings method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.marketplace.UpdateListingMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the updateListing method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(listing_id, quantity_to_list, reserve_price_per_token, buyout_price_per_token, currency_to_accept, start_time, seconds_until_end_time)
Validate the inputs to the updateListing method.


### _class_ thirdweb.abi.marketplace.WinningBidMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the winningBid method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`int`, `str`, `int`, `str`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0)
Validate the inputs to the winningBid method.

## thirdweb.abi.t_w_factory module

Generated wrapper for TWFactory Solidity contract.


### _class_ thirdweb.abi.t_w_factory.AddImplementationMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the addImplementation method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(implementation, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(implementation, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(implementation, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(implementation, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(implementation)
Validate the inputs to the addImplementation method.


### _class_ thirdweb.abi.t_w_factory.ApprovalMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the approval method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0)
Validate the inputs to the approval method.


### _class_ thirdweb.abi.t_w_factory.ApproveImplementationMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the approveImplementation method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(implementation, to_approve, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(implementation, to_approve, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(implementation, to_approve, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(implementation, to_approve, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(implementation, to_approve)
Validate the inputs to the approveImplementation method.


### _class_ thirdweb.abi.t_w_factory.CurrentVersionMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the currentVersion method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0)
Validate the inputs to the currentVersion method.


### _class_ thirdweb.abi.t_w_factory.DefaultAdminRoleMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the DEFAULT_ADMIN_ROLE method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.t_w_factory.DeployProxyByImplementationMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the deployProxyByImplementation method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(implementation, data, salt, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(implementation, data, salt, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(implementation, data, salt, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(implementation, data, salt, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(implementation, data, salt)
Validate the inputs to the deployProxyByImplementation method.


### _class_ thirdweb.abi.t_w_factory.DeployProxyDeterministicMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the deployProxyDeterministic method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_type, data, salt, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_type, data, salt, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_type, data, salt, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_type, data, salt, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_type, data, salt)
Validate the inputs to the deployProxyDeterministic method.


### _class_ thirdweb.abi.t_w_factory.DeployProxyMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the deployProxy method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_type, data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_type, data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_type, data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_type, data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_type, data)
Validate the inputs to the deployProxy method.


### _class_ thirdweb.abi.t_w_factory.DeployerMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the deployer method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0)
Validate the inputs to the deployer method.


### _class_ thirdweb.abi.t_w_factory.FactoryRoleMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the FACTORY_ROLE method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.t_w_factory.GetImplementationMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getImplementation method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_type, version, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_type, version, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_type, version, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_type, version, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_type, version)
Validate the inputs to the getImplementation method.


### _class_ thirdweb.abi.t_w_factory.GetRoleAdminMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleAdmin method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleAdmin method.


### _class_ thirdweb.abi.t_w_factory.GetRoleMemberCountMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMemberCount method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleMemberCount method.


### _class_ thirdweb.abi.t_w_factory.GetRoleMemberMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMember method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, index, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, index, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, index, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, index, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, index)
Validate the inputs to the getRoleMember method.


### _class_ thirdweb.abi.t_w_factory.GrantRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the grantRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the grantRole method.


### _class_ thirdweb.abi.t_w_factory.HasRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the hasRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the hasRole method.


### _class_ thirdweb.abi.t_w_factory.ImplementationMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the implementation method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, index_1, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, index_1, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, index_1, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, index_1, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0, index_1)
Validate the inputs to the implementation method.


### _class_ thirdweb.abi.t_w_factory.IsTrustedForwarderMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the isTrustedForwarder method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(forwarder, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(forwarder, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(forwarder, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(forwarder, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(forwarder)
Validate the inputs to the isTrustedForwarder method.


### _class_ thirdweb.abi.t_w_factory.MulticallMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the multicall method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `List`[`Union`[`bytes`, `str`]]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(data)
Validate the inputs to the multicall method.


### _class_ thirdweb.abi.t_w_factory.RegistryMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the registry method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.t_w_factory.RenounceRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the renounceRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the renounceRole method.


### _class_ thirdweb.abi.t_w_factory.RevokeRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the revokeRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the revokeRole method.


### _class_ thirdweb.abi.t_w_factory.SupportsInterfaceMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.t_w_factory.TWFactory(web3_or_provider, contract_address, validator=None)
Bases: `object`

Wrapper class for TWFactory Solidity contract.

All method parameters of type `bytes` should be encoded as UTF-8,
which can be accomplished via `str.encode("utf_8")`.


#### \__init__(web3_or_provider, contract_address, validator=None)
Get an instance of wrapper for smart contract.


* **Parameters**

    
    * **web3_or_provider** (`Union`[`Web3`, `BaseProvider`]) – Either an instance of `web3.Web3` or
    `web3.providers.base.BaseProvider`


    * **contract_address** (`str`) – where the contract has been deployed


    * **validator** (`Optional`[`TWFactoryValidator`]) – for validation of method inputs.



#### _static_ abi()
Return the ABI to the underlying contract.


#### add_implementation(_: thirdweb.abi.t_w_factory.AddImplementationMetho_ )
Constructor-initialized instance of
`AddImplementationMethod`.


#### approval(_: thirdweb.abi.t_w_factory.ApprovalMetho_ )
Constructor-initialized instance of
`ApprovalMethod`.


#### approve_implementation(_: thirdweb.abi.t_w_factory.ApproveImplementationMetho_ )
Constructor-initialized instance of
`ApproveImplementationMethod`.


#### current_version(_: thirdweb.abi.t_w_factory.CurrentVersionMetho_ )
Constructor-initialized instance of
`CurrentVersionMethod`.


#### default_admin_role(_: thirdweb.abi.t_w_factory.DefaultAdminRoleMetho_ )
Constructor-initialized instance of
`DefaultAdminRoleMethod`.


#### deploy_proxy(_: thirdweb.abi.t_w_factory.DeployProxyMetho_ )
Constructor-initialized instance of
`DeployProxyMethod`.


#### deploy_proxy_by_implementation(_: thirdweb.abi.t_w_factory.DeployProxyByImplementationMetho_ )
Constructor-initialized instance of
`DeployProxyByImplementationMethod`.


#### deploy_proxy_deterministic(_: thirdweb.abi.t_w_factory.DeployProxyDeterministicMetho_ )
Constructor-initialized instance of
`DeployProxyDeterministicMethod`.


#### deployer(_: thirdweb.abi.t_w_factory.DeployerMetho_ )
Constructor-initialized instance of
`DeployerMethod`.


#### factory_role(_: thirdweb.abi.t_w_factory.FactoryRoleMetho_ )
Constructor-initialized instance of
`FactoryRoleMethod`.


#### get_implementation(_: thirdweb.abi.t_w_factory.GetImplementationMetho_ )
Constructor-initialized instance of
`GetImplementationMethod`.


#### get_implementation_added_event(tx_hash)
Get log entry for ImplementationAdded event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting ImplementationAdded event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_implementation_approved_event(tx_hash)
Get log entry for ImplementationApproved event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting ImplementationApproved
    event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_proxy_deployed_event(tx_hash)
Get log entry for ProxyDeployed event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting ProxyDeployed event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_admin(_: thirdweb.abi.t_w_factory.GetRoleAdminMetho_ )
Constructor-initialized instance of
`GetRoleAdminMethod`.


#### get_role_admin_changed_event(tx_hash)
Get log entry for RoleAdminChanged event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleAdminChanged event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_granted_event(tx_hash)
Get log entry for RoleGranted event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleGranted event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_member(_: thirdweb.abi.t_w_factory.GetRoleMemberMetho_ )
Constructor-initialized instance of
`GetRoleMemberMethod`.


#### get_role_member_count(_: thirdweb.abi.t_w_factory.GetRoleMemberCountMetho_ )
Constructor-initialized instance of
`GetRoleMemberCountMethod`.


#### get_role_revoked_event(tx_hash)
Get log entry for RoleRevoked event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleRevoked event



* **Return type**

    `Tuple`[`AttributeDict`]



#### grant_role(_: thirdweb.abi.t_w_factory.GrantRoleMetho_ )
Constructor-initialized instance of
`GrantRoleMethod`.


#### has_role(_: thirdweb.abi.t_w_factory.HasRoleMetho_ )
Constructor-initialized instance of
`HasRoleMethod`.


#### implementation(_: thirdweb.abi.t_w_factory.ImplementationMetho_ )
Constructor-initialized instance of
`ImplementationMethod`.


#### is_trusted_forwarder(_: thirdweb.abi.t_w_factory.IsTrustedForwarderMetho_ )
Constructor-initialized instance of
`IsTrustedForwarderMethod`.


#### multicall(_: thirdweb.abi.t_w_factory.MulticallMetho_ )
Constructor-initialized instance of
`MulticallMethod`.


#### registry(_: thirdweb.abi.t_w_factory.RegistryMetho_ )
Constructor-initialized instance of
`RegistryMethod`.


#### renounce_role(_: thirdweb.abi.t_w_factory.RenounceRoleMetho_ )
Constructor-initialized instance of
`RenounceRoleMethod`.


#### revoke_role(_: thirdweb.abi.t_w_factory.RevokeRoleMetho_ )
Constructor-initialized instance of
`RevokeRoleMethod`.


#### supports_interface(_: thirdweb.abi.t_w_factory.SupportsInterfaceMetho_ )
Constructor-initialized instance of
`SupportsInterfaceMethod`.


### _class_ thirdweb.abi.t_w_factory.TWFactoryValidator(web3_or_provider, contract_address)
Bases: `zero_ex.contract_wrappers.bases.Validator`

No-op input validator.

## thirdweb.abi.t_w_registry module

Generated wrapper for TWRegistry Solidity contract.


### _class_ thirdweb.abi.t_w_registry.AddMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the add method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(deployer, deployment, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(deployer, deployment, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(deployer, deployment, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(deployer, deployment, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(deployer, deployment)
Validate the inputs to the add method.


### _class_ thirdweb.abi.t_w_registry.CountMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the count method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(deployer, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(deployer, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(deployer, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(deployer, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(deployer)
Validate the inputs to the count method.


### _class_ thirdweb.abi.t_w_registry.DefaultAdminRoleMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the DEFAULT_ADMIN_ROLE method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.t_w_registry.GetAllMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getAll method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(deployer, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(deployer, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `List`[`str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(deployer, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(deployer, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(deployer)
Validate the inputs to the getAll method.


### _class_ thirdweb.abi.t_w_registry.GetRoleAdminMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleAdmin method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleAdmin method.


### _class_ thirdweb.abi.t_w_registry.GetRoleMemberCountMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMemberCount method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleMemberCount method.


### _class_ thirdweb.abi.t_w_registry.GetRoleMemberMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMember method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, index, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, index, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, index, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, index, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, index)
Validate the inputs to the getRoleMember method.


### _class_ thirdweb.abi.t_w_registry.GrantRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the grantRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the grantRole method.


### _class_ thirdweb.abi.t_w_registry.HasRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the hasRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the hasRole method.


### _class_ thirdweb.abi.t_w_registry.IsTrustedForwarderMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the isTrustedForwarder method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(forwarder, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(forwarder, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(forwarder, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(forwarder, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(forwarder)
Validate the inputs to the isTrustedForwarder method.


### _class_ thirdweb.abi.t_w_registry.MulticallMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the multicall method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `List`[`Union`[`bytes`, `str`]]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(data)
Validate the inputs to the multicall method.


### _class_ thirdweb.abi.t_w_registry.OperatorRoleMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the OPERATOR_ROLE method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.t_w_registry.RemoveMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the remove method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(deployer, deployment, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(deployer, deployment, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(deployer, deployment, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(deployer, deployment, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(deployer, deployment)
Validate the inputs to the remove method.


### _class_ thirdweb.abi.t_w_registry.RenounceRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the renounceRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the renounceRole method.


### _class_ thirdweb.abi.t_w_registry.RevokeRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the revokeRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the revokeRole method.


### _class_ thirdweb.abi.t_w_registry.SupportsInterfaceMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.t_w_registry.TWRegistry(web3_or_provider, contract_address, validator=None)
Bases: `object`

Wrapper class for TWRegistry Solidity contract.


#### \__init__(web3_or_provider, contract_address, validator=None)
Get an instance of wrapper for smart contract.


* **Parameters**

    
    * **web3_or_provider** (`Union`[`Web3`, `BaseProvider`]) – Either an instance of `web3.Web3` or
    `web3.providers.base.BaseProvider`


    * **contract_address** (`str`) – where the contract has been deployed


    * **validator** (`Optional`[`TWRegistryValidator`]) – for validation of method inputs.



#### _static_ abi()
Return the ABI to the underlying contract.


#### add(_: thirdweb.abi.t_w_registry.AddMetho_ )
Constructor-initialized instance of
`AddMethod`.


#### count(_: thirdweb.abi.t_w_registry.CountMetho_ )
Constructor-initialized instance of
`CountMethod`.


#### default_admin_role(_: thirdweb.abi.t_w_registry.DefaultAdminRoleMetho_ )
Constructor-initialized instance of
`DefaultAdminRoleMethod`.


#### get_added_event(tx_hash)
Get log entry for Added event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Added event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_all(_: thirdweb.abi.t_w_registry.GetAllMetho_ )
Constructor-initialized instance of
`GetAllMethod`.


#### get_deleted_event(tx_hash)
Get log entry for Deleted event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Deleted event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_admin(_: thirdweb.abi.t_w_registry.GetRoleAdminMetho_ )
Constructor-initialized instance of
`GetRoleAdminMethod`.


#### get_role_admin_changed_event(tx_hash)
Get log entry for RoleAdminChanged event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleAdminChanged event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_granted_event(tx_hash)
Get log entry for RoleGranted event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleGranted event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_member(_: thirdweb.abi.t_w_registry.GetRoleMemberMetho_ )
Constructor-initialized instance of
`GetRoleMemberMethod`.


#### get_role_member_count(_: thirdweb.abi.t_w_registry.GetRoleMemberCountMetho_ )
Constructor-initialized instance of
`GetRoleMemberCountMethod`.


#### get_role_revoked_event(tx_hash)
Get log entry for RoleRevoked event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleRevoked event



* **Return type**

    `Tuple`[`AttributeDict`]



#### grant_role(_: thirdweb.abi.t_w_registry.GrantRoleMetho_ )
Constructor-initialized instance of
`GrantRoleMethod`.


#### has_role(_: thirdweb.abi.t_w_registry.HasRoleMetho_ )
Constructor-initialized instance of
`HasRoleMethod`.


#### is_trusted_forwarder(_: thirdweb.abi.t_w_registry.IsTrustedForwarderMetho_ )
Constructor-initialized instance of
`IsTrustedForwarderMethod`.


#### multicall(_: thirdweb.abi.t_w_registry.MulticallMetho_ )
Constructor-initialized instance of
`MulticallMethod`.


#### operator_role(_: thirdweb.abi.t_w_registry.OperatorRoleMetho_ )
Constructor-initialized instance of
`OperatorRoleMethod`.


#### remove(_: thirdweb.abi.t_w_registry.RemoveMetho_ )
Constructor-initialized instance of
`RemoveMethod`.


#### renounce_role(_: thirdweb.abi.t_w_registry.RenounceRoleMetho_ )
Constructor-initialized instance of
`RenounceRoleMethod`.


#### revoke_role(_: thirdweb.abi.t_w_registry.RevokeRoleMetho_ )
Constructor-initialized instance of
`RevokeRoleMethod`.


#### supports_interface(_: thirdweb.abi.t_w_registry.SupportsInterfaceMetho_ )
Constructor-initialized instance of
`SupportsInterfaceMethod`.


### _class_ thirdweb.abi.t_w_registry.TWRegistryValidator(web3_or_provider, contract_address)
Bases: `zero_ex.contract_wrappers.bases.Validator`

No-op input validator.

## thirdweb.abi.token_erc1155 module

Generated wrapper for TokenERC1155 Solidity contract.


### _class_ thirdweb.abi.token_erc1155.BalanceOfBatchMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the balanceOfBatch method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(accounts, ids, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(accounts, ids, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `List`[`int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(accounts, ids, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(accounts, ids, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(accounts, ids)
Validate the inputs to the balanceOfBatch method.


### _class_ thirdweb.abi.token_erc1155.BalanceOfMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the balanceOf method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, _id, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, _id, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, _id, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, _id, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account, _id)
Validate the inputs to the balanceOf method.


### _class_ thirdweb.abi.token_erc1155.BurnBatchMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the burnBatch method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, ids, values, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, ids, values, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, ids, values, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, ids, values, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account, ids, values)
Validate the inputs to the burnBatch method.


### _class_ thirdweb.abi.token_erc1155.BurnMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the burn method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, _id, value, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, _id, value, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, _id, value, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, _id, value, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account, _id, value)
Validate the inputs to the burn method.


### _class_ thirdweb.abi.token_erc1155.ContractTypeMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractType method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.ContractUriMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractURI method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.ContractVersionMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractVersion method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.DefaultAdminRoleMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the DEFAULT_ADMIN_ROLE method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.GetDefaultRoyaltyInfoMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getDefaultRoyaltyInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`str`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.GetPlatformFeeInfoMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getPlatformFeeInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`str`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.GetRoleAdminMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleAdmin method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleAdmin method.


### _class_ thirdweb.abi.token_erc1155.GetRoleMemberCountMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMemberCount method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleMemberCount method.


### _class_ thirdweb.abi.token_erc1155.GetRoleMemberMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMember method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, index, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, index, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, index, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, index, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, index)
Validate the inputs to the getRoleMember method.


### _class_ thirdweb.abi.token_erc1155.GetRoyaltyInfoForTokenMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoyaltyInfoForToken method.


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

    `Tuple`[`str`, `int`]



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
Validate the inputs to the getRoyaltyInfoForToken method.


### _class_ thirdweb.abi.token_erc1155.GrantRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the grantRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the grantRole method.


### _class_ thirdweb.abi.token_erc1155.HasRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the hasRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the hasRole method.


### _class_ thirdweb.abi.token_erc1155.ITokenERC1155MintRequest(\*args, \*\*kwargs)
Bases: `dict`

Python representation of a tuple or struct.

Solidity compiler output does not include the names of structs that appear
in method definitions.  A tuple found in an ABI may have been written in
Solidity as a literal, anonymous tuple, or it may have been written as a
named `struct`, but there is no way to tell from the compiler
output.  This class represents a tuple that appeared in a method
definition.  Its name is derived from a hash of that tuple’s field names,
and every method whose ABI refers to a tuple with that same list of field
names will have a generated wrapper method that refers to this class.

Any members of type `bytes` should be encoded as UTF-8, which can be
accomplished via `str.encode("utf_8")`


#### currency(_: st_ )

#### pricePerToken(_: in_ )

#### primarySaleRecipient(_: st_ )

#### quantity(_: in_ )

#### royaltyBps(_: in_ )

#### royaltyRecipient(_: st_ )

#### to(_: st_ )

#### tokenId(_: in_ )

#### uid(_: Union[bytes, str_ )

#### uri(_: st_ )

#### validityEndTimestamp(_: in_ )

#### validityStartTimestamp(_: in_ )

### _class_ thirdweb.abi.token_erc1155.InitializeMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the initialize method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(default_admin, name, symbol, contract_uri, trusted_forwarders, primary_sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(default_admin, name, symbol, contract_uri, trusted_forwarders, primary_sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(default_admin, name, symbol, contract_uri, trusted_forwarders, primary_sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(default_admin, name, symbol, contract_uri, trusted_forwarders, primary_sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, primary_sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient)
Validate the inputs to the initialize method.


### _class_ thirdweb.abi.token_erc1155.IsApprovedForAllMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the isApprovedForAll method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, operator, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, operator, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, operator, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, operator, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account, operator)
Validate the inputs to the isApprovedForAll method.


### _class_ thirdweb.abi.token_erc1155.IsTrustedForwarderMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the isTrustedForwarder method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(forwarder, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(forwarder, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(forwarder, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(forwarder, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(forwarder)
Validate the inputs to the isTrustedForwarder method.


### _class_ thirdweb.abi.token_erc1155.MintToMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the mintTo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(to, token_id, uri, amount, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(to, token_id, uri, amount, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(to, token_id, uri, amount, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(to, token_id, uri, amount, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(to, token_id, uri, amount)
Validate the inputs to the mintTo method.


### _class_ thirdweb.abi.token_erc1155.MintWithSignatureMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the mintWithSignature method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(req, signature, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(req, signature, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(req, signature, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(req, signature, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(req, signature)
Validate the inputs to the mintWithSignature method.


### _class_ thirdweb.abi.token_erc1155.MulticallMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the multicall method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `List`[`Union`[`bytes`, `str`]]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(data)
Validate the inputs to the multicall method.


### _class_ thirdweb.abi.token_erc1155.NameMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the name method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.NextTokenIdToMintMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the nextTokenIdToMint method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.OwnerMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the owner method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.PlatformFeeBpsMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the platformFeeBps method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.PlatformFeeRecipientMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the platformFeeRecipient method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.PrimarySaleRecipientMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the primarySaleRecipient method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.RenounceRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the renounceRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the renounceRole method.


### _class_ thirdweb.abi.token_erc1155.RevokeRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the revokeRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the revokeRole method.


### _class_ thirdweb.abi.token_erc1155.RoyaltyInfoMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the royaltyInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(token_id, sale_price, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(token_id, sale_price, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`str`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(token_id, sale_price, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(token_id, sale_price, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(token_id, sale_price)
Validate the inputs to the royaltyInfo method.


### _class_ thirdweb.abi.token_erc1155.SafeBatchTransferFromMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the safeBatchTransferFrom method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_from, to, ids, amounts, data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_from, to, ids, amounts, data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_from, to, ids, amounts, data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_from, to, ids, amounts, data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_from, to, ids, amounts, data)
Validate the inputs to the safeBatchTransferFrom method.


### _class_ thirdweb.abi.token_erc1155.SafeTransferFromMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the safeTransferFrom method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_from, to, _id, amount, data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_from, to, _id, amount, data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_from, to, _id, amount, data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_from, to, _id, amount, data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_from, to, _id, amount, data)
Validate the inputs to the safeTransferFrom method.


### _class_ thirdweb.abi.token_erc1155.SaleRecipientForTokenMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the saleRecipientForToken method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0)
Validate the inputs to the saleRecipientForToken method.


### _class_ thirdweb.abi.token_erc1155.SetApprovalForAllMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc1155.SetContractUriMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setContractURI method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(uri, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(uri, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(uri, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(uri, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(uri)
Validate the inputs to the setContractURI method.


### _class_ thirdweb.abi.token_erc1155.SetDefaultRoyaltyInfoMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setDefaultRoyaltyInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(royalty_recipient, royalty_bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(royalty_recipient, royalty_bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(royalty_recipient, royalty_bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(royalty_recipient, royalty_bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(royalty_recipient, royalty_bps)
Validate the inputs to the setDefaultRoyaltyInfo method.


### _class_ thirdweb.abi.token_erc1155.SetOwnerMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setOwner method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(new_owner, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(new_owner, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(new_owner, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(new_owner, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(new_owner)
Validate the inputs to the setOwner method.


### _class_ thirdweb.abi.token_erc1155.SetPlatformFeeInfoMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setPlatformFeeInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(platform_fee_recipient, platform_fee_bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(platform_fee_recipient, platform_fee_bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
Validate the inputs to the setPlatformFeeInfo method.


### _class_ thirdweb.abi.token_erc1155.SetPrimarySaleRecipientMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setPrimarySaleRecipient method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(sale_recipient, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(sale_recipient, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(sale_recipient, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(sale_recipient, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(sale_recipient)
Validate the inputs to the setPrimarySaleRecipient method.


### _class_ thirdweb.abi.token_erc1155.SetRoyaltyInfoForTokenMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setRoyaltyInfoForToken method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(token_id, recipient, bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(token_id, recipient, bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(token_id, recipient, bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(token_id, recipient, bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(token_id, recipient, bps)
Validate the inputs to the setRoyaltyInfoForToken method.


### _class_ thirdweb.abi.token_erc1155.SupportsInterfaceMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc1155.SymbolMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the symbol method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.ThirdwebFeeMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the thirdwebFee method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc1155.TokenERC1155(web3_or_provider, contract_address, validator=None)
Bases: `object`

Wrapper class for TokenERC1155 Solidity contract.

All method parameters of type `bytes` should be encoded as UTF-8,
which can be accomplished via `str.encode("utf_8")`.


#### \__init__(web3_or_provider, contract_address, validator=None)
Get an instance of wrapper for smart contract.


* **Parameters**

    
    * **web3_or_provider** (`Union`[`Web3`, `BaseProvider`]) – Either an instance of `web3.Web3` or
    `web3.providers.base.BaseProvider`


    * **contract_address** (`str`) – where the contract has been deployed


    * **validator** (`Optional`[`TokenERC1155Validator`]) – for validation of method inputs.



#### _static_ abi()
Return the ABI to the underlying contract.


#### balance_of(_: thirdweb.abi.token_erc1155.BalanceOfMetho_ )
Constructor-initialized instance of
`BalanceOfMethod`.


#### balance_of_batch(_: thirdweb.abi.token_erc1155.BalanceOfBatchMetho_ )
Constructor-initialized instance of
`BalanceOfBatchMethod`.


#### burn(_: thirdweb.abi.token_erc1155.BurnMetho_ )
Constructor-initialized instance of
`BurnMethod`.


#### burn_batch(_: thirdweb.abi.token_erc1155.BurnBatchMetho_ )
Constructor-initialized instance of
`BurnBatchMethod`.


#### contract_type(_: thirdweb.abi.token_erc1155.ContractTypeMetho_ )
Constructor-initialized instance of
`ContractTypeMethod`.


#### contract_uri(_: thirdweb.abi.token_erc1155.ContractUriMetho_ )
Constructor-initialized instance of
`ContractUriMethod`.


#### contract_version(_: thirdweb.abi.token_erc1155.ContractVersionMetho_ )
Constructor-initialized instance of
`ContractVersionMethod`.


#### default_admin_role(_: thirdweb.abi.token_erc1155.DefaultAdminRoleMetho_ )
Constructor-initialized instance of
`DefaultAdminRoleMethod`.


#### get_approval_for_all_event(tx_hash)
Get log entry for ApprovalForAll event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting ApprovalForAll event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_default_royalty_event(tx_hash)
Get log entry for DefaultRoyalty event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting DefaultRoyalty event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_default_royalty_info(_: thirdweb.abi.token_erc1155.GetDefaultRoyaltyInfoMetho_ )
Constructor-initialized instance of
`GetDefaultRoyaltyInfoMethod`.


#### get_owner_updated_event(tx_hash)
Get log entry for OwnerUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting OwnerUpdated event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_platform_fee_info(_: thirdweb.abi.token_erc1155.GetPlatformFeeInfoMetho_ )
Constructor-initialized instance of
`GetPlatformFeeInfoMethod`.


#### get_platform_fee_info_updated_event(tx_hash)
Get log entry for PlatformFeeInfoUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting PlatformFeeInfoUpdated
    event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_primary_sale_recipient_updated_event(tx_hash)
Get log entry for PrimarySaleRecipientUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting
    PrimarySaleRecipientUpdated event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_admin(_: thirdweb.abi.token_erc1155.GetRoleAdminMetho_ )
Constructor-initialized instance of
`GetRoleAdminMethod`.


#### get_role_admin_changed_event(tx_hash)
Get log entry for RoleAdminChanged event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleAdminChanged event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_granted_event(tx_hash)
Get log entry for RoleGranted event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleGranted event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_member(_: thirdweb.abi.token_erc1155.GetRoleMemberMetho_ )
Constructor-initialized instance of
`GetRoleMemberMethod`.


#### get_role_member_count(_: thirdweb.abi.token_erc1155.GetRoleMemberCountMetho_ )
Constructor-initialized instance of
`GetRoleMemberCountMethod`.


#### get_role_revoked_event(tx_hash)
Get log entry for RoleRevoked event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleRevoked event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_royalty_for_token_event(tx_hash)
Get log entry for RoyaltyForToken event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoyaltyForToken event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_royalty_info_for_token(_: thirdweb.abi.token_erc1155.GetRoyaltyInfoForTokenMetho_ )
Constructor-initialized instance of
`GetRoyaltyInfoForTokenMethod`.


#### get_tokens_minted_event(tx_hash)
Get log entry for TokensMinted event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting TokensMinted event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_tokens_minted_with_signature_event(tx_hash)
Get log entry for TokensMintedWithSignature event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting TokensMintedWithSignature
    event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_transfer_batch_event(tx_hash)
Get log entry for TransferBatch event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting TransferBatch event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_transfer_single_event(tx_hash)
Get log entry for TransferSingle event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting TransferSingle event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_uri_event(tx_hash)
Get log entry for URI event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting URI event



* **Return type**

    `Tuple`[`AttributeDict`]



#### grant_role(_: thirdweb.abi.token_erc1155.GrantRoleMetho_ )
Constructor-initialized instance of
`GrantRoleMethod`.


#### has_role(_: thirdweb.abi.token_erc1155.HasRoleMetho_ )
Constructor-initialized instance of
`HasRoleMethod`.


#### initialize(_: thirdweb.abi.token_erc1155.InitializeMetho_ )
Constructor-initialized instance of
`InitializeMethod`.


#### is_approved_for_all(_: thirdweb.abi.token_erc1155.IsApprovedForAllMetho_ )
Constructor-initialized instance of
`IsApprovedForAllMethod`.


#### is_trusted_forwarder(_: thirdweb.abi.token_erc1155.IsTrustedForwarderMetho_ )
Constructor-initialized instance of
`IsTrustedForwarderMethod`.


#### mint_to(_: thirdweb.abi.token_erc1155.MintToMetho_ )
Constructor-initialized instance of
`MintToMethod`.


#### mint_with_signature(_: thirdweb.abi.token_erc1155.MintWithSignatureMetho_ )
Constructor-initialized instance of
`MintWithSignatureMethod`.


#### multicall(_: thirdweb.abi.token_erc1155.MulticallMetho_ )
Constructor-initialized instance of
`MulticallMethod`.


#### name(_: thirdweb.abi.token_erc1155.NameMetho_ )
Constructor-initialized instance of
`NameMethod`.


#### next_token_id_to_mint(_: thirdweb.abi.token_erc1155.NextTokenIdToMintMetho_ )
Constructor-initialized instance of
`NextTokenIdToMintMethod`.


#### owner(_: thirdweb.abi.token_erc1155.OwnerMetho_ )
Constructor-initialized instance of
`OwnerMethod`.


#### platform_fee_bps(_: thirdweb.abi.token_erc1155.PlatformFeeBpsMetho_ )
Constructor-initialized instance of
`PlatformFeeBpsMethod`.


#### platform_fee_recipient(_: thirdweb.abi.token_erc1155.PlatformFeeRecipientMetho_ )
Constructor-initialized instance of
`PlatformFeeRecipientMethod`.


#### primary_sale_recipient(_: thirdweb.abi.token_erc1155.PrimarySaleRecipientMetho_ )
Constructor-initialized instance of
`PrimarySaleRecipientMethod`.


#### renounce_role(_: thirdweb.abi.token_erc1155.RenounceRoleMetho_ )
Constructor-initialized instance of
`RenounceRoleMethod`.


#### revoke_role(_: thirdweb.abi.token_erc1155.RevokeRoleMetho_ )
Constructor-initialized instance of
`RevokeRoleMethod`.


#### royalty_info(_: thirdweb.abi.token_erc1155.RoyaltyInfoMetho_ )
Constructor-initialized instance of
`RoyaltyInfoMethod`.


#### safe_batch_transfer_from(_: thirdweb.abi.token_erc1155.SafeBatchTransferFromMetho_ )
Constructor-initialized instance of
`SafeBatchTransferFromMethod`.


#### safe_transfer_from(_: thirdweb.abi.token_erc1155.SafeTransferFromMetho_ )
Constructor-initialized instance of
`SafeTransferFromMethod`.


#### sale_recipient_for_token(_: thirdweb.abi.token_erc1155.SaleRecipientForTokenMetho_ )
Constructor-initialized instance of
`SaleRecipientForTokenMethod`.


#### set_approval_for_all(_: thirdweb.abi.token_erc1155.SetApprovalForAllMetho_ )
Constructor-initialized instance of
`SetApprovalForAllMethod`.


#### set_contract_uri(_: thirdweb.abi.token_erc1155.SetContractUriMetho_ )
Constructor-initialized instance of
`SetContractUriMethod`.


#### set_default_royalty_info(_: thirdweb.abi.token_erc1155.SetDefaultRoyaltyInfoMetho_ )
Constructor-initialized instance of
`SetDefaultRoyaltyInfoMethod`.


#### set_owner(_: thirdweb.abi.token_erc1155.SetOwnerMetho_ )
Constructor-initialized instance of
`SetOwnerMethod`.


#### set_platform_fee_info(_: thirdweb.abi.token_erc1155.SetPlatformFeeInfoMetho_ )
Constructor-initialized instance of
`SetPlatformFeeInfoMethod`.


#### set_primary_sale_recipient(_: thirdweb.abi.token_erc1155.SetPrimarySaleRecipientMetho_ )
Constructor-initialized instance of
`SetPrimarySaleRecipientMethod`.


#### set_royalty_info_for_token(_: thirdweb.abi.token_erc1155.SetRoyaltyInfoForTokenMetho_ )
Constructor-initialized instance of
`SetRoyaltyInfoForTokenMethod`.


#### supports_interface(_: thirdweb.abi.token_erc1155.SupportsInterfaceMetho_ )
Constructor-initialized instance of
`SupportsInterfaceMethod`.


#### symbol(_: thirdweb.abi.token_erc1155.SymbolMetho_ )
Constructor-initialized instance of
`SymbolMethod`.


#### thirdweb_fee(_: thirdweb.abi.token_erc1155.ThirdwebFeeMetho_ )
Constructor-initialized instance of
`ThirdwebFeeMethod`.


#### total_supply(_: thirdweb.abi.token_erc1155.TotalSupplyMetho_ )
Constructor-initialized instance of
`TotalSupplyMethod`.


#### uri(_: thirdweb.abi.token_erc1155.UriMetho_ )
Constructor-initialized instance of
`UriMethod`.


#### verify(_: thirdweb.abi.token_erc1155.VerifyMetho_ )
Constructor-initialized instance of
`VerifyMethod`.


### _class_ thirdweb.abi.token_erc1155.TokenERC1155Validator(web3_or_provider, contract_address)
Bases: `zero_ex.contract_wrappers.bases.Validator`

No-op input validator.


### _class_ thirdweb.abi.token_erc1155.TotalSupplyMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the totalSupply method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index_0, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index_0, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index_0, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index_0, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index_0)
Validate the inputs to the totalSupply method.


### _class_ thirdweb.abi.token_erc1155.UriMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the uri method.


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
Validate the inputs to the uri method.


### _class_ thirdweb.abi.token_erc1155.VerifyMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the verify method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(req, signature, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(req, signature, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`bool`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(req, signature, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(req, signature, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(req, signature)
Validate the inputs to the verify method.

## thirdweb.abi.token_erc20 module

Generated wrapper for TokenERC20 Solidity contract.


### _class_ thirdweb.abi.token_erc20.AllowanceMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the allowance method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(owner, spender, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(owner, spender, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(owner, spender, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(owner, spender, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(owner, spender)
Validate the inputs to the allowance method.


### _class_ thirdweb.abi.token_erc20.ApproveMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the approve method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(spender, amount, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(spender, amount, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(spender, amount, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(spender, amount, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(spender, amount)
Validate the inputs to the approve method.


### _class_ thirdweb.abi.token_erc20.BalanceOfMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the balanceOf method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account)
Validate the inputs to the balanceOf method.


### _class_ thirdweb.abi.token_erc20.BurnFromMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the burnFrom method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, amount, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, amount, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, amount, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, amount, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account, amount)
Validate the inputs to the burnFrom method.


### _class_ thirdweb.abi.token_erc20.BurnMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the burn method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(amount, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(amount, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(amount, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(amount, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(amount)
Validate the inputs to the burn method.


### _class_ thirdweb.abi.token_erc20.CheckpointsMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the checkpoints method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, pos, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, pos, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `ERC20VotesUpgradeableCheckpoint`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, pos, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, pos, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account, pos)
Validate the inputs to the checkpoints method.


### _class_ thirdweb.abi.token_erc20.ContractTypeMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractType method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.ContractUriMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractURI method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.ContractVersionMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractVersion method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.DecimalsMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the decimals method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.DecreaseAllowanceMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the decreaseAllowance method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(spender, subtracted_value, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(spender, subtracted_value, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(spender, subtracted_value, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(spender, subtracted_value, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(spender, subtracted_value)
Validate the inputs to the decreaseAllowance method.


### _class_ thirdweb.abi.token_erc20.DefaultAdminRoleMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the DEFAULT_ADMIN_ROLE method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.DelegateBySigMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the delegateBySig method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(delegatee, nonce, expiry, v, r, s, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(delegatee, nonce, expiry, v, r, s, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(delegatee, nonce, expiry, v, r, s, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(delegatee, nonce, expiry, v, r, s, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(delegatee, nonce, expiry, v, r, s)
Validate the inputs to the delegateBySig method.


### _class_ thirdweb.abi.token_erc20.DelegateMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the delegate method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(delegatee, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(delegatee, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(delegatee, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(delegatee, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(delegatee)
Validate the inputs to the delegate method.


### _class_ thirdweb.abi.token_erc20.DelegatesMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the delegates method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account)
Validate the inputs to the delegates method.


### _class_ thirdweb.abi.token_erc20.DomainSeparatorMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the DOMAIN_SEPARATOR method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.ERC20VotesUpgradeableCheckpoint(\*args, \*\*kwargs)
Bases: `dict`

Python representation of a tuple or struct.

Solidity compiler output does not include the names of structs that appear
in method definitions.  A tuple found in an ABI may have been written in
Solidity as a literal, anonymous tuple, or it may have been written as a
named `struct`, but there is no way to tell from the compiler
output.  This class represents a tuple that appeared in a method
definition.  Its name is derived from a hash of that tuple’s field names,
and every method whose ABI refers to a tuple with that same list of field
names will have a generated wrapper method that refers to this class.

Any members of type `bytes` should be encoded as UTF-8, which can be
accomplished via `str.encode("utf_8")`


#### fromBlock(_: in_ )

#### votes(_: in_ )

### _class_ thirdweb.abi.token_erc20.GetPastTotalSupplyMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getPastTotalSupply method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(block_number, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(block_number, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(block_number, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(block_number, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(block_number)
Validate the inputs to the getPastTotalSupply method.


### _class_ thirdweb.abi.token_erc20.GetPastVotesMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getPastVotes method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, block_number, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, block_number, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, block_number, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, block_number, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account, block_number)
Validate the inputs to the getPastVotes method.


### _class_ thirdweb.abi.token_erc20.GetPlatformFeeInfoMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getPlatformFeeInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`str`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.GetRoleAdminMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleAdmin method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleAdmin method.


### _class_ thirdweb.abi.token_erc20.GetRoleMemberCountMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMemberCount method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleMemberCount method.


### _class_ thirdweb.abi.token_erc20.GetRoleMemberMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMember method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, index, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, index, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, index, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, index, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, index)
Validate the inputs to the getRoleMember method.


### _class_ thirdweb.abi.token_erc20.GetVotesMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getVotes method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account)
Validate the inputs to the getVotes method.


### _class_ thirdweb.abi.token_erc20.GrantRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the grantRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the grantRole method.


### _class_ thirdweb.abi.token_erc20.HasRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the hasRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the hasRole method.


### _class_ thirdweb.abi.token_erc20.ITokenERC20MintRequest(\*args, \*\*kwargs)
Bases: `dict`

Python representation of a tuple or struct.

Solidity compiler output does not include the names of structs that appear
in method definitions.  A tuple found in an ABI may have been written in
Solidity as a literal, anonymous tuple, or it may have been written as a
named `struct`, but there is no way to tell from the compiler
output.  This class represents a tuple that appeared in a method
definition.  Its name is derived from a hash of that tuple’s field names,
and every method whose ABI refers to a tuple with that same list of field
names will have a generated wrapper method that refers to this class.

Any members of type `bytes` should be encoded as UTF-8, which can be
accomplished via `str.encode("utf_8")`


#### currency(_: st_ )

#### price(_: in_ )

#### primarySaleRecipient(_: st_ )

#### quantity(_: in_ )

#### to(_: st_ )

#### uid(_: Union[bytes, str_ )

#### validityEndTimestamp(_: in_ )

#### validityStartTimestamp(_: in_ )

### _class_ thirdweb.abi.token_erc20.IncreaseAllowanceMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the increaseAllowance method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(spender, added_value, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(spender, added_value, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(spender, added_value, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(spender, added_value, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(spender, added_value)
Validate the inputs to the increaseAllowance method.


### _class_ thirdweb.abi.token_erc20.InitializeMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the initialize method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(default_admin, name, symbol, contract_uri, trusted_forwarders, primary_sale_recipient, platform_fee_recipient, platform_fee_bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(default_admin, name, symbol, contract_uri, trusted_forwarders, primary_sale_recipient, platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(default_admin, name, symbol, contract_uri, trusted_forwarders, primary_sale_recipient, platform_fee_recipient, platform_fee_bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(default_admin, name, symbol, contract_uri, trusted_forwarders, primary_sale_recipient, platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, primary_sale_recipient, platform_fee_recipient, platform_fee_bps)
Validate the inputs to the initialize method.


### _class_ thirdweb.abi.token_erc20.IsTrustedForwarderMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the isTrustedForwarder method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(forwarder, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(forwarder, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(forwarder, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(forwarder, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(forwarder)
Validate the inputs to the isTrustedForwarder method.


### _class_ thirdweb.abi.token_erc20.MintToMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the mintTo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(to, amount, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(to, amount, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(to, amount, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(to, amount, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(to, amount)
Validate the inputs to the mintTo method.


### _class_ thirdweb.abi.token_erc20.MintWithSignatureMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the mintWithSignature method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(req, signature, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(req, signature, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(req, signature, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(req, signature, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(req, signature)
Validate the inputs to the mintWithSignature method.


### _class_ thirdweb.abi.token_erc20.MulticallMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the multicall method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `List`[`Union`[`bytes`, `str`]]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(data)
Validate the inputs to the multicall method.


### _class_ thirdweb.abi.token_erc20.NameMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the name method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.NoncesMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the nonces method.


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
Validate the inputs to the nonces method.


### _class_ thirdweb.abi.token_erc20.NumCheckpointsMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the numCheckpoints method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(account)
Validate the inputs to the numCheckpoints method.


### _class_ thirdweb.abi.token_erc20.PauseMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the pause method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.PausedMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the paused method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.PermitMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the permit method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(owner, spender, value, deadline, v, r, s, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(owner, spender, value, deadline, v, r, s, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(owner, spender, value, deadline, v, r, s, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(owner, spender, value, deadline, v, r, s, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(owner, spender, value, deadline, v, r, s)
Validate the inputs to the permit method.


### _class_ thirdweb.abi.token_erc20.PrimarySaleRecipientMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the primarySaleRecipient method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.RenounceRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the renounceRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the renounceRole method.


### _class_ thirdweb.abi.token_erc20.RevokeRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the revokeRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the revokeRole method.


### _class_ thirdweb.abi.token_erc20.SetContractUriMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setContractURI method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(uri, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(uri, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(uri, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(uri, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(uri)
Validate the inputs to the setContractURI method.


### _class_ thirdweb.abi.token_erc20.SetPlatformFeeInfoMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setPlatformFeeInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(platform_fee_recipient, platform_fee_bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(platform_fee_recipient, platform_fee_bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
Validate the inputs to the setPlatformFeeInfo method.


### _class_ thirdweb.abi.token_erc20.SetPrimarySaleRecipientMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setPrimarySaleRecipient method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(sale_recipient, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(sale_recipient, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(sale_recipient, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(sale_recipient, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(sale_recipient)
Validate the inputs to the setPrimarySaleRecipient method.


### _class_ thirdweb.abi.token_erc20.SupportsInterfaceMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc20.SymbolMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the symbol method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.TokenERC20(web3_or_provider, contract_address, validator=None)
Bases: `object`

Wrapper class for TokenERC20 Solidity contract.

All method parameters of type `bytes` should be encoded as UTF-8,
which can be accomplished via `str.encode("utf_8")`.


#### \__init__(web3_or_provider, contract_address, validator=None)
Get an instance of wrapper for smart contract.


* **Parameters**

    
    * **web3_or_provider** (`Union`[`Web3`, `BaseProvider`]) – Either an instance of `web3.Web3` or
    `web3.providers.base.BaseProvider`


    * **contract_address** (`str`) – where the contract has been deployed


    * **validator** (`Optional`[`TokenERC20Validator`]) – for validation of method inputs.



#### _static_ abi()
Return the ABI to the underlying contract.


#### allowance(_: thirdweb.abi.token_erc20.AllowanceMetho_ )
Constructor-initialized instance of
`AllowanceMethod`.


#### approve(_: thirdweb.abi.token_erc20.ApproveMetho_ )
Constructor-initialized instance of
`ApproveMethod`.


#### balance_of(_: thirdweb.abi.token_erc20.BalanceOfMetho_ )
Constructor-initialized instance of
`BalanceOfMethod`.


#### burn(_: thirdweb.abi.token_erc20.BurnMetho_ )
Constructor-initialized instance of
`BurnMethod`.


#### burn_from(_: thirdweb.abi.token_erc20.BurnFromMetho_ )
Constructor-initialized instance of
`BurnFromMethod`.


#### checkpoints(_: thirdweb.abi.token_erc20.CheckpointsMetho_ )
Constructor-initialized instance of
`CheckpointsMethod`.


#### contract_type(_: thirdweb.abi.token_erc20.ContractTypeMetho_ )
Constructor-initialized instance of
`ContractTypeMethod`.


#### contract_uri(_: thirdweb.abi.token_erc20.ContractUriMetho_ )
Constructor-initialized instance of
`ContractUriMethod`.


#### contract_version(_: thirdweb.abi.token_erc20.ContractVersionMetho_ )
Constructor-initialized instance of
`ContractVersionMethod`.


#### decimals(_: thirdweb.abi.token_erc20.DecimalsMetho_ )
Constructor-initialized instance of
`DecimalsMethod`.


#### decrease_allowance(_: thirdweb.abi.token_erc20.DecreaseAllowanceMetho_ )
Constructor-initialized instance of
`DecreaseAllowanceMethod`.


#### default_admin_role(_: thirdweb.abi.token_erc20.DefaultAdminRoleMetho_ )
Constructor-initialized instance of
`DefaultAdminRoleMethod`.


#### delegate(_: thirdweb.abi.token_erc20.DelegateMetho_ )
Constructor-initialized instance of
`DelegateMethod`.


#### delegate_by_sig(_: thirdweb.abi.token_erc20.DelegateBySigMetho_ )
Constructor-initialized instance of
`DelegateBySigMethod`.


#### delegates(_: thirdweb.abi.token_erc20.DelegatesMetho_ )
Constructor-initialized instance of
`DelegatesMethod`.


#### domain_separator(_: thirdweb.abi.token_erc20.DomainSeparatorMetho_ )
Constructor-initialized instance of
`DomainSeparatorMethod`.


#### get_approval_event(tx_hash)
Get log entry for Approval event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Approval event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_delegate_changed_event(tx_hash)
Get log entry for DelegateChanged event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting DelegateChanged event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_delegate_votes_changed_event(tx_hash)
Get log entry for DelegateVotesChanged event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting DelegateVotesChanged event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_past_total_supply(_: thirdweb.abi.token_erc20.GetPastTotalSupplyMetho_ )
Constructor-initialized instance of
`GetPastTotalSupplyMethod`.


#### get_past_votes(_: thirdweb.abi.token_erc20.GetPastVotesMetho_ )
Constructor-initialized instance of
`GetPastVotesMethod`.


#### get_paused_event(tx_hash)
Get log entry for Paused event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Paused event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_platform_fee_info(_: thirdweb.abi.token_erc20.GetPlatformFeeInfoMetho_ )
Constructor-initialized instance of
`GetPlatformFeeInfoMethod`.


#### get_platform_fee_info_updated_event(tx_hash)
Get log entry for PlatformFeeInfoUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting PlatformFeeInfoUpdated
    event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_primary_sale_recipient_updated_event(tx_hash)
Get log entry for PrimarySaleRecipientUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting
    PrimarySaleRecipientUpdated event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_admin(_: thirdweb.abi.token_erc20.GetRoleAdminMetho_ )
Constructor-initialized instance of
`GetRoleAdminMethod`.


#### get_role_admin_changed_event(tx_hash)
Get log entry for RoleAdminChanged event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleAdminChanged event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_granted_event(tx_hash)
Get log entry for RoleGranted event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleGranted event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_member(_: thirdweb.abi.token_erc20.GetRoleMemberMetho_ )
Constructor-initialized instance of
`GetRoleMemberMethod`.


#### get_role_member_count(_: thirdweb.abi.token_erc20.GetRoleMemberCountMetho_ )
Constructor-initialized instance of
`GetRoleMemberCountMethod`.


#### get_role_revoked_event(tx_hash)
Get log entry for RoleRevoked event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleRevoked event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_tokens_minted_event(tx_hash)
Get log entry for TokensMinted event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting TokensMinted event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_tokens_minted_with_signature_event(tx_hash)
Get log entry for TokensMintedWithSignature event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting TokensMintedWithSignature
    event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_transfer_event(tx_hash)
Get log entry for Transfer event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Transfer event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_unpaused_event(tx_hash)
Get log entry for Unpaused event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Unpaused event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_votes(_: thirdweb.abi.token_erc20.GetVotesMetho_ )
Constructor-initialized instance of
`GetVotesMethod`.


#### grant_role(_: thirdweb.abi.token_erc20.GrantRoleMetho_ )
Constructor-initialized instance of
`GrantRoleMethod`.


#### has_role(_: thirdweb.abi.token_erc20.HasRoleMetho_ )
Constructor-initialized instance of
`HasRoleMethod`.


#### increase_allowance(_: thirdweb.abi.token_erc20.IncreaseAllowanceMetho_ )
Constructor-initialized instance of
`IncreaseAllowanceMethod`.


#### initialize(_: thirdweb.abi.token_erc20.InitializeMetho_ )
Constructor-initialized instance of
`InitializeMethod`.


#### is_trusted_forwarder(_: thirdweb.abi.token_erc20.IsTrustedForwarderMetho_ )
Constructor-initialized instance of
`IsTrustedForwarderMethod`.


#### mint_to(_: thirdweb.abi.token_erc20.MintToMetho_ )
Constructor-initialized instance of
`MintToMethod`.


#### mint_with_signature(_: thirdweb.abi.token_erc20.MintWithSignatureMetho_ )
Constructor-initialized instance of
`MintWithSignatureMethod`.


#### multicall(_: thirdweb.abi.token_erc20.MulticallMetho_ )
Constructor-initialized instance of
`MulticallMethod`.


#### name(_: thirdweb.abi.token_erc20.NameMetho_ )
Constructor-initialized instance of
`NameMethod`.


#### nonces(_: thirdweb.abi.token_erc20.NoncesMetho_ )
Constructor-initialized instance of
`NoncesMethod`.


#### num_checkpoints(_: thirdweb.abi.token_erc20.NumCheckpointsMetho_ )
Constructor-initialized instance of
`NumCheckpointsMethod`.


#### pause(_: thirdweb.abi.token_erc20.PauseMetho_ )
Constructor-initialized instance of
`PauseMethod`.


#### paused(_: thirdweb.abi.token_erc20.PausedMetho_ )
Constructor-initialized instance of
`PausedMethod`.


#### permit(_: thirdweb.abi.token_erc20.PermitMetho_ )
Constructor-initialized instance of
`PermitMethod`.


#### primary_sale_recipient(_: thirdweb.abi.token_erc20.PrimarySaleRecipientMetho_ )
Constructor-initialized instance of
`PrimarySaleRecipientMethod`.


#### renounce_role(_: thirdweb.abi.token_erc20.RenounceRoleMetho_ )
Constructor-initialized instance of
`RenounceRoleMethod`.


#### revoke_role(_: thirdweb.abi.token_erc20.RevokeRoleMetho_ )
Constructor-initialized instance of
`RevokeRoleMethod`.


#### set_contract_uri(_: thirdweb.abi.token_erc20.SetContractUriMetho_ )
Constructor-initialized instance of
`SetContractUriMethod`.


#### set_platform_fee_info(_: thirdweb.abi.token_erc20.SetPlatformFeeInfoMetho_ )
Constructor-initialized instance of
`SetPlatformFeeInfoMethod`.


#### set_primary_sale_recipient(_: thirdweb.abi.token_erc20.SetPrimarySaleRecipientMetho_ )
Constructor-initialized instance of
`SetPrimarySaleRecipientMethod`.


#### supports_interface(_: thirdweb.abi.token_erc20.SupportsInterfaceMetho_ )
Constructor-initialized instance of
`SupportsInterfaceMethod`.


#### symbol(_: thirdweb.abi.token_erc20.SymbolMetho_ )
Constructor-initialized instance of
`SymbolMethod`.


#### total_supply(_: thirdweb.abi.token_erc20.TotalSupplyMetho_ )
Constructor-initialized instance of
`TotalSupplyMethod`.


#### transfer(_: thirdweb.abi.token_erc20.TransferMetho_ )
Constructor-initialized instance of
`TransferMethod`.


#### transfer_from(_: thirdweb.abi.token_erc20.TransferFromMetho_ )
Constructor-initialized instance of
`TransferFromMethod`.


#### unpause(_: thirdweb.abi.token_erc20.UnpauseMetho_ )
Constructor-initialized instance of
`UnpauseMethod`.


#### verify(_: thirdweb.abi.token_erc20.VerifyMetho_ )
Constructor-initialized instance of
`VerifyMethod`.


### _class_ thirdweb.abi.token_erc20.TokenERC20Validator(web3_or_provider, contract_address)
Bases: `zero_ex.contract_wrappers.bases.Validator`

No-op input validator.


### _class_ thirdweb.abi.token_erc20.TotalSupplyMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the totalSupply method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.TransferFromMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the transferFrom method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(_from, to, amount, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(_from, to, amount, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(_from, to, amount, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(_from, to, amount, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(_from, to, amount)
Validate the inputs to the transferFrom method.


### _class_ thirdweb.abi.token_erc20.TransferMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the transfer method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(to, amount, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(to, amount, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(to, amount, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(to, amount, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(to, amount)
Validate the inputs to the transfer method.


### _class_ thirdweb.abi.token_erc20.UnpauseMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the unpause method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc20.VerifyMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the verify method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(req, signature, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(req, signature, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`bool`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(req, signature, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(req, signature, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(req, signature)
Validate the inputs to the verify method.

## thirdweb.abi.token_erc721 module

Generated wrapper for TokenERC721 Solidity contract.


### _class_ thirdweb.abi.token_erc721.ApproveMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc721.BalanceOfMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc721.BurnMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the burn method.


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

    `None`



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
Validate the inputs to the burn method.


### _class_ thirdweb.abi.token_erc721.ContractTypeMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractType method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.ContractUriMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractURI method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.ContractVersionMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the contractVersion method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.DefaultAdminRoleMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the DEFAULT_ADMIN_ROLE method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.GetApprovedMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc721.GetDefaultRoyaltyInfoMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getDefaultRoyaltyInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`str`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.GetPlatformFeeInfoMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getPlatformFeeInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`str`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.GetRoleAdminMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleAdmin method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`bytes`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleAdmin method.


### _class_ thirdweb.abi.token_erc721.GetRoleMemberCountMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMemberCount method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role)
Validate the inputs to the getRoleMemberCount method.


### _class_ thirdweb.abi.token_erc721.GetRoleMemberMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoleMember method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, index, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, index, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, index, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, index, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, index)
Validate the inputs to the getRoleMember method.


### _class_ thirdweb.abi.token_erc721.GetRoyaltyInfoForTokenMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the getRoyaltyInfoForToken method.


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

    `Tuple`[`str`, `int`]



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
Validate the inputs to the getRoyaltyInfoForToken method.


### _class_ thirdweb.abi.token_erc721.GrantRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the grantRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the grantRole method.


### _class_ thirdweb.abi.token_erc721.HasRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the hasRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the hasRole method.


### _class_ thirdweb.abi.token_erc721.ITokenERC721MintRequest(\*args, \*\*kwargs)
Bases: `dict`

Python representation of a tuple or struct.

Solidity compiler output does not include the names of structs that appear
in method definitions.  A tuple found in an ABI may have been written in
Solidity as a literal, anonymous tuple, or it may have been written as a
named `struct`, but there is no way to tell from the compiler
output.  This class represents a tuple that appeared in a method
definition.  Its name is derived from a hash of that tuple’s field names,
and every method whose ABI refers to a tuple with that same list of field
names will have a generated wrapper method that refers to this class.

Any members of type `bytes` should be encoded as UTF-8, which can be
accomplished via `str.encode("utf_8")`


#### currency(_: st_ )

#### price(_: in_ )

#### primarySaleRecipient(_: st_ )

#### royaltyBps(_: in_ )

#### royaltyRecipient(_: st_ )

#### to(_: st_ )

#### uid(_: Union[bytes, str_ )

#### uri(_: st_ )

#### validityEndTimestamp(_: in_ )

#### validityStartTimestamp(_: in_ )

### _class_ thirdweb.abi.token_erc721.InitializeMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the initialize method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(default_admin, name, symbol, contract_uri, trusted_forwarders, sale_recipient, royalty_recipient, royalty_bps, platform_fee_bps, platform_fee_recipient)
Validate the inputs to the initialize method.


### _class_ thirdweb.abi.token_erc721.IsApprovedForAllMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc721.IsTrustedForwarderMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the isTrustedForwarder method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(forwarder, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(forwarder, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `bool`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(forwarder, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(forwarder, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(forwarder)
Validate the inputs to the isTrustedForwarder method.


### _class_ thirdweb.abi.token_erc721.MintToMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the mintTo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(to, uri, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(to, uri, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(to, uri, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(to, uri, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(to, uri)
Validate the inputs to the mintTo method.


### _class_ thirdweb.abi.token_erc721.MintWithSignatureMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the mintWithSignature method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(req, signature, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(req, signature, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(req, signature, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(req, signature, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(req, signature)
Validate the inputs to the mintWithSignature method.


### _class_ thirdweb.abi.token_erc721.MulticallMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the multicall method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(data, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(data, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `List`[`Union`[`bytes`, `str`]]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(data, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(data, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(data)
Validate the inputs to the multicall method.


### _class_ thirdweb.abi.token_erc721.NameMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the name method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.NextTokenIdToMintMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the nextTokenIdToMint method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.OwnerMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the owner method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.OwnerOfMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc721.PlatformFeeBpsMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the platformFeeBps method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.PlatformFeeRecipientMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the platformFeeRecipient method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.PrimarySaleRecipientMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the primarySaleRecipient method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.RenounceRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the renounceRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the renounceRole method.


### _class_ thirdweb.abi.token_erc721.RevokeRoleMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the revokeRole method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(role, account, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(role, account, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(role, account, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(role, account, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(role, account)
Validate the inputs to the revokeRole method.


### _class_ thirdweb.abi.token_erc721.RoyaltyInfoMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the royaltyInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(token_id, sale_price, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(token_id, sale_price, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`str`, `int`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(token_id, sale_price, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(token_id, sale_price, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(token_id, sale_price)
Validate the inputs to the royaltyInfo method.


### _class_ thirdweb.abi.token_erc721.SafeTransferFrom1Method(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc721.SafeTransferFrom2Method(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc721.SetApprovalForAllMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc721.SetContractUriMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setContractURI method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(uri, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(uri, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(uri, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(uri, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(uri)
Validate the inputs to the setContractURI method.


### _class_ thirdweb.abi.token_erc721.SetDefaultRoyaltyInfoMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setDefaultRoyaltyInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(royalty_recipient, royalty_bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(royalty_recipient, royalty_bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(royalty_recipient, royalty_bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(royalty_recipient, royalty_bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(royalty_recipient, royalty_bps)
Validate the inputs to the setDefaultRoyaltyInfo method.


### _class_ thirdweb.abi.token_erc721.SetOwnerMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setOwner method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(new_owner, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(new_owner, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(new_owner, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(new_owner, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(new_owner)
Validate the inputs to the setOwner method.


### _class_ thirdweb.abi.token_erc721.SetPlatformFeeInfoMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setPlatformFeeInfo method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(platform_fee_recipient, platform_fee_bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(platform_fee_recipient, platform_fee_bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(platform_fee_recipient, platform_fee_bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(platform_fee_recipient, platform_fee_bps)
Validate the inputs to the setPlatformFeeInfo method.


### _class_ thirdweb.abi.token_erc721.SetPrimarySaleRecipientMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setPrimarySaleRecipient method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(sale_recipient, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(sale_recipient, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(sale_recipient, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(sale_recipient, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(sale_recipient)
Validate the inputs to the setPrimarySaleRecipient method.


### _class_ thirdweb.abi.token_erc721.SetRoyaltyInfoForTokenMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the setRoyaltyInfoForToken method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(token_id, recipient, bps, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(token_id, recipient, bps, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `None`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(token_id, recipient, bps, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(token_id, recipient, bps, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(token_id, recipient, bps)
Validate the inputs to the setRoyaltyInfoForToken method.


### _class_ thirdweb.abi.token_erc721.SupportsInterfaceMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc721.SymbolMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the symbol method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.ThirdwebFeeMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the thirdwebFee method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `str`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.TokenByIndexMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the tokenByIndex method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(index, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(index, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(index, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(index, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(index)
Validate the inputs to the tokenByIndex method.


### _class_ thirdweb.abi.token_erc721.TokenERC721(web3_or_provider, contract_address, validator=None)
Bases: `object`

Wrapper class for TokenERC721 Solidity contract.

All method parameters of type `bytes` should be encoded as UTF-8,
which can be accomplished via `str.encode("utf_8")`.


#### \__init__(web3_or_provider, contract_address, validator=None)
Get an instance of wrapper for smart contract.


* **Parameters**

    
    * **web3_or_provider** (`Union`[`Web3`, `BaseProvider`]) – Either an instance of `web3.Web3` or
    `web3.providers.base.BaseProvider`


    * **contract_address** (`str`) – where the contract has been deployed


    * **validator** (`Optional`[`TokenERC721Validator`]) – for validation of method inputs.



#### _static_ abi()
Return the ABI to the underlying contract.


#### approve(_: thirdweb.abi.token_erc721.ApproveMetho_ )
Constructor-initialized instance of
`ApproveMethod`.


#### balance_of(_: thirdweb.abi.token_erc721.BalanceOfMetho_ )
Constructor-initialized instance of
`BalanceOfMethod`.


#### burn(_: thirdweb.abi.token_erc721.BurnMetho_ )
Constructor-initialized instance of
`BurnMethod`.


#### contract_type(_: thirdweb.abi.token_erc721.ContractTypeMetho_ )
Constructor-initialized instance of
`ContractTypeMethod`.


#### contract_uri(_: thirdweb.abi.token_erc721.ContractUriMetho_ )
Constructor-initialized instance of
`ContractUriMethod`.


#### contract_version(_: thirdweb.abi.token_erc721.ContractVersionMetho_ )
Constructor-initialized instance of
`ContractVersionMethod`.


#### default_admin_role(_: thirdweb.abi.token_erc721.DefaultAdminRoleMetho_ )
Constructor-initialized instance of
`DefaultAdminRoleMethod`.


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



#### get_approved(_: thirdweb.abi.token_erc721.GetApprovedMetho_ )
Constructor-initialized instance of
`GetApprovedMethod`.


#### get_default_royalty_event(tx_hash)
Get log entry for DefaultRoyalty event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting DefaultRoyalty event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_default_royalty_info(_: thirdweb.abi.token_erc721.GetDefaultRoyaltyInfoMetho_ )
Constructor-initialized instance of
`GetDefaultRoyaltyInfoMethod`.


#### get_funds_withdrawn_event(tx_hash)
Get log entry for FundsWithdrawn event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting FundsWithdrawn event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_owner_updated_event(tx_hash)
Get log entry for OwnerUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting OwnerUpdated event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_platform_fee_info(_: thirdweb.abi.token_erc721.GetPlatformFeeInfoMetho_ )
Constructor-initialized instance of
`GetPlatformFeeInfoMethod`.


#### get_platform_fee_info_updated_event(tx_hash)
Get log entry for PlatformFeeInfoUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting PlatformFeeInfoUpdated
    event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_primary_sale_recipient_updated_event(tx_hash)
Get log entry for PrimarySaleRecipientUpdated event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting
    PrimarySaleRecipientUpdated event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_admin(_: thirdweb.abi.token_erc721.GetRoleAdminMetho_ )
Constructor-initialized instance of
`GetRoleAdminMethod`.


#### get_role_admin_changed_event(tx_hash)
Get log entry for RoleAdminChanged event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleAdminChanged event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_granted_event(tx_hash)
Get log entry for RoleGranted event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleGranted event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_role_member(_: thirdweb.abi.token_erc721.GetRoleMemberMetho_ )
Constructor-initialized instance of
`GetRoleMemberMethod`.


#### get_role_member_count(_: thirdweb.abi.token_erc721.GetRoleMemberCountMetho_ )
Constructor-initialized instance of
`GetRoleMemberCountMethod`.


#### get_role_revoked_event(tx_hash)
Get log entry for RoleRevoked event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoleRevoked event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_royalty_for_token_event(tx_hash)
Get log entry for RoyaltyForToken event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting RoyaltyForToken event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_royalty_info_for_token(_: thirdweb.abi.token_erc721.GetRoyaltyInfoForTokenMetho_ )
Constructor-initialized instance of
`GetRoyaltyInfoForTokenMethod`.


#### get_tokens_minted_event(tx_hash)
Get log entry for TokensMinted event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting TokensMinted event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_tokens_minted_with_signature_event(tx_hash)
Get log entry for TokensMintedWithSignature event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting TokensMintedWithSignature
    event



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_transfer_event(tx_hash)
Get log entry for Transfer event.


* **Parameters**

    **tx_hash** (`Union`[`HexBytes`, `bytes`]) – hash of transaction emitting Transfer event



* **Return type**

    `Tuple`[`AttributeDict`]



#### grant_role(_: thirdweb.abi.token_erc721.GrantRoleMetho_ )
Constructor-initialized instance of
`GrantRoleMethod`.


#### has_role(_: thirdweb.abi.token_erc721.HasRoleMetho_ )
Constructor-initialized instance of
`HasRoleMethod`.


#### initialize(_: thirdweb.abi.token_erc721.InitializeMetho_ )
Constructor-initialized instance of
`InitializeMethod`.


#### is_approved_for_all(_: thirdweb.abi.token_erc721.IsApprovedForAllMetho_ )
Constructor-initialized instance of
`IsApprovedForAllMethod`.


#### is_trusted_forwarder(_: thirdweb.abi.token_erc721.IsTrustedForwarderMetho_ )
Constructor-initialized instance of
`IsTrustedForwarderMethod`.


#### mint_to(_: thirdweb.abi.token_erc721.MintToMetho_ )
Constructor-initialized instance of
`MintToMethod`.


#### mint_with_signature(_: thirdweb.abi.token_erc721.MintWithSignatureMetho_ )
Constructor-initialized instance of
`MintWithSignatureMethod`.


#### multicall(_: thirdweb.abi.token_erc721.MulticallMetho_ )
Constructor-initialized instance of
`MulticallMethod`.


#### name(_: thirdweb.abi.token_erc721.NameMetho_ )
Constructor-initialized instance of
`NameMethod`.


#### next_token_id_to_mint(_: thirdweb.abi.token_erc721.NextTokenIdToMintMetho_ )
Constructor-initialized instance of
`NextTokenIdToMintMethod`.


#### owner(_: thirdweb.abi.token_erc721.OwnerMetho_ )
Constructor-initialized instance of
`OwnerMethod`.


#### owner_of(_: thirdweb.abi.token_erc721.OwnerOfMetho_ )
Constructor-initialized instance of
`OwnerOfMethod`.


#### platform_fee_bps(_: thirdweb.abi.token_erc721.PlatformFeeBpsMetho_ )
Constructor-initialized instance of
`PlatformFeeBpsMethod`.


#### platform_fee_recipient(_: thirdweb.abi.token_erc721.PlatformFeeRecipientMetho_ )
Constructor-initialized instance of
`PlatformFeeRecipientMethod`.


#### primary_sale_recipient(_: thirdweb.abi.token_erc721.PrimarySaleRecipientMetho_ )
Constructor-initialized instance of
`PrimarySaleRecipientMethod`.


#### renounce_role(_: thirdweb.abi.token_erc721.RenounceRoleMetho_ )
Constructor-initialized instance of
`RenounceRoleMethod`.


#### revoke_role(_: thirdweb.abi.token_erc721.RevokeRoleMetho_ )
Constructor-initialized instance of
`RevokeRoleMethod`.


#### royalty_info(_: thirdweb.abi.token_erc721.RoyaltyInfoMetho_ )
Constructor-initialized instance of
`RoyaltyInfoMethod`.


#### safe_transfer_from1(_: thirdweb.abi.token_erc721.SafeTransferFrom1Metho_ )
Constructor-initialized instance of
`SafeTransferFrom1Method`.


#### safe_transfer_from2(_: thirdweb.abi.token_erc721.SafeTransferFrom2Metho_ )
Constructor-initialized instance of
`SafeTransferFrom2Method`.


#### set_approval_for_all(_: thirdweb.abi.token_erc721.SetApprovalForAllMetho_ )
Constructor-initialized instance of
`SetApprovalForAllMethod`.


#### set_contract_uri(_: thirdweb.abi.token_erc721.SetContractUriMetho_ )
Constructor-initialized instance of
`SetContractUriMethod`.


#### set_default_royalty_info(_: thirdweb.abi.token_erc721.SetDefaultRoyaltyInfoMetho_ )
Constructor-initialized instance of
`SetDefaultRoyaltyInfoMethod`.


#### set_owner(_: thirdweb.abi.token_erc721.SetOwnerMetho_ )
Constructor-initialized instance of
`SetOwnerMethod`.


#### set_platform_fee_info(_: thirdweb.abi.token_erc721.SetPlatformFeeInfoMetho_ )
Constructor-initialized instance of
`SetPlatformFeeInfoMethod`.


#### set_primary_sale_recipient(_: thirdweb.abi.token_erc721.SetPrimarySaleRecipientMetho_ )
Constructor-initialized instance of
`SetPrimarySaleRecipientMethod`.


#### set_royalty_info_for_token(_: thirdweb.abi.token_erc721.SetRoyaltyInfoForTokenMetho_ )
Constructor-initialized instance of
`SetRoyaltyInfoForTokenMethod`.


#### supports_interface(_: thirdweb.abi.token_erc721.SupportsInterfaceMetho_ )
Constructor-initialized instance of
`SupportsInterfaceMethod`.


#### symbol(_: thirdweb.abi.token_erc721.SymbolMetho_ )
Constructor-initialized instance of
`SymbolMethod`.


#### thirdweb_fee(_: thirdweb.abi.token_erc721.ThirdwebFeeMetho_ )
Constructor-initialized instance of
`ThirdwebFeeMethod`.


#### token_by_index(_: thirdweb.abi.token_erc721.TokenByIndexMetho_ )
Constructor-initialized instance of
`TokenByIndexMethod`.


#### token_of_owner_by_index(_: thirdweb.abi.token_erc721.TokenOfOwnerByIndexMetho_ )
Constructor-initialized instance of
`TokenOfOwnerByIndexMethod`.


#### token_uri(_: thirdweb.abi.token_erc721.TokenUriMetho_ )
Constructor-initialized instance of
`TokenUriMethod`.


#### total_supply(_: thirdweb.abi.token_erc721.TotalSupplyMetho_ )
Constructor-initialized instance of
`TotalSupplyMethod`.


#### transfer_from(_: thirdweb.abi.token_erc721.TransferFromMetho_ )
Constructor-initialized instance of
`TransferFromMethod`.


#### verify(_: thirdweb.abi.token_erc721.VerifyMetho_ )
Constructor-initialized instance of
`VerifyMethod`.


### _class_ thirdweb.abi.token_erc721.TokenERC721Validator(web3_or_provider, contract_address)
Bases: `zero_ex.contract_wrappers.bases.Validator`

No-op input validator.


### _class_ thirdweb.abi.token_erc721.TokenOfOwnerByIndexMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the tokenOfOwnerByIndex method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(owner, index, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(owner, index, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(owner, index, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(owner, index, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(owner, index)
Validate the inputs to the tokenOfOwnerByIndex method.


### _class_ thirdweb.abi.token_erc721.TokenUriMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the tokenURI method.


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
Validate the inputs to the tokenURI method.


### _class_ thirdweb.abi.token_erc721.TotalSupplyMethod(web3_or_provider, contract_address, contract_function)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the totalSupply method.


#### \__init__(web3_or_provider, contract_address, contract_function)
Persist instance data.


#### build_transaction(tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `int`



* **Returns**

    the return value of the underlying method.



#### estimate_gas(tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



### _class_ thirdweb.abi.token_erc721.TransferFromMethod(web3_or_provider, contract_address, contract_function, validator=None)
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


### _class_ thirdweb.abi.token_erc721.VerifyMethod(web3_or_provider, contract_address, contract_function, validator=None)
Bases: `zero_ex.contract_wrappers.bases.ContractMethod`

Various interfaces to the verify method.


#### \__init__(web3_or_provider, contract_address, contract_function, validator=None)
Persist instance data.


#### build_transaction(req, signature, tx_params=None)
Construct calldata to be used as input to the method.


* **Return type**

    `dict`



#### call(req, signature, tx_params=None)
Execute underlying contract method via eth_call.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Tuple`[`bool`, `str`]



* **Returns**

    the return value of the underlying method.



#### estimate_gas(req, signature, tx_params=None)
Estimate gas consumption of method call.


* **Return type**

    `int`



#### send_transaction(req, signature, tx_params=None)
Execute underlying contract method via eth_sendTransaction.


* **Parameters**

    **tx_params** (`Optional`[`TxParams`]) – transaction parameters



* **Return type**

    `Union`[`HexBytes`, `bytes`]



#### validate_and_normalize_inputs(req, signature)
Validate the inputs to the verify method.

## Module contents
