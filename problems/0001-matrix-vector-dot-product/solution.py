import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	columns = len(a[0])
	length = len(b)

	
	if columns == length :
		result = np.dot(a,b)
		return  result
	else:
		return -1
		
