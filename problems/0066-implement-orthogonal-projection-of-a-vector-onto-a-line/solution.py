import numpy as np
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	v = np.array(v)
	L = np.array(L)

	dot_product_of_v_L = np.dot(v,L)
	dot_product_of_L_L = np.dot(L,L)

	return (dot_product_of_v_L/dot_product_of_L_L)*L