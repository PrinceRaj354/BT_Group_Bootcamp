from challenges.challenge_03_discount.discount import calculate_discount

def test_basic_discount():
    discount, final = calculate_discount(1000, 10)
    assert discount == 100
    assert final == 900

def test_zero_discount():
    discount, final = calculate_discount(500, 0)
    assert discount == 0
    assert final == 500

def test_full_discount():
    discount, final = calculate_discount(200, 100)
    assert discount == 200
    assert final == 0

def test_decimal_discount():
    discount, final = calculate_discount(999.99, 12.5)
    expected_discount = (999.99 * 12.5) / 100
    expected_final = 999.99 - expected_discount
    assert discount == expected_discount
    assert final == expected_final
