from challenges.challenge_56_sum_2d_array.sum_2d_array_56 import sum_2d_array


def test_square_matrix():
    matrix = [
        [1, 2],
        [3, 4],
    ]
    assert sum_2d_array(matrix) == 10


def test_rectangular_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    assert sum_2d_array(matrix) == 21


def test_single_row():
    matrix = [[10, 20, 30]]
    assert sum_2d_array(matrix) == 60


def test_single_column():
    matrix = [[1], [2], [3]]
    assert sum_2d_array(matrix) == 6


def test_empty_matrix():
    assert sum_2d_array([]) == 0
