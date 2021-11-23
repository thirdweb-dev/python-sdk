import pathlib
from setuptools import setup, find_packages

from os import environ

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

package_name = "thirdweb-sdk"
if "PACKAGE_NAME" in environ:
    package_name = environ["PACKAGE_NAME"]

setup(
    name=package_name,
    version="0.4.0",
    description="Official Thirdweb sdk",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nftlabs/nftlabs-sdk-python",
    author="NFTLabs",
    author_email="sdk@thirdweb.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["dataclasses-json", "thirdweb-web3",
                      "requests", "thirdweb-contract-wrappers", "web3"],
    py_modules=["thirdweb", "nftlabs"]
)
