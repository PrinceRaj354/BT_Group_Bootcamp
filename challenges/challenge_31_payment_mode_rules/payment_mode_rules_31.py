def calculate_final_amount(grand_total, payment_method):
    surcharge = 0.0

    if payment_method.lower() == "credit card":
        surcharge = grand_total * 0.02

    final_amount = grand_total + surcharge
    return payment_method, round(surcharge, 2), round(final_amount, 2)
