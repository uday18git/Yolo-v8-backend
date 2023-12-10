# data
# train -> images and labels
# val -> images and labels
# test -> images and labels
import os
from ultralytics import YOLO



os.system("yolo task=segment mode=train model=yolov8n-seg.pt data=data.yaml epochs=1 imgsz=640 save=true")

