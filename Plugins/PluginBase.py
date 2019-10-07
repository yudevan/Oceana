from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class BasePlugins(QWidget):
    def __init__(self, parent=None):
        super(BasePlugins, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Default Subwindow title")