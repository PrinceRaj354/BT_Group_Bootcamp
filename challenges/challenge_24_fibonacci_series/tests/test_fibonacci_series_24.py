import pytest
from challenges.challenge_24_fibonacci_series.fibonacci_series import generate_fibonacci_series

def test_normal_series():
    assert generate_fibonacci_series(25) == [1, 1, 2, 3, 5, 8, 13, 21]

def test_exact_limit():
    assert generate_fibonacci_series(21) == [1, 1, 2, 3, 5, 8, 13, 21]

def test_small_limit():
    assert generate_fibonacci_series(5) == [1, 1, 2, 3, 5]

def test_limit_one():
    assert generate_fibonacci_series(1) == [1]

def test_invalid_zero():
    with pytest.raises(ValueError):
        generate_fibonacci_series(0)

def test_invalid_negative():
    with pytest.raises(ValueError):
        generate_fibonacci_series(-10)
