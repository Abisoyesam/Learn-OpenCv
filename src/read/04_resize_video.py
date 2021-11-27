import cv2

# capture image from webcam
capture = cv2.VideoCapture("./videos/ai.mp4")

while True:
    isTrue, frame = capture.read()

    frame = cv2.resize(frame, (0,0), fx=0.2, fy=0.2)

    cv2.imshow("Video", frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()