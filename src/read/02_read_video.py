import cv2

# capture videos
capture = cv2.VideoCapture(0)
# Pass integer 0, 1, 2 .. to it when capturing video from webcam or external camera
# pass 0 if you wanna read from computer webcam
# pass other integers based on the numbers of usb camera connected
# pass file path to a video if you want to read from existing video

while True:
    # read the video from the capture
    isTrue, frame = capture.read()

    # show the video
    cv2.imshow("Video", frame)

    # to stop the video
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()