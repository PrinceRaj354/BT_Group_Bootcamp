from challenges.challenge_36_number_increasing_pattern.number_repeat_pattern_36 import (
    generate_number_increasing_pattern,
)


def test_single_row():
    assert generate_number_increasing_pattern(1) == ["1"]


def test_multiple_rows():
    assert generate_number_increasing_pattern(4) == [
        "1",
        "22",
        "333",
        "4444",
    ]


def test_zero_rows():
    assert generate_number_increasing_pattern(0) == []


def test_negative_rows():
    assert generate_number_increasing_pattern(-3) == []


def test_large_n():
    result = generate_number_increasing_pattern(10)
    assert len(result) == 10
    assert result[-1] == "10101010101010101010"
