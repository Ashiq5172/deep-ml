import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    a = np.array(a)
    rows = len(a)
    cloumns = len(a[0])

    result = []
    for j in range(cloumns):
        row = []
        for i in range(rows):
            row.append(a[i][j])
        result.append(row)

    return result


    