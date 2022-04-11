# thirdweb.abi.t_w_factory package

## Module contents

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
