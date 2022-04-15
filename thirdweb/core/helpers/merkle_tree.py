from typing import Callable, List


class MerkleTree:
    def __init__(self, leaves: List[str], hash_function: Callable[[str], str]):
        self.leaves = leaves
        self.hash_function = hash_function
        self.process_leaves(leaves)

    def process_leaves(self, leaves: List[str]):
        pass
