import  os
import sys
from PyQt5.Qt import  QApplication
from PyQt5 import  QtGui
from core.ui import Window
from core import Settings

if __name__=="__main__":
    appconf = {}
    conf = Settings.getInstance()
    QApp = QApplication(sys.argv)
    QApp.setObjectName("Oceana")
    mainWindow = Window()
    if not QApp.objectName() in conf:
        conf[QApp.objectName()]={}
        appconf = conf[QApp.objectName()]
        appconf["x"] = mainWindow.pos().x()
        appconf["y"] = mainWindow.pos().y()
        appconf["width"] = mainWindow.width()
        appconf["height"] = mainWindow.height()
        appconf["lookandfeel"] ="native"

    appconf = conf[QApp.objectName()]
    mainWindow.setMinimumSize(appconf.as_int("width"),appconf.as_int("height"))
    mainWindow.show()
    conf.write()
    sys.exit(QApp.exec_())