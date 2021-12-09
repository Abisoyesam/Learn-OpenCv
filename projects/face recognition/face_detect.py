import cv2

img = cv2.imread("images/group 2.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier("D:\CLONE\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")

face_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# Increasing the minNeighbor value will allow the image to be prone to noise
# Decreasing the minNeighbor value to get mre robust result

print(f'Number of face(s) found is {len(face_rect)}')

# TO read the cordinate of the image
for (x,y,w,h) in face_rect:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255, 0), thickness=2)

cv2.imshow("Image", img)

cv2.waitKey(0)