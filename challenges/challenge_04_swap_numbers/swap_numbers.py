def swap_numbers(a, b):
    a, b = b, a
    return a, b

if __name__ == "__main__":
    a = float(input().strip())
    b = float(input().strip())
    x, y = swap_numbers(a, b)
    print(x)
    print(y)
