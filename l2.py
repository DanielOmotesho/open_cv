import cv2
import numpy as np

luigi_img=cv2.imread("luigi.png")
new_image=cv2.resize(luigi_img,(625,625))
cv2.imwrite("resized_img.png",new_image)

mario_img=cv2.imread("mario.jpg")
new_image2=cv2.imread("resized_img.png")
output=cv2.addWeighted(new_image2, 0.6, mario_img, 0.3,0)
cv2.imshow("output",output)
cv2.waitKey(0)
cv2.destroyAllWindows()