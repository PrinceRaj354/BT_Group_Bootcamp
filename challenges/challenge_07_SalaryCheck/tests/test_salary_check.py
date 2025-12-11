from challenges.challenge_07_SalaryCheck.salary_check import must_pay_tax

def test_tax_applicable():
    assert must_pay_tax("Rahul", 400000) == "Rahul must pay tax"

def test_tax_not_applicable():
    assert must_pay_tax("Priya", 250000) == "Priya does not need to pay tax"

def test_boundary_condition():
    # Salary = 300000 → no tax
    assert must_pay_tax("Amit", 300000) == "Amit does not need to pay tax"
