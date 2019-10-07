from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from core import Settings

class Window(QMainWindow):
    conf = Settings.getInstance()
    def __init__(self, MainQtApp=None, *args, **kwargs):
        super(Window,self).__init__(MainQtApp,*args,**kwargs)
        self.setWindowTitle("Oceana Navigation Data Package")
        self.status = self.statusBar()
        self.mdiArea = QMdiArea(self)
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.subWindowActivated.connect(self.updateMenus)
        self.windowMapper = QSignalMapper(self)
        self.windowMapper.mapped[QWidget].connect(self.setActiveSubWindow)

        self.setCentralWidget(self.mdiArea)
    def setActiveSubWindow(self, window):
        if window:
            self.mdiArea.setActiveSubWindow(window)
    def updateMenus(self):
        hasMdiChild = (self.activeMdiChild() is not None)

    def activeMdiChild(self):
        activeSubWindow = self.mdiArea.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()

        return None