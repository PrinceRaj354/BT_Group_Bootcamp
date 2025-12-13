from challenges.challenge_33_loyalty_points.loyalty_points_33 import calculate_loyalty_points


def test_zero_amount():
    assert calculate_loyalty_points(0) == 0


def test_below_100_amount():
    assert calculate_loyalty_points(99) == 0


def test_exact_100_amount():
    assert calculate_loyalty_points(100) == 1


def test_multiple_hundreds():
    assert calculate_loyalty_points(750) == 7


def test_large_amount():
    assert calculate_loyalty_points(5250) == 52


def test_negative_amount():
    assert calculate_loyalty_points(-300) == 0
