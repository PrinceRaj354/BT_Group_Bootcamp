from challenges.challenge_28_membership_discounts.membership_discount import apply_membership_discount


def test_member_discount_applied():
    total, discount = apply_membership_discount(10000, 'y')
    assert total == 9800
    assert discount == 200


def test_member_discount_uppercase():
    total, discount = apply_membership_discount(5000, 'Y')
    assert total == 4900
    assert discount == 100


def test_non_member_no_discount():
    total, discount = apply_membership_discount(8000, 'n')
    assert total == 8000
    assert discount == 0
