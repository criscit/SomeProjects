class Book:
    def __init__(self, title: str, author: str, year: int, price: float):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def __repr__(self):
        return f"Book{{title='{self.title}', author='{self.author}', year={self.year}, price={self.price}}}"

    def __eq__(self, other: "Book") -> bool:
        return (
            self.title == other.title
            and self.author == other.author
            and self.year == other.year
            and self.price == other.price
        )

    def compare_to(self, o):
        if self.year != o.year:
            return -1
        return 0
