from challenges.challenge_12_taxable_income.taxable_income import (
    calculate_taxable_income,
    STANDARD_DEDUCTION
)

if __name__ == "__main__":
    annual_gross = float(input("Enter Annual Gross Salary: "))

    taxable_income = calculate_taxable_income(annual_gross)

    print("\n--- Taxable Income Report ---")
    print("Annual Gross Salary:", annual_gross)
    print("Standard Deduction:", STANDARD_DEDUCTION)
    print("Taxable Income:", taxable_income)
