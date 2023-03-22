from imageai.Detection import ObjectDetection
import os
import cv2
import numpy


# from PIL import Image


def imageai_detect(frame):
    execution_path = os.getcwd()
    frame_yolo = os.path.join(execution_path, "frame_yolo.jpg")

    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path, "yolov3.pt"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=frame, output_image_path=frame_yolo,
                                                 minimum_percentage_probability=30)

    for eachObject in detections:
        print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
        print("--------------------------------")
    return frame_yolo


cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()
    yolo = imageai_detect(frame)

    image = cv2.imread(yolo)
    # pil_yolo = Image.open(yolo)
    np_yolo = numpy.array(image)

    cv2.imshow('ImageAI Webcam', np_yolo)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()