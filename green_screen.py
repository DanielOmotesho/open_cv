import cv2
import numpy as np
import time

raw_video = cv2.VideoCapture("gs2.mp4")
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
    #lower_orange = np.array([10, 40, 40])
    #upper_orange = np.array([25, 255, 255])

    mask2=cv2.inRange(hsv,lower_red2,upper_red2)
    mask1=mask1+mask2
    #refining a blurry image
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    #slightly expanding area detected and fills gaaps in detected area to ensure object detected is more accurate
    mask1=cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1 )
    mask2 = cv2.bitwise_not(mask1)
    result = cv2.bitwise_and(background,background,mask = mask1)
    result2 = cv2.bitwise_and(img,img,mask = mask2)
    final_output = cv2.addWeighted (result,1,result2,1,0)
    cv2.imshow("my_first_green_screen",final_output)
    k=cv2.waitKey(10)
    if k ==27:
      break
    


