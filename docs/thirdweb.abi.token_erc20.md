# thirdweb.abi.token_erc20 package

## Module contents

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
