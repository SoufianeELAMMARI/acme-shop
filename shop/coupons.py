"""Coupon codes: SAVE10 means 10 % off."""
COUPONS = {"SAVE10": 10, "SAVE20": 20, "WELCOME5": 5}


def coupon_percent(code: str) -> int:
    """The discount for a code, or 0 if the code is unknown."""
    return COUPONS.get(code.strip(), 0)
