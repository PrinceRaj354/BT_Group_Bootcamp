def generate_series(n: int):
    if n <= 0:
        raise ValueError("N must be a positive integer")
    return list(range(1, n + 1))
