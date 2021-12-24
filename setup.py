from os import environ
from pathlib import Path

from setuptools import find_packages, setup

# The directory containing this file
BASE_DIR = Path(__file__).resolve().parent

# The text of the README file
README = (BASE_DIR / "README.md").read_text()

# Github URL
GITHUB_URL = "https://github.com/nftlabs/nftlabs-sdk-python"

package_name = "thirdweb-sdk"

if "PACKAGE_NAME" in environ:
    package_name = environ["PACKAGE_NAME"]

setup(
    # Project info.
    name=package_name,
    version="0.4.0",
    # Descriptions
    description="Official Thirdweb sdk",
    long_description=README,
    long_description_content_type="text/markdown",
    # Author info.
    author="NFTLabs",
    author_email="sdk@thirdweb.com",
    # Project repo info.
    url=GITHUB_URL,
    project_urls={
        "Documentation": GITHUB_URL,
        "Issue Tracker": GITHUB_URL + "/issues",
    },
    # Licensing.
    license="MIT",
    # Packaging.
    packages=find_packages(exclude=["tests", "tests.*", "tools", "tools.*"]),
    include_package_data=True,
    # Dependencies.
    install_requires=[
        "dataclasses-json==0.5.6",
        "thirdweb-web3==5.24.8",
        "requests==2.26.0",
        "thirdweb-contract-wrappers==2.0.3",
        "web3==5.25.0",
    ],
    # PyPI classifiers.
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Typing :: Typed",
    ],
    # Modules in this package.
    py_modules=["thirdweb", "nftlabs"],
    # Minimum python version
    python_requires=">=3.6",
)
