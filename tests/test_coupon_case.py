from shop.coupons import coupon_percent


def test_lower_case_code():
    assert coupon_percent("save10") == 10


def test_code_with_spaces():
    assert coupon_percent(" SAVE20 ") == 20
