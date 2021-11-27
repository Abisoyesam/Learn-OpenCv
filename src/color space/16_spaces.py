import cv2
from matplotlib.pyplot import imshow

# read image
image = cv2.imread("images/akin.jpg")

# convert BGR to grayscale
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",grayImg)

# BGR to HSV Hue, Saturation, Value
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# BGR to LAB 
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB IMAGE", lab)

# BGR to RGB
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB IMAGE", rgb)

# HSV to BGR
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("HSV --> BGR", hsv_bgr)

# window wait
cv2.waitKey(0)