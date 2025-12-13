import pytest
from challenges.challenge_48_max_array.max_array_48 import max_of_elements


def test_normal_array():
    assert max_of_elements([4, 2, 8, 1, 5]) == 8


def test_single_element():
    assert max_of_elements([10]) == 10


def test_negative_numbers():
    assert max_of_elements([-3, -7, -1]) == -1


def test_mixed_numbers():
    assert max_of_elements([5, -2, 3, 0]) == 5


def test_empty_array_raises_error():
    with pytest.raises(ValueError):
        max_of_elements([])
