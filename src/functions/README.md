# Here are the Basic Function in OpenCV

### To convert image to grayscale:
```
cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```
*cvt means **convert**, i.e convert Color*

### To blur an image:
Use gaussian blur to blur an image
```
cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)
```
**N.B: the tuple (7,7) is the kernel size i.e the level at which the image gets blurred.**
