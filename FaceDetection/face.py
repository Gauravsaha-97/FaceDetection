import cv2

cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml ')

while cap.isOpened():

    success, image = cap.read()
    if success:
        faces = classifier.detectMultiScale(image)

        for face in faces:
            x,y,w,h = face
            cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("My cam", image)

    key = cv2.waitKey(1)
    if key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()