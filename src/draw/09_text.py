import cv2
import numpy as np

# create blank image
blank_image = np.zeros((500,500,3), dtype="uint8")

# write text on image
cv2.putText(blank_image,"Abisoye",(150,150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), thickness=3)
cv2.imshow("Text", blank_image)

cv2.waitKey(0)