from PyQt5.Qt import *
from PyQt5.QtCore import pyqtSlot

class BaseForm(QWidget, QHBoxLayout):
    __label = ""
    __val = vars()
    def __init__(self, parent=None):
        super(BaseForm,self).__init__(parent)
        self.control = QLabel("Default Widget")
        self.label = QLabel("Default Label")
        self.trigger = None # for File browse widget
    def bind(self):
        def getter(self):
            return type(self.findChild(QObject, self.objectName).property(propertyName).toPyObject())

        def setter(self, value):
            self.findChild(QObject, self.objectName).setProperty(propertyName, QVariant(value))

        return property(getter, setter)
    @property
    def getVal(self):
        self.__val =None
        if type(self.control) == QLineEdit:
            self.__val = self.control.text()
        elif type(self.control) == QTextBlock:
            self.__val = self.control.text()
        elif type(self.control) == QCheckBox or type(self.control) == QRadioButton:
            self.__val = self.control.isChecked()
        elif type(self.control) == QSpinBox:
            self.__val = self.control.value()
        else:
            self.__val = self.control.text()
        return self.__val
    property.setter
    def setVal(self, val):
        self.__val = val
    @pyqtSlot()
    def triggered(self):
        yield "Form Triggered"