import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/akin.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", gray)

# Grayscale histogram
gray_hist = cv2.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)