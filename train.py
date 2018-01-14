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
import random
from sklearn.linear_model import LogisticRegression
import pickle

expressions =  {'neutral':neutral.NE,'happy':happy.HA,'fear':afraid.FE,'disgust':disgust.DI,'anger':anger.AN,'surprise':surprise.SU,'sad':sad.SA}

features = np.empty((0,68*2))
labels = []
for i in expressions:
	for j in expressions[i]:
		labels.append(i)
		pos = []
		for (x,y) in j:
			pos.append(x)
			pos.append(y)
		features = np.vstack((features,np.array(pos,dtype='float')))

#features has 213 samples

temp = list(zip(features,labels))
random.shuffle(temp)
features,labels = zip(*temp)

model = LogisticRegression()
model.fit(features,labels)

filename = 'classifiers/clf.sav'
pickle.dump(model,open(filename,'wb'))
