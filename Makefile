.PHONY: abi docs

test:
	poetry run brownie test --network hardhat

setup:
	rm -rf .venv
	poetry shell
	poetry install
	poetry run yarn add hardhat
	make abi

abi:
	abi-gen --language Python -o thirdweb/abi --abis abi/TWRegistry.json
	abi-gen --language Python -o thirdweb/abi --abis abi/TWFactory.json
	abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC20.json
	abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC721.json
	abi-gen --language Python -o thirdweb/abi --abis abi/TokenERC1155.json
	abi-gen --language Python -o thirdweb/abi --abis abi/Marketplace.json
	abi-gen --language Python -o thirdweb/abi --abis abi/ERC165.json
	abi-gen --language Python -o thirdweb/abi --abis abi/IERC20.json
	abi-gen --language Python -o thirdweb/abi --abis abi/IERC721.json
	abi-gen --language Python -o thirdweb/abi --abis abi/IERC1155.json

docs:
	rm -rf sphinx-docs
	poetry run sphinx-apidoc -o sphinx-docs . sphinx-apidoc --full -A 'Adam Majmudar'
	cd sphinx-docs && printf "\n\nimport os\nimport sys\nsys.path.insert(0,os.path.abspath('../'))\n\ndef skip(app, what, name, obj,would_skip, options):\n\tif name in ( '__init__',):\n\t\treturn False\n\treturn would_skip\ndef setup(app):\n\tapp.connect('autodoc-skip-member', skip)" >> conf.py
	cd sphinx-docs && poetry run make markdown
	rm -rf docs && mkdir docs
	mv sphinx-docs/_build/markdown/* ./docs
	find ./docs -name 'thirdweb.abi.*' -delete && find ./docs -name 'thirdweb.common.md' -delete
	rm -rf sphinx-docs