"""A shopping cart: what's in it, and how many."""
from .pricing import money, subtotal


MAX_QTY = 5


class Cart:
    def __init__(self):
        self.lines = {}  # sku -> [price, quantity]

    def add(self, sku: str, price, qty: int = 1) -> None:
        if qty <= 0:
            raise ValueError("quantity must be positive")
        if qty > MAX_QTY:
            raise ValueError(f"at most {MAX_QTY} of the same item")
        if sku in self.lines:
            self.lines[sku][1] += qty
        else:
            self.lines[sku] = [money(price), qty]

    def count(self) -> int:
        return sum(qty for _, qty in self.lines.values())

    def subtotal(self):
        return subtotal(self.lines.values())
