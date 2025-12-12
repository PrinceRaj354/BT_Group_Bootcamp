def generate_square_series(n: int):
    if n <= 0:
        raise ValueError("N must be a positive number")

    result = []
    i = 2  # start with first even number

    while i * i <= n:
        result.append(i * i)
        i += 2  # next even number

    return result
