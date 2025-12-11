from challenges.challenge_05_farmer_problem.farmer import calculate_sales

def test_sales_calculation():
    total, chemical_free = calculate_sales()

    assert round(total) == 14972800
    assert round(chemical_free) == 12092800
