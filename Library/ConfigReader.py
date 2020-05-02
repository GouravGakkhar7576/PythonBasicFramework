import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Config.cfg")
    return config.get(section, key)
