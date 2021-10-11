import web3.providers
from typing import Optional

from nftlabs.modules import CurrencyModule
from nftlabs.options import SdkOptions


class NftlabsSdk(object):
	client: web3.Web3
	options: SdkOptions

	__currency_module: Optional[CurrencyModule]

	"""
	Create instance of the NftlabsSdk
	"""
	def __init__(self, options: SdkOptions, url: str):
		print("Created Nftlabs SDK!")

		self.__currency_module = None
		self.options = options

		self.client = web3.Web3(web3.HTTPProvider(url))
		if not self.client.isConnected():
			raise Exception("Failed to connect to the web3 provider")

	"""
	Returns an instance of the currency module
	"""
	def get_currency_module(self, address: str) -> CurrencyModule:
		if self.__currency_module is not None:
			return self.__currency_module

		module = CurrencyModule(self.__get_client, address)
		self.__currency_module = module
		return self.__currency_module

	"""
	Internal function used to return the current web3 provider used by downstream modules
	"""
	def __get_client(self) -> web3.Web3:
		return self.client
