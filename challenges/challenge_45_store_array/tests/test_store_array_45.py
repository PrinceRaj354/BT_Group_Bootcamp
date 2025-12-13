import pytest
from challenges.challenge_45_store_array.store_array_45 import store_elements


def test_valid_array_storage():
    assert store_elements(5, [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_empty_array():
    assert store_elements(0, []) == []


def test_mismatch_size_raises_error():
    with pytest.raises(ValueError):
        store_elements(3, [1, 2])


def test_negative_size_raises_error():
    with pytest.raises(ValueError):
        store_elements(-1, [])
