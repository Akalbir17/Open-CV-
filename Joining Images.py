import cv2
import numpy as np

img =  cv2.imread("Resource/Lenna_(test_image).png")
hor = np.hstack((img,img,img))
ver = np.vstack((img,img))


cv2.imshow('Lena',ver)
cv2.waitKey(0)