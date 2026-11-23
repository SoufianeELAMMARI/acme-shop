from datetime import date

from shop.coupons import is_valid


def test_valid_before():
    assert is_valid("SAVE10", date(2030, 6, 1))


def test_valid_on_last_day():
    assert is_valid("SAVE10", date(2030, 6, 30))


def test_expired_after():
    assert not is_valid("SAVE10", date(2030, 7, 1))
