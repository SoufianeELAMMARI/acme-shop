from shop.pricing import bulk_discount


def test_bulk_from_ten():
    assert bulk_discount(10) == 10


def test_no_bulk_below_ten():
    assert bulk_discount(9) == 0
