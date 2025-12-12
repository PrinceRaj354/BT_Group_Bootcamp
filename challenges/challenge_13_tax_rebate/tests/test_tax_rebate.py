from challenges.challenge_13_tax_rebate.tax_rebate import (
    calculate_tax_slabs,
    apply_rebate,
    apply_cess,
    calculate_total_tax
)


def test_tax_slabs_basic():
    # Income 4L → only 1L in 5% slab
    assert calculate_tax_slabs(400000) == 100000 * 0.05


def test_tax_slabs_higher():
    # Checking part of 10% slab
    expected = (300000 * 0) + (300000 * 0.05) + (100000 * 0.10)
    assert calculate_tax_slabs(700000) == expected


def test_rebate_applicable():
    assert apply_rebate(600000, 25000) == 0


def test_rebate_not_applicable():
    assert apply_rebate(800000, 30000) == 30000


def test_cess():
    assert apply_cess(10000) == 400  # 4% of 10k


def test_total_tax():
    result = calculate_total_tax(800000)
    assert result["tax_after_rebate"] > 0
    assert result["cess"] == result["tax_after_rebate"] * 0.04
    assert result["total_tax_payable"] == result["tax_after_rebate"] + result["cess"]
