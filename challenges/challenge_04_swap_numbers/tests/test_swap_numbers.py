from challenges.challenge_04_swap_numbers.swap_numbers import swap_numbers

def test_basic_swap():
    x, y = swap_numbers(10, 20)
    assert x == 20
    assert y == 10

def test_negative_numbers():
    x, y = swap_numbers(-5, -9)
    assert x == -9
    assert y == -5

def test_mixed_numbers():
    x, y = swap_numbers(-3, 7)
    assert x == 7
    assert y == -3

def test_float_swap():
    x, y = swap_numbers(2.5, 9.75)
    assert x == 9.75
    assert y == 2.5

def test_same_values():
    x, y = swap_numbers(100, 100)
    assert x == 100
    assert y == 100
