from face import face_capture
import cv2
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

expressions = ['smile','fear','disgust','anger','surprise','curious']

for i in expressions:
	print 'for ', i, '\n'
	raw_input("Hit Enter when ready to take pic:")

	for j in range(5):
		print "capturing in " ,j	
		sleep(1)
	face_capture()
	
