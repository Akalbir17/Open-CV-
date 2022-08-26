import cv2
import numpy as np

img = cv2.imread("Resource/test.jpg")
print(img.shape)
imgR = cv2.resize(img,(800,700))
imgC = img[0:750,250:500]

cv2.imshow('image',img)
cv2.imshow('imageResize',imgR)
cv2.imshow('imageCropped',imgC)
cv2.waitKey(0)