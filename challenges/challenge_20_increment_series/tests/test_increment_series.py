import pytest
from challenges.challenge_20_increment_series.increment_series import generate_increment_series

def test_normal_series():
    assert generate_increment_series(25) == [1, 2, 4, 7, 11, 16, 22]

def test_exact_limit():
    assert generate_increment_series(22) == [1, 2, 4, 7, 11, 16, 22]

def test_small_limit():
    assert generate_increment_series(4) == [1, 2, 4]

def test_single_number():
    assert generate_increment_series(1) == [1]

def test_invalid_zero():
    with pytest.raises(ValueError):
        generate_increment_series(0)

def test_invalid_negative():
    with pytest.raises(ValueError):
        generate_increment_series(-10)
