# thirdweb.abi.marketplace package

## Module contents

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
