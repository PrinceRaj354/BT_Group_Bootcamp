import pytest
from challenges.challenge_60_matrix_multiplication.matrix_multiply_60 import (
    multiply_matrices,
)


def test_square_matrices():
    a = [
        [1, 2],
        [3, 4],
    ]
    b = [
        [5, 6],
        [7, 8],
    ]
    assert multiply_matrices(a, b) == [
        [19, 22],
        [43, 50],
    ]


def test_rectangular_matrices():
    a = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    b = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]
    assert multiply_matrices(a, b) == [
        [58, 64],
        [139, 154],
    ]


def test_single_element_matrices():
    assert multiply_matrices([[3]], [[4]]) == [[12]]


def test_invalid_dimensions_raises_error():
    with pytest.raises(ValueError):
        multiply_matrices([[1, 2]], [[3, 4]])


def test_empty_matrix_raises_error():
    with pytest.raises(ValueError):
        multiply_matrices([], [])
