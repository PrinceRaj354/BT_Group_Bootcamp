def store_elements(n, elements):
    if n < 0:
        raise ValueError("Size of array cannot be negative")
    if len(elements) != n:
        raise ValueError("Number of elements does not match n")
    return list(elements)
