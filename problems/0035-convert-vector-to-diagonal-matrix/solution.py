import numpy as np

def make_diagonal(x):
	len_of_x = len(x)

	diagonal_marix = []
	for i in range(len_of_x):
		row = []
		for j in range(len_of_x):
			if i == j:
				row.append(float(x[i]))
			else:
				row.append(0.0)
		diagonal_marix.append(row)
	
	return diagonal_marix

