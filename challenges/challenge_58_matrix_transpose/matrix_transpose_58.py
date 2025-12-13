def matrix_and_transpose(matrix):
    transpose = []

    if not matrix:
        return matrix, transpose

    rows = len(matrix)
    cols = len(matrix[0])

    for c in range(cols):
        transposed_row = []
        for r in range(rows):
            transposed_row.append(matrix[r][c])
        transpose.append(transposed_row)

    return matrix, transpose
