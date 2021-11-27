import matplotlib.pyplot as plt
import cv2

img = cv2.imread("images/akin.jpg")

# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# BGR
plt.imshow(img)
plt.show()

# RGB
plt.imshow(rgb)
plt.show()
