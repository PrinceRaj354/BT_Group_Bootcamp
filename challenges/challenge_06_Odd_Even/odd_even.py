def is_even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"


if __name__ == "__main__":
    n = int(input().strip())
    print(is_even_or_odd(n))
