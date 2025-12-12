def calculate_tax_slabs(taxable_income):
    """
    Applies New Tax Regime (2023) slab-wise tax.
    """
    slabs = [
        (300000, 0.00),  # 0–3L
        (300000, 0.05),  # 3–6L
        (300000, 0.10),  # 6–9L
        (300000, 0.15),  # 9–12L
        (300000, 0.20),  # 12–15L
    ]

    remaining = taxable_income
    tax = 0

    # Apply slab calculations sequentially
    for limit, rate in slabs:
        if remaining > limit:
            tax += limit * rate
            remaining -= limit
        else:
            tax += remaining * rate
            remaining = 0
            break

    # Above 15L → 30%
    if remaining > 0:
        tax += remaining * 0.30

    return tax


def apply_rebate(taxable_income, tax_amount):
    """
    Section 87A Rebate:
    If taxable income ≤ 7,00,000 → 100% rebate.
    """
    if taxable_income <= 700000:
        return 0
    return tax_amount


def apply_cess(tax_amount):
    """
    Health & Education Cess: 4% of tax amount.
    """
    return tax_amount * 0.04


def calculate_total_tax(taxable_income):
    """
    Full tax calculation: slabs → rebate → cess
    Returns dict with all details.
    """
    slab_tax = calculate_tax_slabs(taxable_income)
    tax_after_rebate = apply_rebate(taxable_income, slab_tax)
    cess = apply_cess(tax_after_rebate)
    total_tax = tax_after_rebate + cess

    return {
        "slab_tax": slab_tax,
        "tax_after_rebate": tax_after_rebate,
        "cess": cess,
        "total_tax_payable": total_tax
    }
