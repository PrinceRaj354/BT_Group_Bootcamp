def sort_array(arr, order="asc"):
    if order not in ("asc", "desc"):
        raise ValueError("Order must be 'asc' or 'desc'")
    return sorted(arr, reverse=(order == "desc"))
