import cv2

img = cv2.imread("./images/akin.jpg")

# resize the image
img = cv2.resize(img, (0,0), fx=0.6, fy=0.5)

cv2.imshow("Akinloye", img)

cv2.waitKey(0)