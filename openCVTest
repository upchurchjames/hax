import cv2

image = cv2.imread('samantha.jpeg')

face_detection = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('img_gray', gray)

faces = face_detection.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    img = cv2.rectangle(image,(x,y),(x + w, y + h),(255, 0, 0),3)

cv2.imwrite('FACE_sam.jpeg', img)

cv2.imshow('rectangle', cv2.imread('FACE_sam.jpeg'))

cv2.waitKey()
