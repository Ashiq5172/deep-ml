import numpy as np

def row_normalize(counts: list[list[float]]) -> list[list[float]]:
    """Convert a count matrix into a row-stochastic probability matrix."""
    rows = len(counts)
    columns = len(counts[0])


    row_sum = []
    for i in range(rows):
        sum = 0
        for j in counts[i]:
            sum += j
        row_sum.append(sum)
    
    for i in range(rows):
        if row_sum[i] == 0:
            for j in range(columns):
                counts[i][j] = 0.0
        else:
            for j in range(columns):
                counts[i][j] /= row_sum[i]
    return  counts 
    
