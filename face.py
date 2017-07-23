def face_capture(N = None):

	import dlib
	import cv2
	import numpy as np

	#detector = dlib.get_frontal_face_detector()
	detector = cv2.CascadeClassifier("lib/haarcascade_frontalface_default.xml")
	predictor = 'lib/shape_predictor_68_face_landmarks.dat'
	predictor = dlib.shape_predictor(predictor)

	cam = cv2.VideoCapture(0)
	#cam = cv2.VideoCapture('../../../G/Himanshu/Series/Chuck/Season 2/Chuck Season 2 Episode 11.ts')		#if nonetype is returned, interchange ts and TS'
	#img = cv2.imread('lib/dlib/examples/faces/2008_002506.jpg')

	JAWLINE_POINTS = list(range(0, 17))  
	RIGHT_EYEBROW_POINTS = list(range(17, 22))  
	LEFT_EYEBROW_POINTS = list(range(22, 27))  
	NOSE_POINTS = list(range(27, 36))  
	RIGHT_EYE_POINTS = list(range(36, 42))  
	LEFT_EYE_POINTS = list(range(42, 48))  
	MOUTH_OUTLINE_POINTS = list(range(48, 61))  
	MOUTH_INNER_POINTS = list(range(61, 68)) 

	faces = []
	positions = []
	a = 0
	while len(faces) == 0:
		if a != 0:
			print 'try again'
		
		while(1):

			ret, img = cam.read()
			#dets = detector(img,1)
	
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
			faces = detector.detectMultiScale(
											gray,
											scaleFactor = 1.1,
											minNeighbors = 5,
											minSize = (30,30)
											#flags = cv2.CV_HAAR_SCALE_IMAGE
											)

			for (x, y ,w, h) in faces:	
				if len(faces) == 1:
					cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
				dlib_rect = dlib.rectangle(int(x), int(y), int(x+w), int(y+h))		
				landmarks = np.matrix([[p.x, p.y] for p in predictor(img, dlib_rect).parts()])		#Landmarks is a matrix with landmark no. as the first coordinate, and the x and y on the second position. x coordinate of 13th landmark is accessed by landmarks[12,0]
		
				for idx, point in enumerate(landmarks):
					pos = (point[0,0], point[0,1])
					positions.append(pos)
					if N == None:
						cv2.putText(img, str(idx), pos, fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale = 0.4, color=(0,0,255))
	
						cv2.circle(img, pos, 2, (0,255,255), -1)

			if N == None:
				cv2.imshow('output',img)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
			else:
				break
			
		a = 1

		del(cam)
		cv2.destroyAllWindows()
		if N == None:
			return faces, positions
		else:
			return img, faces, positions

