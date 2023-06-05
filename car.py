import cv2
import numpy as numpy
import pickle

# img=cv2.imread("CarParkImg.png")      this will move to the while loop inorder to display the rectangle
# cv2.rectangle(img,(50,192),(158,240),(255,0,255),2)

# here we set the width and height of each rectangle
width=(153-50)
height=(184-140)

# this try and except block is fir checking that if we selecting the rectangle then continue from previous selection
try:
    with open("CarParkPos","rb")  as f:
        poslist=pickle.load(f)

except:
    # here we make the empty list to save the position of rectangle we will make
    poslist=[]


# C:\Users\Hp\Downloads\Python\Deep learning\Open CV\OpenCV projects\CarParkingAvailability

# function mouseClick
def mouseClick(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:       #this is for making the rectangle
        poslist.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:      #this for deleting the rectangle that are made wrong  
        for i,pos in enumerate(poslist):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                poslist.pop(i)

# we store all the postion we selected into file for future use



while True:
    img=cv2.imread("CarParkImg.png")
    img = cv2.resize(img,(img.shape[1]-30,img.shape[0]-30))
    cv2.rectangle(img,(50,192),(158,240),(255,0,255),2)
    cv2.setMouseCallback("my image",mouseClick)
    for pos in poslist:
        x,y=pos
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)

    with open("CarParkPos","wb")  as f:
        pickle.dump(poslist,f)
    

    cv2.imshow("my image",img)

# we made the rectangle but we wants to show this rectangle on every space by clicking on it 
    


    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

