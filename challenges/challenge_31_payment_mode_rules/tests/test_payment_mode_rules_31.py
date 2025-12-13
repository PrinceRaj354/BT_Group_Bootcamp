from challenges.challenge_31_payment_mode_rules.payment_mode_rules_31 import calculate_final_amount


def test_cash_payment_no_surcharge():
    method, surcharge, total = calculate_final_amount(1000, "Cash")
    assert method == "Cash"
    assert surcharge == 0.00
    assert total == 1000.00


def test_credit_card_surcharge_applied():
    method, surcharge, total = calculate_final_amount(1000, "Credit Card")
    assert method == "Credit Card"
    assert surcharge == 20.00
    assert total == 1020.00


def test_lowercase_credit_card():
    method, surcharge, total = calculate_final_amount(500, "credit card")
    assert surcharge == 10.00
    assert total == 510.00


def test_zero_amount_credit_card():
    method, surcharge, total = calculate_final_amount(0, "Credit Card")
    assert surcharge == 0.00
    assert total == 0.00


def test_unknown_payment_method_defaults_no_surcharge():
    method, surcharge, total = calculate_final_amount(800, "UPI")
    assert surcharge == 0.00
    assert total == 800.00
