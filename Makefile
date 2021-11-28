.PHONY: clean-pyc clean-build

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = {{ rsrcdir }}
BUILDDIR      = {{ rbuilddir }}

SOURCE_DIR = docs
BUILD_DIR = $(SOURCE_DIR)/_build/html
SERVER_PORT = 8087

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
	PACKAGE_NAME=nftlabs-sdk python3 setup.py sdist bdist_wheel

publish:
	twine upload dist/*

init:
	setup-venv

setup-venv:
	python3 -m venv .env
	source .env/bin/activate

livehtml:
	# windows/mac/linux support
	xdg-open http://localhost:$(SERVER_PORT) || open http://localhost:$(SERVER_PORT) || start http://localhost:$(SERVER_PORT)
	./.env/bin/sphinx-autobuild --port $(SERVER_PORT) $(SOURCE_DIR) $(BUILD_DIR) $(SPHINXOPTS) $(O)
