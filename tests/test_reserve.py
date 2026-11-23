import pytest

from shop.inventory import Inventory, OutOfStock


def test_reserve():
    inv = Inventory({"mug": 3})
    inv.reserve("mug", 2)
    assert inv.available("mug") == 1


def test_reserve_too_many():
    inv = Inventory({"mug": 1})
    with pytest.raises(OutOfStock):
        inv.reserve("mug", 2)
    assert inv.available("mug") == 1
