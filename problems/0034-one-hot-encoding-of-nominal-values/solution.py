import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if n_col is None:
		n_col = np.max(x) + 1
	result = []
	for i in range(len(x)):
		row = []
		for j in range(n_col):
			if x[i] == j:
				row.append(1)
			else :
				row.append(0)
		result.append(row)
	
	return result