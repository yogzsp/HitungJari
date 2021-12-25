import cv2
"""
    Y5P
    IG : yogzsp
    Yogi Surya Prana
    Deteksi Tangan
"""
import time
import os
import tangan
 
wCam, hCam = 640, 480
 
Kamera = cv2.VideoCapture(0)
Kamera.set(3, wCam)
Kamera.set(4, hCam)
 
 
pTime = 0
 
detector = tangan.DeteksiTangan(detectionCon=0.75)
 
tipIds = [4, 8, 12, 16, 20]
 
while True:
    success, img = Kamera.read()
    img = detector.cariTangan(img)
    lmList = detector.cariPosisi(img, draw=False)
    # print(lmList)
 
    if len(lmList) != 0:
        fingers = []
 
        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
 
        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
 
        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)

        cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)   
        cv2.putText(img,str(totalFingers),(45,375),cv2.FONT_HERSHEY_PLAIN,
                                     10,(255,0,0),20)  
 
 
 
    cv2.imshow("Image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

Kamera.release()
cv2.destroyAllWindows()