"""Stock levels per sku."""


class OutOfStock(Exception):
    pass


class Inventory:
    def __init__(self, stock: dict[str, int]):
        self.stock = dict(stock)

    def available(self, sku: str) -> int:
        return self.stock.get(sku, 0)

    def restock(self, sku: str, qty: int) -> None:
        self.stock[sku] = self.available(sku) + qty
