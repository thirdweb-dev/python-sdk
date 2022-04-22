# Using Custom Contracts

With the thirdweb SDK, you can get an SDK interface for **any** contract. That's right - the thirdweb SDK doesn't *only* support thirdweb contracts, it supports any contract that you want to use with it and gives you all the convenience of using the thirdweb SDK without the pain of dealing with low level libraries or managing your own ABIs.

Let's take a look at how we can use this functionality!

## Getting a Custom Contract Instance

If you've published and deployed your contracts with the Thirdweb CLI, the process of using custom contracts looks like the following:

```python
# Just pass in the address of your contract and your ready
custom = sdk.get_custom_contract(<CUSTOM_CONTRACT_ADDRESS>) 
```

That's it! Now you have a custom contract instance which has the full functionality of your contract (we'll go over how to use this functionality soon).

You've just completely eliminated the need to use ABIs or anything of the sort - the thirdweb SDK and publisher handles all of this for you under the hood.

Alternatively, if you didn't publish your contract with the thirdweb CLI, you can manually pass in your contract ABI to get an interface.

```python
abi = ... # Add or import your contract abi 
custom = sdk.get_custom_contract(<CUSTOM_CONTRACT_ADDRESS>, abi)
```

### Using Contract Functions

Every custom contract gives you direct access to every function on your contract through the `functions` scope. For example, if I had an NFT custom contract and I wanted to call the `balance` function with a token ID of `1`, I would do the following:

```python
# Any arguments passed to the balance function go into the args of "call"
custom.functions.balance().call(1)
```

Even better, if you're contract implements common interfaces recognized by the thirdweb SDK, we'll give you even nicer convenience functions to make this function calls. For example, let's say my contract implements the `ERC721` interface. If I want to call the `balance` function, I could also do the following:

```python
# ERC721 functions are scoped to the "nft" name space
custom.nft.balance()
```

### Supported Interfaces

Below is a list of all the currently supported contract interfaces and their corresponding namespaces:

| Interface      | Namespace |
| ----------- | ----------- |
| ContractMetadata     | `custom.metadata` |
| ContractRoles   | `custom.roles` |
| ContractRoyalties   | `custom.royalties` |
| ContractPrimarySales   | `custom.platform_fee` |
| ERC20   | `custom.token` |
| ERC721   | `custom.nft` |
| ERC1155   | `custom.edition` |
