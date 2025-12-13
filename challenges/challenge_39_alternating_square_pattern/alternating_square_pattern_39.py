def generate_alternating_square_pattern(n):
    if n <= 0:
        return []

    result = []
    current = 1
    sign = 1

    for row in range(1, n + 1):
        row_values = []
        for _ in range(row):
            value = (current ** 2) * sign
            row_values.append(str(value))
            current += 1
            sign *= -1
        result.append(" ".join(row_values))

    return result
