from decimal import Decimal

from shop.pricing import split


def test_split_even():
    assert split(9, 3) == [Decimal("3.00")] * 3


def test_split_adds_up():
    shares = split(10, 3)
    assert sum(shares) == Decimal("10.00")
    assert max(shares) - min(shares) <= Decimal("0.01")
