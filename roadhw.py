import cv2
image=cv2.imread("road_.png")

cv2.imshow("img",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

starting_point=(0,0)
ending_point=(1900,1000)
rgb=(0,0,255)
line_image=cv2.line(image,starting_point,ending_point,rgb,5)
cv2.imshow("line_image", line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()