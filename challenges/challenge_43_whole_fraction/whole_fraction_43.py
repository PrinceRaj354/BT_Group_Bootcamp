import math


def separate_whole_and_fraction(value):
    whole = math.trunc(value)
    fraction = round(value - whole, 10)
    return whole, fraction
