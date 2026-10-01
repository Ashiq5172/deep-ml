import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	batches = []
	i = 0

	while i < len(X):
		x_batch = X[i:i+batch_size]

		if y is not None:
			y_batch = y[i:i+batch_size]
			batches.append([x_batch,y_batch])
		else:
			batches.append(x_batch)
		
		i = i + batch_size
	
	return batches

		