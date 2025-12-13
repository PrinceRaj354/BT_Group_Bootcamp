from challenges.challenge_55_2d_array.array_2d_55 import create_and_display_2d_array


def test_square_matrix():
    matrix = [
        [1, 2],
        [3, 4],
    ]
    assert create_and_display_2d_array(matrix) == [
        [1, 2],
        [3, 4],
    ]


def test_rectangular_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    assert create_and_display_2d_array(matrix) == [
        [1, 2, 3],
        [4, 5, 6],
    ]


def test_single_row():
    matrix = [[10, 20, 30]]
    assert create_and_display_2d_array(matrix) == [[10, 20, 30]]


def test_single_column():
    matrix = [[1], [2], [3]]
    assert create_and_display_2d_array(matrix) == [[1], [2], [3]]


def test_empty_matrix():
    assert create_and_display_2d_array([]) == []
