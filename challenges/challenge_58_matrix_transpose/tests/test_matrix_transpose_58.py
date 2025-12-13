from challenges.challenge_58_matrix_transpose.matrix_transpose_58 import (
    matrix_and_transpose,
)


def test_square_matrix():
    matrix = [
        [1, 2],
        [3, 4],
    ]
    original, transpose = matrix_and_transpose(matrix)
    assert original == [[1, 2], [3, 4]]
    assert transpose == [[1, 3], [2, 4]]


def test_rectangular_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    original, transpose = matrix_and_transpose(matrix)
    assert original == [[1, 2, 3], [4, 5, 6]]
    assert transpose == [[1, 4], [2, 5], [3, 6]]


def test_single_row():
    matrix = [[1, 2, 3]]
    original, transpose = matrix_and_transpose(matrix)
    assert original == [[1, 2, 3]]
    assert transpose == [[1], [2], [3]]


def test_single_column():
    matrix = [[1], [2], [3]]
    original, transpose = matrix_and_transpose(matrix)
    assert original == [[1], [2], [3]]
    assert transpose == [[1, 2, 3]]


def test_empty_matrix():
    original, transpose = matrix_and_transpose([])
    assert original == []
    assert transpose == []
