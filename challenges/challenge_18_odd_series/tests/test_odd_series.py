import pytest
from challenges.challenge_18_odd_series.odd_series import generate_odd_series

def test_normal_series():
    assert generate_odd_series(10) == [1, 3, 5, 7, 9]

def test_small_series():
    assert generate_odd_series(3) == [1, 3]

def test_exact_odd_limit():
    assert generate_odd_series(5) == [1, 3, 5]

def test_invalid_zero():
    with pytest.raises(ValueError):
        generate_odd_series(0)

def test_invalid_negative():
    with pytest.raises(ValueError):
        generate_odd_series(-7)
