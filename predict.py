import os
import numpy as np
from face import face_capture
from processing import normalize
import cv2
from sklearn.externals import joblib
import dlib
import pickle

predictor = 'lib/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor)
detector = cv2.CascadeClassifier("lib/haarcascade_frontalface_default.xml")

img_path = 'training_dataset/pics/jaffe/'
lis = [i for i in os.listdir(img_path) if 'tiff' in i]

#lis = ['KA.AN1.39.tiff','KA.DI1.42.tiff','KA.FE3.47.tiff','KA.HA1.29.tiff','KA.NE1.26.tiff','KA.SA2.34.tiff','KA.SU3.38.tiff']
labels = []
abbvr = {'NE':'neutral','HA':'happy','FE':'fear','DI':'disgust','AN':'anger','SU':'surprise', 'SA':'sad'}

w = 100; h = 120; eye_dist = 20
cam = cv2.VideoCapture(0)
emotion = ''

def trial():
	L = []
	emotions = []
	for i in lis:
		img_name = i
		img = cv2.imread(img_path+i)
		L.append(abbvr[img_name[3:5]])
		face, positions = face_capture(cam=None, img_path=img_path, img_name=i, detector=detector, predictor=predictor)
		try:
			[[x,y,w,h]] = face
		except ValueError:
			[x,y,w,h] = [0]*4

		pos = normalize(face, positions, w, h, eye_dist)
		print i
		print "\n", pos
		print "\n", lis
		exit(0)
		positions = []
		for (x,y) in pos:
			positions.append(x)
			positions.append(y)
		positions = np.array(positions).reshape(1,-1)

		'''labels = []
		
		for j in range(len(positions)):
			clf = joblib.load('classifiers/'+str(j)+'.pkl')
			label = clf.predict([list(positions[j])])
			labels.append(label[0])
		
		emotions.append(max(set(labels),key=labels.count))'''
		
		clf = pickle.load(open('classifiers/clf.sav','rb'))
		label = clf.predict(positions)
		emotions.append(label[0])
		
		'''cv2.putText(img,emotion,(x+w/10,y+h+20),fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color=(0,0,255),thickness = 2)	
		cv2.imshow(img_name,img)
	
		if cv2.waitKey(0) & 0xFF == ord('n'):
			cv2.destroyAllWindows()
		elif cv2.waitKey(0) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			exit(0)'''

	NO = len(L)
	correct = 0
	for i in range(len(L)):
		if L[i] == emotions[i]:
			correct = correct + 1
	accuracy = correct/float(NO)
	print accuracy
	exit(0)

trial()
	

while(1):

	img, face, positions = face_capture(cam=cam, img_path=None, img_name=None, detector=detector, predictor=predictor)
	try:
		[[x,y,w,h]] = face
	except ValueError:
		[x,y,w,h] = [0]*4
	cv2.putText(img,emotion,(x+w/10,y+h+20),fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color=(0,0,255),thickness = 2)	
	cv2.imshow('output',img)
	
	if cv2.waitKey(1) & len(face) != 1:
		continue
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	positions = normalize(face, positions, w, h, eye_dist)
	positions = np.array(positions)
	positions = positions.reshape(1,68*2)
	label = clf.predict(positions)

	print label
	emotion=label[0]
