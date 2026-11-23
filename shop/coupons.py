"""Coupon codes: SAVE10 means 10 % off."""
from datetime import date

COUPONS = {"SAVE10": 10, "SAVE20": 20, "WELCOME5": 5}


LAST_DAY = {"SAVE10": date(2030, 6, 30), "SAVE20": date(2030, 1, 31), "WELCOME5": date(2031, 12, 31)}


def is_valid(code: str, today: date) -> bool:
    """True up to and including the coupon's last day."""
    return code in LAST_DAY and today < LAST_DAY[code]


def coupon_percent(code: str) -> int:
    """The discount for a code, or 0 if the code is unknown."""
    return COUPONS.get(code, 0)
