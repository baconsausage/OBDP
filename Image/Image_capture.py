import cv2, os, time, shutil

myPath = 'Webcam/'
count = 0
moduleVal = 5
countSave = 0

# Initialize VideoCapture
cap = cv2.VideoCapture(0)


# Initialize FPS
# fps_start_time = time.time()
# fps = 0
# frame_count = 0


def saveDataFunc():
    if os.path.exists(myPath):
        shutil.rmtree(myPath)
    os.makedirs(myPath)


if True: saveDataFunc()

while True:
    ret, frame = cap.read()

    if True:
        img = cv2.resize(frame, (512, 512))
        if count % moduleVal == 0:
            cv2.imwrite(myPath + str(countSave) + ".png", frame)
            countSave += 1
        count += 1

    cv2.imshow("Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
