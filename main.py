import inference
import cv2 as cv
from ultralytics import YOLO #for model

#DEFINING MODEL
model = YOLO("yolov8n.pt")

#LOADING MODEL
model.load("yolov8n.pt")

# results = model.predict(source=1, show=True) #predict: track just no IDs
results = model.track(source=1, show=True) #track: shows IDs



