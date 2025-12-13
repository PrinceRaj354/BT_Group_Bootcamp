def calculate_item_total(item_code, description, quantity, price):
    if not item_code or not description:
        raise ValueError("Item code and description cannot be empty")

    if quantity <= 0 or price <= 0:
        raise ValueError("Quantity and price must be positive")

    total = quantity * price

    return {
        "item_code": item_code,
        "description": description,
        "quantity": quantity,
        "price": price,
        "total": total
    }
