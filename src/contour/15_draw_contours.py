import cv2
import numpy as np

# read image
image = cv2.imread("images/akin.jpg")

# create blank image
blank = np.zeros(image.shape, dtype="uint8")

# gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# threshold image
ret, thres = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)

# contours
contours, hierarchies = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour(s) found!!!")

# draw contours on blank
cv2.drawContours(blank, contours, -1, (0,0,255), 2)
cv2.imshow("Contours drawn", blank)

cv2.waitKey(0)