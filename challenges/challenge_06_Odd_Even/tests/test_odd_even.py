from challenges.challenge_06_Odd_Even.odd_even import is_even_or_odd

def test_even_number():
    assert is_even_or_odd(10) == "Even"

def test_odd_number():
    assert is_even_or_odd(7) == "Odd"

def test_zero():
    assert is_even_or_odd(0) == "Even"

def test_negative_even():
    assert is_even_or_odd(-4) == "Even"

def test_negative_odd():
    assert is_even_or_odd(-9) == "Odd"
