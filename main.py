import cv2
import numpy as np 
import cvzone
import pickle

width=(147-50)
height=(184-140)
cap =cv2.VideoCapture("carPark.mp4")

with open("CarParkPos","rb")  as f:
        poslist=pickle.load(f)

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    
    success,img=cap.read()

    for pos in poslist:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)
    # cv2.imshow("my image",img)



    cv2.imshow("my car",img)
    # cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
