def generate_factorial_pattern(n):
    if n <= 0:
        return []

    result = []
    current = 1

    for row in range(1, n + 1):
        row_values = []
        temp = 1
        for _ in range(row):
            temp *= current
            row_values.append(str(temp))
            current += 1
        result.append(" ".join(row_values))

    return result
