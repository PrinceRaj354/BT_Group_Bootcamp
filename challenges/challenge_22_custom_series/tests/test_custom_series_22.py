import pytest
from challenges.challenge_22_custom_series.custom_series import generate_custom_series

def test_initial_terms():
    assert generate_custom_series(30) == [1, 4, 7, 12, 23]

def test_extended_terms():
    assert generate_custom_series(50) == [1, 4, 7, 12, 23, 46]

def test_small_limit():
    assert generate_custom_series(5) == [1, 4]

def test_single_value():
    assert generate_custom_series(1) == [1]

def test_invalid_zero():
    with pytest.raises(ValueError):
        generate_custom_series(0)

def test_invalid_negative():
    with pytest.raises(ValueError):
        generate_custom_series(-10)
