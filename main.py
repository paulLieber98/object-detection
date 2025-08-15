import inference
import cv2 as cv
from ultralytics import YOLO #for model
import time
import pygame


#SETUP FOR DING
pygame.mixer.init()
pygame.mixer.music.load('ding-36029 (1).mp3')

#DEFINING MODEL
model = YOLO("yolov8s.pt")

#LOADING MODEL
model.load("yolov8s.pt")

# results = model.track(source=1, show=True) #track: shows IDs

#accessing IDs + confidence threshold
people_ids = []
confidence_threshold = 0.9

#DING IF PERSON IS DETECTED
last_ding_time = 0  # Track when we last played the ding
ding_cooldown = 2.0  # Minimum seconds between dings

for result in model.track(source=1, show=True, stream = True):
# for result in results: #iterate through each output from result object
    #if only a person label is detected, add ID to list
    if result.boxes is not None and len(result.boxes) > 0:
        #store class indices and IDs in variables
        class_indices = result.boxes.cls #accessing class indices
        track_ids = result.boxes.id #accessing IDs

        #iterate through each detection
        for i, class_id_x in enumerate(class_indices):
            #check if this detection is a person (class 0)
            if class_id_x == 0: #0 = person in class indices 
                if result.boxes.conf[i] > confidence_threshold:
                    current_time = time.time()
                    #only ding if enough time has passed since last ding
                    if current_time - last_ding_time >= ding_cooldown:
                        #mp3 ding
                        pygame.mixer.music.play()
                        print("ding")
                        last_ding_time = current_time



#ADDING PEOPLE IDS TO A LIST
# for result in results: #iterate through each output from result object
#     #if only a person label is detected, add ID to list
#     if result.boxes is not None and len(result.boxes) > 0:
#         #store class indices and IDs in variables
#         class_indices = result.boxes.cls #accessing class indices
#         track_ids = result.boxes.id #accessing IDs
        
#         #iterate through each detection
#         for i, class_id_x in enumerate(class_indices):
#             #check if this detection is a person (class 0)
#             if class_id_x == 0: #0 = person in class indices 
#                 #add the corresponding ID to the list
#                 if track_ids is not None and i < len(track_ids): #check if ID exists + if index is in range
#                     tracking_id = track_ids[i]
#                     if tracking_id not in people_ids: #check if this ID is already in list
#                         if result.boxes.conf[i] > confidence_threshold: #check if confidence of person detected is above threshold
#                             people_ids.append(tracking_id)

# print(f'ids of people: {people_ids}')