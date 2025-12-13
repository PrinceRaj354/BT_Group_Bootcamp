def display_matrix_and_transpose(matrix):
    if not matrix:
        return matrix, []

    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []

    for c in range(cols):
        row = []
        for r in range(rows):
            row.append(matrix[r][c])
        transpose.append(row)

    return matrix, transpose
