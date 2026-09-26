import numpy as np
def precision(y_true, y_pred):
	# Your code here
	tp = 0
	fn = 0
	fp = 0 
	tn = 0

	for i in range(len(y_true)):

		if y_true[i] == 1 and y_pred[i] == 1  :
			tp += 1
		
		elif y_true[i] == 1 and y_pred[i] == 0 :
			fn += 1
		
		elif y_true[i] == 0 and y_pred[i] == 1  :
			fp += 1
		
		else :
			tn += 1

	if tp+fp > 0:
		return tp /(tp + fp)
	else :
		return 0