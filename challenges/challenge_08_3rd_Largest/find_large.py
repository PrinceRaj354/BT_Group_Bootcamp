def third_largest(numbers):

    unique_nums = list(set(numbers))

    if len(unique_nums) < 3:
        raise ValueError("Need at least 3 unique numbers")

    unique_nums.sort(reverse=True)
    return unique_nums[2]   # 3rd largest
