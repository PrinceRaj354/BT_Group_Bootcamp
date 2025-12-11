from challenges.challenge_02_simple_interest.simple_interest import calculate_simple_interest

def test_positive_values():
    assert calculate_simple_interest(1000, 5, 2) == 100

def test_zero_principal():
    assert calculate_simple_interest(0, 5, 2) == 0

def test_zero_rate():
    assert calculate_simple_interest(1000, 0, 2) == 0

def test_zero_time():
    assert calculate_simple_interest(1000, 5, 0) == 0

def test_decimal_values():
    assert calculate_simple_interest(1500.5, 4.5, 1.5) == (1500.5 * 4.5 * 1.5) / 100
