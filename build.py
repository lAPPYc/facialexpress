def build():

	from face import face_capture
	import cv2
	import numpy as np
	import matplotlib.pyplot as plt
	from time import sleep
	import os
	from processing import normalize
	import dlib
	
	predictor = 'lib/shape_predictor_68_face_landmarks.dat'
	predictor = dlib.shape_predictor(predictor)
	
	detector = cv2.CascadeClassifier("lib/haarcascade_frontalface_default.xml")
	NE=[];HA=[];FE=[];DI=[];AN=[];SU=[];SA=[]
	
	expressions =  {'NE':'neutral','HA':'happy','FE':'afraid','DI':'disgust','AN':'anger','SU':'surprise','SA':'sad'}
	w = 100; h = 120; eye_dist = 20
	abbvr = {'NE':NE,'HA':HA,'FE':FE,'DI':DI,'AN':AN,'SU':SU, 'SA':SA}

	img_path = 'training_dataset/pics/jaffe/'
	lis = [i for i in os.listdir(img_path) if 'tiff' in i]
	#lis = ['KA.AN1.39.tiff','KA.DI1.42.tiff','KA.FE3.47.tiff','KA.HA1.29.tiff','KA.NE1.26.tiff','KA.SA2.34.tiff','KA.SU3.38.tiff']

	labels = []

	for i in lis:

		face, position = face_capture(cam = None,img_path=img_path,img_name=i, detector=detector, predictor=predictor)
		i = i.split('.')
		i = i[1]
		i = i[0:2]

		position = normalize(face, position,w,h,eye_dist)
		abbvr[i].append(position)
	
	for i in expressions:
		put = open('training_dataset/'+expressions[i]+'.py','w')
		put.write(i+'=')
		put.write(str(abbvr[i]))
