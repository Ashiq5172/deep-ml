import numpy as np

def recall(y_true, y_pred):

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

	if tp+fn > 0:
		return tp /(tp + fn)
	else :
		return 0
