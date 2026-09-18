def compressed_col_sparse_matrix(dense_matrix):
    rows = len(dense_matrix)
    columns = len(dense_matrix[0])

    values = []
    row_indices = []
    column_pointer = [0]

    count = 0

    for j in range(columns):
        for i in range(rows):

            if dense_matrix[i][j] != 0:
                values.append(dense_matrix[i][j])
                row_indices.append(i)
                count += 1

        column_pointer.append(count)

    return values, row_indices, column_pointer