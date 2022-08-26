import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img[:] = 0,0,255
cv2.line(img,(0,0),(400,400),(0,0,255),3)
cv2.rectangle(img,(50,50),(450,450),(0,250,0),2)
cv2.circle(img,(450,450),50 ,(255,0,0),3)
cv2.putText(img,'OpenCv',(200,50),cv2.FONT_ITALIC,2,(0,150,0),10)
cv2.imshow("image",img)
cv2.waitKey(0)