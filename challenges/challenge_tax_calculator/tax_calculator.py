def calculate_gross_salary(basic, hra, allowances):
    return basic + hra + allowances


def calculate_taxable_income(gross_salary, standard_deduction=50000):
    taxable = gross_salary - standard_deduction
    return max(taxable, 0)


def calculate_tax_new_regime(taxable_income):
    """
    New Tax Regime 2023 slabs:
    0–3L       → 0%
    3–6L       → 5%
    6–9L       → 10%
    9–12L      → 15%
    12–15L     → 20%
    15L+       → 30%
    """

    slabs = [
        (300000, 0.00),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
    ]
    
    remaining = taxable_income
    tax = 0

    # Apply slab rates
    for limit, rate in slabs:
        if remaining > limit:
            tax += limit * rate
            remaining -= limit
        else:
            tax += remaining * rate
            remaining = 0
            break

    # Income above 15L → 30%
    if remaining > 0:
        tax += remaining * 0.30

    return tax


def apply_rebate(tax_payable, taxable_income):
    """Rebate u/s 87A: If taxable income <= 7 lakh → rebate up to 25,000"""
    if taxable_income <= 700000:
        return 0
    return tax_payable


def generate_salary_report(name, basic, hra, allowances):
    gross = calculate_gross_salary(basic, hra, allowances)
    taxable = calculate_taxable_income(gross)
    tax_before_rebate = calculate_tax_new_regime(taxable)
    tax_after_rebate = apply_rebate(tax_before_rebate, taxable)
    net_salary = gross - tax_after_rebate

    return {
        "name": name,
        "gross_salary": gross,
        "taxable_income": taxable,
        "tax_payable": tax_after_rebate,
        "net_salary": net_salary
    }


if __name__ == "__main__":
    name = input("Enter employee name: ")
    basic = float(input("Enter Basic Salary: "))
    hra = float(input("Enter HRA: "))
    allowances = float(input("Enter Other Allowances: "))

    report = generate_salary_report(name, basic, hra, allowances)

    print("\n--- Salary Report ---")
    print("Employee:", report["name"])
    print("Gross Salary:", report["gross_salary"])
    print("Taxable Income:", report["taxable_income"])
    print("Tax Payable:", report["tax_payable"])
    print("Net Salary:", report["net_salary"])
