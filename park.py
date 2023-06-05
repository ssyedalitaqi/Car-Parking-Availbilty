# import numpy as np
# import pandas as pd 
# import pickle
# import cvzone
# import cv2

# cap=cv2.VideoCapture("carPark.mp4")
# success,vid=cap.read()
# while True:
#     cv2.imshow("video",vid)
#     cv2.waitKey(1)

# cv.detroyedAllWIndow()    


import numpy as np
import pandas as pd 
import pickle
import cvzone
import cv2

cap = cv2.VideoCapture("carPark.mp4")
success, vid = cap.read()

while True:
    cv2.imshow("video", vid)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
