.PHONY: clean-pyc clean-build

SHELL := /bin/bash

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = {{ rsrcdir }}
BUILDDIR      = {{ rbuilddir }}

DOCS_SERVER_PORT = 8087

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test:
	pytest tests

build:
	python3 setup.py sdist bdist_wheel

publish:
	twine upload dist/*

init : setup-venv

setup-venv:
	python3 -m venv .env
	source .env/bin/activate
	pip install -r requirements.txt

live-docs:
	# windows/mac/linux support
	xdg-open http://localhost:$(DOCS_SERVER_PORT) || open http://localhost:$(DOCS_SERVER_PORT) || start http://localhost:$(DOCS_SERVER_PORT)
	cd docs && mkdocs serve --dev-addr localhost:$(DOCS_SERVER_PORT)

build-docs:
	source .env/bin/activate && cd docs && mkdocs build
