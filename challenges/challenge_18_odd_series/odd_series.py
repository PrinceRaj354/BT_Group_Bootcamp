def generate_odd_series(n: int):
    if n <= 0:
        raise ValueError("N must be a positive integer")
    return [i for i in range(1, n + 1, 2)]
