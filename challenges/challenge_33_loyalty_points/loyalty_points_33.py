def calculate_loyalty_points(grand_total):
    if grand_total <= 0:
        return 0
    return int(grand_total // 100)
