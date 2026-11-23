from shop.pricing import format_price


def test_format_small():
    assert format_price(4.5) == "$4.50"


def test_format_thousands():
    assert format_price(1234.5) == "$1,234.50"
