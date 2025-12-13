def generate_star_increasing_pattern(n):
    if n <= 0:
        return []
    return ["*" * i for i in range(1, n + 1)]
