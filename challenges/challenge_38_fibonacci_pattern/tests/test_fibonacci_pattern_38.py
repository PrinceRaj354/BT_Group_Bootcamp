from challenges.challenge_38_fibonacci_pattern.fibonacci_pattern_38 import (
    generate_fibonacci_pattern,
)


def test_single_row():
    assert generate_fibonacci_pattern(1) == ["1"]


def test_two_rows():
    assert generate_fibonacci_pattern(2) == [
        "1",
        "1 2",
    ]


def test_four_rows():
    assert generate_fibonacci_pattern(4) == [
        "1",
        "1 2",
        "3 5 8",
        "13 21 34 55",
    ]


def test_zero_rows():
    assert generate_fibonacci_pattern(0) == []


def test_negative_rows():
    assert generate_fibonacci_pattern(-4) == []


def test_large_n_row_count():
    result = generate_fibonacci_pattern(10)
    assert len(result) == 10
