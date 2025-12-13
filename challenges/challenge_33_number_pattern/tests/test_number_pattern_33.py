from challenges.challenge_33_number_pattern.number_pattern_33 import generate_number_pattern


def test_single_row():
    assert generate_number_pattern(1) == ["11111"]


def test_multiple_rows():
    assert generate_number_pattern(4) == [
        "11111",
        "22222",
        "33333",
        "44444",
    ]


def test_zero_rows():
    assert generate_number_pattern(0) == []


def test_negative_rows():
    assert generate_number_pattern(-3) == []


def test_large_n():
    result = generate_number_pattern(10)
    assert len(result) == 10
    assert result[0] == "11111"
    assert result[-1] == "1010101010"
