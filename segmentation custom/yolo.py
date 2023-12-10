# data
# train -> images and labels
# val -> images and labels
# test -> images and labels
from ultralytics import YOLO

model = YOLO("yolov8n-seg.yaml")


results = model.train(data="data.yaml", epochs=1) #train the model

