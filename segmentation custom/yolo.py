# data
# train -> images and labels
# val -> images and labels
# test -> images and labels
import os
from ultralytics import YOLO

# os.system("yolo task=segment mode=train model=yolov8n-seg.pt data=data.yaml epochs=1 ")

if __name__ == '__main__':
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    model = YOLO('yolov8n-seg.pt')  # load a pretrained YOLOv8n detection model
    model.train(data='data.yaml', epochs=9, device=0)

# model.train(data='data.yaml', epochs=1,device=0)
# !!!! blunderrrr
# remember to use the correct model