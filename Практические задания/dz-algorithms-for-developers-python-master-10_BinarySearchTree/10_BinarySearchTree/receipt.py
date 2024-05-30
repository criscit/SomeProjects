class Receipt:
    def __init__(self, receipt_number: int, amount: float):
        self.receipt_number: int = receipt_number
        self.amount: float = amount

    def __str__(self) -> str:
        return f"Receipt receipt_number={self.receipt_number}"
