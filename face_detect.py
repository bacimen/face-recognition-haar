import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)


def process_face():
    while (True):
        ret, webcam = video_capture.read()

        gray = cv2.cvtColor(webcam, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in face:
            cv2.rectangle(webcam, (x, y), (x + w, y + h), (254, 148, 112), 2)
        cv2.imshow('Webcam', webcam)
        if cv2.waitKey(1) == (ord('q') | ord('Q')):
            break

def main():
    process_face()
    video_capture.release()
    cv2.destroyAllWindows()

main()