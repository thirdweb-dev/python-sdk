# Thirdweb Python SDK

The thirdweb SDK for Python.
## Installation

```bash
$ pip install thirdweb-sdk
```

## Generate Python ABI Wrappers

Use the [abi-gen](https://www.npmjs.com/package/@0x/abi-gen) package to create the Python ABIs. You can install it with the following command:

```bash
$ npm install -g @0x/abi-gen
```

Assuming you have the thirdweb contract ABIs in this directory at `/abi`, you can run the following command to generate an ABI.

```bash
$ abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC721.json
```

Alternatively, if your system can run .sh files, you can run the following to generate all ABIs at once (from your /abi folder):

```bash
$ bash scripts/generate_abis.sh
```
