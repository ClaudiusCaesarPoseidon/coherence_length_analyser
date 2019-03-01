import os
from .dialog import Dialog
from ...lib import functions
from PySide2 import QtCore, QtWidgets, QtGui
from ConvertQt import uic


class Command_Line_Arguments(Dialog):
    resized = QtCore.Signal()

    def __init__(self):
        """load widget from ui file, connect signals to slots and initialise"""\
        """class attribute"""
        super().__init__()
        # loads the widgets from the ui file
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
        return val

    def end(self):
        val = self.parse_text(self.Input.text())
        self.done(val)

    def set_Size(self):
        # sets the fontsize of the widgets according to window size
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
