# thirdweb.abi.token_erc1155 package

## Module contents

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
