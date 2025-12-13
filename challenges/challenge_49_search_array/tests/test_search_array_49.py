from challenges.challenge_49_search_array.search_array_49 import search_element


def test_element_found():
    assert search_element([10, 20, 30, 40], 30) == 2


def test_element_not_found():
    assert search_element([1, 2, 3, 4], 5) == -1


def test_first_element():
    assert search_element([7, 8, 9], 7) == 0


def test_last_element():
    assert search_element([7, 8, 9], 9) == 2


def test_empty_array():
    assert search_element([], 10) == -1
