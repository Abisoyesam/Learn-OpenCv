import cv2
import numpy as np

# create a blank image
blank_image = np.zeros((500,500,3), dtype="uint8")

# draw a circle
cv2.circle(blank_image,(250,250), 100, (0,255,0), thickness=2)
# to get the center of the image use (blank_image.shape[1]//2, blank_image.shape[0]//2) instead of (250,250)
# cv2.circle(blank_image,(blank_image.shape[1]//2, blank_image.shape[0]//2), 100, (0,255,0), thickness=2)

cv2.imshow("Circle", blank_image)

cv2.waitKey(0)