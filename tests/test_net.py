from decimal import Decimal

from shop.pricing import add_tax, price_without_tax


def test_net_from_gross():
    assert price_without_tax(120, 20) == Decimal("100.00")


def test_round_trip():
    assert add_tax(price_without_tax(59.99, 20), 20) == Decimal("59.99")
