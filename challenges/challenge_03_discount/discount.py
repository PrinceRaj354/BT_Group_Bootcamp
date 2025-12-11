def calculate_discount(amount, discount_percent):
    discount = (amount * discount_percent) / 100
    final_amount = amount - discount
    return discount, final_amount

if __name__ == "__main__":
    amount = float(input().strip())
    discount_percent = float(input().strip())
    discount, final_amount = calculate_discount(amount, discount_percent)
    print(discount)
    print(final_amount)
