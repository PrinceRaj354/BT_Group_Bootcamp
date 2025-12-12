from challenges.challenge_15_report_generation.report_generator import generate_report

def test_report_formatting():
    data = {
        "Name": "John Doe",
        "EmpID": "E12345",
        "Gross Monthly Salary": "85000",
        "Annual Gross Salary": "1020000",
        "Taxable Income": "970000",
        "Tax Payable": "76800",
        "Annual Net Salary": "943200"
    }

    report = generate_report(data)

    assert "Employee Tax Report" in report
    assert "John Doe" in report
    assert "E12345" in report
    assert "Gross Monthly Salary" in report
    assert "943200" in report  # net salary appears
