import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	rows = len(dense_matrix)
	columns = len(dense_matrix[0])

	val_arr = []
	col_index = []
	row_pointer = [0]

	count = 0 

	for i in range(rows):
		
		for j in range(columns):

			if dense_matrix[i][j] != 0:
				val_arr.append(dense_matrix[i][j])
				col_index.append(j)
				count += 1
		
		row_pointer.append(count)

	x = (val_arr,col_index,row_pointer)
	return x
