class Yuumi:
    from configLoader import fileLoader
    import numpy as np
    import cv2
    from PIL import ImageGrab
    import pyautogui

    cfg = fileLoader("config.cfg")

    cfg.readConfig()

    cfgData = cfg.cfg
    print(cfgData)

    cfg.close()

    # variables:
    # cfg is object
    # cfgDict is dictionary of cfg data

    init = True

    while True:
        img = ImageGrab.grab(cfgData[0]) #BGR not RGB
        img_np = np.array(img)
        mapFrame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        hudImg = ImageGrab.grab(cfgData[1])
        hudImg_np = np.array(hudImg)
        hudFrame = cv2.cvtColor(hudImg_np, cv2.COLOR_BGR2RGB)

        cv2.imshow("f1", mapFrame)
        cv2.imshow("f2", hudFrame)
        #print(pyautogui.position())
        
        if init:
            cv2.moveWindow("f1",cfgData[2],cfgData[3])
            cv2.moveWindow("f2",cfgData[4],cfgData[5])
            init = False

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
