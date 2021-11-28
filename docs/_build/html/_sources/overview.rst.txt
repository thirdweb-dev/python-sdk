SDK Overview
============

The ``thirdweb-sdk`` package bridges the gap between your client/server
side applications and on-chain smart-contracts.

The collection of modules allows you to mint, transfer, burn, and query
on-chain assets across many chains. Our goal is to make the SDK as clean as
possible while providing the most amount of functionality.

Installation
~~~~~~~~~~~~

Start by installing the Thirdweb sdk

.. code-block:: bash

   $ pip install thirdweb-sdk

Initializing Up The SDK
------------------

In order to setup the SDK, the minimum configuration that's required is an
**RPC URL**. The URL will depend on what chain you'd like to interact with.

Here's a table of common public RPC's you can use as you work through our
docs.

+------------------------------+----------+------------------------------------------+
| Chain Name                   | ID       | RPC URL                                  |
+==============================+==========+==========================================+
| Ethereum Mainnet             | 1        | https://main-light.eth.linkpool.io       |
+------------------------------+----------+------------------------------------------+
| Ethereum Rinkeby (testnet)   | 4        | https://rinkeby-light.eth.linkpool.io/   |
+------------------------------+----------+------------------------------------------+
| Polygon Mainnet              | 137      | https://polygon-rpc.com                  |
+------------------------------+----------+------------------------------------------+
| Polygon Mumbai (testnet)     | 80001    | https://rpc-mumbai.matic.today           |
+------------------------------+----------+------------------------------------------+

For this example and throughout most of our documentation, we'll use the Poly{gon Mumbai chain (ID ``80001``).

.. code-block:: python
	:emphasize-lines: 1, 11, 13


	testing = 1
	while True:
		hello!
