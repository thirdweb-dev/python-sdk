""" Interact with the NFT module of the app"""
from typing import cast
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
        try:
            supply = self.__abi_module.total_supply.call(token_id)
        except:
            supply = 0

        metadata = self.get_token_metadata(token_id)
        return {
            "metadata": metadata,
            "supply": supply
        }

    def get_token_metadata(self, token_id: int):
        # todo
        pass
    def get_all(self, query: Query = None):  # todo
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

    def get_owned(self, address: str = None):
        """
        :param address: Address of the owner
        :return: List of drops
        Gets all drops owned by a user
        """
        if not address:
            address = self.get_signer_address()
        max_id = self.__abi_module.next_token_to_mint.call()
        balances = self.__abi_module.balance_of_batch(
            [address] * max_id, [i for i in range(max_id)]
        )
        owned_balances = [i for i in balances if i > 0]
        token_ids = [self.__abi_module.token_of_owner_by_index.call(
            address, i) for i in range(len(owned_balances))]
        return [self.get(i) for i in token_ids]

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
        cv = get_currency_value(
            self.get_signer_address(),
            pm.currency_value,
            pm.pricePerToken
        )
        return {
            "start_timestamp": Date(pm.start_timestamp * 1000),
            "max_mint_supply": pm.max_mint_supply,
            "current_mint_supply": pm.current_mint_supply,
            "available_supply": pm.max_mint_supply - pm.current_mint_supply,
            "quantity_limit_per_transaction": pm.quantity_limit_per_transaction,
            "merkle_root": pm.merkle_root,
            "price_per_token": pm.pricePerToken,
            "currency": pm.currency,
            "price": pm.price_per_token,
            "currency_metadata": cv
        }

    def get_active_claim_condition(self, token_id: int):
        index = self.__abi_module.get_last_started_mint_condition_index.call(
            token_id)
        mc = self.__abi_module.mint_conditions.call(index)
        return self.transform_result_to_claim_condition(mc)

    def get_all_claim_conditions(self, token_id: int):
        claim_condition = self.__abi_module.claim_conditions.call(token_id)
        count = claim_condition.total_condition_count
        conditions = []
        i = 0
        while i < count:
            mc = self.__abi_module.get_claim_condition_at_index.call(
                token_id, i)
            conditions.append(self.transform_result_to_claim_condition(mc))
            i += 1
        return conditions

    def get_sales_recipient(self, token_id: int):
        """
        :param token_id: ID of the drop
        :return: Address of the recipient
        Gets the recipient of a drop
        """
        sales_recipient = self.__abi_module.sales_recipient.call(token_id)
        if sales_recipient == "0x0000000000000000000000000000000000000000":
            return self.__abi_module.default_sales_recipient.call()
        return sales_recipient

    def balance_of(self, address: str, token_id: int):
        return self.__abi_module.balance_of.call(address, token_id)

    def balance(self, token_id: int):
        return self.__abi_module.balance_of.call(self.get_signer_address(), token_id)

    def is_approved(self, address: str, operator: str):
        return self.__abi_module.is_approved_for_all.call(address, operator)

    def lazy_mint_batch(self, metadatas: list):
        """
        :param metadata: List of metadata
        :return: List of token IDs
        Lazy mints a batch of drops
        """
        token_ids = self.create_batch(metadatas)
        return [self.get(i) for i in token_ids]

    def create_batch(self, metadatas: list):
        """
        :param metadata: List of metadata
        :return: List of token IDs
        Creates a batch of drops
        """
        start_file_number = self.__abi_module.next_token_id_to_mint()
        base_uri = self.get_storage().upload_batch(
            metadatas, self.address, start_file_number)  # todo upload metadata batch

        tx = self.__abi_module.lazy_mint.build_transaction(
            len(metadatas), base_uri)
        receipt = self.execute_tx(tx)
        return receipt  # todo event parsing

    def set_approval(self, operator: str, approved: bool = True):
        """
        :param operator: Address of the operator
        :param approved: Approved or not
        Sets approval for a user
        """
        self.__abi_module.set_approval_for_all(operator, approved)

    def transfer(self, to: str, token_id: str, amount: int, data: bytes):
        """
        :param to: Address of the recipient
        :param token_id: ID of the drop
        :param amount: Amount of the drop
        :param data: Data to be stored
        Transfers a drop
        """
        from_address = self.get_signer_address()
        tx = self.__abi_module.transfer.build_transaction(
            from_address, to, token_id, amount, data)
        self.execute_tx(tx)

    def get_metadata(self):
        """
        :return: Metadata of the module
        Gets the metadata of the module
        """
        return self.__abi_module.get_metadata.call()

    def set_claim_condition(self, token_id: int, factory):
        """
        :param token_id: ID of the drop
        :param factory: Factory of the condition
        :return:
        Sets the claim condition of a drop
        """
        conditions = [{
            "start_timestamp": x.start_timestamp,
            "max_claim_supply": x.max_claim_supply,
            "supply_claimed": x.supply_claimed,
            "quantity_limit_per_transaction": x.quantity_limit_per_transaction,
            "wait_time_in_seconds_between_claims": x.wait_time_in_seconds_per_transaction,
            "price_per_token": x.price_per_token,
            "currency": x.currency if x.currency != "0x0000000000000000000000000000000000000000" else "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            "merkle_root": x.merkle_root
        } for x in factory.build_conditions()]

        merkle_info = {}
        for x in factory.allSnapshots():
            merkle_info[x.merkle_root] = x.snapshot_uri
        metadata = self.get_metadata()
        if not metadata:
            raise Exception("Metadata is not set, this should never happen")
        if len(factory.allSnapshots()) == 0 and 'merkle' in metadata:
            metadata["merkle"] = {}
        else:
            metadata["merkle"] = merkle_info

        metadata_uri = self.get_storage().upload_metadata(metadata)
        # todo multicall
        from_address = self.get_signer_address()
        return self.execute_tx(self.__abi_module.set_claim_condition.build_transaction(factory.get_claim_condition(), metadata_uri, from_address))

    def claim(self, token_id: int, quantity: int, proofs: list):
        mc = self.get_active_claim_condition()
        # todo overrides
        address_to_claim = self.get_signer_address()
        metadata = self.get_metadata()
        address_to_claim = self.get_signer_address()
        if not (mc.merkle_root.startswith("0x0000000000000000000000000000000000000000")):
            snapshot = self.get_storage().get(metadata.merkle[mc.merkle_root])
            snapshot_data = json.loads(snapshot)  # deserialize
            item = list(
                filter(lambda x: x["address"] == address_to_claim, snapshot_data))
            if item is None:
                return Exception("No claim for this address")
            proofs = item.proof
        if mc.price_per_token > 0:
            if is_native_currency(mc.currency):  # todo
                overrides["value"] = mc.price_per_token * quantity
            else:
                pass  # todo erc20 faactory
        tx = self.__abi_module.claim.build_transaction(
            token_id, quantity, proofs)
        return self.execute_tx(tx)  # todo overrides

    def burn(self, token_id: int, amount: int):
        """
        :param token_id: ID of the drop
        Burns a drop
        """
        return self.execute_tx(self.__abi_module.burn.build_transaction(self.get_signer_address(), token_id, amount))

    def transfer_from(self, transfer_from: str, to: str, token_id: int, amount: int, data: bytes):
        """
        :param transfer_from: Address of the sender
        :param to: Address of the recipient
        :param token_id: ID of the drop
        :param amount: Amount of the drop
        :param data: Data to be stored
        Transfers a drop from one user to another
        """
        tx = self.__abi_module.transfer_from.build_transaction(
            transfer_from, to, token_id, amount, data)
        return self.execute_tx(tx)

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

    def set_royalty_bps(self, amount: int):  # todo multicall
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

    def set_restricted_transfer(self, restricted: bool):
        """
        :param restricted: Whether the transfer is restricted
        :return: The transaction hash

        Sets whether the transfer is restricted
        """
        tx = self.__abi_module.set_restricted_transfer.build_transaction(
            restricted, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def get_royalty_bps(self):
        """
        :return: The royalty percentage
        Gets the royalty percentage for the NFT
        """
        return self.__abi_module.royalty_bps.call()

    def get_royalty_recipient_address(self):
        """
        :return: The address of the recipient
        Gets the address of the recipient
        """
        metadata = self.get_metadata().metadata
        if 'fee_recipient' not in metadata.metadata:
            return metadata['fee_recipient']
        return ""

    def get_claim_conditions_factory(self):
        """
        :return: The address of the factory
        Gets the address of the factory
        """
        # todo
        pass

    def get_all_claimer_addresses(self, token_id: int):
        """
        :param token_id: The ID of the drop
        :return: The list of claimers
        Gets the list of claimers for the drop
        """
        # todo
        pass

    def can_claim(self, token_id: int, quantity: int):
        """
        :param token_id: The ID of the drop
        :return: Whether the drop can be claimed
        Checks whether the drop can be claimed
        """
        try:
            mc = self.get_active_claim_condition()
            proofs = self.get_claimer_proofs(mc.merkle_root)
            overrides = {}  # todo
            if mc.price_per_token > 0:
                if is_native_currency(mc.currency):
                    overrides["value"] = mc.price_per_token * quantity
                else:
                    pass  # todo
            self.__abi_module.claim.call_static(
                token_id, quantity, proofs, overrides)
            return True
        except:
            return False
        pass
