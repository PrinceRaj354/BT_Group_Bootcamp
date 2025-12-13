from challenges.challenge_42_alternating_series.alternating_series_42 import (
    generate_alternating_series,
)


def test_first_five_terms():
    assert generate_alternating_series(5) == [1, -5, 9, -13, 17]


def test_single_term():
    assert generate_alternating_series(1) == [1]


def test_even_count():
    assert generate_alternating_series(6) == [1, -5, 9, -13, 17, -21]


def test_zero_terms():
    assert generate_alternating_series(0) == []


def test_negative_terms():
    assert generate_alternating_series(-4) == []
