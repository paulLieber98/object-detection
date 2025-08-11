import inference
import cv2 as cv
from ultralytics import YOLO #for model

#DEFINING MODEL
model = YOLO("yolov8n.pt")

#LOADING MODEL
model.load("yolov8n.pt")

results = model.predict(source=1, show=True)

# #WEBCAM OPENCV
# webcam = cv.VideoCapture(1)

# if not webcam.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = webcam.read()
 
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     #flip so not inverted (dont know why it does this by default)
#     frame = cv.flip(frame, 1)
#     # Display the resulting frame
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) == ord('q'):
#         break
 
# # When everything done, release the capture
# webcam.release()
# cv.destroyAllWindows()