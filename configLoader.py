

class fileLoader():

    def __init__(self,config):
        self.f = open(config, 'r') #input as config.cfg
        self.data = self.f.read()
        self.cfg = {}

    def printConfig(self):
        print("Data\n---")
        print(self.data)
        print("---")
        print("Dictionary")
        print("---")
        for key in self.cfg:
            print(key + ": "+str(self.cfg[key]))
        print("---")

    def readConfig(self):
        self.cfg = eval(self.data)

    def close(self):
        self.f.close()
