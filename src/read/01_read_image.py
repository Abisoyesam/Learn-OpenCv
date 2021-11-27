import cv2

# read the image
img = cv2.imread("./images/akin.jpg")

# show the image
cv2.imshow("Akinloye", img)

# image window to wait
cv2.waitKey(0)