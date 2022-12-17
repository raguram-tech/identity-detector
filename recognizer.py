import cv2
from twilio.rest import Client
import keys
from mail import sendMail
from sms import sendSms

client = Client(keys.account_sid, keys.auth_token)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX
id = 0

names = ['None', 'Lalith', 'Lalith', 'Lalith', 'Lalith', 'Nivetha', 'Nivetha', 'Nivetha', 'Nivetha', 'Raguram',
         'Raguram', 'Raguram', 'Raguram', 'Mouliraj', 'Mouliraj', 'Mouliraj', 'Mouliraj']
rno = ['None', '20CSR105', '20CSR105', '20CSR105', '20CSR105', '20CSR143', '20CSR143', '20CSR143', '20CSR143',
       '20CSR160', '20CSR160', '20CSR160', '20CSR160', '20CSR125', '20CSR125', '20CSR125', '20CSR125']

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

count = 0
print("\nRecognizing Faces")
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)), )
    xa, ya = 0, 0
    no = ""
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        confidence = round((100 - confidence))
        xa, ya = x, y

        if int(confidence) > 30:
            no = rno[id]
            id = names[id]
            # confidence = "  {0}%".format(round(confidence))
            cv2.putText(img, str(id), (x + 5, y - 40), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(no), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            count = 0
        else:
            id = "unknown"
            no = "unknown"
            count = 1
            break
    cv2.putText(img, str(id), (xa + 5, ya - 40), font, 1, (255, 255, 255), 2)
    if id == "unknown" and no == "unknown" and count == 1:
        ret, image = cam.read()
        if ret:
            cv2.imwrite("unknown.png", image)
        # sendSms()
        # sendMail("unknown.png")
        count = 0

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

print("\nExiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
