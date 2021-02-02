# pylint: skip-file
import cv2
import face_recognition
from PIL import Image, ImageDraw
import numpy

jewel_img = cv2.imread("jewelery.png")
frame = cv2.imread('sample4.jfif')
frame = cv2.resize(frame,(432,576))

# Returns a list of face landmarks present on frame
face_landmarks_list = face_recognition.face_landmarks(frame)
cv2.imshow("frame",frame)
cv2.waitKey(1300)
# For demo images only one person is present in image 
#face_landmarks = face_landmarks_list[0]

