def preprocessing():
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

	expressions =  {'neutral':neutral.NE,'smile':happy.HA,'fear':afraid.FE,'disgust':disgust.DI,'anger':anger.AN,'surprise':surprise.SU,'sad':sad.SA}

	
	features = []
	labels = []
	
	for i in expressions:
		for j in range(len(expressions[i])):
			features.append(expressions[i][j])
			labels.append(i)
	
	features = np.array(features)
	labels = np.array(labels)
	
	nsamples, nx, ny = features.shape
	features = features.reshape((nsamples,nx*ny))
	
	return features, labels

features, labels = preprocessing()

def train(features_train, labels_train):

	from sklearn.naive_bayes import GaussianNB
	
	clf = GaussianNB()
	clf.fit(features_train, labels_train)
	
	return clf

classifier = train(features, labels)

from sklearn.externals import joblib
joblib.dump(classifier,'classifier.pkl')







