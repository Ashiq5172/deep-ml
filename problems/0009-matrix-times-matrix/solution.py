def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    rows_a = len(a)
    col_a = len(a[0])

    rows_b = len(b)
    col_b = len(b[0])
    result = []

    if col_a != rows_b:
        return -1

    
    else :
        for i in range (rows_a):
            row = []
            for k in range(col_b):
                sum = 0
                for j in range(col_a):
                    sum += a[i][j]*b[j][k]
                row.append(sum)
            result.append(row)
            
    return result