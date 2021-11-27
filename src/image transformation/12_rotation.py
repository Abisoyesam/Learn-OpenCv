import cv2 

img = cv2.imread("images/akin.jpg")
cv2.imshow("Image",img)

# rotation
def rotate(image, angle, rotationpoint=None):
    (height, width) = image.shape[:2]

    if rotationpoint == None:
        rotationpoint = (width//2, height//2)

    rotMatrix = cv2.getRotationMatrix2D(rotationpoint,angle,1.0)
    dimensions = (width, height)

    return cv2.warpAffine(image, rotMatrix, dimensions)

rotatedImg = rotate(img, -20)
# negative >> clockwise, positive >> anti-clockwise
cv2.imshow("Rotated Image", rotatedImg)

cv2.waitKey(0)