from configparser import ConfigParser

# config = ConfigParser()
# config.read(".\\ConfigurationData\\conf.ini")
# print(config.get("locators","name_XPATH"))
# # print(config.get("basic info","testsiteurl"))


def readConfig(section,key):
    config = ConfigParser()
    config.read(".\\ConfigurationData\\conf.ini")
    return config.get(section,key)
