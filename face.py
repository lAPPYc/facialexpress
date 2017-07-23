def face_capture(cam, detector, predictor):

	import dlib
	import cv2
	import numpy as np

	#detector = dlib.get_frontal_face_detector()
	

	faces = []
	positions = []
			
	ret, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	
	faces = detector.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 5,minSize = (30,30)#,flags = cv2.CV_HAAR_SCALE_IMAGE
										)
	for (x, y ,w, h) in faces:	
		if len(faces) != 0:
			
			cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
			dlib_rect = dlib.rectangle(int(x), int(y), int(x+w), int(y+h))		
			
			landmarks = np.matrix([[p.x, p.y] for p in predictor(img, dlib_rect).parts()])		#Landmarks is a matrix with landmark no. as the first coordinate, and the x and y on the second position. x coordinate of 13th landmark is accessed by landmarks[12,0]

			for idx, point in enumerate(landmarks):
				pos = (point[0,0], point[0,1])
				positions.append(pos)
				cv2.putText(img, str(idx), pos, fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale = 0.4, color=(0,0,255))
				cv2.circle(img, pos, 2, (0,255,255), -1)
	
	return img, faces, positions

