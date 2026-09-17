def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	rows = len(matrix)
	columns = len(matrix[0])
	result = []

	if mode == 'row':
		for i in range(rows):
			sum = 0
			for j in matrix[i]:
				sum += j
			result.append(sum/columns)

	else :
		for j in range(columns):
			sum = 0
			for i in range(rows):
				sum += matrix[i][j]
			result.append(sum/rows)


	return result