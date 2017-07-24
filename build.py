def build(no):

	from face import face_capture
	import cv2
	import numpy as np
	import matplotlib.pyplot as plt
	from time import sleep
	import os
	from processing import create, normalize
	import dlib
	
	predictor = 'lib/shape_predictor_68_face_landmarks.dat'
	predictor = dlib.shape_predictor(predictor)
	
	detector = cv2.CascadeClassifier("lib/haarcascade_frontalface_default.xml")
	
	expressions =  ['neutral','smile','fear','disgust','anger','surprise','curious']
	w = 100; h = 120; eye_dist = 20

	for i in expressions:
		put = open('training_dataset/'+i+'.py','a')
		lis = []

		for l in range(no):
			print '\n\nfor ', i, '\n'
			cam = cv2.VideoCapture(0)

			while(1):
				img, face, position = face_capture(cam, detector, predictor)
				cv2.imshow('output',img)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					if len(face) != 1:
						print 'try again, for ', i
						continue
					break
			del(cam)

			position = normalize(face, position,w,h,eye_dist)
			lis.append(position)

		put.write(i+'='+str(lis))
		put.close()
