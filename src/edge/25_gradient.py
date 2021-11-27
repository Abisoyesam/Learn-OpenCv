import cv2
import numpy as np

img = cv2.imread("images/akin.jpg")
cv2.imshow("Image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Laplacain
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)

# Sobel : It computes gradients to direction
sobelX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
combined_shobel = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("SobelX", sobelX)
cv2.imshow("SobelY", sobelY)
cv2.imshow("Combined", combined_shobel)

cv2.waitKey(0)