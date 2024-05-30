class PhonesHash:
    def __init__(self):
        self.values = [None] * 40

    def get_index_by_key(self, key: int) -> int:
        return key % 40

    def get_value_by_key(self, key: int) -> int:
        index = self.get_index_by_key(key)
        return self.values[index]


"""
79101002030: 900,
79101234567: 100,
79999999999: 999,
74952223344: 1
… всего 40 номеров ...
"""
phones_hash = PhonesHash()
phones_hash.values[30] = 900
phones_hash.values[7] = 100
phones_hash.values[39] = 999
phones_hash.values[24] = 1
#  ...
