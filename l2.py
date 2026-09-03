import cv2
import numpy as np

luigi_img=cv2.imread("luigi.png")
new_image=cv2.resize(luigi_img,(625,625))
cv2.imwrite("resized_img.png",new_image)



mario_img=cv2.imread("mario.jpg")
new_image2=cv2.imread("resized_img.png")
output=cv2.addWeighted(new_image2, 0.6, mario_img, 0.3,0)
output2=cv2.subtract(mario_img,new_image2)
cv2.imshow("output",output)
cv2.imshow("output2",output2)
cv2.waitKey(0)
cv2.destroyAllWindows()

mario_img=cv2.imread("luigi.png")
kernel = np.ones((5,5),np.uint8)
image=cv2.erode(mario_img, kernel)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


gaussian= cv2.GaussianBlur(new_image,(19,19),0)
cv2.imshow("gaussian",gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

median=cv2.medianBlur(new_image,5)
cv2.imshow("median",median)
cv2.waitKey(0)
cv2.destroyAllWindows()

bilateral = cv2.bilateralFilter(new_image, 19, 75, 75)
cv2.imshow("bilateral", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

border= cv2.imread("spongebob.png")
borderedImage= cv2.copyMakeBorder(border,10,10,10,10,cv2.BORDER_CONSTANT)
cv2.imshow("border",borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

