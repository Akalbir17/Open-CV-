import cv2
import numpy as np
width,height = 250,350
img=cv2.imread("Resource\king cards.jpg")
pts1 = np.float32([[98,293],[246,118],[452,469],[597,262]])
pts2 = np.float32([[0,0],[width,0],[0,height],[height,width]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgout = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('Cards',img)
cv2.imshow('Warp Perspective',imgout)
cv2.waitKey(0)