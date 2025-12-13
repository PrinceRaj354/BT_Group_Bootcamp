from challenges.challenge_46_sum_array.sum_array_46 import sum_of_elements


def test_normal_array():
    assert sum_of_elements([1, 2, 3, 4, 5]) == 15


def test_single_element():
    assert sum_of_elements([10]) == 10


def test_empty_array():
    assert sum_of_elements([]) == 0


def test_negative_numbers():
    assert sum_of_elements([-1, -2, -3]) == -6


def test_mixed_numbers():
    assert sum_of_elements([5, -2, 3]) == 6
