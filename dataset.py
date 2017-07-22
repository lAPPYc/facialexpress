from face import face_capture
import cv2
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import os

expressions = ['neutral','smile','fear','disgust','anger','surprise','curious']
w = 100; h = 120
eye_dist = 20
for i in expressions:
	os.system('touch training_dataset/'+i+'.txt')

for i in expressions:
	put = open('training_dataset/'+i+'.txt','a')
	for l in range(10):
		print '\n\nfor ', i, '\n'
		'''raw_input("Hit Enter when ready to take pic:")

		for j in range(3):
			print "capturing in " ,3-j	
			sleep(1)'''
		face, position = face_capture()
		
		''''x = []
		y = []
		for j in position:
			x.append(j[0])
			y.append(j[1])
		plt.scatter(x,y)
		plt.show()'''
	
		w1 = face[0][2]; h1 = face[0][3]
		scaleWX = float(w)/float(w1); scaleWY = float(h)/float(h1)	
	
		def translate((x,y)):
			x = x-face[0][0]
			y = y-face[0][1]
			return (x,y)
		
		def coordinates((x,y)):
			x = x-origX
			y = -y+origY
			return (x,y)
	
		pos1 = position[45]
		pos2 = position[36]
		orig = position[27]
		
		orig = translate(orig)
		pos1 = translate(pos1)		
		pos2 = translate(pos2)
		
		origX = orig[0]
		origY = orig[1]
		
		pos1 = coordinates(pos1)
		pos2 = coordinates(pos2)
		
		pos1 = (float(pos1[0])*float(scaleWX),float(pos1[1])/float(scaleWY))
		pos2 = (float(pos2[0])*float(scaleWX),float(pos2[1])/float(scaleWY))

		scaleX = float(eye_dist)/float(pos2[0]-pos1[0])

		#X = []; Y = []

		for j in range(len(position)):
			k = translate(position[j])
			k = coordinates(k)
			k = (float(k[0])*float(scaleWX),float(k[1])*float(scaleWY))
			position[j] = (k[0]*scaleX,k[1])
	
		''''for j in range(len(position)):		
			X.append(position[j][0])
			Y.append(position[j][1])
		
		plt.scatter(X,Y)
		plt.show()'''
		put.write(str(position)+',')
	put.close()

	
	
	
	
	
	
