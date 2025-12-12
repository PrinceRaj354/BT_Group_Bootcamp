def calculate_gross_monthly(basic_salary, special_allowances):
    return basic_salary + special_allowances


def calculate_annual_gross(gross_monthly, bonus_percentage):
    bonus_amount = (bonus_percentage / 100) * (gross_monthly * 12)
    return (gross_monthly * 12) + bonus_amount
