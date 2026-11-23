from shop.coupons import coupon_percent
from shop.inventory import Inventory


def test_known_coupon():
    assert coupon_percent("SAVE10") == 10


def test_unknown_coupon():
    assert coupon_percent("FREE100") == 0


def test_stock_available():
    assert Inventory({"mug": 3}).available("mug") == 3


def test_stock_unknown_sku():
    assert Inventory({}).available("tee") == 0


def test_restock():
    inv = Inventory({"mug": 1})
    inv.restock("mug", 4)
    assert inv.available("mug") == 5


def test_restock_new_sku():
    inv = Inventory({})
    inv.restock("tee", 2)
    assert inv.available("tee") == 2
