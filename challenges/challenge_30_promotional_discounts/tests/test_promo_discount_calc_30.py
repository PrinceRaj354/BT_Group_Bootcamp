from challenges.challenge_30_promotional_discounts.promo_discount_calc_30 import calculate_grand_total


def test_no_promo_items():
    items = [
        {"code": "ITEM1", "price": 100, "quantity": 2},
        {"code": "ITEM2", "price": 50, "quantity": 1},
    ]
    assert calculate_grand_total(items) == 250.00


def test_single_promo_item():
    items = [
        {"code": "PROMO10", "price": 200, "quantity": 1},
    ]
    assert calculate_grand_total(items) == 180.00


def test_mixed_items():
    items = [
        {"code": "PROMO10", "price": 100, "quantity": 2},
        {"code": "ITEM3", "price": 50, "quantity": 2},
    ]
    assert calculate_grand_total(items) == 280.00


def test_zero_quantity():
    items = [
        {"code": "PROMO10", "price": 100, "quantity": 0},
    ]
    assert calculate_grand_total(items) == 0.00


def test_empty_items():
    assert calculate_grand_total([]) == 0.00
