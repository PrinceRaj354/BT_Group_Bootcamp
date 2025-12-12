from challenges.challenge_11_basic_salary.salary import (
    calculate_gross_monthly,
    calculate_annual_gross,
)

if __name__ == "__main__":
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")
    basic = float(input("Enter Basic Monthly Salary: "))
    allowances = float(input("Enter Special Allowances (Monthly): "))
    bonus_percent = float(input("Enter Annual Bonus Percentage: "))

    gross_monthly = calculate_gross_monthly(basic, allowances)
    annual_gross = calculate_annual_gross(gross_monthly, bonus_percent)

    print("\n--- Employee Salary Report ---")
    print("Name:", name)
    print("Employee ID:", emp_id)
    print("Gross Monthly Salary:", gross_monthly)
    print("Annual Gross Salary:", annual_gross)
