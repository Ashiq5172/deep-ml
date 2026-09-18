import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = [0.0]*len(b)
	for _ in range(n):
		new_x = [0.0]*len(b)
		
		for i in range(len(A)):
			total = 0.0

			for j in range(len(A)):
				if i != j :
					total += A[i][j]*x[j]
			
			new_x[i] = (b[i] - total)/A[i][i]
		x = new_x


	return [round(value, 4) for value in x]