def generate_number_pattern(n):
    if n <= 0:
        return []
    return [str(i) * 5 for i in range(1, n + 1)]
