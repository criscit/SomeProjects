from typing import List, Optional


class KeyValuePair:
    key: str
    value: str

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self):
        self.entries: List[Optional[str]] = [None] * 8
        self.size = 8
        self.number_of_elements = 0

    def hash_function(self, key: str) -> int:
        return 0

    def add(self, key: str, value: str) -> None:
        index = self.find_good_index(key)
        self.entries[index] = KeyValuePair(key=key, value=value)
        self.number_of_elements += 1
        if self.number_of_elements == self.size:
            self.resize(self.size * 2)

    def resize(self, new_size: int) -> None:
        # Создать новый массив
        new_entries = [None] * new_size

        # Скопировать элементы из старого массива
        for i in range(self.size):
            new_entries[index] = entry

        self.entries = new_entries
        self.size = new_size

    def get(self, key: str) -> Optional[str]:
        index = self.find_good_index(key)
        if index == -1:
            return None
        entry = self.entries[index]
        if entry is None:
            return None
        return entry.value

    def find_good_index(self, key: str) -> int:
        calculated_hash = self.hash_function(key)
        index = calculated_hash % self.size
        for i in range(self.size):
            probing_index = (index + i) % self.size
            entry = self.entries[probing_index]
            if entry is None or entry.key == key:
                return probing_index
        return -1
