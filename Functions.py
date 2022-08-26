import cv2
import numpy as np

img = cv2.imread("Resource/test.jpg")
kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(11,11),0)
imgCanny = cv2.Canny(img,100,100)
imgDilate = cv2.dilate(imgCanny,kernel, iterations=2) 
imgErode = cv2.erode(imgDilate,kernel,iterations=2)
cv2.imshow("canny",imgCanny)
cv2.imshow("dilate",imgDilate)
cv2.imshow("erode",imgErode)
cv2.waitKey(0)
