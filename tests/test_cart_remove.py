from shop.cart import Cart


def test_remove_one():
    cart = Cart()
    cart.add("mug", 8.50, 2)
    cart.remove("mug")
    assert cart.count() == 1


def test_remove_missing_is_ignored():
    Cart().remove("tee")
