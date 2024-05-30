class Item:
    amount_compare_to = 0
    amount_equals = 0

    def __init__(self, data: int):
        self.data = data

    @classmethod
    def clear_amount_compare_to(cls):
        cls.amount_compare_to = 0

    def __eq__(self, o: "Item") -> bool:
        Item.amount_equals += 1
        if not isinstance(o, Item):
            return False

        return self.data == o.data

    def __str__(self) -> str:
        return str(self.data)

    def compare_to(self, o: "Item") -> int:
        Item.amount_compare_to += 1
        if self.data > o.data:
            return 1
        if self.data < o.data:
            return -1
        return 0
