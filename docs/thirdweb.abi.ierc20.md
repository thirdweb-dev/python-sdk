# thirdweb.abi.ierc20 package

## Module contents

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
