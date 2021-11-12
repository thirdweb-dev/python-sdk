.PHONY: clean-pyc clean-build

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