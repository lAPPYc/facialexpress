from train import classifier
from face import face_capture
from dataset import expressions
from dataset import w, h, eye_dist
from processing import normalize
import cv2

while(1):

	img, face, positions = face_capture()

	positions = normalize(face, position, w, h, eye_dist)

	label = classifier.predict(positions)

	cv2.putText(img,str(label),positions[8],fontFace = 									cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
									fontScale = 0.4,
									color=(0,0,255))

	cv2.imshow('output',img)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
