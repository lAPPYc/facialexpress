def preprocessing():
	global expressions
	import numpy as np
	import sys
	sys.path.append('training_dataset')
	import neutral
	import smile
	import fear
	import disgust
	import anger
	import surprise
	import curious
	
	expressions =  {'neutral':neutral.neutral,'smile':smile.smile,'fear':fear.fear,'disgust':disgust.disgust,'anger':anger.anger,'surprise':surprise.surprise,'curious':curious.curious}

	
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







