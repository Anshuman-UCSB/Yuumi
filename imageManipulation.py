import numpy as np
import cv2
from PIL import ImageGrab

class imageRec:
    def getHealthValue(self, x1, x2, y1, y2):

        bbox = (x1, x2, y1, y2)

        img = ImageGrab.grab(bbox=(x1,x2,y1,y2)) #BGR not RGB
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        left = 0
        right = x2-x1
        yVal = y1+y2
        yVal /= 2

        

        cv2.imshow("hpbar", frame)
        cv2.moveWindow("hpbar",3160,650)
