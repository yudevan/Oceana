from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from core.settings import Settings

class PluginRegister(dict):
    __instance = None
    __plugins ={}

    @staticmethod
    def getInstance():
        if PluginRegister.__instance is not None:
            return PluginRegister.__instance
        else:
            return PluginRegister()
    def __init__(self):
        super(PluginRegister, self).__init__()
        self.__instance = self

class BasePlugins(QWidget):
    name = "BasePlugin"
    desc = "Base Plugin Structure"
    auth = "Wahyudin Aziz"
    auth_email = "yudevan@yahoo.com"
    ver = "1.0"

    __base_settings={}
    def __init__(self, parent=None):
        super(BasePlugins, self).__init__(parent)
        self.conf = Settings.getInstance()
        self.register = PluginRegister.getInstance()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Default Subwindow title")
    def readSettigs(self):
        if self.name in dict(self.conf['Plugins']).keys():
            self.__base_settings = self.conf[self.name]
        else:
            self.conf['Plugins'][self.name]={}

