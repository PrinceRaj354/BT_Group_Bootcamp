def generate_fibonacci_pattern(n):
    if n <= 0:
        return []

    result = []
    fib = [1, 1]

    for row in range(1, n + 1):
        while len(fib) < sum(range(1, row + 1)):
            fib.append(fib[-1] + fib[-2])

        start = sum(range(1, row))
        end = start + row
        result.append(" ".join(str(x) for x in fib[start:end]))

    return result
