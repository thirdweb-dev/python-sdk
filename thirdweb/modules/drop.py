""" Interact with the NFT module of the app"""
from thirdweb_web3 import Web3
from ..abi.lazy_nft import Drop
from .base import BaseModule
import json
from types.drop import Query, claim

class DropModule(BaseModule):
    """ Interact with the NFT module of the app"""

    address: str
    """
    Address of the module
    """
    __abi_module: Drop

    def __init__(self, address: str, client: Web3):
        """
        :param address: The address of the module
        :param client: Web3 client
        Initializes the module
        """
        super().__init__()
        self.address = address
        """
        NFT module contract address [https://thirdweb.com/: Dashboard: Project ➝ NFT Module]
        """

        self.__abi_module = Drop(client, address)

    def get(self, token_id: str):
        """
        :param token_id: ID of the drop
        :return: Drop object
        Gets a drop
        """
        owner = self.owner_of(token_id)
        metadata = self.get_token_metadata(token_id)
        return {
            "metadata": metadata,
            "owner": owner,
        }


    def get_all(self, query: Query = None):
        """
        :param query: Query object
        :return: List of drops
        Gets all drops
        """
        
        start = query.start
        count = query.count
        maxid = min([self.__abi_module.next_token_id.call(), (start + count)])
        response = [self.get(i) for i in range(start, maxid)]
        return response

    def get_all_unclaimed(self, query: Query = None):
        start = query.start
        count = query.count
        maxid = min([self.__abi_module.get_max_id.call(), (start + count)])
        unminted = self.__abi_module.next_mint_token_id.call()
        response = []
        for i in range(start, (maxid - unminted)):
            response.append(self.get(i))
        return response

    def get_all_claimed(self, query: Query = None):
        start = query.start
        count = query.count
        maxid = min(
            [self.__abi_module.next_mint_token_id.call(), (start + count)])
        response = [self.get(i) for i in range(start, maxid)]
        return response

    def owner_of(self, token_id: str):
        """
        :param token_id: ID of the drop
        :return: Address of the owner
        Gets the owner of a drop
        """
        return self.__abi_module.owner_of.call(token_id)

    def get_owned(self, address: str = None):
        """
        :param address: Address of the owner
        :return: List of drops
        Gets all drops owned by a user
        """
        if not address:
            address = self.get_signer_address()
        balance = self.__abi_module.balance_of.call(address)
        indices = [i for i in range(balance)]
        token_ids = [self.__abi_module.token_of_owner_by_index.call(
            address, i) for i in indices]
        return [self.get(i) for i in token_ids]



    def transform_result_to_claim_condition(self, pm: claim):
        # todo
        return

    def get_active_mint_condition(self):
        """
        :return: Active mint condition
        Gets the active mint condition
        """
        return self.__abi_module.mint_conditions(self.__abi_module.get_last_started_mint_condition_index.call())

    def get_active_claim_condition(self):
        index = self.__abi_module.get_last_started_mint_condition_index.call()
        mc = self.__abi_module.mint_conditions.call(index)
        return self.transform_result_to_claim_condition(mc)

    def get_all_mint_conditions(self):
        conditions = []
        i = 0
        while True:
            try:
                conditions.append(self.__abi_module.mint_conditions.call(i))
                i += 1
            except:
                break
        return conditions

    def get_all_claim_conditions(self):
        conditions = []
        i = 0
        while True:
            try:
                mc = self.__abi_module.mint_conditions.call(i)
                conditions.append(self.transform_result_to_claim_condition(mc))
                i += 1
            except:
                break
        return conditions

    def total_supply(self):
        """
        :return: Total supply of drops
        Gets the total supply of drops
        """
        return self.__abi_module.total_supply.call()

    def max_total_supply(self):
        """
        :return: Max total supply of drops
        Gets the max total supply of drops
        """
        return self.__abi_module.max_total_supply.call()

    def is_approved(self, address: str, operator: str):
        return self.__abi_module.is_approved_for_all.call(address, operator)

    def set_approval(self, operator: str, approved: bool = True):
        """
        :param operator: Address of the operator
        :param approved: Approved or not
        Sets approval for a user
        """
        self.__abi_module.set_approval_for_all(operator, approved)        

    def transfer(self, to: str, token_id: str):
        """
        :param to: Address of the new owner
        :param token_id: ID of the drop
        Transfers a drop
        """
        from_address = self.get_signer_address()
        self.__abi_module.safe_transfer_from(from_address, to, token_id)

    def total_unclaimed_supply(self):
        return self.__abi_module.next_token_id.call() - self.__abi_module.next_mint_token_id.call()

    def balance_of(self, address: str):
        """
        :param address: Address of the owner
        :return: Balance of the owner
        Gets the balance of the owner
        """
        return self.__abi_module.balance_of.call(address)

    def balance(self):
        """
        :return: Balance of the module
        Gets the balance of the module
        """
        return self.balance_of(self.get_signer_address())

    def total_claimed_supply(self):
        """
        :return: Total claimed supply of drops
        Gets the total claimed supply of drops
        """
        return self.__abi_module.next_mint_token_id.call()

    def lazy_mint_batch(self, uris: list):
        """
        :param uris: List of uris to mint
        :return: List of minted drops
        Mints a batch of drops
        """
        return self.__abi_module.lazy_mint_batch.call(uris)

    def lazy_mint_amount(self, amount: int):
        """
        :param amount: Amount of drops to mint
        :return: List of minted drops
        Mints a batch of drops
        """
        return self.__abi_module.lazy_mint_amount.call(amount)

    def lazy_mint(self, metadata):
        self.lazy_mint_batch([metadata])

    def get_metadata(self):
        """
        :return: Metadata of the module
        Gets the metadata of the module
        """
        return self.__abi_module.get_metadata.call()

    def set_claim_condition(self, factory):
        """
        :param condition: Claim condition
        Sets the mint condition
        """
        merkle_info = {}
        for x in factory.allSnapshots():
            merkle_info[x.merkle_root] = x.merkle_path
        metadata = self.get_metadata()
        if not metadata:
            return Exception("No metadata")
        if len(factory.allSnapshots()) == 0 and 'merkle' in metadata:
            metadata["merkle"] = {}
        else:
            metadata["merkle"] = merkle_info

        metadata_uri = self.get_storage().upload_metadata(metadata)
        # todo multicall
        from_address = self.get_signer_address()
        return self.execute_tx(self.__abi_module.set_claim_condition.call(factory.get_claim_condition(), metadata_uri, from_address))

    def set_mint_conditions(self, factory):
        return self.set_claim_conditions(factory)

    def can_claim(self, quantity: int, proofs: list):
        """
        :param quantity: Amount of drops to claim
        :param proofs: List of proofs
        :return: True if can claim
        Checks if can claim
        """
        try:
            mc = self.get_active_claim_condition()
            overrides = {}  # todo overrides
            if mc.price_per_token.gt(0):
                if mc.currency == "0x0000000000000000000000000000000000000000":
                    overrides['value'] = mc.price_per_token * quantity
                else:
                    owner = self.get_signer_address()
                    spender = self.address
                    allowance = self.__abi_module.allowance.call(
                        owner, spender)  # todo erc20 module
                    total_price = mc.price_per_token * quantity
                    if allowance < total_price:
                        return Exception("Not enough allowance")

            self.__abi_module.claim.call(quantity, proofs, overrides)
            return True
        except:
            return False

    def claim(self, quantity: int, proofs: list):
        mc = self.get_active_claim_condition()
        metadata = self.get_metadata()
        address_to_claim = self.get_signer_address()
        if not (mc.merkle_root.startswith("0x0000000000000000000000000000000000000000")):
            snapshot = self.get_storage().get(metadata.merkle[mc.merkle_root])
            snapshot_data = json.loads(snapshot)
            item  = list(filter(lambda x:x["address"]==address_to_claim, snapshot_data))
            if item is None:
                return Exception("No claim for this address")
            proofs = item.proof

        

    def burn(self, token_id: int):
        """
        :param token_id: ID of the drop
        Burns a drop
        """
        return self.execute_tx(self.__abi_module.burn.call(token_id))

    def transfer_from(self, transfer_from: str, to: str, token_id: int):
        """
        :param transfer_from: Address of the owner
        :param to: Address of the new owner
        :param token_id: ID of the drop
        Transfers a drop
        """
        return self.execute_tx(self.__abi_module.transfer_from.call(transfer_from, to, token_id))

    def set_module_metadata(self, metadata: str):
        """
        :param metadata: The metadata to set
        :return: The transaction hash

        Sets the metadata for the module
        """
        uri = self.get_storage().upload_metadata(
            metadata, self.address, self.get_signer_address())
        tx = self.__abi_module.set_contract_uri.build_transaction(
            uri, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def set_royalty_bps(self, amount: int):
        """
        :param amount: the amount of BPS to set
        :return: the metadata of the token

        Sets the royalty percentage for the NFT
        """
        metadata = self.get_metadata()
        if not metadata:
            return Exception("No metadata")

        tx = self.__abi_module.set_royalty_bps.build_transaction(
            amount, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def set_base_token_uri(self, uri: str):
        """
        :param uri: The URI to set
        :return: The transaction hash

        Sets the base token URI for the NFT
        """
        tx = self.__abi_module.set_base_token_uri.build_transaction(
            uri, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def set_max_total_supply(self, amount: int):
        """
        :param amount: The amount to set
        :return: The transaction hash

        Sets the max total supply for the NFT
        """
        tx = self.__abi_module.set_max_total_supply.build_transaction(
            amount, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def get_royalty_recipient_address(self):
        """
        :return: The address of the recipient
        Gets the address of the recipient
        """
        metadata = self.get_metadata().metadata
        if 'fee_recipient' not in metadata.metadata:
            return metadata['fee_recipient']
        return ""
