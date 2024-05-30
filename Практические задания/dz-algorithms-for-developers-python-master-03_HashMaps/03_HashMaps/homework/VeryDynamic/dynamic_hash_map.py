# Modify sys.path to import modules from examples dir
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from typing import List

from examples.Dynamic.hash_map import HashMap


class DynamicHashMap(HashMap):
    def delete_key(self, key: str) -> None:
        # TODO please implement
        pass

    def get_all_keys(self) -> List[str]:
        # TODO please implement
        return [""]

    def get_all_values(self) -> List[str]:
        # TODO please implement
        return [""]
