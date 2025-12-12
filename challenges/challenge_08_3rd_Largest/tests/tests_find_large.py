from challenges.challenge_08_3rd_Largest.find_large import third_largest
import pytest

def test_third_largest_normal():
    assert third_largest([10, 20, 30, 40, 50]) == 30

def test_third_largest_with_duplicates():
    assert third_largest([5, 5, 10, 20, 20, 30]) == 10

def test_third_largest_negative_numbers():
    assert third_largest([-1, -5, -3, -2, -4]) == -3

def test_error_when_less_than_three_unique():
    with pytest.raises(ValueError):
        third_largest([10, 20, 20])
