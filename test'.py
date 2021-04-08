import cv2 as cv
cap = cv.VideoCapture('videos/vid1.mp4') # Making capture object

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('Frame not available')
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('video', gray)
    if cv.waitKey(5) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
