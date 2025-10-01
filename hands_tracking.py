from cvzone.HandTrackingModule import HandDetector
import cv2, time

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=2)

pTime = cTime = 0

while True:

    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True)  
    
    if hands:
        print(hands[0]["lmList"])
        print(hands[0]["bbox"])
        print(hands[0]["type"])
    

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()