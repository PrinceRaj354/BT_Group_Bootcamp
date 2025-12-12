import pytest
from challenges.challenge_19_square_series.square_series import generate_square_series

def test_normal_series():
    assert generate_square_series(70) == [4, 16, 36, 64]

def test_exact_match():
    assert generate_square_series(36) == [4, 16, 36]

def test_small_limit():
    assert generate_square_series(10) == [4]

def test_no_output():
    assert generate_square_series(3) == []

def test_invalid_zero():
    with pytest.raises(ValueError):
        generate_square_series(0)

def test_invalid_negative():
    with pytest.raises(ValueError):
        generate_square_series(-20)
