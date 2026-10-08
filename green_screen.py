import cv2
import numpy as np
import time

raw_video = cv2.VideoCapture("gs.mp4")
time.sleep(1)
count=0
background=0

for i in range(60):
    return_val, background = raw_video.read()
    if return_val ==False:
        continue
    #flipping means inverting
background= np.flip(background, axis = 1)#flipping horizontally is the 1 value 
while(raw_video.isOpened()):
    return_val,img = raw_video.read()
    if return_val==False:
        break
    count+=1
    img=np.flip(img,axis=1)
    hsv =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red = np.array([10,40,40])
    upper_red = np.array([100,255,255])
    mask1=cv2.inRange(hsv,lower_red,upper_red)
    lower_red2 = np.array([155,40,40])
    upper_red2 = np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red2,upper_red2)
    mask1=mask1+mask2
    

