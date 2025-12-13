def calculate_item_total(quantity, price):
    return quantity * price


def calculate_grand_total(items):
    grand_total = 0
    for item in items:
        grand_total += calculate_item_total(item["quantity"], item["price"])
    return grand_total
