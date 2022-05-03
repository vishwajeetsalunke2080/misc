import cv2


imagePath= r"C:\Users\vishw\Desktop\python projects\IMG20210612085825.jpg"
cascPath= r"C:\Users\vishw\Desktop\python projects\haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags=cv2.COVAR_SCALE
)

print("found {0} faces!".format(len(faces)))

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("faces found",image)
cv2.waitKey(0)
