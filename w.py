import cv2
import numpy as np

image=cv2.imread("coin.jpg",-1)

#it helps iinitialize filter settings
params=cv2.SimpleBlobDetector_Params()

#area filtering
params.filterByArea=True
params.minArea = 100

#identifying not exact circles
params.filterByCircularity = True
params.minCircularity = 0.6


params.filterByConvexity = True
params.minConvexity = 0.2

params.filterByInertia = True
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)
keypoints= detector.detect(image)
print(keypoints)

blank = np.zeros((1,1))
blobs= cv2.drawKeypoints(image,keypoints,blank,(25,96,2),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs = len(keypoints)
font= cv2.FONT_HERSHEY_COMPLEX
pos=(0,0)
fontscale=7
print(keypoints)
rgb=(25,96,2)
cv2.putText(blobs,"number of circles"+str(number_of_blobs),pos,font,fontscale,rgb,7)
cv2.imshow("img",blobs)
cv2.waitKey(0)

cv2.destroyAllWindows()