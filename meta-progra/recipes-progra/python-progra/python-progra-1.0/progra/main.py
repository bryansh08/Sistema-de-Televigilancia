import sys
import cv2

def main(argv=None):
    if argv is None:
        argv = sys.argv

    video=cv2.VideoCapture(0)
    a=0
    while True:
        a=a+1
        check, frame = video.read()
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Grabando", frame)
        key=cv2.waitKey(1)

        if key==ord('q'):
            break

    print (a)

    video.release()

    cv2.destroyAllWindows
    return 0 
