from decimal import Decimal

from shop.pricing import apply_discount


def test_discount_rounding():
    # half a cent rounds up, like the till: 19.99 - 50 % = 9.995 -> 10.00
    assert apply_discount(19.99, 50) == Decimal("10.00")
