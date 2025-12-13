from challenges.challenge_54_binary_search.binary_search_54 import binary_search


def test_element_found_middle():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_element_found_first():
    assert binary_search([2, 4, 6, 8], 2) == 0


def test_element_found_last():
    assert binary_search([2, 4, 6, 8], 8) == 3


def test_element_not_found():
    assert binary_search([1, 2, 3, 4], 6) == -1


def test_empty_array():
    assert binary_search([], 10) == -1
