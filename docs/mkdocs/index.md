# Getting Started

The thirdweb SDK for Python. Currently supports Mainnet, Rinkeby, Goerli, Polygon, and Mumbai.
## Installation

```bash
pip install thirdweb-sdk
```

## Getting Started

To start using this SDK, you just need to pass in a provider configuration.
### Instantiating the SDK

Once you have all the necessary dependencies, you can follow the following setup steps to get started with the SDK read-only functions:

```python
from thirdweb import ThirdwebSDK
from web3 import Web3

# Add your own RPC URL here or use a public one
RPC_URL = "https://rpc-mumbai.maticvigil.com"

# Instantiate a new provider to pass into the SDK
provider = Web3(Web3.HTTPProvider(RPC_URL))

# Finally, you can create a new instance of the SDK to use
sdk = ThirdwebSDK(provider)
```

### Working With Contracts

Once you instantiate the SDK, you can use it to access your thirdweb contracts. You can use the SDK's contract getter functions like `get_token`, `get_edition`, `get_nft_collection`, and `get_marketplace` to get the respective SDK contract instances. To use an NFT Collection contract for example, you can do the following.

```python
# Add your NFT Collection contract address here
NFT_COLLECTION_ADDRESS = "0x.."

# And you can instantiate your contract with just one line
nft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)

# Now you can use any of the read-only SDK contract functions
nfts = nft_collection.get_all()
print(nfts)
```

### Signing Transactions

> Warning: Never commit private keys to file tracking history, or your account could be compromised. Make sure to add `.env` to your `.gitignore` file.

Meanwhile, if you want to use write functions as well and connect a signer, you can use the following setup (if you want to use your private key as displayed below, make sure to run `pip install python-dotenv` as well):

```python
from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
from eth_account import Account
from dotenv import load_dotenv
from web3 import Web3
import os

# Load environment variables into this file
load_dotenv()

# This PRIVATE KEY is coming from your environment variables. Make sure to never put it in a tracked file or share it with anyone.
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

# Add your own RPC URL here or use a public one
RPC_URL = "https://rpc-mumbai.maticvigil.com"

# Instantiate a new provider to pass into the SDK
provider = Web3(Web3.HTTPProvider(RPC_URL))

# Optionally, instantiate a new signer to pass into the SDK
signer = Account.from_key(PRIVATE_KEY)

# Finally, you can create a new instance of the SDK to use
sdk = ThirdwebSDK(provider, signer)

# Instantiate a new NFT Collection contract as described above.
NFT_COLLECTION_ADDRESS = "0x.."
nft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)

# Now you can use any of the SDK contract functions including write functions
nft_collection.mint(NFTMetadataInput.from_json({ "name": "Cool NFT", "description": "Minted with the Python SDK!" }))
```

If you wanted to use the SDK with a signer above, make sure to include your PRIVATE_KEY in your `.env` file, and make sure this file is NOT tracked in any repository (make sure to add it to your `.gitignore` file). Adding your private key to your `.env` would look like the following:

```
PRIVATE_KEY=your-private-key-here
```
