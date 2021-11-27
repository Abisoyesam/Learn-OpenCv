import cv2

img = cv2.imread("images/akin.jpg")
cv2.imshow("Image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple Thresholding
threshold, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Simple Threshold", thresh)

threshold, thresh_inv = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Simple Threshold Inverse", thresh_inv)

# Adaptive threshold
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
cv2.imshow("Adaptive Threshold", adaptive)

cv2.waitKey(0)