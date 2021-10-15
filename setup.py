import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="nftlabs-sdk",
    version="0.0.6",
    description="Official Nftlabs sdk",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nftlabs/nftlabs-sdk-python",
    author="NFTLabs",
    author_email="pythonsdk@thirdweb.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["dataclasses-json", "web3", "requests", "0x-contract-wrappers"],
)