from challenges.challenge_26_grand_total.item_entry import calculate_item_total, calculate_grand_total


def test_single_item_total():
    assert calculate_item_total(2, 50) == 100


def test_grand_total_multiple_items():
    items = [
        {"quantity": 2, "price": 50},
        {"quantity": 1, "price": 100},
        {"quantity": 3, "price": 20}
    ]
    assert calculate_grand_total(items) == 260


def test_empty_items():
    assert calculate_grand_total([]) == 0
