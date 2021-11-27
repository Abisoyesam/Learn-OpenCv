import cv2

img = cv2.imread("images/akin.jpg")
cv2.imshow("Image", img)

# Averaging blur
aver = cv2.blur(img, (3,3))
cv2.imshow("Average Blur", aver)

# gaussian blur
gauss = cv2.GaussianBlur(img, (3,3), 0)
cv2.imshow("Gaussian blur", img)

# median blur : more effective than the Gauss and Averaging 
med = cv2.medianBlur(img, 3)
cv2.imshow("Median blur", med)

# bilateral blur: Most effective and usally used in Computer Vision Project 
# It as well retains edges even when image is blurred
bilat = cv2.bilateralFilter(img, 5, 15, 15)
cv2.imshow("Bilateral blur", bilat)

cv2.waitKey(0)