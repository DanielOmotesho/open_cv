import cv2

image=cv2.imread("pikachu_img.png",cv2.IMREAD_COLOR)
cv2.imshow("pikachu",image)
cv2.waitKey(0)



#changing the image to no colour(grey) 
image2=cv2.imread("pikachu_img.png",0)
cv2.imshow("pikachu",image2)

#saving the image
cv2.imwrite("pikachu_2.png",image2)


#deleting the page using any key
cv2.waitKey(0)

image3=cv2.imread("pikachu_img.png",1)
B, G, R= cv2.split(image)
cv2.imshow("blue",B)
cv2.imshow("green",G)
cv2.imshow("red",R)
cv2.waitKey(0)
cv2.destroyAllWindows()
