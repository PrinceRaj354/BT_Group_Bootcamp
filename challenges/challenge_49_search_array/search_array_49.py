def search_element(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
