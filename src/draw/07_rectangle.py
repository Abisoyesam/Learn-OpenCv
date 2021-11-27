import cv2
import numpy as np

# create blank image
blankImg = np.zeros((500,500,3), dtype="uint8")
cv2.imshow("Blank", blankImg)

# draw a rectangle on blank image
cv2.rectangle(blankImg, (0,0), (250,250), (0,255,0), thickness=2)

# to fill the entire rectangle with solid color 
cv2.rectangle(blankImg, (0,0), (250,250), (0,255,0), thickness=cv2.FILLED)
cv2.rectangle(blankImg, (0,0), (250,250), (0,255,0), thickness=-1)

# display the rectangle
cv2.imshow("Rectangle", blankImg)

cv2.waitKey(0)