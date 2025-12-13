def store_elements_in_array(n, elements):
    if n < 0:
        raise ValueError("Array size cannot be negative")
    if len(elements) != n:
        raise ValueError("Number of elements must match array size")
    return list(elements)
