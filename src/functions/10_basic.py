import cv2

img = cv2.imread("images/akin.jpg")
cv2.imshow("Image", img)

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# blur an image using guassian blur
blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT) # Ksize (3,3) always has to be odd number
cv2.imshow("Blur", blur)

# Edge cascade: To find edges in the image
canny = cv2.Canny(blur, 125, 175)
cv2.imshow("Canny Edges", canny)
# Reduce Canny by blurin the image

# dilating images
dilated = cv2.dilate(canny, (7,7), iterations=1)
cv2.imshow("Dilated Image", dilated)

# Eroding: to get edges back in a dilated images
eroded = cv2.erode(dilated, (3,3), iterations=1)
cv2.imshow("Eroded", eroded)

# resize image
resized = cv2.resize(img, (520,520), interpolation=cv2.INTER_CUBIC)
# use INTER_CUBIC when enlarging the image and INTER_LINEAR or INTER_AREA when shrinking the image
cv2.imshow("Resized", resized)

# Crop Image
cropped = img[50:200, 150:400]
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)