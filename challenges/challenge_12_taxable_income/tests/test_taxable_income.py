from challenges.challenge_12_taxable_income.taxable_income import (
    calculate_taxable_income,
    STANDARD_DEDUCTION
)


def test_taxable_income_normal():
    assert calculate_taxable_income(500000) == 500000 - STANDARD_DEDUCTION


def test_taxable_income_below_deduction():
    assert calculate_taxable_income(30000) == 0  # cannot be negative


def test_taxable_income_equal_to_deduction():
    assert calculate_taxable_income(STANDARD_DEDUCTION) == 0
