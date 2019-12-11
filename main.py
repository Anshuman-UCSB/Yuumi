from configLoader import fileLoader

cfg = fileLoader("config.cfg")

cfg.readConfig()

cfgDict = cfg.cfg
print(cfgDict)

cfg.close()
