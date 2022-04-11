# thirdweb.abi.ierc1155 package

## Module contents

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
