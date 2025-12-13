import pytest
from challenges.challenge_53_sort_array.sort_array_53 import sort_array


def test_sort_ascending():
    assert sort_array([3, 1, 4, 2], "asc") == [1, 2, 3, 4]


def test_sort_descending():
    assert sort_array([3, 1, 4, 2], "desc") == [4, 3, 2, 1]


def test_default_sort_is_ascending():
    assert sort_array([5, 2, 9]) == [2, 5, 9]


def test_sort_with_negative_numbers():
    assert sort_array([-1, 3, -5, 2], "asc") == [-5, -1, 2, 3]


def test_invalid_order_raises_error():
    with pytest.raises(ValueError):
        sort_array([1, 2, 3], "invalid")
