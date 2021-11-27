import cv2

img = cv2.imread("images/akin.jpg")
cv2.imshow("Image", img)

# Flip image
flipImg = cv2.flip(img, 0)
# Flipping code can either be 0,1,-1
# 0 >> Vertically over x-axis, 1 >> Horizontally over y-axis, -1 >> both horizontally and verically
cv2.imshow("Flipped Image", flipImg)


cv2.waitKey(0)