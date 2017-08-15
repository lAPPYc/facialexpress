import os
import numpy as np
from face import face_capture
from processing import normalize
import cv2
from sklearn.externals import joblib
import dlib

predictor = 'lib/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor)
detector = cv2.CascadeClassifier("lib/haarcascade_frontalface_default.xml")

img_path = 'training_dataset/pics/jaffe/'
lis = [i for i in os.listdir(img_path) if 'tiff' in i]
#lis = ['KA.AN1.39.tiff','KA.DI1.42.tiff','KA.FE3.47.tiff','KA.HA1.29.tiff','KA.NE1.26.tiff','KA.SA2.34.tiff','KA.SU3.38.tiff']
labels = []

w = 100; h = 120; eye_dist = 20
cam = cv2.VideoCapture(0)
emotion = ''

def trial():
	for i in lis:
		img_name = i
		img = cv2.imread(img_path+i)
		face, positions = face_capture(cam=None, img_path=img_path, img_name=i, detector=detector, predictor=predictor)
		try:
			[[x,y,w,h]] = face
		except ValueError:
			[x,y,w,h] = [0]*4

		positions = normalize(face, positions, w, h, eye_dist)
		labels = []
		print len(positions)
		
		for i in range(len(positions)):
			clf = joblib.load('classifiers/'+str(i)+'.pkl')
			label = clf.predict(positions[i])
			labels.append(label[0])
		
		emotion=max(set(labels),key=labels.count)
		
		cv2.putText(img,emotion,(x+w/10,y+h+20),fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color=(0,0,255),thickness = 2)	
		cv2.imshow(img_name,img)
	
		if cv2.waitKey(0) & 0xFF == ord('q'):
			cv2.destroyAllWindows()

#trial()
	

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
