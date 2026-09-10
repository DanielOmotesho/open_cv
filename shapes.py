import cv2
image=cv2.imread("tom_jerry.jpg")

tandj=cv2.resize(image,(500,500))
cv2.imshow("image",tandj)
cv2.waitKey(0)
cv2.destroyAllWindows()

#line
starting_point=(0,0)
ending_point=(500,500)
rgb=(34,68,92)
line_image=cv2.line(tandj,starting_point,ending_point,rgb,10)
cv2.imshow("line_image", line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#square / rectangle
starting_point2=(50,50)
ending_point2=(450,450)
rgb2=(176,176,176)
square_image=cv2.rectangle(tandj,starting_point2,ending_point2,rgb2,10)
cv2.imshow("square_image",square_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#filled square
starting_point3=(100,100)
ending_point3=(150,150)
rgb3=(230,230,12)
filled_square_image=cv2.rectangle(tandj,starting_point3,ending_point3,rgb3,-1)
cv2.imshow("filled square",filled_square_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#circle
centre_point= (300,250)
radius= 30
rgb4=(40,250,1)
circle_img=cv2.circle(tandj,centre_point,radius,rgb4,-1)
cv2.imshow("circle",circle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#textonimage
font=cv2.FONT_HERSHEY_COMPLEX
pos= (200,200)
fontScale=1
rgb5=(12,89,0)
textonimage=cv2.putText(tandj,"hellooooo",pos,font,fontScale,rgb5,10,cv2.LINE_AA)
cv2.imshow("text",textonimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
