import pytest
from challenges.challenge_51_store_array.store_array_51 import store_elements_in_array


def test_valid_array():
    assert store_elements_in_array(3, [1, 2, 3]) == [1, 2, 3]


def test_empty_array():
    assert store_elements_in_array(0, []) == []


def test_size_mismatch_raises_error():
    with pytest.raises(ValueError):
        store_elements_in_array(2, [1])


def test_negative_size_raises_error():
    with pytest.raises(ValueError):
        store_elements_in_array(-1, [])
