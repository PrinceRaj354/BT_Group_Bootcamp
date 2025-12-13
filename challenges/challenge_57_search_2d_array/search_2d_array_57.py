def element_exists_2d(matrix, target):
    for row in matrix:
        for value in row:
            if value == target:
                return True
    return False
