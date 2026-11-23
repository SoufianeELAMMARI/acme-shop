from decimal import Decimal

import pytest

from shop.pricing import add_tax, apply_discount, money, shipping, subtotal, total


def test_money_rounds_half_up():
    assert money(2.675) == Decimal("2.68")


def test_money_keeps_two_places():
    assert str(money(3)) == "3.00"


def test_subtotal():
    assert subtotal([(9.99, 2), (5, 1)]) == Decimal("24.98")


def test_subtotal_empty():
    assert subtotal([]) == Decimal("0.00")


def test_discount_ten_percent():
    assert apply_discount(100, 10) == Decimal("90.00")


def test_discount_zero():
    assert apply_discount(19.99, 0) == Decimal("19.99")


def test_discount_rejects_over_100():
    with pytest.raises(ValueError):
        apply_discount(10, 120)


def test_tax_twenty_percent():
    assert add_tax(50, 20) == Decimal("60.00")


def test_shipping_below_threshold():
    assert shipping(49.99) == Decimal("4.99")


def test_shipping_free_from_60():
    assert shipping(60) == Decimal("0.00")


def test_shipping_paid_at_50():
    assert shipping(50) == Decimal("4.99")


def test_total_small_order():
    assert total([(10, 2)]) == Decimal("24.99")


def test_total_with_discount_and_tax():
    assert total([(40, 2)], discount_percent=10, tax_rate=20) == Decimal("86.40")


def test_total_with_shipping_at_55():
    assert total([(55, 1)]) == Decimal("59.99")
