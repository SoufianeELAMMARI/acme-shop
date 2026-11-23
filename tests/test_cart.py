from decimal import Decimal

import pytest

from shop.cart import Cart


def test_empty_cart():
    assert Cart().count() == 0


def test_add_items():
    cart = Cart()
    cart.add("mug", 8.50, 2)
    cart.add("tee", 15)
    assert cart.count() == 3


def test_add_same_sku_twice():
    cart = Cart()
    cart.add("mug", 8.50)
    cart.add("mug", 8.50)
    assert cart.lines["mug"][1] == 2


def test_cart_subtotal():
    cart = Cart()
    cart.add("mug", 8.50, 2)
    assert cart.subtotal() == Decimal("17.00")


def test_add_rejects_zero():
    with pytest.raises(ValueError):
        Cart().add("mug", 8.50, 0)
