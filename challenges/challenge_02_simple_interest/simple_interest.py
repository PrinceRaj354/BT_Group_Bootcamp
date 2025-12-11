def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100

if __name__ == "__main__":
    p = float(input().strip())
    r = float(input().strip())
    t = float(input().strip())
    print(calculate_simple_interest(p, r, t))
