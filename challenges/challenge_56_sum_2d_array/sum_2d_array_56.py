def sum_2d_array(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total
