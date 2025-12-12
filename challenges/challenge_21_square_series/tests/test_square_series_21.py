import pytest
from challenges.challenge_21_square_series.square_series import generate_square_series

def test_normal_series():
    assert generate_square_series(50) == [1, 4, 9, 16, 25, 36, 49]

def test_exact_square_limit():
    assert generate_square_series(36) == [1, 4, 9, 16, 25, 36]

def test_small_limit():
    assert generate_square_series(5) == [1, 4]

def test_single_value():
    assert generate_square_series(1) == [1]

def test_invalid_zero():
    with pytest.raises(ValueError):
        generate_square_series(0)

def test_invalid_negative():
    with pytest.raises(ValueError):
        generate_square_series(-10)
