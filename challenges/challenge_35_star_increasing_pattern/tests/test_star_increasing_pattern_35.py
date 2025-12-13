from challenges.challenge_35_star_increasing_pattern.star_increasing_pattern_35 import generate_star_increasing_pattern


def test_single_row():
    assert generate_star_increasing_pattern(1) == ["*"]


def test_multiple_rows():
    assert generate_star_increasing_pattern(4) == ["*", "**", "***", "****"]


def test_zero_rows():
    assert generate_star_increasing_pattern(0) == []


def test_negative_rows():
    assert generate_star_increasing_pattern(-3) == []


def test_large_n():
    result = generate_star_increasing_pattern(10)
    assert len(result) == 10
    assert result[-1] == "**********"
