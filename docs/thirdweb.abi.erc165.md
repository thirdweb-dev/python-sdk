# thirdweb.abi.erc165 package

## Module contents

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
