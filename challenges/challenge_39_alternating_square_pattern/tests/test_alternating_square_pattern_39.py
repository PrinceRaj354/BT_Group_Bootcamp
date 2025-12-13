from challenges.challenge_39_alternating_square_pattern.alternating_square_pattern_39 import (
    generate_alternating_square_pattern,
)


def test_single_row():
    assert generate_alternating_square_pattern(1) == ["1"]


def test_two_rows():
    assert generate_alternating_square_pattern(2) == [
        "1",
        "-4 9",
    ]


def test_four_rows():
    assert generate_alternating_square_pattern(4) == [
        "1",
        "-4 9",
        "-16 25 -36",
        "49 -64 81 -100",
    ]


def test_zero_rows():
    assert generate_alternating_square_pattern(0) == []


def test_negative_rows():
    assert generate_alternating_square_pattern(-3) == []


def test_large_n_row_count():
    result = generate_alternating_square_pattern(10)
    assert len(result) == 10
