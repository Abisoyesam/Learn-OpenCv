import cv2
import numpy as np

# create blank image
blank = np.zeros((500,500,3), dtype="uint8")
cv2.imshow("blank", blank)

# paint the blank image with certain color
blank[:] = 0,255,0  # Remember: BGR >> Blue, Green, Red in OpenCv
# blank[200:400, 300:500] = 0,255,0
cv2.imshow("Green", blank)

cv2.waitKey(0)