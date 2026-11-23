from shop.pricing import points


def test_points_whole():
    assert points(20) == 20


def test_points_never_round_up():
    assert points(19.99) == 19
