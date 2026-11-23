"""Stock levels per sku."""


class OutOfStock(Exception):
    pass


class Inventory:
    def __init__(self, stock: dict[str, int]):
        self.stock = dict(stock)

    def available(self, sku: str) -> int:
        return self.stock.get(sku, 0)

    def reserve(self, sku: str, qty: int) -> None:
        """Take qty out of stock, or raise OutOfStock."""
        self.stock[sku] = self.available(sku) - qty

    def restock(self, sku: str, qty: int) -> None:
        self.stock[sku] = self.available(sku) + qty
