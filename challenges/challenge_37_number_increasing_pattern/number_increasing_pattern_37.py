def generate_number_increasing_pattern(n):
    if n <= 0:
        return []
    return ["".join(str(i) for i in range(1, row + 1)) for row in range(1, n + 1)]
