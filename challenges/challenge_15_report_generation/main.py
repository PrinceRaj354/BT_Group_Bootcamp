from challenges.challenge_15_report_generation.report_generator import generate_report

if __name__ == "__main__":
    # Simulated pre-calculated values (from previous challenges)
    employee_data = {
        "Name": input("Enter Name: "),
        "EmpID": input("Enter Employee ID: "),
        "Gross Monthly Salary": input("Enter Gross Monthly Salary: "),
        "Annual Gross Salary": input("Enter Annual Gross Salary: "),
        "Taxable Income": input("Enter Taxable Income: "),
        "Tax Payable": input("Enter Total Tax Payable: "),
        "Annual Net Salary": input("Enter Annual Net Salary: ")
    }

    print("\n" + generate_report(employee_data))
