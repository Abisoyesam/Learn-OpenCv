'''
Spliting and Merging an image into different color channels (i.e) RED, BLUE, GREEN
'''

import cv2
import numpy as np

img = cv2.imread("images/akin.jpg")

# blank image
blank = np.zeros(img.shape[:2], dtype="uint8")

# splitting
b,g,r = cv2.split(img)

# they are all in grayscale
# cv2.imshow("Blue", b)
# cv2.imshow("Green", g)
# cv2.imshow("Red", r)

# merging
merged = cv2.merge([b,g,r])
cv2.imshow("Merge", merged)

# merging to get exact color
blue = cv2.merge([b,blank,blank])
cv2.imshow("Blue", blue)

green = cv2.merge([blank,g,blank])
cv2.imshow("Green", green)

red = cv2.merge([blank,blank,r])
cv2.imshow("Red", red)

print(img.shape, b.shape, g.shape, r.shape)

cv2.waitKey(0)
