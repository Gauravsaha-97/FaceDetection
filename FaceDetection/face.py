import cv2

cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

while cap.isOpened():

    success, image = cap.read()

    if success:
        faces = classifier.detectMultiScale(image)

        for face in faces:
            x,y,w,h = face
            cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),2)

            eye_colored_region = image[y:y+h,x:x+w]
            eyes = eye_classifier.detectMultiScale(eye_colored_region)
            for eye in eyes:
                ex,ey,ew,eh = eye
                cv2.rectangle(eye_colored_region, (ex,ey),(ex+ew,ey+eh),(0,255,0),5)
        cv2.imshow("My cam", image)

    key = cv2.waitKey(1)
    if key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()