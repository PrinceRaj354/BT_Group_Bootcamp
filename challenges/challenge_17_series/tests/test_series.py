import pytest
from challenges.challenge_17_series.series import generate_series

def test_normal_series():
    assert generate_series(5) == [1, 2, 3, 4, 5]

def test_single_value():
    assert generate_series(1) == [1]

def test_large_value():
    assert generate_series(10) == [1,2,3,4,5,6,7,8,9,10]

def test_invalid_zero():
    with pytest.raises(ValueError):
        generate_series(0)

def test_invalid_negative():
    with pytest.raises(ValueError):
        generate_series(-5)
