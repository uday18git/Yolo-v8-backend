# data
# train -> images and labels
# val -> images and labels
# test -> images and labels
from ultralytics import YOLO

model = YOLO("yolov8n-seg.yaml")
model.to('cuda')
results = model.train(data="config.yaml", epochs=10) #train the model

