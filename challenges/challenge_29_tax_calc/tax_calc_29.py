def calculate_tax_and_total(grand_total):
    if grand_total < 5000:
        tax_rate = 0.05
    elif grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    tax_amount = grand_total * tax_rate
    final_total = grand_total + tax_amount

    return round(tax_amount, 2), round(final_total, 2)
