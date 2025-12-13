def generate_star_pattern(n):
    if n <= 0:
        return []
    return ["*****" for _ in range(n)]
