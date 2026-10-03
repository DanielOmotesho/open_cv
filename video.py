import os
import cv2
import PIL
from PIL import Image


path="C:\\Users\\danie\\OneDrive\\jetlearn\\open_cv\\video_gallery\\photos"

mean_height=0
mean_width=0

num_of_images=len(os.listdir("."))
print (num_of_images)
for file in os.listdir(path):
    if file.endswith((".jpg")):
        img=Image.open(os.path.join(path,file))
        width,height=img.size
        print (width,height)
        mean_width=mean_width+width
        mean_height = mean_height+height

mean_width = mean_width // 3
mean_height= mean_height // 3
for file in os.listdir(path):
    if file.endswith ((".jpg")):
        img=Image.open(os.path.join(path,file))
        img_resized = img.resize((mean_width,mean_height),Image.Resampling.LANCZOS)
        img_resized.save(file,"png",quality = 95)

video_name="MyFirstVideo.avi"
images=[]
for img in os.listdir(path):
    images.append(img)

print(images)
frame=cv2.imread(os.path.join(path, images[0]))
height,width,layers = frame.shape
video = cv2.VideoWriter(video_name,0,1,(width,height))

for image in images: 
    video.write(cv2.imread(os.path.join(path,image)))
cv2.destroyAllWindows()
video.release()

