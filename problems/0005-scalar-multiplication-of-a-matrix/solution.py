import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	

	rows = len(matrix)
	columns = len(matrix[0])

	result = []

	for i in range(rows):
		row = []

		for j in range(columns):
			row.append(scalar*matrix[i][j])
		result.append(row)
	
	
	return result
