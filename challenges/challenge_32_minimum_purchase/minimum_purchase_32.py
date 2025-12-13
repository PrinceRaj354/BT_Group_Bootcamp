def validate_minimum_purchase(final_grand_total, minimum_amount=500):
    if final_grand_total < minimum_amount:
        return False, "Minimum purchase amount of ₹500 is not met."
    return True, "Invoice can be generated."
