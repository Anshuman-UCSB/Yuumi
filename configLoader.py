

class fileLoader():

    def __init__(self,config):
        self.f = open(config, 'r') #input as config.cfg
        self.data = self.f.read()
        self.cfg = []
        self.cfgDict = {}

    def printConfig(self):
        print("Data\n---")
        print(self.data)
        print("---")
        print("Dictionary")
        print("---")
        for key in self.cfgDict:
            print(key + ": "+str(self.cfgDict[key]))
        print("---")

    def readConfig(self):
        self.cfgDict = eval(self.data)
        mapBox = (self.cfgDict["mapX"],self.cfgDict["mapY"],self.cfgDict["mapW"],self.cfgDict["mapH"])
        self.cfg.append(mapBox)
        hudBox = (self.cfgDict["hudX"],self.cfgDict["hudY"],self.cfgDict["hudW"],self.cfgDict["hudH"])
        self.cfg.append(hudBox)
        self.cfg.append(self.cfgDict["f1X"])
        self.cfg.append(self.cfgDict["f1Y"])
        self.cfg.append(self.cfgDict["f2X"])
        self.cfg.append(self.cfgDict["f2Y"])
        self.cfg.append(self.cfgDict["f3X"])
        self.cfg.append(self.cfgDict["f3Y"])

        champBox = (self.cfgDict["champsX"],self.cfgDict["champsY"],self.cfgDict["champsW"],self.cfgDict["champsH"])
        self.cfg.append(champBox)
        self.cfg.append([self.cfgDict["champPortraitX1"],self.cfgDict["champPortraitX2"], self.cfgDict["champPortraitY"]])

    def close(self):
        self.f.close()
