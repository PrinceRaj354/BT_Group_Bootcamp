from challenges.challenge_37_number_increasing_pattern.number_increasing_pattern_37 import (
    generate_number_increasing_pattern,
)


def test_single_row():
    assert generate_number_increasing_pattern(1) == ["1"]


def test_multiple_rows():
    assert generate_number_increasing_pattern(4) == [
        "1",
        "12",
        "123",
        "1234",
    ]


def test_zero_rows():
    assert generate_number_increasing_pattern(0) == []


def test_negative_rows():
    assert generate_number_increasing_pattern(-5) == []


def test_large_n():
    result = generate_number_increasing_pattern(10)
    assert len(result) == 10
    assert result[-1] == "12345678910"
