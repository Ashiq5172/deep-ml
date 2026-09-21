def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	len_of_matrix = len(matrix)

	determinant = 0
	
	if len_of_matrix == 1:
		determinant = matrix[0][0]
		trace = matrix[0][0]
		return (determinant,trace)

	elif len_of_matrix == 2:
		determinant = matrix[0][0]*matrix[1][1] -matrix[1][0]*matrix[0][1]
		trace = matrix[0][0] + matrix[1][1]

	else :
		for j in range(len_of_matrix):
			sub_matrix = []
			for i in range(1,len_of_matrix):
				row = []

				for k in range(len_of_matrix):
					if j!= k:
						row.append(matrix[i][k])
				sub_matrix.append(row)
			sub_matrix_determinant_trace = matrix_determinant_and_trace(sub_matrix)

			determinant += ((-1)**j)*matrix[0][j]*sub_matrix_determinant_trace[0]
	
	trace = 0
	for i in range(len(matrix)):
		trace += matrix[i][i]

	return (determinant , trace)	
	
