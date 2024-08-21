from facial_emotion_recognition import EmotionRecognition
import cv2

# initialize the emotion recognition class
er = EmotionRecognition(device='gpu')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = er.recognise_emotion(frame)

    cv2.imshow("Emotion", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
