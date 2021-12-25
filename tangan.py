"""
    Y5P
    IG : yogzsp
    Yogi Surya Prana
    Deteksi Tangan
"""
import cv2
import mediapipe as mp
import time
 

 LogoY5P = """                           ********
                       ****        ****
                   ****                ***
                 ****   ****     0000
                **00   ***   ****  1111
               **11  ***   **    **   0000
              **00  **   **  *  *  **
              **11       **   **   **
                           ** ** **    ****
                             ****    ****
                       0000        ****
                         1111            11**
                           0000      00****
                                 11****
                           ********

0000000000000000000000000000000000000000000000000000000000000
11    **          **    **************      **********     11
11      **      **      **                  **        **   11
11        **  **        ************        **        **   11
11          **                      **      ** *******     11
11          **                      **      **             11
11          **           ***********        **             11
0000000000000000000000000000000000000000000000000000000000000


Developer : Y5P
Tools Name : Y5PFinger
Instagram : yogzsp
Website : yogisuryaprana.hostd.my.id

"""

print(LogoY5P)
 
class DeteksiTangan():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
 
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
 
    def cariTangan(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
 
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img
 
    def cariPosisi(self, img, handNo=0, draw=True):
 
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
 
        return lmList
 
 
def main():
    pTime = 0
    cTime = 0
    Kamera = cv2.VideoCapture(0)
    detector = DeteksiTangan()
    while True:
        success, img = Kamera.read()
        img = detector.cariTangan(img)
 
        cv2.imshow("Rentangkan Jari", img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27 or k == ord('q'):
            break
            
    Kamera.release()
    cv2.destroyAllWindows()
 
 
if __name__ == "__main__":
    main()