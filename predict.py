import numpy as np
from face import face_capture
from processing import normalize
import cv2
from sklearn.externals import joblib
import dlib

predictor = 'lib/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor)
detector = cv2.CascadeClassifier("lib/haarcascade_frontalface_default.xml")


expressions =  ['neutral','smile','fear','disgust','anger','surprise','curious']
w = 100; h = 120; eye_dist = 20
cam = cv2.VideoCapture(0)
emotion = ''

while(1):

	img, face, positions = face_capture(cam, detector, predictor)
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
	clf = joblib.load('classifier.pkl')
	label = clf.predict(positions)

	print label
	emotion=label[0]
