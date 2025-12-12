def generate_increment_series(n: int):
    if n <= 0:
        raise ValueError("N must be a positive integer")

    result = [1]
    increment = 1

    while True:
        next_value = result[-1] + increment
        if next_value > n:
            break
        result.append(next_value)
        increment += 1

    return result
