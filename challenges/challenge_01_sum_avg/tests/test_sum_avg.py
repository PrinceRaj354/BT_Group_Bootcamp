from challenges.challenge_01_sum_avg.sum_avg import sum_and_average

def test_positive_numbers():
    s, avg = sum_and_average(10, 20)
    assert s == 30
    assert avg == 15

def test_negative_and_positive():
    s, avg = sum_and_average(-5, 5)
    assert s == 0
    assert avg == 0

def test_floats():
    s, avg = sum_and_average(2.5, 3.5)
    assert s == 6.0
    assert avg == 3.0
