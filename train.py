global expressions
import numpy as np
import sys
sys.path.append('training_dataset')
import neutral
import happy
import afraid
import disgust
import anger
import surprise
import sad
from sklearn import svm

expressions =  {'neutral':neutral.NE,'happy':happy.HA,'fear':afraid.FE,'disgust':disgust.DI,'anger':anger.AN,'surprise':surprise.SU,'sad':sad.SA}
	
for i in range(68):
	features = []
	labels = []

	for j in expressions:

		for k in expressions[j]:
			features.append(list(k[i]))
			labels.append(j)

	clf = svm.SVC(kernel = 'rbf')
	clf.fit(features, labels)

	from sklearn.externals import joblib
	joblib.dump(clf,'classifiers/'+str(i)+'.pkl')
