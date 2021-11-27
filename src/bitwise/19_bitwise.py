import cv2
import numpy as np

blank = np.zeros((400,400,3), dtype="uint8")

rect = cv2.rectangle(blank.copy(), (50,50), (350,350), (255,255,255), -1)
circle = cv2.circle(blank.copy(),(200,200), 200, (255,255,255), -1)

# cv2.imshow("Rectangle", rect)
# cv2.imshow("Circle", circle)

# bitwise AND >> returns intersecting regions
AND = cv2.bitwise_and(rect, circle)
cv2.imshow("AND", AND)

# bitwise OR >> intersecting and non-intersecting region
OR = cv2.bitwise_or(rect, circle)
cv2.imshow("OR", OR)

# bitwise XOR >> intersecting region
XOR = cv2.bitwise_xor(rect, circle)
cv2.imshow("XOR", XOR)

# bitwise NOT >> revert binary color 
NOT = cv2.bitwise_not(rect)
cv2.imshow("Rectangle NOT", NOT)

cv2.waitKey(0)