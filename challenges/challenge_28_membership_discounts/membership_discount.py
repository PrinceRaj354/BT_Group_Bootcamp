def apply_membership_discount(grand_total, is_member):
    if is_member.lower() == 'y':
        discount = 0.02 * grand_total
        grand_total -= discount
        return round(grand_total, 2), round(discount, 2)

    return round(grand_total, 2), 0
