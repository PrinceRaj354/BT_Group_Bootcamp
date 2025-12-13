def apply_discounts(grand_total, total_quantity):
    discount = 0

    if grand_total > 10000:
        discount += 0.10 * grand_total
        grand_total -= discount

    if total_quantity > 20:
        qty_discount = 0.05 * grand_total
        discount += qty_discount
        grand_total -= qty_discount

    return round(grand_total, 2), round(discount, 2)
