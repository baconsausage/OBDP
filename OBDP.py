# Dealing with Imports
from imageai.Detection import ObjectDetection
import os, cv2, shutil
import numpy as np
import matplotlib.pyplot as plt

count = 0
countSave = 0
modVal = 10
Webcam_path = 'Webcam/'
Detection_path = 'Detection/'


# saveframe function to clear Webcam Path every new run
def saveframe():
    if os.path.exists(Webcam_path):
        shutil.rmtree(Webcam_path)
    os.makedirs(Webcam_path)


saveframe()


# detectframe function to clear Detection Path every new image detected
def detectframe():
    if os.path.exists(Detection_path):
        shutil.rmtree(Detection_path)
    os.makedirs(Detection_path)


detectframe()


# Accessing Latest Image from Webcam path
def updated_image():
    files = os.listdir(Webcam_path)
    i = files[-1]
    abs_path = Webcam_path + i
    return abs_path


# Object detection on images from Webcam Path
def obj_detect(latest):
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path, "yolov3.pt"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=latest,
                                                 output_image_path=os.path.join(Detection_path, "Image_detected.png"),
                                                 minimum_percentage_probability=30)
    # display_detect(output_image_path)
    # work on this in yer next session


execution_path = os.getcwd()

cap = cv2.VideoCapture(0)

# Main Loop
while True:
    ret, frame = cap.read()

    if True:
        if count % modVal == 0:
            cv2.imwrite(Webcam_path + 'Image.png', frame)
        count += 1

    if True:
        latest = updated_image()
        obj_detect(latest)
        print('success!')

    cv2.imshow("Working", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()