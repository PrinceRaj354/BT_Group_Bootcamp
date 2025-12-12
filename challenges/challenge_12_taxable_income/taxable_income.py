STANDARD_DEDUCTION = 50000

def calculate_taxable_income(annual_gross_salary):
    """
    Calculates taxable income after applying standard deduction.
    """
    taxable = annual_gross_salary - STANDARD_DEDUCTION
    return max(taxable, 0)  # Taxable income cannot be negative
