import cv2
import numpy as np
from numpy.lib.type_check import imag

image = cv2.imread("images/akin.jpg")
cv2.imshow("Image", image)

# Translation is basically "SHIFTING" the image along the X and Y axis
def translate(image,x,y):
    transMatric = np.float32([[1,0,x],[0,1,y]])
    dimension = (image.shape[1], image.shape[0])
    return cv2.warpAffine(image,transMatric,dimension)

# Negative X is left and positive X is right, Negative Y axis is up while positive is down
translated = translate(image, -100, 100)
cv2.imshow("Translate", translated)

cv2.waitKey(0)