class Yuumi:
    from configLoader import fileLoader
    import numpy as np
    import cv2
    from PIL import ImageGrab
    import pyautogui
    from imageManipulation import imageRec

    cfg = fileLoader("config.cfg")

    cfg.readConfig()

    cfgData = cfg.cfg
    print(cfgData)

    cfg.close()

    imgrec = imageRec()

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

        champImg = ImageGrab.grab(cfgData[8])
        champImg_np = np.array(champImg)
        champFrame = cv2.cvtColor(champImg_np, cv2.COLOR_BGR2RGB)

        cv2.imshow("f1", mapFrame)
        cv2.imshow("f2", hudFrame)
        cv2.imshow("f3", champFrame)
        #print(pyautogui.position())
        imgrec.getHealthValue(cfgData[9][0], cfgData[9][1], cfgData[9][2], cfgData[9][3])

        if init:
            cv2.moveWindow("f1",cfgData[2],cfgData[3])
            cv2.moveWindow("f2",cfgData[4],cfgData[5])
            cv2.moveWindow("f3",cfgData[6],cfgData[7])
            init = False

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
