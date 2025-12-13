from challenges.challenge_52_reverse_array.reverse_array_52 import reverse_array


def test_normal_array():
    assert reverse_array([1, 2, 3, 4]) == [4, 3, 2, 1]


def test_single_element():
    assert reverse_array([10]) == [10]


def test_empty_array():
    assert reverse_array([]) == []


def test_array_with_duplicates():
    assert reverse_array([1, 2, 2, 3]) == [3, 2, 2, 1]


def test_array_with_negative_numbers():
    assert reverse_array([-1, -2, 3]) == [3, -2, -1]
