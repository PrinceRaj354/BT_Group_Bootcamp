def generate_number_increasing_pattern(n):
    if n <= 0:
        return []
    return [str(i) * i for i in range(1, n + 1)]
