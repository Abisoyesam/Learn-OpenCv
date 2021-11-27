import cv2

image = cv2.imread("images/akin.jpg")
cv2.imshow("Image", image)

# gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# threshold the image
ret, thres = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Image", thres)

# contours
contours, hierarchies = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour(s) found!!!")

cv2.waitKey(0)