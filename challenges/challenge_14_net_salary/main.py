from challenges.challenge_14_net_salary.net_salary import (
    generate_net_salary_report
)

if __name__ == "__main__":
    annual_gross = float(input("Enter Annual Gross Salary: "))
    total_tax = float(input("Enter Total Tax Payable (including cess): "))

    report = generate_net_salary_report(annual_gross, total_tax)

    print("\n--- Net Salary Report ---")
    print("Annual Gross Salary:", report["annual_gross_salary"])
    print("Total Tax Payable:", report["total_tax_payable"])
    print("Annual Net Salary:", report["annual_net_salary"])
