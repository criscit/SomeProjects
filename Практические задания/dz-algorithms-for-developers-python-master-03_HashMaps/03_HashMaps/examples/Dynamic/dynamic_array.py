from typing import List, Optional


class DynamicArray:
    def __init__(self):
        self.values: List[Optional[int]] = [None] * 8
        self.size = 8
        self.current_index = 0

    def add(self, value: int) -> None:
        self.values[self.current_index] = value
        self.current_index += 1
        if self.current_index == self.size:
            self.resize(self.size * 2)

    def resize(self, new_size: int) -> None:
        new_values = [None] * new_size
        i = 0
        while i < size:
            new_values[i] = values[i]
            i += 1
        self.values = new_values
        self.size = new_size
