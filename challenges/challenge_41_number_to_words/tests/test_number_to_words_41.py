from challenges.challenge_41_number_to_words.number_to_words_41 import (
    convert_number_to_words,
)


def test_given_example():
    assert convert_number_to_words(270176) == "Two Seven Zero One Seven Six"


def test_single_digit():
    assert convert_number_to_words(5) == "Five"


def test_number_with_zero():
    assert convert_number_to_words(1010) == "One Zero One Zero"


def test_all_digits():
    assert convert_number_to_words(1234567890) == (
        "One Two Three Four Five Six Seven Eight Nine Zero"
    )


def test_large_number():
    result = convert_number_to_words(987654321)
    assert result.startswith("Nine")
    assert result.endswith("One")
