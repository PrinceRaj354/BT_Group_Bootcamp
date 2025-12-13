def calculate_grand_total(items, promo_code="PROMO10", discount_rate=0.10):
    total = 0.0

    for item in items:
        item_total = item["price"] * item["quantity"]
        if item["code"] == promo_code:
            item_total -= item_total * discount_rate
        total += item_total

    return round(total, 2)
