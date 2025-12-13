from challenges.challenge_57_search_2d_array.search_2d_array_57 import (
    element_exists_2d,
)


def test_element_present():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    assert element_exists_2d(matrix, 5) is True


def test_element_not_present():
    matrix = [
        [1, 2],
        [3, 4],
    ]
    assert element_exists_2d(matrix, 9) is False


def test_single_row():
    matrix = [[10, 20, 30]]
    assert element_exists_2d(matrix, 20) is True


def test_single_column():
    matrix = [[1], [2], [3]]
    assert element_exists_2d(matrix, 3) is True


def test_empty_matrix():
    assert element_exists_2d([], 1) is False
