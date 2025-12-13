from challenges.challenge_34_number_pattern.number_pattern_seq_34 import generate_number_pattern


def test_single_row():
    assert generate_number_pattern(1) == ["12345"]


def test_multiple_rows():
    assert generate_number_pattern(4) == [
        "12345",
        "12345",
        "12345",
        "12345",
    ]


def test_zero_rows():
    assert generate_number_pattern(0) == []


def test_negative_rows():
    assert generate_number_pattern(-5) == []


def test_large_n():
    result = generate_number_pattern(10)
    assert len(result) == 10
    assert all(row == "12345" for row in result)
