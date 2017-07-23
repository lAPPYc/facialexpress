from face import face_capture
from processing import normalize
import cv2
from sklearn.externals import joblib

expressions =  ['neutral','smile','fear','disgust','anger','surprise','curious']
w = 100; h = 120; eye_dist = 20

while(1):
	
	print 'captureing'
	img, face, positions = face_capture(1)
	print 'captured, analyzing'
	if len(face) != 1:
		continue	
	
	positions = normalize(face, positions, w, h, eye_dist)
	print 'normalized'
	clf = joblib.load('classifier.pkl')
	print 'loaded'
	label = clf.predict(positions)

	print label

	cv2.putText(img,str(label),(100,100),fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale = 4, color=(0,0,255))

	cv2.imshow('output',img)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
