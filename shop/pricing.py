"""Prices, discounts, tax and shipping. Money is always a Decimal with two places."""
from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")
FREE_SHIPPING_FROM = Decimal("50.00")
SHIPPING = Decimal("4.99")


def money(value) -> Decimal:
    """Any number -> a Decimal rounded to the cent, halves rounded up."""
    return Decimal(str(value)).quantize(CENT, rounding=ROUND_HALF_UP)


def subtotal(items) -> Decimal:
    """items: (price, quantity) pairs."""
    return money(sum((money(price) * qty for price, qty in items), Decimal("0")))


def apply_discount(amount, percent) -> Decimal:
    """Take percent off amount, rounded to the cent like the till does."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    discounted = float(amount) * (100 - percent) / 100
    return Decimal(str(round(discounted, 2)))


def add_tax(amount, rate) -> Decimal:
    """rate is a percentage, e.g. 20 for 20 %."""
    return money(money(amount) * (Decimal(100) + Decimal(str(rate))) / 100)


def shipping(amount) -> Decimal:
    """Free from 50.00, a flat 4.99 below."""
    return Decimal("0.00") if money(amount) >= FREE_SHIPPING_FROM else SHIPPING


def total(items, discount_percent=0, tax_rate=0) -> Decimal:
    """Subtotal, minus the discount, plus tax, plus shipping."""
    after_discount = apply_discount(subtotal(items), discount_percent)
    return money(add_tax(after_discount, tax_rate) + shipping(after_discount))
