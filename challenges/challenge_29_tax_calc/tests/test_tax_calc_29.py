from challenges.challenge_29_tax_calc.tax_calc_29 import calculate_tax_and_total


def test_below_5000():
    tax, total = calculate_tax_and_total(4000)
    assert tax == 200
    assert total == 4200


def test_between_5000_and_20000():
    tax, total = calculate_tax_and_total(10000)
    assert tax == 1000
    assert total == 11000


def test_above_20000():
    tax, total = calculate_tax_and_total(25000)
    assert tax == 3750
    assert total == 28750


def test_exact_5000():
    tax, total = calculate_tax_and_total(5000)
    assert tax == 500
    assert total == 5500
