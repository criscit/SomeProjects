class Contact:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def to_string(self) -> str:
        return f"name='{self.name}', number='{self.number}'"

    __str__ = to_string
