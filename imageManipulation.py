import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui

class imageRec:
    def getHealthValue(self, x1, x2, y1, y2):

        bbox = (x1, y1, x2, y2)

        #print("{}, {}  {}, {}".format(x1, y1, x2, y2))

        img = ImageGrab.grab(bbox) #BGR not RGB
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)



        left = 0
        right = len(frame[0])
        yVal = y1-y2
        yVal /= 2

        mid = -1
        while(right-left>=1):
            mid = int((right+left)/2)
            if(frame[int(yVal)][int(mid)][1]>120):
                left = mid+1
            else:
                right = mid-1
            #print("left {}, right {}, mid{}".format(left,right,mid))
        print("Health is {0:.2f}%".format(100*mid/len(frame[0])))

        upper = 60
        lower = 5

        if 100*mid/len(frame[0]) < upper and 100*mid/len(frame[0]) > lower:

            pyautogui.click(x=1205,y=983)
            print("Healing, health is at {}".format(100*mid/len(frame[0])))


        cv2.imshow("hpbar", frame)
        cv2.moveWindow("hpbar",3160,650)
