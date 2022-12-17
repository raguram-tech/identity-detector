import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

face_detector = cv2.CascadeClassifier('face.xml')

# For each person, enter one numeric face id
face_id = input('\n Enter User ID and press <return> ==>  ')

print("\nInitializing face capture. Look the camera and wait...")
# Initialize individual sampling face count
count = 0
# images
while True:

    ret, img = cam.read()
    cv2.imshow('image', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1

        # Save the captured image into the dataset folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30:  # Take 30 face sample and stop video
        break

# Do a bit of cleanup
print("\nExiting Program")
cam.release()
cv2.destroyAllWindows()
