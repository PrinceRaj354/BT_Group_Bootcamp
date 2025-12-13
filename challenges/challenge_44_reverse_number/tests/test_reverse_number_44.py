from challenges.challenge_44_reverse_number.reverse_number_44 import reverse_number


def test_positive_number():
    assert reverse_number(12345) == 54321


def test_number_with_trailing_zero():
    assert reverse_number(1200) == 21


def test_single_digit():
    assert reverse_number(7) == 7


def test_zero():
    assert reverse_number(0) == 0


def test_negative_number():
    assert reverse_number(-456) == -654
