import inference
import cv2 as cv
from ultralytics import YOLO #for model

#DEFINING MODEL
model = YOLO("yolov8n.pt")

#LOADING MODEL
model.load("yolov8n.pt")

results = model.track(source=1, show=True) #track: shows IDs

#accessing IDs + confidence threshold
people_ids = []
confidence_threshold = 0.9

for result in results: #iterate through each output from result object
    #if only a person label is detected, add ID to list
    if result.boxes is not None and len(result.boxes) > 0:
        #store class indices and IDs in variables
        class_indices = result.boxes.cls #accessing class indices
        track_ids = result.boxes.id #accessing IDs
        
        #iterate through each detection
        for i, class_id_x in enumerate(class_indices):
            #check if this detection is a person (class 0)
            if class_id_x == 0: #0 = person in class indices 
                #add the corresponding ID to the list
                if track_ids is not None and i < len(track_ids): #check if ID exists + if index is in range
                    tracking_id = track_ids[i]
                    if tracking_id not in people_ids: #check if this ID is already in list
                        if result.boxes.conf[i] > confidence_threshold: #check if confidence of person detected is above threshold
                            people_ids.append(tracking_id)

print(f'ids of people: {people_ids}')





