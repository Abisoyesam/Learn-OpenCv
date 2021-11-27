'''
Masking helps to focus on the part of image we want. For instance, Face only in face recognition
'''
import cv2
import numpy as np

img = cv2.imread("images/akin.jpg")
cv2.imshow("Image", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# mask = cv2.circle(blank, (264,230), 185, 255, -1)
mask = cv2.rectangle(blank,(50,50), (413,400), (255,255,255),-1)

masked_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Masked", masked_img)


cv2.waitKey(0)