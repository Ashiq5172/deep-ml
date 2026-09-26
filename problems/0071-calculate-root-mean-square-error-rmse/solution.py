
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	y_true = np.ravel(y_true)
	y_pred = np.ravel(y_pred)

	total = 0
	for i in range(len(y_true)):
		total += (y_true[i] - y_pred[i])**2

	rmse_res = (total/len(y_true)) ** 0.5
	return round(rmse_res.item(),3)
