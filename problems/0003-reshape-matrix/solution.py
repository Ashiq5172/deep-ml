import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	rows ,columns = new_shape

	flat = []
	for row in a:
		for i in row:
			flat.append(i)
	index = 0
	reshaped_matrix = []
	if len(flat) != rows*columns :
		return []
	
	else :
		for i in range(rows):
			row = []
			for j in range(columns):
				row.append(flat[index])
				index += 1
			reshaped_matrix.append(row)

	return reshaped_matrix