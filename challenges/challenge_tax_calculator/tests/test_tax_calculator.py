from challenges.challenge_tax_calculator.tax_calculator import (
    calculate_gross_salary,
    calculate_taxable_income,
    calculate_tax_new_regime,
    apply_rebate,
    generate_salary_report
)


def test_gross_salary():
    assert calculate_gross_salary(30000, 10000, 5000) == 45000


def test_taxable_income():
    assert calculate_taxable_income(500000) == 450000
    assert calculate_taxable_income(40000) == 0  # cannot be negative


def test_tax_slabs():
    assert calculate_tax_new_regime(200000) == 0
    assert calculate_tax_new_regime(400000) == 5000  # 3–4L → 5%


def test_rebate():
    assert apply_rebate(25000, 600000) == 0
    assert apply_rebate(25000, 800000) == 25000


def test_full_report():
    report = generate_salary_report("John", 300000, 100000, 100000)
    assert report["gross_salary"] == 500000
    assert report["taxable_income"] == 450000
    assert report["tax_payable"] >= 0
