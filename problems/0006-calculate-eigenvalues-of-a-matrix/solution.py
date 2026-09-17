def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	a1,a2 = matrix[0]
	a3,a4 = matrix[1]

	b = a1 + a4
	c = a1*a4 - a2*a3
	a = 1

	b_squr = b **2
	_4_ac = 4*a*c 
	
	eigenvalue_2 = (b - (b_squr - _4_ac)**(0.5))/2 
	eigenvalue_1 = (b + (b_squr - _4_ac)**(0.5))/2

	eigenvalues = [eigenvalue_1,eigenvalue_2]
	return eigenvalues