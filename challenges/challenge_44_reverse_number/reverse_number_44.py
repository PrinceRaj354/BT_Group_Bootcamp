def reverse_number(number):
    sign = -1 if number < 0 else 1
    num = abs(number)
    reverse = 0

    while num > 0:
        reverse = reverse * 10 + (num % 10)
        num //= 10

    return sign * reverse
