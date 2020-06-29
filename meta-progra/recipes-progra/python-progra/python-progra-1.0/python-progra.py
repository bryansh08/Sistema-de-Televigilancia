import cv2, time
import numpy as np
from datetime import datetime

haar_full_face_cascade = cv2.CascadeClassifier("/haarcascade_frontalface_default.xml")
haar_upper_body_cascade = cv2.CascadeClassifier("/haarcascade_upperbody.xml")
haar_lower_body_cascade = cv2.CascadeClassifier("/haarcascade_lowerbody.xml")
haar_full_catface_cascade = cv2.CascadeClassifier("/haarcascade_frontalcatface_extended.xml")
haar_full_body_cascade = cv2.CascadeClassifier("/haarcascade_fullbody.xml")

cont=0 
grupo=[]

video_capture = cv2.VideoCapture(0)
video_width = video_capture.get(3)
video_height = video_capture.get(4)
f= open("registro.txt","w+")

while True:
    ret, frame = video_capture.read()

    #frame = imutils.resize(frame, width=1000) # resize original video for better viewing performance
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert video to grayscale

    #Cuerpo superior   
    upper_body = haar_upper_body_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.01,
        minNeighbors = 10,
        minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    #Cuerpo inferior
    lower_body = haar_lower_body_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.01,
        minNeighbors = 10,
        minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    #Cuerpo completo
    full_body = haar_full_body_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.01,
        minNeighbors = 10,
        minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    #Cara completa
    full_face = haar_full_face_cascade.detectMultiScale(
          gray,
          scaleFactor = 1.01,
          minNeighbors = 10,
          minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
          flags = cv2.CASCADE_SCALE_IMAGE
     )
    #Cara gato
    full_catface = haar_full_catface_cascade.detectMultiScale(
          gray,
          scaleFactor = 1.01,
          minNeighbors = 10,
          minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
          flags = cv2.CASCADE_SCALE_IMAGE
     )

    for (x, y, w, h) in upper_body:
        verde=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # creates green color rectangle with a thickness size of 1
        cv2.putText(frame, "Human Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # creates green color text with text size of 0.5 & thickness size of 2
        cont=cont+1
        grupo=[grupo,verde]
        now = datetime.now()
        nows = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write("\n Intrusion humana  %s:" % nows )
        
    for (x, y, w, h) in lower_body :
        verde1=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # creates green color rectangle with a thickness size of 1
        cv2.putText(frame, "Human Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # creates green color text with text size of 0.5 & thickness size of 2
        cont=cont+1
        grupo=[grupo,verde1]
        now = datetime.now()
        nows = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write("\n Intrusion humana  %s:" % nows )

    for (x, y, w, h) in full_body :
        verde2=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # creates green color rectangle with a thickness size of 1
        cv2.putText(frame, "Human Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # creates green color text with text size of 0.5 & thickness size of 2
        cont=cont+1
        grupo=[grupo,verde2]
        now = datetime.now()
        nows = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write("\n Intrusion humana  %s:" % nows )
        
    for (x, y, w, h) in full_face :
        verde3=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # creates green color rectangle with a thickness size of 1
        cv2.putText(frame, "Human Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cont=cont+1
        grupo=[grupo,verde3]
        now = datetime.now()
        nows = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write("\n Intrusion humana  %s:" % nows )
        
    for (x, y, w, h) in full_catface :
        verde4=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # creates green color rectangle with a thickness size of 1
        cv2.putText(frame, "Cat Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cont=cont+1
        grupo=[grupo,verde4]
        now = datetime.now()
        nows = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write("\n Intrusion animal %s:" % nows )
        
    cv2.imshow('Video en vivo', frame) # Display video

    # stop script when "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print (cont)
        f.close()
        f = open('registro.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
        break

# Release capture
video_capture.release()
cv2.destroyAllWindows()
