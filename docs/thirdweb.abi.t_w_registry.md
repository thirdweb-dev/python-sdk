# thirdweb.abi.t_w_registry package

## Module contents

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
