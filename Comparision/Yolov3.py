from imageai.Detection import ObjectDetection
import os
from PIL import Image

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolov3.pt"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "download.jpg"),
                                             output_image_path=os.path.join(execution_path, "download_yolo.jpg"),
                                             minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
    print("--------------------------------")

im = Image.open(execution_path + '\\' + 'download_yolo.jpg')
im.show()