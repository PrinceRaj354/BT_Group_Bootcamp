from challenges.challenge_14_net_salary.net_salary import (
    calculate_net_salary,
    generate_net_salary_report
)


def test_net_salary_basic():
    assert calculate_net_salary(600000, 50000) == 550000


def test_net_salary_zero_tax():
    assert calculate_net_salary(700000, 0) == 700000


def test_report_generation():
    report = generate_net_salary_report(500000, 30000)
    assert report["annual_gross_salary"] == 500000
    assert report["total_tax_payable"] == 30000
    assert report["annual_net_salary"] == 470000
