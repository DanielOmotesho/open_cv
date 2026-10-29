import cv2,os,numpy,sys

size = 4
haar_file = 'haarcascade_frontalface_default.xml'
dataset = 'dataset/daniel'
print('Recognizing Face Please Be in suffiecient Lights...')

width = 130
height = 100

images = []
labels = []

for filename in os.listdir(dataset):
    #redirecting to the exact file location where image is
    path = os.path.join(dataset,filename)
    image = cv2.imread(path,0)

    if image is not None:
        image = cv2.resize(image,(width,height))
        images.append(image)
        labels.append(0)

#helps convert images and labels to array format
images= numpy.array(images)

labels = numpy.array(labels)

#learns patterns of images and uses the patterns to compare new face with faces that it was trained.
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)

#it detects faces located in an image
face_cascade = cv2.CascadeClassifier(haar_file)

webcam = cv2.VideoCapture(0)

while True:
    ret,frame = webcam.read()

    if not ret:
        break

    gray = cv2.cvtColour(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

#the command detects the face and crops the face using x,y amd width and height
    for (x,y,w,h) in faces:
        face = gray[y:y+h, x:x+w]
        face_resize = cv2.resize(face,(width,height))
        prediction = model.predict(face_resize)
        if prediction[1] < 70:
            text = "daniel"
            color= (56,72,251)

