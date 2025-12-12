def generate_custom_series(n: int):
    if n <= 0:
        raise ValueError("N must be a positive integer")

    series = [1]
    first_diff = [3, 3, 5, 11]  # known starting differences

    # Generate differences based on 2nd difference pattern:
    # second diffs: 0,2,6 → next +12 → then +20 → etc.
    second_diff_next = 12  # after 0,2,6

    # Apply known differences first
    for diff in first_diff:
        next_val = series[-1] + diff
        if next_val > n:
            return series
        series.append(next_val)

    # Continue generating dynamically
    last_first_diff = first_diff[-1]

    while True:
        # next first difference increases by second_diff_next
        new_diff = last_first_diff + second_diff_next
        next_val = series[-1] + new_diff

        if next_val > n:
            break

        series.append(next_val)

        last_first_diff = new_diff
        second_diff_next += 8  # second differences grow by +2, +4, +6, +8, ...

    return series
