from challenges.challenge_43_whole_fraction.whole_fraction_43 import (
    separate_whole_and_fraction,
)


def test_positive_value():
    assert separate_whole_and_fraction(12.75) == (12, 0.75)


def test_no_fraction():
    assert separate_whole_and_fraction(5.0) == (5, 0.0)


def test_only_fraction_less_than_one():
    assert separate_whole_and_fraction(0.25) == (0, 0.25)


def test_negative_value():
    assert separate_whole_and_fraction(-7.6) == (-7, -0.6)


def test_large_value():
    whole, fraction = separate_whole_and_fraction(123456.789)
    assert whole == 123456
    assert round(fraction, 3) == 0.789
