from challenges.challenge_11_basic_salary.salary import (
    calculate_gross_monthly,
    calculate_annual_gross,
)


def test_gross_monthly():
    assert calculate_gross_monthly(30000, 5000) == 35000


def test_annual_gross_with_bonus():
    gross_monthly = 40000
    annual = calculate_annual_gross(gross_monthly, 10)
    expected = (40000 * 12) + (0.10 * (40000 * 12))
    assert annual == expected


def test_annual_gross_no_bonus():
    gross_monthly = 50000
    annual = calculate_annual_gross(gross_monthly, 0)
    assert annual == 50000 * 12
