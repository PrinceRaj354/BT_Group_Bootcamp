def generate_fibonacci_series(n: int):
    if n <= 0:
        raise ValueError("N must be a positive integer")

    series = [1, 1]

    if n == 1:
        return [1]

    while True:
        next_val = series[-1] + series[-2]
        if next_val > n:
            break
        series.append(next_val)

    return series
