import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/akin.jpg")
cv2.imshow("Image", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

mask = cv2.circle(blank, (264,230), 185, 255, -1)

masked = cv2.bitwise_and(img, img, mask=mask)
# cv2.imshow("Masked image", masked)

# Color Histogram
colours = ("b","g","r")

plt.figure("Color Histogram"), plt.title("Color Histogram")
plt.xlabel("Bins"), plt.ylabel("# of pixels")

for i, col in enumerate(colours):
    hist = cv2.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv2.waitKey(0)