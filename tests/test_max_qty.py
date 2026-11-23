import pytest

from shop.cart import Cart


def test_five_is_fine():
    cart = Cart()
    cart.add("mug", 8.50, 5)
    assert cart.count() == 5


def test_six_in_one_go():
    with pytest.raises(ValueError):
        Cart().add("mug", 8.50, 6)


def test_six_over_two_adds():
    cart = Cart()
    cart.add("mug", 8.50, 3)
    with pytest.raises(ValueError):
        cart.add("mug", 8.50, 3)
    assert cart.count() == 3
