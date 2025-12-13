from challenges.challenge_50_count_odd_even.count_odd_even_50 import count_odd_even


def test_mixed_numbers():
    assert count_odd_even([1, 2, 3, 4, 5, 6]) == (3, 3)


def test_all_even():
    assert count_odd_even([2, 4, 6, 8]) == (0, 4)


def test_all_odd():
    assert count_odd_even([1, 3, 5, 7]) == (4, 0)


def test_single_element_even():
    assert count_odd_even([10]) == (0, 1)


def test_single_element_odd():
    assert count_odd_even([9]) == (1, 0)


def test_empty_array():
    assert count_odd_even([]) == (0, 0)
