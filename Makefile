.PHONY: abi docs

DOCS_SERVER_PORT = 8087

clean-env:
	rm -rf .venv
	poetry shell

init:
	# Setup poetry first: https://python-poetry.org/docs/
	poetry install
	poetry run yarn add hardhat
	poetry run pip3 install eth-brownie
	npm install -g @0x/abi-gen
	yarn
	poetry shell
	pip3 install pydoc-markdown
	pip3 install 0x-order-utils

test:
	poetry run brownie test --network hardhat

abis:
	# If you regenerate registry ABI, you will need to fix a typing error
	python3 scripts/generate_abis.py

snippets:
	poetry run python3 scripts/generate_snippets.py

docs:
	cd docs && rm -rf pydoc-markdown && rm -rf docs
	cd docs && poetry run pydoc-markdown
	mv docs/build/docs docs/pydoc-markdown
	rm -rf docs/build
	cp -R docs/pydoc-markdown/content docs/docs
	cp docs/common/index.md docs/docs/index.md
	cp docs/common/custom.md docs/docs/custom.md
	make snippets

publish:
	poetry version prerelease
	rm -rf dist
	poetry build
	poetry publish

live-docs:
	make docs
	xdg-open http://localhost:$(DOCS_SERVER_PORT) || open http://localhost:$(DOCS_SERVER_PORT) || start http://localhost:$(DOCS_SERVER_PORT)
	cd docs/pydoc-markdown && poetry run mkdocs serve --dev-addr localhost:$(DOCS_SERVER_PORT)

test-docker:
	cp docs.Dockerfile Dockerfile
	docker build --no-cache -t docker-test .
	docker run -dp 3000:3000 docker-test