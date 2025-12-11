def sum_and_average(a, b):
    s = a + b
    avg = s / 2
    return s, avg

if __name__ == "__main__":
    a = float(input().strip())
    b = float(input().strip())
    s, avg = sum_and_average(a, b)
    print(s)
    print(avg)
