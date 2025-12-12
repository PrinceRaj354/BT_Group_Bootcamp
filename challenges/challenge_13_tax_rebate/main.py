from challenges.challenge_13_tax_rebate.tax_rebate import calculate_total_tax

if __name__ == "__main__":
    taxable_income = float(input("Enter Taxable Income: "))

    result = calculate_total_tax(taxable_income)

    print("\n--- Tax Breakdown Report ---")
    print("Slab-wise Tax:", result["slab_tax"])
    print("Tax After Rebate:", result["tax_after_rebate"])
    print("4% Cess:", result["cess"])
    print("Total Tax Payable:", result["total_tax_payable"])
