#-
try:
    from configobj import ConfigObj
except:
    raise("ConfigObj module doesn't exist. Please install it before coninuing")

class Settings(ConfigObj):
    """
    This Module is a singleton Setting class
    which will store all the settings of the program
    the format of the settings file is the same as ini file

    it can be edited either using text editor or programmatically
    using ConfigObj module
    :param configfile: Is the path of the config file relative to main project
    """
    __instance=None
    __running={}
    __widgets={}

    @staticmethod
    def getInstance():
        if Settings.__instance:
            return Settings.__instance
        else:
            return Settings()

    def __init__(self, configfile="storage/config/preferences.cfg"):
        super(Settings, self).__init__(configfile)
        self.__instance = self
    def __repr__(self):
        print(self)
    @property
    def Widgets(self,name):
        if name in self.__widgets.keys():
            return self.__widgets[name]
    @property
    def running(self):
        return self.__running
    @property
    def onfile(self):
        return self