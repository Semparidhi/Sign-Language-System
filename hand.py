import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

while True:
    s, img = cap.read()
    img=cv2.flip(img,1)
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgCrop = img[y:y+h, x:x+w]
        # cv2.imshow("imgCrop", imgCrop)

    cv2.imshow("images", img)
    cv2.waitKey(1)
