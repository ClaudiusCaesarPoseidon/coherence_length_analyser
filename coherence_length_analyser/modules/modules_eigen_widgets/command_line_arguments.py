import os
from ...lib import functions
from PyQt5 import QtCore, QtWidgets, uic, QtGui
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


class Command_Line_Arguments(QtWidgets.QDialog):
    resized = QtCore.Signal()

    def __init__(self):
        super().__init__()
        file = functions.resource_path(
            os.path.join("ui", "Command_Line_Arguments.ui"))
        uic.loadUi(file, self)
        self.Ok.clicked.connect(self.end)
        self.resized.connect(self.set_Size)

    def resizeEvent(self, event):
        self.resized.emit()
        return super().resizeEvent(event)

    def parse_text(self, text):
        self.text_list = text.split(" ")
        val = 0
#        for item in self.text_list:
#            if item in("-win", "--windowed"):
#                val += 1
#            if item in("-b", "--borderless"):
#                val += 10
#            if item in("-min", "--minimised"):
#                val += 100
#            if item in("-int", "--interactive"):
#                val += 1000
#            if item in("-ipy", "--ipython"):
#                val += 10000
        return val

    def end(self):
        val = self.parse_text(self.Input.text())
        self.done(val)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            event.ignore()
        else:
            event.accept()

    def set_Size(self):
        self.height = int(self.geometry().height())
        fontsize = (self.height / 30)
        font_button = QtGui.QFont()
        font_button.setPointSize(fontsize)
        fontsize = (self.height / 30)
        if fontsize <= 8:
            fontsize = 8
        if fontsize >= 16:
            fontsize = 16
        font_text = QtGui.QFont()
        font_text.setPointSize(fontsize)
        for item in self.findChildren(QtWidgets.QPushButton):
            item.setFont(font_button)
        for item in self.findChildren(QtWidgets.QLineEdit):
            item.setFont(font_text)
        for item in self.findChildren(QtWidgets.QPlainTextEdit):
            item.setFont(font_text)
        for item in self.findChildren(QtWidgets.QComboBox):
            item.setFont(font_text)
