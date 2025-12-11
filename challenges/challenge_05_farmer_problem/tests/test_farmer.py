from challenges.challenge_05_farmer_problem.farmer import calculate_sales

def test_sales_calculation():
    total, chemical_free = calculate_sales()

    # Expected values computed manually
    assert round(total) == 31696000
    assert round(chemical_free) == 19936000
