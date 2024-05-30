# Modify sys.path to import modules from examples dir
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from examples.Dynamic.dynamic_array import DynamicArray


class VeryDynamicArray(DynamicArray):
    def delete_element_at(self, index: int) -> None:
        # TODO please implement
        pass
