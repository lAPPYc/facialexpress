expressions =  ['neutral','smile','fear','disgust','anger','surprise','curious']

def preprocessing():
	global expressions
	
	features = []
	labels = []
	
	for i in expressions:
		f = open('training_dataset/'+i+'.txt','r')
		data  = f.read()
		data = data.split(';')
		data.pop()
		for j in range(len(data)):
			features.append(data[j])
			labels.append(i)
	
	return features, labels

features, labels = preprocessing()

print 'train is working'

def train(features_train, labels_train):

	from sklearn.naive_bayes import GaussianNB
	
	clf = GaussianNB()
	clf.fit(features_train, labels_train)
	
	return clf

classifier = train(features, labels)
