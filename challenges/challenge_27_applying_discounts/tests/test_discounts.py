from challenges.challenge_27_applying_discounts.discounts import apply_discounts


def test_no_discount():
    total, discount = apply_discounts(5000, 5)
    assert total == 5000
    assert discount == 0


def test_price_discount_only():
    total, discount = apply_discounts(12000, 10)
    assert total == 10800
    assert discount == 1200


def test_quantity_discount_only():
    total, discount = apply_discounts(8000, 25)
    assert total == 7600
    assert discount == 400


def test_both_discounts():
    total, discount = apply_discounts(20000, 30)
    assert total == 17100
    assert discount == 2900
