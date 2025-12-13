import pytest
from challenges.challenge_47_min_array.min_array_47 import min_of_elements


def test_normal_array():
    assert min_of_elements([4, 2, 8, 1, 5]) == 1


def test_single_element():
    assert min_of_elements([10]) == 10


def test_negative_numbers():
    assert min_of_elements([-3, -7, -1]) == -7


def test_mixed_numbers():
    assert min_of_elements([5, -2, 3, 0]) == -2


def test_empty_array_raises_error():
    with pytest.raises(ValueError):
        min_of_elements([])
