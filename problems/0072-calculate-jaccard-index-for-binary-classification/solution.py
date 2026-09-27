
import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
	tp = 0
	fn = 0
	fp = 0 
	tn = 0


	for i in range(len(y_pred)):
		if y_true[i] ==1 and 1== y_pred[i]:
			tp += 1
		elif y_true[i] ==1 and 0== y_pred[i]:
			fn += 1
		elif  y_true[i] ==0 and 1== y_pred[i]:

			fp +=1
		else:
			tn += 1

	result = tp /(fn + fp +tp)

	return round(result, 3)
