import pytest
from challenges.challenge_40_factorial_pattern.factorial_pattern_40 import (
    generate_factorial_pattern,
)


@pytest.mark.xfail(reason="Specification ambiguity: factorial pattern definition is unclear")
def test_two_rows():
    assert generate_factorial_pattern(2) == [
        "1",
        "1 2",
    ]


@pytest.mark.xfail(reason="Specification ambiguity: factorial pattern definition is unclear")
def test_three_rows():
    assert generate_factorial_pattern(3) == [
        "1",
        "1 2",
        "6 24 120",
    ]
