import cv2
import numpy as np

# create a blank image
blank_image = np.zeros((500,500,3), dtype="uint8")

# draw a line on the blank image
cv2.line(blank_image,(30,50),(250,250), (255,255,255), thickness=2)
cv2.imshow("Line", blank_image)

cv2.waitKey(0)