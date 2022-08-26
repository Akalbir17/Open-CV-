import cv2

faceCascade = cv2.CascadeClassifier("Resource\haarcascade_frontalface_default.xml")
eyesCascade = cv2.CascadeClassifier("Resource\haarcascade_eye.xml")
path = "Resource\Lenna_(test_image).png"
img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = faceCascade.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = img [y:y+h,x:x+w]
    eyes = eyesCascade.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0))

    cv2.imshow("webcam",img)

    cv2.waitKey(0) 

cv2.destroyAllWindows()