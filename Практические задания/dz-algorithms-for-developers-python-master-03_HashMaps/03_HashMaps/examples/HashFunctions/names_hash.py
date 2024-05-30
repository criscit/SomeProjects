class NamesHash:
    def __init__(self):
        self.values = [None] * 8

    def get_index_by_key(self, key: str) -> int:
        return len(key)

    def get_value_by_key(self, key: str) -> int:
        index = self.get_index_by_key(key)
        return self.values[index]


names_hash = NamesHash()
names_hash.values[2] = 14  # Ия
names_hash.values[3] = 99  # Аня
names_hash.values[4] = 30  # Миша
names_hash.values[5] = 42  # Антон
names_hash.values[6] = 87  # Владик
names_hash.values[7] = 71  # Николай
