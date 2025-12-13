def generate_alternating_series(n):
    if n <= 0:
        return []

    result = []
    value = 1
    sign = 1

    for _ in range(n):
        result.append(sign * value)
        value += 4
        sign *= -1

    return result
