import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/akin.jpg")

blank = np.zeros(img.shape[:2], dtype="uint8")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", gray)

circle = cv2.circle(blank, (264,230), 185, 255, -1)

mask = cv2.bitwise_and(gray, gray, mask=circle)
cv2.imshow("Masked image", mask)
# Grayscale histogram
gray_hist = cv2.calcHist([gray], [0], mask, [256], [0,256])

# plot histogram
# plt.figure(), plt.title("Grayscale Histogram")
# plt.xlabel("Bins"), plt.ylabel("# of pixels")
# plt.plot(gray_hist), plt.xlim([0,256]), plt.show()

fig, ax = plt.subplots()
ax.plot(gray_hist)
ax.set(title="Grayscale histogram", xlabel="Bins", ylabel="# of pixels"), plt.xlim([0,256]), plt.show()

cv2.waitKey(0)