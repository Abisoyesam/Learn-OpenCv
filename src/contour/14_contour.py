import cv2

# Read image
image = cv2.imread("images/akin.jpg")
cv2.imshow("Image", image)

'''
Contours are basically the boundary of an object. From mathematical point of view, they are not the same as Edges.
Contours are useful in shape analysis, or object detection 
'''

# convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# blur the image
blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow("Blur Image", blur)

# grab edges using canny
canny = cv2.Canny(blur, 125, 175)
cv2.imshow("Canny Image", canny)

# contours
contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
'''
RETR_TREE >> for all hierarchical contours
RETR_EXTERNAL >> for external contours
RETR_LIST >> all contours in the image
---------------------------------------------------------
contours is a python list of contours found in an image
---------------------------------------------------------
'''
print(f'{len(contours)} contour(s) found!')

cv2.waitKey(3000) # 3000 >> 3 seconds