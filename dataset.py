from face import face_capture
import cv2
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import os
from processing import *

expressions =  ['neutral','smile','fear','disgust','anger','surprise','curious']
w = 100; h = 120
eye_dist = 20

def build(no):

	for i in expressions:
		put = open('training_dataset/'+i+'.txt','a')
	
		for l in range(no):
			print '\n\nfor ', i, '\n'
			'''raw_input("Hit Enter when ready to take pic:")

			for j in range(3):
				print "capturing in " ,3-j	
				sleep(1)'''
			face, position = face_capture()
			print position
			print len(position)
			print type(position)
			print type(position[0])
			position = normalize(face, position,w,h,eye_dist)
			
			put.write(str(position)+':')
		put.close()

create()
build(5)
