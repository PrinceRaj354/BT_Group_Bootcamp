def calculate_net_salary(annual_gross_salary, total_tax_payable):
    """
    Net Salary = Annual Gross Salary - Total Tax Payable
    """
    return annual_gross_salary - total_tax_payable


def generate_net_salary_report(annual_gross_salary, total_tax_payable):
    net_salary = calculate_net_salary(annual_gross_salary, total_tax_payable)

    return {
        "annual_gross_salary": annual_gross_salary,
        "total_tax_payable": total_tax_payable,
        "annual_net_salary": net_salary
    }
