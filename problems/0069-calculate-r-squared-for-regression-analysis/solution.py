
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	y_true = np.ravel(y_true)
	y_pred = np.ravel(y_pred)

	total = 0
	sum_ = 0
	for i in range(len(y_pred)):
		total += (y_pred[i]-y_true[i])**2
		sum_ += y_pred[i]
	avg = sum_ /len(y_true)
	sum_ = 0
	for i in range(len(y_pred)):
		sum_ += (y_true[i]-avg)**2

	
		
	r_squared_ = 1 - (total/sum_)


	return  r_squared_