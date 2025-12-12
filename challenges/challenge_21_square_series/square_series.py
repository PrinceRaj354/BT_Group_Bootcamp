def generate_square_series(n: int):
    if n <= 0:
        raise ValueError("N must be a positive integer")
    
    result = []
    i = 1

    while i * i <= n:
        result.append(i * i)
        i += 1

    return result
