from challenges.challenge_32_minimum_purchase.minimum_purchase_32 import validate_minimum_purchase


def test_below_minimum_amount():
    status, message = validate_minimum_purchase(450)
    assert status is False
    assert message == "Minimum purchase amount of ₹500 is not met."


def test_exact_minimum_amount():
    status, message = validate_minimum_purchase(500)
    assert status is True
    assert message == "Invoice can be generated."


def test_above_minimum_amount():
    status, message = validate_minimum_purchase(1200)
    assert status is True
    assert message == "Invoice can be generated."


def test_zero_amount():
    status, message = validate_minimum_purchase(0)
    assert status is False


def test_negative_amount():
    status, message = validate_minimum_purchase(-100)
    assert status is False
