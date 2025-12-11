def calculate_sales():
    acres_per_crop = 80 / 5

    tomato_acres = acres_per_crop
    tomato_yield_30 = 0.30 * tomato_acres * 10 * 1000
    tomato_yield_70 = 0.70 * tomato_acres * 12 * 1000
    tomato_sales = (tomato_yield_30 + tomato_yield_70) * 7


    potato_sales = (acres_per_crop * 10 * 1000) * 20

    cabbage_sales = (acres_per_crop * 14 * 1000) * 24

    sunflower_sales = (acres_per_crop * 700) * 200

    sugarcane_sales = (acres_per_crop * 45 * 4000)

    total_sales = (tomato_sales + potato_sales + cabbage_sales +
                   sunflower_sales + sugarcane_sales)

    chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales

    return total_sales, chemical_free_sales


if __name__ == "__main__":
    total, chemical_free = calculate_sales()
    print(total)
    print(chemical_free)
